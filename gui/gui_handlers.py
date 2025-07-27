# -*- coding: utf-8 -*-
"""
Event Handlers for GUI Components
Обработчики событий для компонентов интерфейса

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import glob
from datetime import datetime

from qgis.PyQt.QtCore import QThread, Qt
from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
from qgis.PyQt.QtGui import QColor

from qgis.core import QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem


class GuiEventHandlers:
    """Класс для обработки событий интерфейса"""
    
    def __init__(self, main_dialog):
        self.dialog = main_dialog
    
    def onLanguageChanged(self, index):
        """Обработка смены языка"""
        language_map = {
            0: 'ru',    # Русский
            1: 'en',    # English  
            2: 'zh',    # 中文
            3: 'hi',    # हिंदी
            4: 'es',    # Español
            5: 'ar',    # العربية
            6: 'fr',    # Français
            7: 'pt',    # Português
            8: 'de'     # Deutsch
        }
        
        new_language = language_map.get(index, 'ru')
        
        # Импортируем translations из основного модуля
        from ..translations import translations
        translations.set_language(new_language)
        
        # Обновляем интерфейс
        self.dialog.updateLanguage()
        
        # Для RTL языков (арабский)
        if new_language == 'ar':
            self.dialog.setLayoutDirection(Qt.RightToLeft)
        else:
            self.dialog.setLayoutDirection(Qt.LeftToRight)
    
    def showAuthorInfo(self):
        """Показать информацию об авторе"""
        from .gui_dialogs import AuthorInfoDialog
        dialog = AuthorInfoDialog(self.dialog)
        dialog.exec_()
    
    def showCrsExamples(self):
        """Показать примеры систем координат"""
        from .gui_dialogs import CrsExamplesDialog
        dialog = CrsExamplesDialog(self.dialog)
        dialog.exec_()
    
    def onModeChanged(self):
        """Обработка смены режима конвертации"""
        is_batch = self.dialog.mode_widget.batch_mode.isChecked()
        self.dialog.input_widget.single_widget.setVisible(not is_batch)
        self.dialog.input_widget.batch_widget.setVisible(is_batch)
    
    def selectInputFile(self):
        """Выбор входного файла"""
        from ..translations import translations
        
        filename, _ = QFileDialog.getOpenFileName(
            self.dialog, 
            translations.get_text('select_input_file'), 
            '', 
            translations.get_text('supported_formats')
        )
        if filename:
            self.dialog.input_widget.input_file_line.setText(filename)
            if not self.dialog.output_widget.output_folder_line.text():
                self.dialog.output_widget.output_folder_line.setText(os.path.dirname(filename))
    
    def selectInputFolder(self):
        """Выбор входной папки"""
        from ..translations import translations
        
        folder = QFileDialog.getExistingDirectory(
            self.dialog, 
            translations.get_text('select_input_folder')
        )
        if folder:
            self.dialog.input_widget.input_folder_line.setText(folder)
            if not self.dialog.output_widget.output_folder_line.text():
                self.dialog.output_widget.output_folder_line.setText(folder)
    
    def selectOutputFolder(self):
        """Выбор выходной папки"""
        from ..translations import translations
        
        folder = QFileDialog.getExistingDirectory(
            self.dialog, 
            translations.get_text('select_output_folder')
        )
        if folder:
            self.dialog.output_widget.output_folder_line.setText(folder)
    
    def startConversion(self):
        """Запуск процесса конвертации"""
        from ..translations import translations
        from ..worker import ConversionWorker
        from .gui_dialogs import WarningDialog
        
        # Сбор файлов для обработки
        files_to_process = []
        
        if self.dialog.mode_widget.single_mode.isChecked():
            input_file = self.dialog.input_widget.input_file_line.text()
            if not input_file or not os.path.exists(input_file):
                dialog = WarningDialog('Ошибка', translations.get_text('error_no_input_file'))
                dialog.exec_()
                return
            files_to_process = [input_file]
        else:
            input_folder = self.dialog.input_widget.input_folder_line.text()
            if not input_folder or not os.path.exists(input_folder):
                dialog = WarningDialog('Ошибка', translations.get_text('error_no_input_folder'))
                dialog.exec_()
                return
            
            # Поиск всех поддерживаемых файлов в папке (MIF и TAB)
            mif_pattern = os.path.join(input_folder, '*.mif')
            tab_pattern = os.path.join(input_folder, '*.tab')
            files_to_process = glob.glob(mif_pattern) + glob.glob(tab_pattern)
            
            if not files_to_process:
                dialog = WarningDialog('Ошибка', translations.get_text('error_no_files_found'))
                dialog.exec_()
                return
        
        output_folder = self.dialog.output_widget.output_folder_line.text()
        if not output_folder:
            dialog = WarningDialog('Ошибка', translations.get_text('error_no_output_folder'))
            dialog.exec_()
            return
        
        # Создание выходной папки если не существует
        os.makedirs(output_folder, exist_ok=True)
        
        crs_text = self.dialog.processing_widget.crs_text.toPlainText().strip()
        if not crs_text:
            dialog = WarningDialog('Ошибка', translations.get_text('error_no_crs'))
            dialog.exec_()
            return
        
        # Получение выходного формата
        output_format = 'GeoJSON' if 'GeoJSON' in self.dialog.output_widget.output_format_combo.currentText() else 'ESRI Shapefile'
        
        # Очистка результатов
        self.dialog.results_table.setRowCount(0)
        self.dialog.log_message(f"🚀 === {translations.get_text('start_conversion')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        
        # Настройка UI для процесса конвертации
        self.dialog.progress_bar.setVisible(True)
        self.dialog.progress_bar.setValue(0)
        self.dialog.control_buttons.convert_button.setEnabled(False)
        self.dialog.control_buttons.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        self.dialog.control_buttons.cancel_button.setEnabled(True)
        
        # Создание и запуск воркера
        max_workers = self.dialog.processing_widget.threads_spinbox.value()
        self.dialog.worker = ConversionWorker(files_to_process, output_folder, crs_text, output_format, max_workers)
        self.dialog.worker_thread = QThread()
        self.dialog.worker.moveToThread(self.dialog.worker_thread)
        
        # Подключение сигналов
        self.dialog.worker_thread.started.connect(self.dialog.worker.run)
        self.dialog.worker.progress.connect(self.dialog.progress_bar.setValue)
        self.dialog.worker.log_message.connect(self.dialog.log_message)
        self.dialog.worker.file_completed.connect(self.onFileCompleted)
        self.dialog.worker.finished.connect(self.onConversionFinished)
        self.dialog.worker.error.connect(self.onConversionError)
        
        # Запуск
        self.dialog.worker_thread.start()
    
    def cancelConversion(self):
        """Отмена конвертации"""
        from ..translations import translations
        
        if self.dialog.worker:
            self.dialog.worker.cancel()
            self.dialog.log_message(f"⚠️ {translations.get_text('conversion_cancelled')}")
    
    def clearLogs(self):
        """Очистка логов и результатов"""
        self.dialog.log_text.clear()
        self.dialog.results_table.setRowCount(0)
        self.dialog.log_message("🧹 Logs and results cleared")
    
    def onFileCompleted(self, filename, success, message):
        """Обработка завершения файла"""
        from ..translations import translations
        
        # Добавление результата в таблицу
        row = self.dialog.results_table.rowCount()
        self.dialog.results_table.insertRow(row)
        
        # Файл
        file_item = QTableWidgetItem(filename)
        file_item.setToolTip(filename)
        self.dialog.results_table.setItem(row, 0, file_item)
        
        # Статус с иконками
        status_text = f"✅ {translations.get_text('success')}" if success else f"❌ {translations.get_text('error')}"
        status_item = QTableWidgetItem(status_text)
        
        if success:
            status_item.setBackground(QColor('#d5f4e6'))  # Светло-зеленый
            status_item.setForeground(QColor('#27ae60'))  # Темно-зеленый текст
        else:
            status_item.setBackground(QColor('#fadbd8'))  # Светло-красный
            status_item.setForeground(QColor('#e74c3c'))  # Темно-красный текст
            
        self.dialog.results_table.setItem(row, 1, status_item)
        
        # Сообщение
        message_item = QTableWidgetItem(message)
        message_item.setToolTip(message)
        self.dialog.results_table.setItem(row, 2, message_item)
        
        # Автоматическая прокрутка к последней строке
        self.dialog.results_table.scrollToBottom()
    
    def onConversionFinished(self):
        """Обработка завершения конвертации"""
        from ..translations import translations
        from .gui_dialogs import SuccessDialog, WarningDialog, ErrorDialog
        
        self.dialog.progress_bar.setValue(100)
        self.dialog.control_buttons.convert_button.setEnabled(True)
        self.dialog.control_buttons.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
        self.dialog.control_buttons.cancel_button.setEnabled(False)
        self.dialog.log_message(f"🎉 === Conversion completed {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        
        # Статистика
        total_files = self.dialog.results_table.rowCount()
        success_count = 0
        error_count = 0
        
        for row in range(total_files):
            status_item = self.dialog.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                success_count += 1
            else:
                error_count += 1
        
        self.dialog.log_message(f"📊 Statistics: {success_count} successful, {error_count} errors out of {total_files} files")
        
        # Добавление результата в проект если нужно
        if self.dialog.processing_widget.add_to_project_cb.isChecked() and success_count > 0:
            self.addResultsToProject()
        
        # Очистка воркера
        if self.dialog.worker_thread:
            self.dialog.worker_thread.quit()
            self.dialog.worker_thread.wait()
            self.dialog.worker_thread = None
            self.dialog.worker = None
        
        # Уведомление о завершении
        if success_count == total_files:
            dialog = SuccessDialog('Успех', f'All {total_files} files converted successfully!')
            dialog.exec_()
        elif success_count > 0:
            dialog = WarningDialog('Частичный успех', f'{success_count} files converted successfully, {error_count} failed.')
            dialog.exec_()
        else:
            dialog = ErrorDialog('Ошибка', 'No files were converted successfully.')
            dialog.exec_()
    
    def onConversionError(self, error_message):
        """Обработка критической ошибки"""
        from ..translations import translations
        from .gui_dialogs import ErrorDialog
        
        self.dialog.log_message(f"🔥 CRITICAL ERROR: {error_message}")
        dialog = ErrorDialog(translations.get_text('critical_error'), error_message)
        dialog.exec_()
        self.onConversionFinished()
    
    def addResultsToProject(self):
        """Добавление успешно конвертированных файлов в проект"""
        output_folder = self.dialog.output_widget.output_folder_line.text()
        crs_text = self.dialog.processing_widget.crs_text.toPlainText().strip()
        output_format = 'GeoJSON' if 'GeoJSON' in self.dialog.output_widget.output_format_combo.currentText() else 'ESRI Shapefile'
        
        # Создание CRS объекта
        crs = QgsCoordinateReferenceSystem()
        if crs_text.startswith('EPSG:'):
            epsg_code = int(crs_text.split(':')[1])
            crs.createFromId(epsg_code)
        else:
            crs.createFromString(crs_text)
        
        added_count = 0
        for row in range(self.dialog.results_table.rowCount()):
            status_item = self.dialog.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                filename = self.dialog.results_table.item(row, 0).text()
                
                if output_format == 'GeoJSON':
                    # Для GeoJSON файлов
                    if filename.lower().endswith('.mif'):
                        output_file = os.path.join(output_folder, filename.replace('.mif', '.geojson'))
                        layer_name = filename.replace('.mif', '')
                    else:  # .tab
                        output_file = os.path.join(output_folder, filename.replace('.tab', '.geojson'))
                        layer_name = filename.replace('.tab', '')
                else:
                    # Для Shapefile
                    if filename.lower().endswith('.mif'):
                        output_file = os.path.join(output_folder, filename.replace('.mif', '.shp'))
                        layer_name = filename.replace('.mif', '')
                    else:  # .tab
                        output_file = os.path.join(output_folder, filename.replace('.tab', '.shp'))
                        layer_name = filename.replace('.tab', '')
                
                if os.path.exists(output_file):
                    layer = QgsVectorLayer(output_file, layer_name, "ogr")
                    if layer.isValid():
                        layer.setCrs(crs)
                        QgsProject.instance().addMapLayer(layer)
                        added_count += 1
        
        if added_count > 0:
            self.dialog.log_message(f"📁 Added to project: {added_count} layers")
    
    def closeEvent(self, event):
        """Обработка закрытия окна"""
        from ..translations import translations
        from .gui_dialogs import ConfirmationDialog
        
        if (self.dialog.worker and self.dialog.worker_thread and 
            self.dialog.worker_thread.isRunning()):
            
            dialog = ConfirmationDialog(
                translations.get_text('confirmation'), 
                translations.get_text('confirm_close')
            )
            if dialog.exec_() == QMessageBox.Yes:
                self.cancelConversion()
                if self.dialog.worker_thread:
                    self.dialog.worker_thread.quit()
                    self.dialog.worker_thread.wait()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
