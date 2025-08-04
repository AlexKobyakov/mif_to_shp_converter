# -*- coding: utf-8 -*-
"""
Main GUI Dialog
Главное диалоговое окно интерфейса

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from datetime import datetime

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QSplitter, 
    QScrollArea, QWidget, QTabWidget, QFrame, QLabel
)

from .gui_components import ModernProgressBar, apply_global_styles
from .gui_widgets import (
    HeaderWidget, ConversionModeWidget, InputDataWidget, 
    OutputDataWidget, ProcessingOptionsWidget, ResultsTableWidget,
    LogTextWidget, ControlButtonsWidget
)
from .gui_handlers import GuiEventHandlers


class MifToShpDialog(QDialog):
    """Главное диалоговое окно конвертера с модульной архитектурой"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Инициализация переменных
        self.worker = None
        self.worker_thread = None
        
        # Настройка окна
        self.setupWindow()
        
        # Создание интерфейса
        self.setupUi()
        
        # Создание обработчиков событий
        self.handlers = GuiEventHandlers(self)
        
        # Подключение сигналов
        self.connectSignals()
        
        # Применение стилей
        self.applyStyles()
        
        # Обновление языка
        self.updateLanguage()
    
    def setupWindow(self):
        """Настройка основных параметров окна"""
        from ..translation_manager import translations
        
        self.setWindowTitle(f"🎯 {translations.get_text('window_title')}")
        self.setMinimumSize(1000, 750)  # Увеличен минимальный размер
        self.resize(1200, 850)  # Увеличен размер по умолчанию
        
        # Центрирование окна
        self.setWindowFlags(Qt.Dialog | Qt.WindowTitleHint | Qt.WindowCloseButtonHint)
    
    def setupUi(self):
        """Создание основного интерфейса"""
        # Главный макет
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(15, 15, 15, 15)  # Увеличены отступы
        main_layout.setSpacing(15)  # Увеличено расстояние
        
        # Создание компонентов
        self.createHeader()
        self.createMainContent()
        
        # Добавление в главный макет
        main_layout.addWidget(self.header)
        main_layout.addWidget(self.main_splitter, 1)
    
    def createHeader(self):
        """Создание заголовка"""
        self.header = HeaderWidget()
    
    def createMainContent(self):
        """Создание основного содержимого"""
        # Главный сплиттер
        self.main_splitter = QSplitter(Qt.Vertical)
        self.main_splitter.setChildrenCollapsible(False)
        
        # Верхняя часть - настройки
        self.createSettingsArea()
        
        # Нижняя часть - прогресс и результаты
        self.createResultsArea()
        
        # Добавление в сплиттер
        self.main_splitter.addWidget(self.settings_area)
        self.main_splitter.addWidget(self.results_area)
        self.main_splitter.setSizes([500, 250])  # Больше места для настроек
    
    def createSettingsArea(self):
        """Создание области настроек"""
        # Прокручиваемая область
        self.settings_scroll = QScrollArea()
        self.settings_scroll.setWidgetResizable(True)
        self.settings_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.settings_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        
        # Контейнер настроек
        settings_container = QWidget()
        settings_layout = QVBoxLayout(settings_container)
        settings_layout.setContentsMargins(15, 15, 15, 15)  # Увеличены отступы
        settings_layout.setSpacing(20)  # Увеличено расстояние
        
        # Создание табов настроек
        self.createSettingsTabs()
        
        # Кнопки управления
        self.control_buttons = ControlButtonsWidget()
        
        # Добавление в макет
        settings_layout.addWidget(self.settings_tabs)
        settings_layout.addWidget(self.control_buttons)
        settings_layout.addStretch()
        
        # Установка виджета в scroll area
        self.settings_scroll.setWidget(settings_container)
        self.settings_area = self.settings_scroll
    
    def createSettingsTabs(self):
        """Создание табов настроек"""
        self.settings_tabs = QTabWidget()
        self.settings_tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                background-color: #f8f9fa;
            }
            QTabBar::tab {
                background: #ecf0f1;
                border: 1px solid #bdc3c7;
                padding: 8px 16px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background: #3498db;
                color: white;
                font-weight: bold;
            }
            QTabBar::tab:hover:!selected {
                background: #d5dbdb;
            }
        """)
        
        # Первый таб - Входные/Выходные данные
        self.createInputOutputTab()
        
        # Второй таб - Параметры обработки
        self.createProcessingTab()
        
        # Добавление табов
        self.settings_tabs.addTab(self.io_tab_widget, "📥📤 Входные/Выходные данные")
        self.settings_tabs.addTab(self.processing_tab_widget, "⚙️ Параметры обработки")
    
    def createInputOutputTab(self):
        """Создание таба входных/выходных данных"""
        self.io_tab_widget = QWidget()
        io_layout = QVBoxLayout(self.io_tab_widget)
        io_layout.setContentsMargins(20, 20, 20, 20)  # Увеличены отступы
        io_layout.setSpacing(20)  # Увеличено расстояние
        
        # Создание виджетов
        self.mode_widget = ConversionModeWidget()
        self.input_widget = InputDataWidget()
        self.output_widget = OutputDataWidget()
        
        # Добавление в макет
        io_layout.addWidget(self.mode_widget)
        io_layout.addWidget(self.input_widget)
        io_layout.addWidget(self.output_widget)
        io_layout.addStretch()
    
    def createProcessingTab(self):
        """Создание таба параметров обработки"""
        self.processing_tab_widget = QWidget()
        processing_layout = QVBoxLayout(self.processing_tab_widget)
        processing_layout.setContentsMargins(20, 20, 20, 20)  # Увеличены отступы
        processing_layout.setSpacing(20)  # Увеличено расстояние
        
        # Создание виджета параметров
        self.processing_widget = ProcessingOptionsWidget()
        
        # Добавление в макет
        processing_layout.addWidget(self.processing_widget)
        processing_layout.addStretch()
    
    def createResultsArea(self):
        """Создание области результатов"""
        self.results_area = QWidget()
        results_layout = QVBoxLayout(self.results_area)
        results_layout.setContentsMargins(15, 15, 15, 15)  # Увеличены отступы
        results_layout.setSpacing(15)  # Увеличено расстояние
        
        # Прогресс-бар
        self.createProgressSection()
        
        # Табы результатов
        self.createResultsTabs()
        
        # Добавление в макет
        results_layout.addWidget(self.progress_frame)
        results_layout.addWidget(self.results_tabs, 1)
    
    def createProgressSection(self):
        """Создание секции прогресса"""
        self.progress_frame = QFrame()
        progress_layout = QVBoxLayout(self.progress_frame)
        progress_layout.setContentsMargins(0, 0, 0, 0)
        
        # Метка прогресса
        self.progress_label = QLabel("📊 Прогресс")
        self.progress_label.setStyleSheet("font-weight: bold; color: #2c3e50;")
        
        # Прогресс-бар
        self.progress_bar = ModernProgressBar()
        self.progress_bar.setVisible(False)
        
        progress_layout.addWidget(self.progress_label)
        progress_layout.addWidget(self.progress_bar)
    
    def createResultsTabs(self):
        """Создание табов результатов"""
        self.results_tabs = QTabWidget()
        self.results_tabs.setStyleSheet("""
            QTabWidget::pane {
                border: 2px solid #bdc3c7;
                border-radius: 8px;
                background-color: white;
            }
            QTabBar::tab {
                background: #ecf0f1;
                border: 1px solid #bdc3c7;
                padding: 6px 12px;
                margin-right: 2px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
            }
            QTabBar::tab:selected {
                background: white;
                border-bottom-color: white;
                font-weight: bold;
            }
        """)
        
        # Таб логов
        self.log_text = LogTextWidget()
        
        # Таб результатов
        self.results_table = ResultsTableWidget()
        
        # Добавление табов
        self.results_tabs.addTab(self.log_text, "📋 Логи")
        self.results_tabs.addTab(self.results_table, "📈 Результаты")
    
    def connectSignals(self):
        """Подключение сигналов к обработчикам"""
        # Заголовок
        self.header.language_combo.currentIndexChanged.connect(self.handlers.onLanguageChanged)
        self.header.donation_button.clicked.connect(self.handlers.showDonation)
        self.header.author_button.clicked.connect(self.handlers.showAuthorInfo)
        
        # Режим конвертации
        self.mode_widget.single_mode.toggled.connect(self.handlers.onModeChanged)
        self.mode_widget.batch_mode.toggled.connect(self.handlers.onModeChanged)
        
        # Выбор файлов и папок
        self.input_widget.input_file_button.clicked.connect(self.handlers.selectInputFile)
        self.input_widget.input_folder_button.clicked.connect(self.handlers.selectInputFolder)
        self.output_widget.output_folder_button.clicked.connect(self.handlers.selectOutputFolder)
        
        # Примеры CRS
        self.processing_widget.examples_button.clicked.connect(self.handlers.showCrsExamples)
        
        # Кнопки управления
        self.control_buttons.convert_button.clicked.connect(self.handlers.startConversion)
        self.control_buttons.cancel_button.clicked.connect(self.handlers.cancelConversion)
        self.control_buttons.clear_log_button.clicked.connect(self.handlers.clearLogs)
    
    def applyStyles(self):
        """Применение глобальных стилей"""
        self.setStyleSheet(apply_global_styles())
    
    def updateLanguage(self):
        """Обновление языка интерфейса"""
        from ..translation_manager import translations
        
        # Обновление заголовка окна
        self.setWindowTitle(f"🎯 {translations.get_text('window_title')}")
        
        # Обновление табов настроек
        self.settings_tabs.setTabText(0, f"📥📤 {translations.get_text('input_output')}")
        self.settings_tabs.setTabText(1, f"⚙️ {translations.get_text('processing_options')}")
        
        # Обновление групп режима конвертации
        self.mode_widget.mode_group_box.setTitle(f"🔄 {translations.get_text('conversion_mode')}")
        self.mode_widget.single_mode.setText(f"📄 {translations.get_text('single_file')}")
        self.mode_widget.batch_mode.setText(f"📁 {translations.get_text('batch_processing')}")
        
        # Обновление входных данных
        self.input_widget.input_group.setTitle(f"📥 {translations.get_text('input_file')}")
        self.input_widget.input_file_line.setPlaceholderText(translations.get_text('select_input_file'))
        self.input_widget.input_folder_line.setPlaceholderText(translations.get_text('select_input_folder'))
        self.input_widget.input_file_button.setText(f"📂 {translations.get_text('browse')}")
        self.input_widget.input_folder_button.setText(f"📂 {translations.get_text('browse')}")
        
        # Обновление выходных данных
        self.output_widget.output_group.setTitle(f"📤 {translations.get_text('output_folder')}")
        self.output_widget.output_folder_line.setPlaceholderText(translations.get_text('select_output_folder'))
        self.output_widget.output_folder_button.setText(f"📂 {translations.get_text('browse')}")
        
        # Обновление параметров обработки
        self.processing_widget.threading_group.setTitle(f"⚡ {translations.get_text('threading_settings')}")
        self.processing_widget.thread_count_label.setText(f"🧵 {translations.get_text('thread_count')}")
        
        self.processing_widget.crs_group.setTitle(f"🌍 {translations.get_text('coordinate_system')}")
        self.processing_widget.crs_hint_label.setText(f"📝 {translations.get_text('crs_format_hint')}")
        self.processing_widget.add_to_project_cb.setText(f"✅ {translations.get_text('add_to_project')}")
        
        # Обновление прогресса
        self.progress_label.setText(f"📊 {translations.get_text('progress')}")
        
        # Обновление табов результатов
        self.results_tabs.setTabText(0, f"📋 {translations.get_text('logs')}")
        self.results_tabs.setTabText(1, f"📈 {translations.get_text('results')}")
        
        # Обновление заголовков таблицы
        self.results_table.setHorizontalHeaderLabels([
            f"📄 {translations.get_text('file')}",
            f"📊 {translations.get_text('status')}",
            f"💬 {translations.get_text('message')}"
        ])
        
        # Обновление кнопок
        if 'Converting' in self.control_buttons.convert_button.text() or 'Конвертация' in self.control_buttons.convert_button.text():
            self.control_buttons.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        else:
            self.control_buttons.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
            
        self.control_buttons.cancel_button.setText(f"❌ {translations.get_text('cancel')}")
        self.control_buttons.clear_log_button.setText(f"🧹 {translations.get_text('clear_logs')}")
    
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
    
    def closeEvent(self, event):
        """Обработка закрытия окна"""
        self.handlers.closeEvent(event)
