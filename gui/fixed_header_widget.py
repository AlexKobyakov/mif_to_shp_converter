# -*- coding: utf-8 -*-
"""
Fixed Header Widget with working language dropdown
Исправленный виджет заголовка с работающим выпадающим списком языков

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QWidget, QHBoxLayout, QLabel, QComboBox, QFrame
from qgis.PyQt.QtGui import QPalette, QColor

from .gui_components import ModernButton


class FixedHeaderWidget(QFrame):
    """Исправленный виджет градиентного заголовка с работающим dropdown"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(90)
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
        main_layout.setContentsMargins(20, 15, 20, 15)
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
        controls_layout.setSpacing(15)
        
        # Создаем элементы управления
        self.createLanguageSelector(controls_layout)
        self.createDonationButton(controls_layout)
        self.createAuthorButton(controls_layout)
        
        # Добавляем элементы в главный макет
        main_layout.addWidget(self.title_label)
        main_layout.addStretch()
        main_layout.addWidget(self.controls_widget)
    
    def createLanguageSelector(self, layout):
        """Создание селектора языка с принудительными стилями"""
        # Контейнер
        lang_container = QWidget()
        lang_layout = QHBoxLayout(lang_container)
        lang_layout.setContentsMargins(0, 0, 0, 0)
        lang_layout.setSpacing(8)
        
        # Иконка
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
        
        # Комбобокс с принудительными настройками
        self.language_combo = QComboBox()
        self.language_combo.setFixedSize(140, 32)
        
        # Добавляем элементы
        self.language_combo.addItems([
            "🇷🇺 Русский", "🇺🇸 English", "🇨🇳 中文", "🇮🇳 हिंदी", 
            "🇪🇸 Español", "🇸🇦 العربية", "🇫🇷 Français", 
            "🇧🇷 Português", "🇩🇪 Deutsch"
        ])
        
        # ПРИНУДИТЕЛЬНАЯ настройка палитры
        self.forceDropdownColors()
        
        # Простые стили для самого комбобокса
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
    
    def forceDropdownColors(self):
        """Принудительная настройка цветов dropdown"""
        try:
            # Получаем view (выпадающий список)
            view = self.language_combo.view()
            
            # Создаем новую палитру с явными цветами
            palette = QPalette()
            
            # Устанавливаем все возможные цвета
            palette.setColor(QPalette.Base, QColor(255, 255, 255))           # Белый фон
            palette.setColor(QPalette.Text, QColor(0, 0, 0))                 # Черный текст
            palette.setColor(QPalette.Window, QColor(255, 255, 255))         # Белое окно
            palette.setColor(QPalette.WindowText, QColor(0, 0, 0))           # Черный текст окна
            palette.setColor(QPalette.Button, QColor(255, 255, 255))         # Белая кнопка
            palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))           # Черный текст кнопки
            palette.setColor(QPalette.Highlight, QColor(52, 152, 219))       # Синяя подсветка
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255)) # Белый текст подсветки
            palette.setColor(QPalette.AlternateBase, QColor(248, 249, 250))  # Альтернативный фон
            
            # Применяем палитру к комбобоксу и view
            self.language_combo.setPalette(palette)
            view.setPalette(palette)
            
            # Принудительные стили для view
            view.setStyleSheet("""
                QListView {
                    background-color: white !important;
                    color: black !important;
                    border: 2px solid #bdc3c7;
                    border-radius: 4px;
                    outline: none;
                    font-size: 11px;
                    font-weight: bold;
                    padding: 2px;
                }
                QListView::item {
                    padding: 8px 12px;
                    color: black !important;
                    background-color: white !important;
                    border: none;
                    min-height: 24px;
                }
                QListView::item:selected {
                    background-color: #3498db !important;
                    color: white !important;
                }
                QListView::item:hover {
                    background-color: #5dade2 !important;
                    color: white !important;
                }
            """)
            
            # Дополнительные настройки через Qt properties
            view.setProperty("color", "black")
            view.setProperty("background-color", "white")
            
            # Обновляем отображение
            view.update()
            self.language_combo.update()
            
        except Exception as e:
            print(f"Warning: Could not force dropdown colors: {e}")
    
    def createDonationButton(self, layout):
        """Создание кнопки поддержки"""
        from ..translation_manager import translations
        
        self.donation_button = ModernButton(f"☕ {translations.get_text('header_support')}")
        self.donation_button.setFixedSize(120, 32)
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
        self.author_button.setFixedSize(100, 32)
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
