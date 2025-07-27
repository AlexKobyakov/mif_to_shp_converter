# -*- coding: utf-8 -*-
"""
MIF/TAB to SHP/GeoJSON Converter Plugin for QGIS
Конвертирует файлы MID/MIF и TAB в Shapefile или GeoJSON с поддержкой пакетной обработки и многопоточности

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import sys
import glob
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime

from qgis.PyQt.QtCore import (QSettings, QTranslator, QCoreApplication, Qt, 
                              pyqtSignal, QObject, QThread, QTimer, QLocale)
from qgis.PyQt.QtGui import QIcon, QFont, QPalette, QPixmap, QColor, QLinearGradient
from qgis.PyQt.QtWidgets import (QAction, QDialog, QVBoxLayout, QHBoxLayout, 
                                 QLabel, QLineEdit, QPushButton, QTextEdit, 
                                 QFileDialog, QMessageBox, QProgressBar, QCheckBox,
                                 QRadioButton, QButtonGroup, QGroupBox, QSpinBox,
                                 QSplitter, QTabWidget, QWidget, QTableWidget,
                                 QTableWidgetItem, QHeaderView, QAbstractItemView,
                                 QComboBox, QFrame, QScrollArea, QGridLayout)

from qgis.core import (QgsProject, QgsVectorLayer, QgsCoordinateReferenceSystem,
                       QgsVectorFileWriter, QgsWkbTypes, QgsFeature, QgsGeometry,
                       QgsField, QgsFields, Qgis, QgsApplication)
from qgis.utils import iface


class Translations:
    """Класс для управления переводами на 5 языков"""
    
    def __init__(self):
        self.current_language = 'ru'  # По умолчанию русский
        self.translations = {
            'ru': {
                'window_title': 'MIF/TAB в SHP/GeoJSON Конвертер - Пакетный конвертер',
                'conversion_mode': 'Режим конвертации',
                'single_file': 'Один файл',
                'batch_processing': 'Пакетная обработка (папка)',
                'input_file': 'Входной файл:',
                'input_folder': 'Папка с файлами:',
                'output_folder': 'Выходная папка:',
                'output_format': 'Выходной формат:',
                'browse': 'Обзор...',
                'threading_settings': 'Настройки многопоточности',
                'thread_count': 'Количество потоков:',
                'coordinate_system': 'Система координат',
                'crs_format_hint': 'Формат: EPSG:код, PROJ4 или WKT',
                'add_to_project': 'Добавить результат в проект QGIS',
                'progress': 'Прогресс:',
                'logs': 'Логи',
                'results': 'Результаты',
                'start_conversion': 'Начать конвертацию',
                'cancel': 'Отмена',
                'clear_logs': 'Очистить логи',
                'converting': 'Конвертация...',
                'language': 'Язык:',
                'file': 'Файл',
                'status': 'Статус',
                'message': 'Сообщение',
                'success': 'Успешно',
                'error': 'Ошибка',
                'select_input_file': 'Выберите входной файл',
                'select_input_folder': 'Выберите папку с файлами',
                'select_output_folder': 'Выберите выходную папку',
                'error_no_input_file': 'Выберите корректный входной файл',
                'error_no_input_folder': 'Выберите корректную папку',
                'error_no_files_found': 'В выбранной папке не найдено поддерживаемых файлов',
                'error_no_output_folder': 'Укажите выходную папку',
                'error_no_crs': 'Укажите систему координат',
                'conversion_cancelled': 'Отмена конвертации...',
                'confirm_close': 'Конвертация в процессе. Остановить и закрыть?',
                'confirmation': 'Подтверждение',
                'critical_error': 'Критическая ошибка',
                'supported_formats': 'MIF/TAB файлы (*.mif *.tab)',
                'author_info': 'Автор: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nГод создания: 2025',
                'about_author': 'Об авторе',
                'settings': 'Настройки',
                'input_output': 'Входные и выходные данные',
                'processing_options': 'Параметры обработки'
            },
            'en': {
                'window_title': 'MIF/TAB to SHP/GeoJSON Converter - Batch Converter',
                'conversion_mode': 'Conversion Mode',
                'single_file': 'Single File',
                'batch_processing': 'Batch Processing (Folder)',
                'input_file': 'Input File:',
                'input_folder': 'Input Folder:',
                'output_folder': 'Output Folder:',
                'output_format': 'Output Format:',
                'browse': 'Browse...',
                'threading_settings': 'Threading Settings',
                'thread_count': 'Thread Count:',
                'coordinate_system': 'Coordinate System',
                'crs_format_hint': 'Format: EPSG:code, PROJ4 or WKT',
                'add_to_project': 'Add result to QGIS project',
                'progress': 'Progress:',
                'logs': 'Logs',
                'results': 'Results',
                'start_conversion': 'Start Conversion',
                'cancel': 'Cancel',
                'clear_logs': 'Clear Logs',
                'converting': 'Converting...',
                'language': 'Language:',
                'file': 'File',
                'status': 'Status',
                'message': 'Message',
                'success': 'Success',
                'error': 'Error',
                'select_input_file': 'Select input file',
                'select_input_folder': 'Select input folder',
                'select_output_folder': 'Select output folder',
                'error_no_input_file': 'Select a valid input file',
                'error_no_input_folder': 'Select a valid folder',
                'error_no_files_found': 'No supported files found in selected folder',
                'error_no_output_folder': 'Specify output folder',
                'error_no_crs': 'Specify coordinate system',
                'conversion_cancelled': 'Cancelling conversion...',
                'confirm_close': 'Conversion in progress. Stop and close?',
                'confirmation': 'Confirmation',
                'critical_error': 'Critical Error',
                'supported_formats': 'MIF/TAB files (*.mif *.tab)',
                'author_info': 'Author: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nYear: 2025',
                'about_author': 'About Author',
                'settings': 'Settings',
                'input_output': 'Input & Output',
                'processing_options': 'Processing Options'
            },
            'zh': {
                'window_title': 'MIF/TAB转SHP/GeoJSON转换器 - 批量转换器',
                'conversion_mode': '转换模式',
                'single_file': '单个文件',
                'batch_processing': '批量处理（文件夹）',
                'input_file': '输入文件：',
                'input_folder': '输入文件夹：',
                'output_folder': '输出文件夹：',
                'output_format': '输出格式：',
                'browse': '浏览...',
                'threading_settings': '多线程设置',
                'thread_count': '线程数：',
                'coordinate_system': '坐标系统',
                'crs_format_hint': '格式：EPSG:代码、PROJ4或WKT',
                'add_to_project': '将结果添加到QGIS项目',
                'progress': '进度：',
                'logs': '日志',
                'results': '结果',
                'start_conversion': '开始转换',
                'cancel': '取消',
                'clear_logs': '清除日志',
                'converting': '转换中...',
                'language': '语言：',
                'file': '文件',
                'status': '状态',
                'message': '消息',
                'success': '成功',
                'error': '错误',
                'select_input_file': '选择输入文件',
                'select_input_folder': '选择输入文件夹',
                'select_output_folder': '选择输出文件夹',
                'error_no_input_file': '请选择有效的输入文件',
                'error_no_input_folder': '请选择有效的文件夹',
                'error_no_files_found': '在选定文件夹中未找到支持的文件',
                'error_no_output_folder': '请指定输出文件夹',
                'error_no_crs': '请指定坐标系统',
                'conversion_cancelled': '正在取消转换...',
                'confirm_close': '转换正在进行中。停止并关闭？',
                'confirmation': '确认',
                'critical_error': '严重错误',
                'supported_formats': 'MIF/TAB文件 (*.mif *.tab)',
                'author_info': '作者：Кобяков Александр Викторович (Alex Kobyakov)\n邮箱：kobyakov@lesburo.ru\n创建年份：2025',
                'about_author': '关于作者',
                'settings': '设置',
                'input_output': '输入输出',
                'processing_options': '处理选项'
            },
            'hi': {
                'window_title': 'MIF/TAB से SHP/GeoJSON कन्वर्टर - बैच कन्वर्टर',
                'conversion_mode': 'रूपांतरण मोड',
                'single_file': 'एकल फ़ाइल',
                'batch_processing': 'बैच प्रोसेसिंग (फ़ोल्डर)',
                'input_file': 'इनपुट फ़ाइल:',
                'input_folder': 'इनपुट फ़ोल्डर:',
                'output_folder': 'आउटपुट फ़ोल्डर:',
                'output_format': 'आउटपुट प्रारूप:',
                'browse': 'ब्राउज़...',
                'threading_settings': 'थ्रेडिंग सेटिंग्स',
                'thread_count': 'थ्रेड गिनती:',
                'coordinate_system': 'समन्वय प्रणाली',
                'crs_format_hint': 'प्रारूप: EPSG:कोड, PROJ4 या WKT',
                'add_to_project': 'QGIS प्रोजेक्ट में परिणाम जोड़ें',
                'progress': 'प्रगति:',
                'logs': 'लॉग',
                'results': 'परिणाम',
                'start_conversion': 'रूपांतरण शुरू करें',
                'cancel': 'रद्द करें',
                'clear_logs': 'लॉग साफ़ करें',
                'converting': 'रूपांतरित कर रहा है...',
                'language': 'भाषा:',
                'file': 'फ़ाइल',
                'status': 'स्थिति',
                'message': 'संदेश',
                'success': 'सफल',
                'error': 'त्रुटि',
                'select_input_file': 'इनपुट फ़ाइल चुनें',
                'select_input_folder': 'इनपुट फ़ोल्डर चुनें',
                'select_output_folder': 'आउटपुट फ़ोल्डर चुनें',
                'error_no_input_file': 'एक वैध इनपुट फ़ाइल चुनें',
                'error_no_input_folder': 'एक वैध फ़ोल्डर चुनें',
                'error_no_files_found': 'चयनित फ़ोल्डर में कोई समर्थित फ़ाइल नहीं मिली',
                'error_no_output_folder': 'आउटपुट फ़ोल्डर निर्दिष्ट करें',
                'error_no_crs': 'समन्वय प्रणाली निर्दिष्ट करें',
                'conversion_cancelled': 'रूपांतरण रद्द कर रहा है...',
                'confirm_close': 'रूपांतरण प्रगति में है। रोकें और बंद करें?',
                'confirmation': 'पुष्टि',
                'critical_error': 'गंभीर त्रुटि',
                'supported_formats': 'MIF/TAB फ़ाइलें (*.mif *.tab)',
                'author_info': 'लेखक: Кобяков Александр Викторович (Alex Kobyakov)\nईमेल: kobyakov@lesburo.ru\nवर्ष: 2025',
                'about_author': 'लेखक के बारे में',
                'settings': 'सेटिंग्स',
                'input_output': 'इनपुट आउटपुट',
                'processing_options': 'प्रसंस्करण विकल्प'
            },
            'es': {
                'window_title': 'Convertidor MIF/TAB a SHP/GeoJSON - Convertidor por Lotes',
                'conversion_mode': 'Modo de Conversión',
                'single_file': 'Archivo Único',
                'batch_processing': 'Procesamiento por Lotes (Carpeta)',
                'input_file': 'Archivo de Entrada:',
                'input_folder': 'Carpeta de Entrada:',
                'output_folder': 'Carpeta de Salida:',
                'output_format': 'Formato de Salida:',
                'browse': 'Examinar...',
                'threading_settings': 'Configuración de Hilos',
                'thread_count': 'Cantidad de Hilos:',
                'coordinate_system': 'Sistema de Coordenadas',
                'crs_format_hint': 'Formato: EPSG:código, PROJ4 o WKT',
                'add_to_project': 'Agregar resultado al proyecto QGIS',
                'progress': 'Progreso:',
                'logs': 'Registros',
                'results': 'Resultados',
                'start_conversion': 'Iniciar Conversión',
                'cancel': 'Cancelar',
                'clear_logs': 'Limpiar Registros',
                'converting': 'Convirtiendo...',
                'language': 'Idioma:',
                'file': 'Archivo',
                'status': 'Estado',
                'message': 'Mensaje',
                'success': 'Éxito',
                'error': 'Error',
                'select_input_file': 'Seleccionar archivo de entrada',
                'select_input_folder': 'Seleccionar carpeta de entrada',
                'select_output_folder': 'Seleccionar carpeta de salida',
                'error_no_input_file': 'Seleccionar un archivo de entrada válido',
                'error_no_input_folder': 'Seleccionar una carpeta válida',
                'error_no_files_found': 'No se encontraron archivos compatibles en la carpeta seleccionada',
                'error_no_output_folder': 'Especificar carpeta de salida',
                'error_no_crs': 'Especificar sistema de coordenadas',
                'conversion_cancelled': 'Cancelando conversión...',
                'confirm_close': '¿Conversión en progreso. Detener y cerrar?',
                'confirmation': 'Confirmación',
                'critical_error': 'Error Crítico',
                'supported_formats': 'Archivos MIF/TAB (*.mif *.tab)',
                'author_info': 'Autor: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nAño: 2025',
                'about_author': 'Acerca del Autor',
                'settings': 'Configuración',
                'input_output': 'Entrada y Salida',
                'processing_options': 'Opciones de Procesamiento'
            }
        }
    
    def get_text(self, key):
        return self.translations.get(self.current_language, {}).get(key, key)
    
    def set_language(self, language):
        if language in self.translations:
            self.current_language = language


# Глобальный объект переводов
translations = Translations()


class ModernGroupBox(QGroupBox):
    """Современная группа с улучшенным стилем"""
    def __init__(self, title=""):
        super().__init__(title)
        self.setStyleSheet("""
            QGroupBox {
                font-weight: bold;
                border: 2px solid #cccccc;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
                background-color: #f8f9fa;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 8px 0 8px;
                color: #2c3e50;
                background-color: #ecf0f1;
                border-radius: 4px;
            }
        """)


class ModernButton(QPushButton):
    """Современная кнопка с улучшенным стилем"""
    def __init__(self, text="", primary=False):
        super().__init__(text)
        if primary:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 6px;
                    font-weight: bold;
                    font-size: 13px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #21618c;
                }
                QPushButton:disabled {
                    background-color: #bdc3c7;
                }
            """)
        else:
            self.setStyleSheet("""
                QPushButton {
                    background-color: #ecf0f1;
                    color: #2c3e50;
                    border: 2px solid #bdc3c7;
                    padding: 8px 16px;
                    border-radius: 6px;
                    font-size: 13px;
                }
                QPushButton:hover {
                    background-color: #d5dbdb;
                    border-color: #85929e;
                }
                QPushButton:pressed {
                    background-color: #aeb6bf;
                }
            """)


class ModernProgressBar(QProgressBar):
    """Современный прогресс-бар"""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QProgressBar {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
                background-color: #ecf0f1;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #3498db, stop: 1 #2ecc71);
                border-radius: 6px;
            }
        """)


# Worker класс для многопоточной обработки
class ConversionWorker(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    log_message = pyqtSignal(str)
    file_completed = pyqtSignal(str, bool, str)

    def __init__(self, files_list, output_dir, crs_text, output_format, max_workers=4):
        super().__init__()
        self.files_list = files_list
        self.output_dir = output_dir
        self.crs_text = crs_text
        self.output_format = output_format
        self.max_workers = max_workers
        self.is_cancelled = False
        
    def cancel(self):
        self.is_cancelled = True
        
    def run(self):
        try:
            total_files = len(self.files_list)
            completed = 0
            
            self.log_message.emit(f"Starting conversion of {total_files} files...")
            self.log_message.emit(f"Using {self.max_workers} threads")
            self.log_message.emit(f"Output format: {self.output_format}")
            
            # Создание CRS объекта
            crs = QgsCoordinateReferenceSystem()
            if self.crs_text.startswith('EPSG:'):
                epsg_code = int(self.crs_text.split(':')[1])
                crs.createFromId(epsg_code)
            else:
                crs.createFromString(self.crs_text)
            
            if not crs.isValid():
                self.error.emit('Invalid coordinate system')
                return
            
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_file = {
                    executor.submit(self.convert_single_file, file_path, crs): file_path 
                    for file_path in self.files_list
                }
                
                for future in as_completed(future_to_file):
                    if self.is_cancelled:
                        break
                        
                    file_path = future_to_file[future]
                    try:
                        success, message = future.result()
                        self.file_completed.emit(os.path.basename(file_path), success, message)
                        
                        if success:
                            self.log_message.emit(f"✓ {os.path.basename(file_path)}: {message}")
                        else:
                            self.log_message.emit(f"✗ {os.path.basename(file_path)}: {message}")
                            
                    except Exception as e:
                        self.log_message.emit(f"✗ {os.path.basename(file_path)}: Error - {str(e)}")
                        self.file_completed.emit(os.path.basename(file_path), False, str(e))
                    
                    completed += 1
                    progress_value = int((completed / total_files) * 100)
                    self.progress.emit(progress_value)
            
            if not self.is_cancelled:
                self.log_message.emit(f"Conversion completed. Processed files: {completed}")
            else:
                self.log_message.emit("Conversion cancelled by user")
                
        except Exception as e:
            self.error.emit(f"Critical error: {str(e)}")
        finally:
            self.finished.emit()
    
    def convert_single_file(self, input_file, crs):
        try:
            filename = os.path.basename(input_file)
            
            if self.output_format == 'GeoJSON':
                if filename.lower().endswith('.mif'):
                    output_file = os.path.join(self.output_dir, filename.replace('.mif', '.geojson'))
                else:
                    output_file = os.path.join(self.output_dir, filename.replace('.tab', '.geojson'))
                driver_name = "GeoJSON"
            else:
                if filename.lower().endswith('.mif'):
                    output_file = os.path.join(self.output_dir, filename.replace('.mif', '.shp'))
                else:
                    output_file = os.path.join(self.output_dir, filename.replace('.tab', '.shp'))
                driver_name = "ESRI Shapefile"
            
            layer = QgsVectorLayer(input_file, "temp_layer", "ogr")
            if not layer.isValid():
                return False, f"Failed to load {filename}"
            
            layer.setCrs(crs)
            
            save_options = QgsVectorFileWriter.SaveVectorOptions()
            save_options.driverName = driver_name
            save_options.fileEncoding = "UTF-8"
            
            error = QgsVectorFileWriter.writeAsVectorFormatV3(
                layer, output_file, QgsProject.instance().transformContext(), save_options)
            
            if error[0] == QgsVectorFileWriter.NoError:
                return True, f"Successfully converted to {os.path.basename(output_file)}"
            else:
                return False, f"Write error: {error[1]}"
                
        except Exception as e:
            return False, f"Processing error: {str(e)}"


# Основной класс плагина
class MifToShpConverter:
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        
        # Инициализация переводов
        locale = QSettings().value('locale/userLocale')[0:2]
        if locale == 'en':
            translations.set_language('en')
        elif locale == 'zh':
            translations.set_language('zh')
        elif locale == 'hi':
            translations.set_language('hi')
        elif locale == 'es':
            translations.set_language('es')
        else:
            translations.set_language('ru')

        self.actions = []
        self.menu = self.tr('&MIF/TAB to SHP/GeoJSON Converter')
        self.first_start = None

    def tr(self, message):
        return QCoreApplication.translate('MifToShpConverter', message)

    def add_action(self, icon_path, text, callback, enabled_flag=True,
                   add_to_menu=True, add_to_toolbar=True, status_tip=None,
                   whats_this=None, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        icon_path = ':/plugins/mif_to_shp_converter/icon.png'
        self.add_action(
            icon_path,
            text=self.tr('Convert MIF/TAB to SHP/GeoJSON'),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.first_start = True

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.tr('&MIF/TAB to SHP/GeoJSON Converter'), action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        if self.first_start:
            self.first_start = False
            self.dlg = MifToShpDialog()

        self.dlg.show()
        result = self.dlg.exec_()


# Улучшенное диалоговое окно с современным дизайном
class MifToShpDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.worker = None
        self.worker_thread = None
        self.setupUi()
        self.connectSignals()
        self.updateLanguage()
        self.applyModernStyle()

    def applyModernStyle(self):
        """Применение современного стиля к диалогу"""
        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QLabel {
                color: #2c3e50;
                font-size: 13px;
            }
            QLineEdit {
                border: 2px solid #ddd;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                background-color: #ffffff;
            }
            QLineEdit:focus {
                border-color: #3498db;
            }
            QTextEdit {
                border: 2px solid #ddd;
                border-radius: 6px;
                padding: 8px;
                font-size: 12px;
                background-color: #ffffff;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
            QComboBox {
                border: 2px solid #ddd;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                background-color: #ffffff;
                min-width: 120px;
            }
            QComboBox:focus {
                border-color: #3498db;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border: 2px solid #3498db;
                width: 8px;
                height: 8px;
                border-radius: 2px;
            }
            QSpinBox {
                border: 2px solid #ddd;
                border-radius: 6px;
                padding: 8px;
                font-size: 13px;
                background-color: #ffffff;
                min-width: 80px;
            }
            QSpinBox:focus {
                border-color: #3498db;
            }
            QCheckBox {
                color: #2c3e50;
                font-size: 13px;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #bdc3c7;
                border-radius: 4px;
                background-color: #ffffff;
            }
            QCheckBox::indicator:checked {
                background-color: #3498db;
                border-color: #3498db;
            }
            QRadioButton {
                color: #2c3e50;
                font-size: 13px;
                spacing: 8px;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #bdc3c7;
                border-radius: 9px;
                background-color: #ffffff;
            }
            QRadioButton::indicator:checked {
                background-color: #3498db;
                border-color: #3498db;
            }
            QTabWidget::pane {
                border: 2px solid #ddd;
                border-radius: 6px;
                background-color: #ffffff;
            }
            QTabBar::tab {
                background-color: #ecf0f1;
                border: 2px solid #bdc3c7;
                border-bottom: none;
                border-radius: 6px 6px 0 0;
                padding: 8px 16px;
                margin-right: 2px;
                font-size: 13px;
                color: #2c3e50;
            }
            QTabBar::tab:selected {
                background-color: #3498db;
                color: white;
                border-color: #3498db;
            }
            QTabBar::tab:hover {
                background-color: #d5dbdb;
            }
            QTableWidget {
                border: 2px solid #ddd;
                border-radius: 6px;
                background-color: #ffffff;
                gridline-color: #ecf0f1;
                font-size: 12px;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ecf0f1;
            }
            QTableWidget::item:selected {
                background-color: #3498db;
                color: white;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
                font-size: 13px;
            }
            QSplitter::handle {
                background-color: #bdc3c7;
                border-radius: 2px;
            }
            QSplitter::handle:horizontal {
                width: 4px;
            }
            QSplitter::handle:vertical {
                height: 4px;
            }
        """)

    def setupUi(self):
        self.setWindowTitle('MIF/TAB to SHP/GeoJSON Converter')
        self.setMinimumSize(1000, 800)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Заголовок приложения
        header_frame = QFrame()
        header_frame.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #3498db, stop: 1 #2ecc71);
                border-radius: 10px;
                padding: 15px;
            }
        """)
        header_layout = QHBoxLayout()
        
        title_label = QLabel("🗺️ MIF/TAB to SHP/GeoJSON Converter")
        title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 20px;
                font-weight: bold;
                background: transparent;
            }
        """)
        
        # Панель языка и информации об авторе
        lang_layout = QHBoxLayout()
        self.lang_label = QLabel('Language:')
        self.lang_label.setStyleSheet("QLabel { color: white; font-size: 14px; background: transparent; }")
        
        self.lang_combo = QComboBox()
        self.lang_combo.addItems(['🇷🇺 Русский', '🇺🇸 English', '🇨🇳 中文', '🇮🇳 हिंदी', '🇪🇸 Español'])
        self.lang_combo.setCurrentText('🇷🇺 Русский' if translations.current_language == 'ru' else 
                                      '🇺🇸 English' if translations.current_language == 'en' else
                                      '🇨🇳 中文' if translations.current_language == 'zh' else
                                      '🇮🇳 हिंदी' if translations.current_language == 'hi' else
                                      '🇪🇸 Español')
        self.lang_combo.setStyleSheet("""
            QComboBox {
                background-color: rgba(255, 255, 255, 0.9);
                color: #2c3e50;
                border: none;
                border-radius: 6px;
                font-size: 13px;
                min-width: 150px;
            }
        """)
        
        # Информация об авторе
        author_button = ModernButton('👤 About Author / Об авторе')
        author_button.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.9);
                color: #2c3e50;
                border: none;
                border-radius: 6px;
                font-weight: bold;
                font-size: 13px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 1.0);
            }
        """)
        author_button.clicked.connect(self.showAuthorInfo)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        lang_layout.addWidget(self.lang_label)
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addWidget(author_button)
        header_layout.addLayout(lang_layout)
        
        header_frame.setLayout(header_layout)
        main_layout.addWidget(header_frame)
        
        # Создание сплиттера для разделения настроек и логов
        splitter = QSplitter(Qt.Vertical)
        
        # Верхняя часть - настройки в прокручиваемой области
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        
        settings_widget = QWidget()
        settings_layout = QVBoxLayout()
        settings_layout.setSpacing(20)
        
        # Создание табов для настроек
        settings_tabs = QTabWidget()
        
        # Таб 1: Входные и выходные данные
        io_tab = QWidget()
        io_layout = QVBoxLayout()
        io_layout.setSpacing(15)
        
        # Группа выбора режима
        self.mode_group_box = ModernGroupBox("🔄 Conversion Mode")
        mode_layout = QHBoxLayout()
        
        self.mode_group = QButtonGroup()
        self.single_mode = QRadioButton("📄 Single File")
        self.batch_mode = QRadioButton("📁 Batch Processing")
        self.single_mode.setChecked(True)
        
        self.mode_group.addButton(self.single_mode, 0)
        self.mode_group.addButton(self.batch_mode, 1)
        
        mode_layout.addWidget(self.single_mode)
        mode_layout.addWidget(self.batch_mode)
        mode_layout.addStretch()
        self.mode_group_box.setLayout(mode_layout)
        io_layout.addWidget(self.mode_group_box)
        
        # Группа входных данных
        input_group = ModernGroupBox("📥 Input Data")
        input_layout = QVBoxLayout()
        
        # Одиночный файл
        self.single_file_layout = QHBoxLayout()
        self.input_file_label = QLabel('📄 Input File:')
        self.input_file_line = QLineEdit()
        self.input_file_button = ModernButton('📂 Browse...')
        self.single_file_layout.addWidget(self.input_file_label)
        self.single_file_layout.addWidget(self.input_file_line)
        self.single_file_layout.addWidget(self.input_file_button)
        
        # Папка для пакетной обработки
        self.batch_folder_layout = QHBoxLayout()
        self.input_folder_label = QLabel('📁 Input Folder:')
        self.input_folder_line = QLineEdit()
        self.input_folder_button = ModernButton('📂 Browse...')
        self.batch_folder_layout.addWidget(self.input_folder_label)
        self.batch_folder_layout.addWidget(self.input_folder_line)
        self.batch_folder_layout.addWidget(self.input_folder_button)
        
        # Создание виджетов для скрытия/показа
        self.single_widget = QWidget()
        self.single_widget.setLayout(self.single_file_layout)
        
        self.batch_widget = QWidget()
        self.batch_widget.setLayout(self.batch_folder_layout)
        self.batch_widget.setVisible(False)
        
        input_layout.addWidget(self.single_widget)
        input_layout.addWidget(self.batch_widget)
        input_group.setLayout(input_layout)
        io_layout.addWidget(input_group)
        
        # Группа выходных данных
        output_group = ModernGroupBox("📤 Output Data")
        output_layout = QVBoxLayout()
        
        # Выходная папка
        folder_layout = QHBoxLayout()
        self.output_folder_label = QLabel('📁 Output Folder:')
        self.output_folder_line = QLineEdit()
        self.output_folder_button = ModernButton('📂 Browse...')
        folder_layout.addWidget(self.output_folder_label)
        folder_layout.addWidget(self.output_folder_line)
        folder_layout.addWidget(self.output_folder_button)
        output_layout.addLayout(folder_layout)
        
        # Выходной формат
        format_layout = QHBoxLayout()
        self.output_format_label = QLabel('📋 Output Format:')
        self.output_format_combo = QComboBox()
        self.output_format_combo.addItems(['🗺️ ESRI Shapefile', '🌐 GeoJSON'])
        format_layout.addWidget(self.output_format_label)
        format_layout.addWidget(self.output_format_combo)
        format_layout.addStretch()
        output_layout.addLayout(format_layout)
        
        output_group.setLayout(output_layout)
        io_layout.addWidget(output_group)
        
        io_tab.setLayout(io_layout)
        settings_tabs.addTab(io_tab, "📥📤 Input & Output")
        
        # Таб 2: Параметры обработки
        processing_tab = QWidget()
        processing_layout = QVBoxLayout()
        processing_layout.setSpacing(15)
        
        # Настройки многопоточности
        self.threading_group = ModernGroupBox("⚡ Threading Settings")
        threading_layout = QGridLayout()
        
        self.thread_count_label = QLabel('🧵 Thread Count:')
        self.threads_spinbox = QSpinBox()
        self.threads_spinbox.setMinimum(1)
        self.threads_spinbox.setMaximum(16)
        self.threads_spinbox.setValue(4)
        
        thread_info_label = QLabel('💡 Tip: More threads = faster processing for multiple files')
        thread_info_label.setStyleSheet("QLabel { color: #7f8c8d; font-style: italic; }")
        
        threading_layout.addWidget(self.thread_count_label, 0, 0)
        threading_layout.addWidget(self.threads_spinbox, 0, 1)
        threading_layout.addWidget(thread_info_label, 1, 0, 1, 2)
        threading_layout.setColumnStretch(2, 1)
        
        self.threading_group.setLayout(threading_layout)
        processing_layout.addWidget(self.threading_group)
        
        # Система координат
        self.crs_group = ModernGroupBox("🌍 Coordinate System")
        crs_layout = QVBoxLayout()
        
        crs_info_layout = QHBoxLayout()
        self.crs_hint_label = QLabel('📝 Format: EPSG:code, PROJ4 or WKT')
        crs_examples_button = ModernButton('📖 Examples')
        crs_examples_button.clicked.connect(self.showCrsExamples)
        crs_info_layout.addWidget(self.crs_hint_label)
        crs_info_layout.addWidget(crs_examples_button)
        crs_info_layout.addStretch()
        crs_layout.addLayout(crs_info_layout)
        
        self.crs_text = QTextEdit()
        self.crs_text.setMaximumHeight(80)
        self.crs_text.setPlainText('EPSG:4326')
        crs_layout.addWidget(self.crs_text)
        
        self.add_to_project_cb = QCheckBox('✅ Add result to QGIS project')
        self.add_to_project_cb.setChecked(True)
        crs_layout.addWidget(self.add_to_project_cb)
        
        self.crs_group.setLayout(crs_layout)
        processing_layout.addWidget(self.crs_group)
        
        processing_layout.addStretch()
        processing_tab.setLayout(processing_layout)
        settings_tabs.addTab(processing_tab, "⚙️ Processing Options")
        
        settings_layout.addWidget(settings_tabs)
        settings_widget.setLayout(settings_layout)
        scroll_area.setWidget(settings_widget)
        splitter.addWidget(scroll_area)
        
        # Нижняя часть - прогресс и логи
        progress_widget = QWidget()
        progress_layout = QVBoxLayout()
        progress_layout.setSpacing(10)
        
        # Прогресс бар с улучшенным дизайном
        progress_header = QHBoxLayout()
        self.progress_label = QLabel('📊 Progress:')
        self.progress_label.setStyleSheet("QLabel { font-weight: bold; }")
        progress_header.addWidget(self.progress_label)
        progress_header.addStretch()
        progress_layout.addLayout(progress_header)
        
        self.progress_bar = ModernProgressBar()
        self.progress_bar.setVisible(False)
        self.progress_bar.setMinimumHeight(25)
        progress_layout.addWidget(self.progress_bar)
        
        # Табы для логов и результатов с иконками
        self.tab_widget = QTabWidget()
        
        # Таб с логами
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setFont(QFont("Consolas", 10))
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: 'Consolas', 'Monaco', monospace;
                line-height: 1.4;
            }
        """)
        self.tab_widget.addTab(self.log_text, "📋 Logs")
        
        # Таб с результатами
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(['📄 File', '📊 Status', '💬 Message'])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.results_table.setAlternatingRowColors(True)
        self.tab_widget.addTab(self.results_table, "📈 Results")
        
        progress_layout.addWidget(self.tab_widget)
        progress_widget.setLayout(progress_layout)
        splitter.addWidget(progress_widget)
        
        # Установка пропорций сплиттера
        splitter.setSizes([500, 300])
        main_layout.addWidget(splitter)
        
        # Кнопки управления с улучшенным дизайном
        button_frame = QFrame()
        button_frame.setStyleSheet("""
            QFrame {
                background-color: #ecf0f1;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        button_layout = QHBoxLayout()
        
        self.convert_button = ModernButton('🚀 Start Conversion', primary=True)
        self.cancel_button = ModernButton('❌ Cancel')
        self.clear_log_button = ModernButton('🧹 Clear Logs')
        
        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.clear_log_button)
        button_layout.addStretch()
        
        button_frame.setLayout(button_layout)
        main_layout.addWidget(button_frame)
        
        self.setLayout(main_layout)

    def showCrsExamples(self):
        """Показать примеры систем координат"""
        examples_text = """
🌍 Common Coordinate Systems Examples:

📍 Geographic Coordinate Systems:
• EPSG:4326 - WGS 84 (World)
• EPSG:4269 - NAD83 (North America)
• EPSG:4258 - ETRS89 (Europe)

📍 Projected Coordinate Systems:
• EPSG:3857 - Web Mercator (Google Maps)
• EPSG:32633 - UTM Zone 33N (Europe)
• EPSG:2154 - RGF93 / Lambert-93 (France)
• EPSG:3395 - World Mercator

📍 Russian Coordinate Systems:
• EPSG:3857 - Pseudo-Mercator
• EPSG:4284 - Pulkovo 1942
• EPSG:28403 - Pulkovo 1942 / Gauss-Kruger zone 3

Just enter the EPSG code like: EPSG:4326
"""
        QMessageBox.information(self, '📖 CRS Examples', examples_text)

    def connectSignals(self):
        # Кнопки файлов и папок
        self.input_file_button.clicked.connect(self.selectInputFile)
        self.input_folder_button.clicked.connect(self.selectInputFolder)
        self.output_folder_button.clicked.connect(self.selectOutputFolder)
        
        # Переключение режимов
        self.mode_group.buttonClicked.connect(self.onModeChanged)
        
        # Кнопки управления
        self.convert_button.clicked.connect(self.startConversion)
        self.cancel_button.clicked.connect(self.cancelConversion)
        self.clear_log_button.clicked.connect(self.clearLogs)
        
        # Смена языка
        self.lang_combo.currentTextChanged.connect(self.onLanguageChanged)

    def onLanguageChanged(self, text):
        if '🇺🇸 English' in text:
            translations.set_language('en')
        elif '🇨🇳 中文' in text:
            translations.set_language('zh')
        elif '🇮🇳 हिंदी' in text:
            translations.set_language('hi')
        elif '🇪🇸 Español' in text:
            translations.set_language('es')
        else:
            translations.set_language('ru')
        self.updateLanguage()

    def updateLanguage(self):
        """Обновление текстов интерфейса"""
        self.setWindowTitle(translations.get_text('window_title'))
        
        # Обновление всех текстов
        self.mode_group_box.setTitle(f"🔄 {translations.get_text('conversion_mode')}")
        self.single_mode.setText(f"📄 {translations.get_text('single_file')}")
        self.batch_mode.setText(f"📁 {translations.get_text('batch_processing')}")
        
        self.input_file_label.setText(f"📄 {translations.get_text('input_file')}")
        self.input_folder_label.setText(f"📁 {translations.get_text('input_folder')}")
        self.output_folder_label.setText(f"📁 {translations.get_text('output_folder')}")
        self.output_format_label.setText(f"📋 {translations.get_text('output_format')}")
        
        self.input_file_button.setText(f"📂 {translations.get_text('browse')}")
        self.input_folder_button.setText(f"📂 {translations.get_text('browse')}")
        self.output_folder_button.setText(f"📂 {translations.get_text('browse')}")
        
        self.threading_group.setTitle(f"⚡ {translations.get_text('threading_settings')}")
        self.thread_count_label.setText(f"🧵 {translations.get_text('thread_count')}")
        
        self.crs_group.setTitle(f"🌍 {translations.get_text('coordinate_system')}")
        self.crs_hint_label.setText(f"📝 {translations.get_text('crs_format_hint')}")
        self.add_to_project_cb.setText(f"✅ {translations.get_text('add_to_project')}")
        
        self.progress_label.setText(f"📊 {translations.get_text('progress')}")
        
        # Обновление табов
        self.tab_widget.setTabText(0, f"📋 {translations.get_text('logs')}")
        self.tab_widget.setTabText(1, f"📈 {translations.get_text('results')}")
        
        # Обновление заголовков таблицы
        self.results_table.setHorizontalHeaderLabels([
            f"📄 {translations.get_text('file')}",
            f"📊 {translations.get_text('status')}",
            f"💬 {translations.get_text('message')}"
        ])
        
        # Обновление кнопок
        if 'Converting' in self.convert_button.text() or 'Конвертация' in self.convert_button.text():
            self.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        else:
            self.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
            
        self.cancel_button.setText(f"❌ {translations.get_text('cancel')}")
        self.clear_log_button.setText(f"🧹 {translations.get_text('clear_logs')}")

    def showAuthorInfo(self):
        """Показать информацию об авторе"""
        author_dialog = QMessageBox()
        author_dialog.setWindowTitle('👤 Author Information')
        author_dialog.setTextFormat(Qt.RichText)
        author_dialog.setText(f"""
        <div style="text-align: center; padding: 20px;">
            <h2 style="color: #3498db;">🎯 MIF/TAB to SHP/GeoJSON Converter</h2>
            <hr style="border: 1px solid #bdc3c7;">
            <p><b>👨‍💻 Author:</b> Кобяков Александр Викторович<br>
            <i>(Alex Kobyakov)</i></p>
            <p><b>📧 Email:</b> <a href="mailto:kobyakov@lesburo.ru">kobyakov@lesburo.ru</a></p>
            <p><b>📅 Year:</b> 2025</p>
            <p><b>🏢 Organization:</b> Lesburo</p>
            <hr style="border: 1px solid #bdc3c7;">
            <p style="color: #7f8c8d; font-style: italic;">
            Professional GIS data conversion tool<br>
            Supporting multiple languages and formats
            </p>
        </div>
        """)
        author_dialog.setStandardButtons(QMessageBox.Ok)
        author_dialog.exec_()

    def onModeChanged(self):
        is_batch = self.batch_mode.isChecked()
        self.single_widget.setVisible(not is_batch)
        self.batch_widget.setVisible(is_batch)

    def selectInputFile(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, translations.get_text('select_input_file'), '', 
            translations.get_text('supported_formats'))
        if filename:
            self.input_file_line.setText(filename)
            if not self.output_folder_line.text():
                self.output_folder_line.setText(os.path.dirname(filename))

    def selectInputFolder(self):
        folder = QFileDialog.getExistingDirectory(self, translations.get_text('select_input_folder'))
        if folder:
            self.input_folder_line.setText(folder)
            if not self.output_folder_line.text():
                self.output_folder_line.setText(folder)

    def selectOutputFolder(self):
        folder = QFileDialog.getExistingDirectory(self, translations.get_text('select_output_folder'))
        if folder:
            self.output_folder_line.setText(folder)

    def startConversion(self):
        # Сбор файлов для обработки
        files_to_process = []
        
        if self.single_mode.isChecked():
            input_file = self.input_file_line.text()
            if not input_file or not os.path.exists(input_file):
                QMessageBox.warning(self, 'Error', translations.get_text('error_no_input_file'))
                return
            files_to_process = [input_file]
        else:
            input_folder = self.input_folder_line.text()
            if not input_folder or not os.path.exists(input_folder):
                QMessageBox.warning(self, 'Error', translations.get_text('error_no_input_folder'))
                return
            
            # Поиск всех поддерживаемых файлов в папке (MIF и TAB)
            mif_pattern = os.path.join(input_folder, '*.mif')
            tab_pattern = os.path.join(input_folder, '*.tab')
            files_to_process = glob.glob(mif_pattern) + glob.glob(tab_pattern)
            
            if not files_to_process:
                QMessageBox.warning(self, 'Error', translations.get_text('error_no_files_found'))
                return
        
        output_folder = self.output_folder_line.text()
        if not output_folder:
            QMessageBox.warning(self, 'Error', translations.get_text('error_no_output_folder'))
            return
        
        # Создание выходной папки если не существует
        os.makedirs(output_folder, exist_ok=True)
        
        crs_text = self.crs_text.toPlainText().strip()
        if not crs_text:
            QMessageBox.warning(self, 'Error', translations.get_text('error_no_crs'))
            return
        
        # Получение выходного формата
        output_format = 'GeoJSON' if 'GeoJSON' in self.output_format_combo.currentText() else 'ESRI Shapefile'
        
        # Очистка результатов
        self.results_table.setRowCount(0)
        self.log_message(f"🚀 === {translations.get_text('start_conversion')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        
        # Настройка UI для процесса конвертации
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.convert_button.setEnabled(False)
        self.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        
        # Создание и запуск воркера
        max_workers = self.threads_spinbox.value()
        self.worker = ConversionWorker(files_to_process, output_folder, crs_text, output_format, max_workers)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        
        # Подключение сигналов
        self.worker_thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.log_message.connect(self.log_message)
        self.worker.file_completed.connect(self.onFileCompleted)
        self.worker.finished.connect(self.onConversionFinished)
        self.worker.error.connect(self.onConversionError)
        
        # Запуск
        self.worker_thread.start()

    def cancelConversion(self):
        if self.worker:
            self.worker.cancel()
            self.log_message(f"⚠️ {translations.get_text('conversion_cancelled')}")

    def onFileCompleted(self, filename, success, message):
        # Добавление результата в таблицу
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        
        # Файл
        file_item = QTableWidgetItem(filename)
        file_item.setToolTip(filename)
        self.results_table.setItem(row, 0, file_item)
        
        # Статус с иконками
        status_text = f"✅ {translations.get_text('success')}" if success else f"❌ {translations.get_text('error')}"
        status_item = QTableWidgetItem(status_text)
        
        if success:
            status_item.setBackground(QColor('#d5f4e6'))  # Светло-зеленый
            status_item.setForeground(QColor('#27ae60'))  # Темно-зеленый текст
        else:
            status_item.setBackground(QColor('#fadbd8'))  # Светло-красный
            status_item.setForeground(QColor('#e74c3c'))  # Темно-красный текст
            
        self.results_table.setItem(row, 1, status_item)
        
        # Сообщение
        message_item = QTableWidgetItem(message)
        message_item.setToolTip(message)
        self.results_table.setItem(row, 2, message_item)
        
        # Автоматическая прокрутка к последней строке
        self.results_table.scrollToBottom()

    def onConversionFinished(self):
        self.progress_bar.setValue(100)
        self.convert_button.setEnabled(True)
        self.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
        self.log_message(f"🎉 === Conversion completed {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        
        # Статистика
        total_files = self.results_table.rowCount()
        success_count = 0
        error_count = 0
        
        for row in range(total_files):
            status_item = self.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                success_count += 1
            else:
                error_count += 1
        
        self.log_message(f"📊 Statistics: {success_count} successful, {error_count} errors out of {total_files} files")
        
        # Добавление результата в проект если нужно
        if self.add_to_project_cb.isChecked() and success_count > 0:
            self.addResultsToProject()
        
        # Очистка воркера
        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.worker = None
        
        # Уведомление о завершении
        if success_count == total_files:
            QMessageBox.information(self, '🎉 Success', 
                                  f'All {total_files} files converted successfully!')
        elif success_count > 0:
            QMessageBox.warning(self, '⚠️ Partial Success', 
                              f'{success_count} files converted successfully, {error_count} failed.')
        else:
            QMessageBox.critical(self, '❌ Error', 
                               'No files were converted successfully.')

    def onConversionError(self, error_message):
        self.log_message(f"🔥 CRITICAL ERROR: {error_message}")
        QMessageBox.critical(self, translations.get_text('critical_error'), error_message)
        self.onConversionFinished()

    def addResultsToProject(self):
        """Добавление успешно конвертированных файлов в проект"""
        output_folder = self.output_folder_line.text()
        crs_text = self.crs_text.toPlainText().strip()
        output_format = 'GeoJSON' if 'GeoJSON' in self.output_format_combo.currentText() else 'ESRI Shapefile'
        
        # Создание CRS объекта
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
            self.log_message(f"📁 Added to project: {added_count} layers")

    def log_message(self, message):
        """Добавление сообщения в лог с цветовой раскраской"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        # Определение цвета на основе типа сообщения
        if message.startswith('🚀') or message.startswith('🎉'):
            color = '#2ecc71'  # Зеленый для успеха
        elif message.startswith('⚠️'):
            color = '#f39c12'  # Оранжевый для предупреждений
        elif message.startswith('🔥') or message.startswith('❌'):
            color = '#e74c3c'  # Красный для ошибок
        elif message.startswith('✅'):
            color = '#27ae60'  # Темно-зеленый для успешных файлов
        elif message.startswith('✗'):
            color = '#c0392b'  # Темно-красный для ошибок файлов
        elif message.startswith('📊') or message.startswith('📁'):
            color = '#3498db'  # Синий для информации
        else:
            color = '#ecf0f1'  # Белый для обычных сообщений
        
        formatted_message = f'<span style="color: #95a5a6;">[{timestamp}]</span> <span style="color: {color};">{message}</span>'
        self.log_text.append(formatted_message)
        
        # Автопрокрутка к концу
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)

    def clearLogs(self):
        """Очистка логов и результатов"""
        self.log_text.clear()
        self.results_table.setRowCount(0)
        self.log_message("🧹 Logs and results cleared")

    def closeEvent(self, event):
        """Обработка закрытия окна"""
        if self.worker and self.worker_thread and self.worker_thread.isRunning():
            reply = QMessageBox.question(
                self, 
                translations.get_text('confirmation'), 
                translations.get_text('confirm_close'),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
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

