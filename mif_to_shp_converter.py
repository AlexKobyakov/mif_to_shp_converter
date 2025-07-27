# -*- coding: utf-8 -*-
"""
MIF/TAB to SHP/GeoJSON Converter Plugin for QGIS
Professional multilingual converter with modern UI supporting 9 languages

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Organization: Lesburo
Year: 2025
"""

import os
import sys
import glob
from datetime import datetime
from qgis.PyQt.QtCore import Qt, QThread, QLocale
from qgis.PyQt.QtGui import QIcon, QColor
from qgis.PyQt.QtWidgets import (QAction, QDialog, QVBoxLayout, QHBoxLayout, 
                                 QLabel, QLineEdit, QPushButton, QTextEdit, 
                                 QFileDialog, QMessageBox, QProgressBar, QCheckBox,
                                 QRadioButton, QButtonGroup, QGroupBox, QSpinBox,
                                 QTableWidget, QTableWidgetItem, QComboBox)

from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem
from qgis.utils import iface

from .translations import translations
from .worker import ConversionWorker


class MifToShpConverter:
    """Main plugin class"""

    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        self.actions = []
        self.menu = '&MIF/TAB Converter'
        self.toolbar = self.iface.addToolBar('MifToShpConverter')
        self.toolbar.setObjectName('MifToShpConverter')

    def add_action(self, icon_path, text, callback, enabled_flag=True, add_to_menu=True,
                   add_to_toolbar=True, status_tip=None, whats_this=None, parent=None):
        """Add a toolbar icon to the toolbar."""
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToVectorMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        self.add_action(
            icon_path,
            text='MIF/TAB to SHP/GeoJSON Converter',
            callback=self.run,
            parent=self.iface.mainWindow())

    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginVectorMenu('&MIF/TAB Converter', action)
            self.iface.removeToolBarIcon(action)
        del self.toolbar

    def run(self):
        """Run method that performs all the real work"""
        dialog = MifToShpConverterDialog()
        dialog.exec_()


class MifToShpConverterDialog(QDialog):
    """Main dialog class"""

    def __init__(self):
        super().__init__()
        self.worker = None
        self.worker_thread = None
        self.setupUI()
        self.setupLanguage()

    def setupUI(self):
        """Setup the user interface"""
        self.setWindowTitle("MIF/TAB to SHP/GeoJSON Converter")
        self.setMinimumSize(800, 600)
        self.resize(1000, 700)

        # Main layout
        main_layout = QVBoxLayout()

        # Language selection
        lang_layout = QHBoxLayout()
        lang_layout.addWidget(QLabel("Language / Язык:"))
        self.language_combo = QComboBox()
        self.language_combo.addItems(['Русский', 'English', '中文', 'हिन्दी', 'Español', 
                                     'العربية', 'Français', 'Português', 'Deutsch'])
        self.language_combo.currentTextChanged.connect(self.changeLanguage)
        lang_layout.addWidget(self.language_combo)
        lang_layout.addStretch()
        main_layout.addLayout(lang_layout)

        # Mode selection
        mode_group = QGroupBox("Conversion Mode")
        mode_layout = QVBoxLayout()
        self.mode_group = QButtonGroup()
        
        self.single_mode = QRadioButton("Single File")
        self.batch_mode = QRadioButton("Batch Processing (Folder)")
        self.batch_mode.setChecked(True)
        
        self.mode_group.addButton(self.single_mode)
        self.mode_group.addButton(self.batch_mode)
        mode_layout.addWidget(self.single_mode)
        mode_layout.addWidget(self.batch_mode)
        mode_group.setLayout(mode_layout)
        main_layout.addWidget(mode_group)

        # Input section
        input_layout = QHBoxLayout()
        self.input_label = QLabel("Input:")
        self.input_line = QLineEdit()
        self.input_button = QPushButton("Browse...")
        self.input_button.clicked.connect(self.selectInput)
        input_layout.addWidget(self.input_label)
        input_layout.addWidget(self.input_line)
        input_layout.addWidget(self.input_button)
        main_layout.addLayout(input_layout)

        # Output section
        output_layout = QHBoxLayout()
        self.output_label = QLabel("Output Folder:")
        self.output_line = QLineEdit()
        self.output_button = QPushButton("Browse...")
        self.output_button.clicked.connect(self.selectOutput)
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output_line)
        output_layout.addWidget(self.output_button)
        main_layout.addLayout(output_layout)

        # Settings section
        settings_layout = QHBoxLayout()
        
        # Format
        settings_layout.addWidget(QLabel("Format:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(['ESRI Shapefile', 'GeoJSON'])
        settings_layout.addWidget(self.format_combo)

        # CRS
        settings_layout.addWidget(QLabel("CRS:"))
        self.crs_line = QLineEdit("EPSG:4326")
        settings_layout.addWidget(self.crs_line)

        # Threads
        settings_layout.addWidget(QLabel("Threads:"))
        self.threads_spinbox = QSpinBox()
        self.threads_spinbox.setRange(1, 16)
        self.threads_spinbox.setValue(4)
        settings_layout.addWidget(self.threads_spinbox)

        main_layout.addLayout(settings_layout)

        # Add to project checkbox
        self.add_to_project_cb = QCheckBox("Add results to QGIS project")
        self.add_to_project_cb.setChecked(True)
        main_layout.addWidget(self.add_to_project_cb)

        # Progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)

        # Control buttons
        button_layout = QHBoxLayout()
        self.convert_button = QPushButton("🚀 Start Conversion")
        self.convert_button.clicked.connect(self.startConversion)
        self.cancel_button = QPushButton("❌ Cancel")
        self.cancel_button.clicked.connect(self.cancelConversion)
        self.clear_button = QPushButton("🧹 Clear Logs")
        self.clear_button.clicked.connect(self.clearResults)
        
        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        main_layout.addLayout(button_layout)

        # Results table
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(['File', 'Status', 'Details'])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        main_layout.addWidget(self.results_table)

        # Log area
        self.log_text = QTextEdit()
        self.log_text.setMaximumHeight(150)
        main_layout.addWidget(self.log_text)

        self.setLayout(main_layout)

    def setupLanguage(self):
        """Setup language detection"""
        locale = QLocale.system().name()
        if locale.startswith('ru'):
            self.language_combo.setCurrentText('Русский')
            translations.set_language('ru')
        elif locale.startswith('zh'):
            self.language_combo.setCurrentText('中文')
            translations.set_language('zh')
        elif locale.startswith('hi'):
            self.language_combo.setCurrentText('हिन्दी')
            translations.set_language('hi')
        elif locale.startswith('es'):
            self.language_combo.setCurrentText('Español')
            translations.set_language('es')
        elif locale.startswith('ar'):
            self.language_combo.setCurrentText('العربية')
            translations.set_language('ar')
            self.setLayoutDirection(Qt.RightToLeft)
        elif locale.startswith('fr'):
            self.language_combo.setCurrentText('Français')
            translations.set_language('fr')
        elif locale.startswith('pt'):
            self.language_combo.setCurrentText('Português')
            translations.set_language('pt')
        elif locale.startswith('de'):
            self.language_combo.setCurrentText('Deutsch')
            translations.set_language('de')
        else:
            self.language_combo.setCurrentText('English')
            translations.set_language('en')

    def changeLanguage(self, language_text):
        """Change interface language"""
        language_map = {
            'Русский': 'ru',
            'English': 'en',
            '中文': 'zh',
            'हिन्दी': 'hi',
            'Español': 'es',
            'العربية': 'ar',
            'Français': 'fr',
            'Português': 'pt',
            'Deutsch': 'de'
        }
        
        language = language_map.get(language_text, 'en')
        translations.set_language(language)
        
        if language == 'ar':
            self.setLayoutDirection(Qt.RightToLeft)
        else:
            self.setLayoutDirection(Qt.LeftToRight)
        self.updateTexts()

    def updateTexts(self):
        self.setWindowTitle(translations.get_text('window_title'))
        self.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
        self.cancel_button.setText(f"❌ {translations.get_text('cancel')}")
        self.clear_button.setText(f"🧹 {translations.get_text('clear_logs')}")

    def selectInput(self):
        if self.single_mode.isChecked():
            file_path, _ = QFileDialog.getOpenFileName(
                self, 'Select MIF/TAB file', '', 'MIF/TAB files (*.mif *.tab)')
            if file_path:
                self.input_line.setText(file_path)
                if not self.output_line.text():
                    self.output_line.setText(os.path.dirname(file_path))
        else:
            folder = QFileDialog.getExistingDirectory(self, 'Select folder with MIF/TAB files')
            if folder:
                self.input_line.setText(folder)
                if not self.output_line.text():
                    self.output_line.setText(folder)

    def selectOutput(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select output folder')
        if folder:
            self.output_line.setText(folder)

    def startConversion(self):
        input_path = self.input_line.text()
        output_path = self.output_line.text()
        crs_text = self.crs_line.text()
        
        if not input_path or not output_path or not crs_text:
            QMessageBox.warning(self, 'Error', 'Please fill all required fields')
            return
        
        # Сбор файлов
        files_to_process = []
        if self.single_mode.isChecked():
            if os.path.exists(input_path):
                files_to_process = [input_path]
        else:
            if os.path.exists(input_path):
                mif_files = glob.glob(os.path.join(input_path, '*.mif'))
                tab_files = glob.glob(os.path.join(input_path, '*.tab'))
                files_to_process = mif_files + tab_files
        
        if not files_to_process:
            QMessageBox.warning(self, 'Error', 'No supported files found')
            return
        
        os.makedirs(output_path, exist_ok=True)
        
        output_format = 'GeoJSON' if 'GeoJSON' in self.format_combo.currentText() else 'ESRI Shapefile'
        
        # UI настройка
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.convert_button.setEnabled(False)
        self.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        
        self.results_table.setRowCount(0)
        self.log_message("🚀 Starting conversion...")
        
        # Worker
        max_workers = self.threads_spinbox.value()
        self.worker = ConversionWorker(files_to_process, output_path, crs_text, output_format, max_workers)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        
        # Сигналы
        self.worker_thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.log_message.connect(self.log_message)
        self.worker.file_completed.connect(self.onFileCompleted)
        self.worker.finished.connect(self.onConversionFinished)
        self.worker.error.connect(self.onConversionError)
        
        self.worker_thread.start()

    def cancelConversion(self):
        if self.worker:
            self.worker.cancel()
            self.log_message("⚠️ Cancelling conversion...")

    def clearResults(self):
        self.log_text.clear()
        self.results_table.setRowCount(0)
        self.log_message("🧹 Results cleared")

    def onFileCompleted(self, filename, success, message):
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        
        self.results_table.setItem(row, 0, QTableWidgetItem(filename))
        status_text = f"✅ {translations.get_text('success')}" if success else f"❌ {translations.get_text('error')}"
        status_item = QTableWidgetItem(status_text)
        
        if success:
            status_item.setBackground(QColor('#d4edda'))
        else:
            status_item.setBackground(QColor('#f8d7da'))
            
        self.results_table.setItem(row, 1, status_item)
        self.results_table.setItem(row, 2, QTableWidgetItem(message))

    def onConversionFinished(self):
        self.progress_bar.setValue(100)
        self.convert_button.setEnabled(True)
        self.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
        self.log_message("🎉 Conversion completed!")
        
        # Статистика
        total_files = self.results_table.rowCount()
        success_count = 0
        for row in range(total_files):
            status_item = self.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                success_count += 1
        
        self.log_message(f"📊 Statistics: {success_count}/{total_files} files converted successfully")
        
        # Добавление в проект
        if self.add_to_project_cb.isChecked() and success_count > 0:
            self.addResultsToProject()
        
        # Уведомление
        if success_count == total_files:
            QMessageBox.information(self, '🎉 Success', f'All {total_files} files converted successfully!')
        elif success_count > 0:
            QMessageBox.warning(self, '⚠️ Partial Success', 
                              f'{success_count} of {total_files} files converted successfully.')
        else:
            QMessageBox.critical(self, '❌ Error', 'No files were converted successfully.')
        
        # Очистка
        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.worker = None

    def onConversionError(self, error_message):
        self.log_message(f"🔥 CRITICAL ERROR: {error_message}")
        QMessageBox.critical(self, 'Critical Error', error_message)
        self.onConversionFinished()

    def addResultsToProject(self):
        """Добавление файлов в проект QGIS"""
        output_folder = self.output_line.text()
        crs_text = self.crs_line.text()
        output_format = 'GeoJSON' if 'GeoJSON' in self.format_combo.currentText() else 'ESRI Shapefile'
        
        crs = QgsCoordinateReferenceSystem()
        if crs_text.startswith('EPSG:'):
            epsg_code = int(crs_text.split(':')[1])
            crs.createFromId(epsg_code)
        else:
            crs.createFromString(crs_text)
        
        added_count = 0
        for row in range(self.results_table.rowCount()):
            status_item = self.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                filename = self.results_table.item(row, 0).text()
                
                if output_format == 'GeoJSON':
                    if filename.lower().endswith('.mif'):
                        output_file = os.path.join(output_folder, filename.replace('.mif', '.geojson'))
                        layer_name = filename.replace('.mif', '')
                    else:
                        output_file = os.path.join(output_folder, filename.replace('.tab', '.geojson'))
                        layer_name = filename.replace('.tab', '')
                else:
                    if filename.lower().endswith('.mif'):
                        output_file = os.path.join(output_folder, filename.replace('.mif', '.shp'))
                        layer_name = filename.replace('.mif', '')
                    else:
                        output_file = os.path.join(output_folder, filename.replace('.tab', '.shp'))
                        layer_name = filename.replace('.tab', '')
                
                if os.path.exists(output_file):
                    layer = QgsVectorLayer(output_file, layer_name, "ogr")
                    if layer.isValid():
                        layer.setCrs(crs)
                        QgsProject.instance().addMapLayer(layer)
                        added_count += 1
        
        if added_count > 0:
            self.log_message(f"📁 Added to project: {added_count} layers")

    def log_message(self, message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        if message.startswith('🚀') or message.startswith('🎉'):
            color = '#2ecc71'
        elif message.startswith('⚠️'):
            color = '#f39c12'
        elif message.startswith('🔥') or message.startswith('❌'):
            color = '#e74c3c'
        elif message.startswith('✅'):
            color = '#27ae60'
        elif message.startswith('✗'):
            color = '#c0392b'
        elif message.startswith('📊') or message.startswith('📁'):
            color = '#3498db'
        else:
            color = '#ecf0f1'
        
        formatted_message = f'<span style="color: #95a5a6;">[{timestamp}]</span> <span style="color: {color};">{message}</span>'
        self.log_text.append(formatted_message)
        
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)

    def closeEvent(self, event):
        if self.worker and self.worker_thread and self.worker_thread.isRunning():
            reply = QMessageBox.question(self, 'Confirmation', 
                                       'Conversion in progress. Stop and close?',
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cancelConversion()
                if self.worker_thread:
                    self.worker_thread.quit()
                    self.worker_thread.wait()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
