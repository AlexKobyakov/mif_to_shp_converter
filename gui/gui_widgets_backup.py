# -*- coding: utf-8 -*-
"""
Specialized GUI Widgets
Специализированные виджеты интерфейса

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QTabWidget, QComboBox, QSpinBox, QCheckBox, QTextEdit,
    QFrame, QTableWidget, QHeaderView
)

from .gui_components import ModernGroupBox, ModernButton


class HeaderWidget(QFrame):
    """Виджет градиентного заголовка"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(90)  # Увеличиваем высоту для лучшего размещения
        self.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                            stop:0 #3498db, stop:1 #2ecc71);
                border-radius: 10px;
                margin: 5px;
            }
        """)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса заголовка"""
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(20, 15, 20, 15)  # Увеличиваем отступы
        main_layout.setSpacing(20)
        
        # Заголовок
        self.title_label = QLabel("🎯 MIF/TAB to SHP/GeoJSON Converter v2.3")
        self.title_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 18px;
                font-weight: bold;
                background: transparent;
            }
        """)
        
        # Правая панель с элементами управления
        self.controls_widget = QWidget()
        controls_layout = QHBoxLayout(self.controls_widget)
        controls_layout.setContentsMargins(0, 0, 0, 0)
        controls_layout.setSpacing(15)  # Увеличиваем расстояние между элементами
        
        # Селектор языка с иконкой
        self.createLanguageSelector(controls_layout)
        
        # Кнопка поддержки
        self.createDonationButton(controls_layout)
        
        # Кнопка автора
        self.createAuthorButton(controls_layout)
        
        # Добавляем элементы в главный макет
        main_layout.addWidget(self.title_label)
        main_layout.addStretch()  # Отдаляем элементы управления вправо
        main_layout.addWidget(self.controls_widget)
    
    def createLanguageSelector(self, layout):
        """Создание селектора языка"""
        # Контейнер для языкового селектора
        lang_container = QWidget()
        lang_layout = QHBoxLayout(lang_container)
        lang_layout.setContentsMargins(0, 0, 0, 0)
        lang_layout.setSpacing(8)
        
        # Иконка языка
        lang_icon = QLabel("🌐")
        lang_icon.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 16px;
                background: transparent;
                min-width: 20px;
                min-height: 20px;
            }
        """)
        
        # Комбобокс языков
        self.language_combo = QComboBox()
        self.language_combo.setFixedSize(140, 32)  # Увеличиваем размер
        self.language_combo.addItems([
            "🇷🇺 Русский", "🇺🇸 English", "🇨🇳 中文", "🇮🇳 हिंदी", 
            "🇪🇸 Español", "🇸🇦 العربية", "🇫🇷 Français", 
            "🇧🇷 Português", "🇩🇪 Deutsch"
        ])
        
        # Устанавливаем палитру для выпадающего списка
        from qgis.PyQt.QtGui import QPalette
        from qgis.PyQt.QtCore import Qt
        
        # Настраиваем палитру
        palette = self.language_combo.palette()
        palette.setColor(QPalette.Base, Qt.white)
        palette.setColor(QPalette.Text, Qt.black)
        palette.setColor(QPalette.Window, Qt.white)
        palette.setColor(QPalette.WindowText, Qt.black)
        palette.setColor(QPalette.Button, Qt.white)
        palette.setColor(QPalette.ButtonText, Qt.black)
        self.language_combo.setPalette(palette)
        
        # Принудительно устанавливаем свойства view
        from qgis.PyQt.QtGui import QColor
        
        # Получаем view и принудительно настраиваем его
        view = self.language_combo.view()
        
        # Создаем новую палитру с явными цветами
        view_palette = view.palette()
        view_palette.setColor(view_palette.Base, QColor(255, 255, 255))  # Белый фон
        view_palette.setColor(view_palette.Text, QColor(0, 0, 0))        # Черный текст
        view_palette.setColor(view_palette.Window, QColor(255, 255, 255))
        view_palette.setColor(view_palette.WindowText, QColor(0, 0, 0))
        view_palette.setColor(view_palette.Highlight, QColor(52, 152, 219))       # Синяя подсветка
        view_palette.setColor(view_palette.HighlightedText, QColor(255, 255, 255)) # Белый текст
        view.setPalette(view_palette)
        
        # Очень простые стили для view
        view.setStyleSheet("""
            * {
                background-color: white !important;
                color: black !important;
            }
            QListView {
                background: white !important;
                color: black !important;
                border: 2px solid gray;
                font-size: 11px;
                font-weight: bold;
            }
            QListView::item {
                padding: 8px;
                color: black !important;
                background: white !important;
                border: none;
            }
            QListView::item:selected {
                background: #3498db !important;
                color: white !important;
            }
        """)
        self.language_combo.setStyleSheet("""
            QComboBox {
                background: rgba(255, 255, 255, 0.2);
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 6px;
                padding: 6px 12px;
                font-weight: bold;
                font-size: 11px;
            }
            QComboBox:hover {
                background: rgba(255, 255, 255, 0.3);
                border-color: rgba(255, 255, 255, 0.5);
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
                background: transparent;
            }
            QComboBox::down-arrow {
                color: white;
                width: 12px;
                height: 12px;
            }
        """)
        
        lang_layout.addWidget(lang_icon)
        lang_layout.addWidget(self.language_combo)
        layout.addWidget(lang_container)
    
    def createDonationButton(self, layout):
        """Создание кнопки поддержки"""
        from ..translation_manager import translations
        
        self.donation_button = ModernButton(f"☕ {translations.get_text('header_support')}")
        self.donation_button.setFixedSize(120, 32)  # Увеличиваем размер
        self.donation_button.setToolTip("❤️ Поддержите разработку плагина!")
        self.donation_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 rgba(244, 93, 34, 0.9), 
                                            stop:1 rgba(230, 81, 0, 0.9));
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                font-weight: bold;
                font-size: 11px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 rgba(244, 93, 34, 1.0), 
                                            stop:1 rgba(230, 81, 0, 1.0));
                border-color: rgba(255, 255, 255, 0.5);
                transform: translateY(-1px);
            }
            QPushButton:pressed {
                transform: translateY(1px);
            }
        """)
        layout.addWidget(self.donation_button)
    
    def createAuthorButton(self, layout):
        """Создание кнопки автора"""
        from ..translation_manager import translations
        
        self.author_button = ModernButton(f"👤 {translations.get_text('header_about_author')}")
        self.author_button.setFixedSize(100, 32)  # Увеличиваем размер
        self.author_button.setToolTip("📝 Информация об авторе плагина")
        self.author_button.setStyleSheet("""
            QPushButton {
                background: rgba(255, 255, 255, 0.2);
                color: white;
                border: 2px solid rgba(255, 255, 255, 0.3);
                border-radius: 8px;
                font-weight: bold;
                font-size: 11px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background: rgba(255, 255, 255, 0.3);
                border-color: rgba(255, 255, 255, 0.5);
                transform: translateY(-1px);
            }
            QPushButton:pressed {
                transform: translateY(1px);
            }
        """)
        layout.addWidget(self.author_button)


class ConversionModeWidget(QWidget):
    """Виджет выбора режима конвертации"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        from qgis.PyQt.QtWidgets import QRadioButton, QButtonGroup
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Группа режимов
        self.mode_group_box = ModernGroupBox("🔄 Режим конвертации")
        mode_layout = QHBoxLayout(self.mode_group_box)
        mode_layout.setContentsMargins(15, 20, 15, 15)
        
        self.mode_group = QButtonGroup()
        self.single_mode = QRadioButton("📄 Один файл")
        self.batch_mode = QRadioButton("📁 Пакетная обработка")
        self.single_mode.setChecked(True)
        
        self.mode_group.addButton(self.single_mode)
        self.mode_group.addButton(self.batch_mode)
        
        mode_layout.addWidget(self.single_mode)
        mode_layout.addWidget(self.batch_mode)
        mode_layout.addStretch()
        
        layout.addWidget(self.mode_group_box)


class InputDataWidget(QWidget):
    """Виджет входных данных"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Группа входных данных
        self.input_group = ModernGroupBox("📥 Входные данные")
        input_layout = QVBoxLayout(self.input_group)
        input_layout.setContentsMargins(15, 20, 15, 15)
        input_layout.setSpacing(10)
        
        # Виджет для одного файла
        self.single_widget = QWidget()
        single_layout = QHBoxLayout(self.single_widget)
        single_layout.setContentsMargins(0, 0, 0, 0)
        
        self.input_file_line = QLineEdit()
        self.input_file_line.setPlaceholderText("Выберите входной файл")
        self.input_file_button = ModernButton("📂 Обзор...", "secondary")
        
        single_layout.addWidget(self.input_file_line, 1)
        single_layout.addWidget(self.input_file_button)
        
        # Виджет для папки
        self.batch_widget = QWidget()
        batch_layout = QHBoxLayout(self.batch_widget)
        batch_layout.setContentsMargins(0, 0, 0, 0)
        
        self.input_folder_line = QLineEdit()
        self.input_folder_line.setPlaceholderText("Выберите папку с файлами")
        self.input_folder_button = ModernButton("📂 Обзор...", "secondary")
        
        batch_layout.addWidget(self.input_folder_line, 1)
        batch_layout.addWidget(self.input_folder_button)
        
        self.batch_widget.setVisible(False)
        
        input_layout.addWidget(self.single_widget)
        input_layout.addWidget(self.batch_widget)
        
        layout.addWidget(self.input_group)


class OutputDataWidget(QWidget):
    """Виджет выходных данных"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Группа выходных данных
        self.output_group = ModernGroupBox("📤 Выходные данные")
        output_layout = QVBoxLayout(self.output_group)
        output_layout.setContentsMargins(15, 20, 15, 15)
        output_layout.setSpacing(10)
        
        # Выходная папка
        folder_layout = QHBoxLayout()
        self.output_folder_line = QLineEdit()
        self.output_folder_line.setPlaceholderText("Выберите выходную папку")
        self.output_folder_button = ModernButton("📂 Обзор...", "secondary")
        
        folder_layout.addWidget(self.output_folder_line, 1)
        folder_layout.addWidget(self.output_folder_button)
        
        # Формат выходных данных
        format_layout = QHBoxLayout()
        format_label = QLabel("📊 Выходной формат:")
        format_label.setMinimumWidth(150)
        
        self.output_format_combo = QComboBox()
        self.output_format_combo.addItems([
            "🗂️ ESRI Shapefile (.shp)",
            "🌐 GeoJSON (.geojson)"
        ])
        
        format_layout.addWidget(format_label)
        format_layout.addWidget(self.output_format_combo, 1)
        format_layout.addStretch()
        
        output_layout.addLayout(folder_layout)
        output_layout.addLayout(format_layout)
        
        layout.addWidget(self.output_group)


class ProcessingOptionsWidget(QWidget):
    """Виджет параметров обработки"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(15)
        
        # Группа многопоточности
        self.threading_group = ModernGroupBox("⚡ Настройки многопоточности")
        threading_layout = QHBoxLayout(self.threading_group)
        threading_layout.setContentsMargins(15, 20, 15, 15)
        
        self.thread_count_label = QLabel("🧵 Количество потоков:")
        self.threads_spinbox = QSpinBox()
        self.threads_spinbox.setRange(1, 16)
        self.threads_spinbox.setValue(4)
        self.threads_spinbox.setToolTip("Количество параллельных потоков для обработки файлов")
        
        threading_layout.addWidget(self.thread_count_label)
        threading_layout.addWidget(self.threads_spinbox)
        threading_layout.addStretch()
        
        # Группа системы координат
        self.crs_group = ModernGroupBox("🌍 Система координат")
        crs_layout = QVBoxLayout(self.crs_group)
        crs_layout.setContentsMargins(15, 20, 15, 15)
        crs_layout.setSpacing(10)
        
        # Подсказка по формату
        self.crs_hint_label = QLabel("📝 Формат: EPSG:код, PROJ4 или WKT")
        self.crs_hint_label.setStyleSheet("color: #7f8c8d; font-style: italic;")
        
        # Поле ввода CRS
        self.crs_text = QTextEdit()
        self.crs_text.setMaximumHeight(80)
        self.crs_text.setPlainText("EPSG:4326")
        self.crs_text.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                padding: 8px;
                font-family: 'Consolas', 'Monaco', monospace;
            }
            QTextEdit:focus {
                border-color: #3498db;
            }
        """)
        
        # Кнопка примеров CRS
        from ..translation_manager import translations
        self.examples_button = ModernButton(f"📋 {translations.get_text('crs_examples_button')}", "secondary")
        
        # Чекбокс добавления в проект
        self.add_to_project_cb = QCheckBox("✅ Добавить результат в проект QGIS")
        self.add_to_project_cb.setChecked(True)
        
        crs_layout.addWidget(self.crs_hint_label)
        crs_layout.addWidget(self.crs_text)
        crs_layout.addWidget(self.examples_button)
        crs_layout.addWidget(self.add_to_project_cb)
        
        layout.addWidget(self.threading_group)
        layout.addWidget(self.crs_group)


class ResultsTableWidget(QTableWidget):
    """Виджет таблицы результатов"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        self.setColumnCount(3)
        self.setHorizontalHeaderLabels([
            "📄 Файл",
            "📊 Статус", 
            "💬 Сообщение"
        ])
        
        # Настройка заголовков
        header = self.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        
        # Стилизация
        self.setAlternatingRowColors(True)
        self.setStyleSheet("""
            QTableWidget {
                gridline-color: #bdc3c7;
                background-color: white;
                alternate-background-color: #f8f9fa;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #ecf0f1;
            }
            QHeaderView::section {
                background-color: #34495e;
                color: white;
                padding: 8px;
                border: none;
                font-weight: bold;
            }
        """)


class LogTextWidget(QTextEdit):
    """Виджет логов с темной темой"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        self.setReadOnly(True)
        self.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                border: none;
                padding: 10px;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 11px;
            }
        """)


class ControlButtonsWidget(QWidget):
    """Виджет кнопок управления"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 15, 0, 0)  # Увеличен верхний отступ
        layout.setSpacing(15)  # Увеличено расстояние
        
        self.convert_button = ModernButton("🚀 Начать конвертацию")
        self.cancel_button = ModernButton("❌ Отмена", "secondary")
        self.clear_log_button = ModernButton("🧹 Очистить логи", "secondary")
        
        self.cancel_button.setEnabled(False)
        
        layout.addWidget(self.convert_button)
        layout.addWidget(self.cancel_button)
        layout.addWidget(self.clear_log_button)
        layout.addStretch()
