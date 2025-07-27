# -*- coding: utf-8 -*-
"""
Donation Widget Component
Компонент виджета пожертвований

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

try:
    from qgis.PyQt.QtWebEngineWidgets import QWebEngineView
    WEB_ENGINE_AVAILABLE = True
except ImportError:
    WEB_ENGINE_AVAILABLE = False

from qgis.PyQt.QtCore import Qt, QUrl
from qgis.PyQt.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from qgis.PyQt.QtGui import QDesktopServices, QIcon, QPixmap
import webbrowser


class DonationWidget(QWidget):
    """Виджет для пожертвований с поддержкой Ko-fi"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        layout.setSpacing(10)
        
        # Заголовок
        header = QLabel("☕ Support Development")
        header.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-weight: bold;
                font-size: 12px;
                padding: 5px;
            }
        """)
        
        # Описание
        description = QLabel("Help support the development of this plugin!")
        description.setStyleSheet("""
            QLabel {
                color: #7f8c8d;
                font-size: 10px;
                padding: 2px;
            }
        """)
        description.setWordWrap(True)
        
        # Кнопки пожертвований
        buttons_layout = QHBoxLayout()
        
        # Ko-fi кнопка
        self.kofi_button = QPushButton("☕ Ko-fi")
        self.kofi_button.setStyleSheet("""
            QPushButton {
                background-color: #f45d22;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-weight: bold;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #e55a1f;
            }
        """)
        self.kofi_button.clicked.connect(self.openKofi)
        
        # PayPal кнопка (альтернатива)
        self.paypal_button = QPushButton("💳 PayPal")
        self.paypal_button.setStyleSheet("""
            QPushButton {
                background-color: #0070ba;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 6px 12px;
                font-weight: bold;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #005ea6;
            }
        """)
        self.paypal_button.clicked.connect(self.openPayPal)
        
        buttons_layout.addWidget(self.kofi_button)
        buttons_layout.addWidget(self.paypal_button)
        buttons_layout.addStretch()
        
        # Добавление в макет
        layout.addWidget(header)
        layout.addWidget(description)
        layout.addLayout(buttons_layout)
        
        # Стилизация контейнера
        self.setStyleSheet("""
            DonationWidget {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 6px;
            }
        """)
        self.setMaximumHeight(80)
    
    def openKofi(self):
        """Открыть Ko-fi страницу"""
        url = "https://ko-fi.com/kobyakov"
        QDesktopServices.openUrl(QUrl(url))
    
    def openPayPal(self):
        """Открыть PayPal страницу"""
        # Замените на вашу PayPal ссылку
        url = "https://paypal.me/kobyakov"
        QDesktopServices.openUrl(QUrl(url))


class WebDonationDialog(QWidget):
    """Диалог с встроенным веб-виджетом Ko-fi (если доступен WebEngine)"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("☕ Support Development")
        self.setMinimumSize(400, 500)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        
        if WEB_ENGINE_AVAILABLE:
            # Веб-виджет Ko-fi
            self.web_view = QWebEngineView()
            
            # HTML с встроенным Ko-fi виджетом
            html_content = """
            <!DOCTYPE html>
            <html>
            <head>
                <meta charset="UTF-8">
                <title>Ko-fi Donation</title>
                <style>
                    body {
                        margin: 0;
                        padding: 20px;
                        font-family: Arial, sans-serif;
                        background-color: #f8f9fa;
                    }
                    .header {
                        text-align: center;
                        margin-bottom: 20px;
                    }
                    .description {
                        text-align: center;
                        color: #666;
                        margin-bottom: 30px;
                    }
                </style>
            </head>
            <body>
                <div class="header">
                    <h2>☕ Support MIF/TAB Converter Development</h2>
                </div>
                <div class="description">
                    <p>Help support the development of this free QGIS plugin!</p>
                    <p>Your donations help maintain and improve the plugin.</p>
                </div>
                
                <!-- Ko-fi Button -->
                <script src='https://storage.ko-fi.com/cdn/scripts/overlay-widget.js'></script>
                <script>
                  kofiWidgetOverlay.draw('kobyakov', {
                    'type': 'floating-chat',
                    'floating-chat.donateButton.text': 'Support Me',
                    'floating-chat.donateButton.background-color': '#f45d22',
                    'floating-chat.donateButton.text-color': '#fff'
                  });
                </script>
                
                <!-- Альтернативная кнопка -->
                <div style="text-align: center; margin-top: 30px;">
                    <a href="https://ko-fi.com/kobyakov" target="_blank" 
                       style="display: inline-block; background-color: #f45d22; color: white; 
                              padding: 12px 24px; text-decoration: none; border-radius: 6px;
                              font-weight: bold;">
                        ☕ Buy me a coffee on Ko-fi
                    </a>
                </div>
            </body>
            </html>
            """
            
            self.web_view.setHtml(html_content)
            layout.addWidget(self.web_view)
        else:
            # Fallback если WebEngine недоступен
            fallback_label = QLabel("""
            <div style="text-align: center; padding: 20px;">
                <h3>☕ Support Development</h3>
                <p>WebEngine не доступен в вашей версии QGIS.</p>
                <p>Кнопка ниже откроет Ko-fi в браузере.</p>
            </div>
            """)
            fallback_label.setTextFormat(Qt.RichText)
            
            donation_widget = DonationWidget()
            
            layout.addWidget(fallback_label)
            layout.addWidget(donation_widget)
        
        # Кнопка закрытия
        close_button = QPushButton("✅ Закрыть")
        close_button.clicked.connect(self.close)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        
        layout.addWidget(close_button)


def test_web_engine():
    """Тест доступности WebEngine"""
    try:
        from qgis.PyQt.QtWebEngineWidgets import QWebEngineView
        return True
    except ImportError:
        return False


# Экспорт компонентов
__all__ = ['DonationWidget', 'WebDonationDialog', 'test_web_engine', 'WEB_ENGINE_AVAILABLE']
