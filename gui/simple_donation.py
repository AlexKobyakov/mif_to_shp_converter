# -*- coding: utf-8 -*-
"""
Simple Donation Dialog
Простой диалог поддержки без веб-компонентов

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.PyQt.QtCore import Qt, QUrl
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QFrame
from qgis.PyQt.QtGui import QDesktopServices, QFont, QPixmap


class SimpleDonationDialog(QDialog):
    """Простой диалог поддержки разработки"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("☕ Support Development")
        self.setFixedSize(450, 350)  # Увеличены размеры
        self.setModal(True)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)  # Увеличены отступы
        layout.setSpacing(20)  # Увеличено расстояние
        
        # Заголовок
        title = QLabel("☕ Support Plugin Development")
        title.setStyleSheet("""
            QLabel {
                color: #2c3e50;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                padding: 10px;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        
        # Описание
        description = QLabel("""
        <div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 MIF/TAB to SHP/GeoJSON Converter</b></p>
            <p>This plugin is developed and maintained for <b>free</b>!</p>
            <p>Your support helps keep it updated and improved.</p>
            <p style="color: #7f8c8d; font-size: 12px;">Every coffee counts! ❤️</p>
        </div>
        """)
        description.setTextFormat(Qt.RichText)
        description.setStyleSheet("""
            QLabel {
                background-color: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
                color: #495057;
            }
        """)
        
        # Кнопки поддержки
        buttons_frame = QFrame()
        buttons_layout = QVBoxLayout(buttons_frame)
        buttons_layout.setSpacing(10)
        
        # Ko-fi кнопка
        kofi_button = QPushButton("☕ Buy me a coffee on Ko-fi")
        kofi_button.setStyleSheet("""
            QPushButton {
                background-color: #f45d22;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px 20px;  /* Увеличен padding */
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;  /* Минимальная высота */
            }
            QPushButton:hover {
                background-color: #e55a1f;
                transform: translateY(-1px);
            }
        """)
        kofi_button.clicked.connect(self.openKofi)
        
        # PayPal кнопка
        paypal_button = QPushButton("💳 Donate via PayPal")
        paypal_button.setStyleSheet("""
            QPushButton {
                background-color: #0070ba;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px 20px;  /* Увеличен padding */
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;  /* Минимальная высота */
            }
            QPushButton:hover {
                background-color: #005ea6;
                transform: translateY(-1px);
            }
        """)
        paypal_button.clicked.connect(self.openPayPal)
        
        # GitHub Sponsors кнопка
        github_button = QPushButton("💖 Sponsor on GitHub")
        github_button.setStyleSheet("""
            QPushButton {
                background-color: #24292e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 15px 20px;  /* Увеличен padding */
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;  /* Минимальная высота */
            }
            QPushButton:hover {
                background-color: #1b1f23;
                transform: translateY(-1px);
            }
        """)
        github_button.clicked.connect(self.openGitHub)
        
        buttons_layout.addWidget(kofi_button)
        buttons_layout.addWidget(paypal_button)
        buttons_layout.addWidget(github_button)
        
        # Кнопка закрытия
        close_button = QPushButton("✅ Maybe Later")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #6c757d;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #5a6268;
            }
        """)
        close_button.clicked.connect(self.accept)
        
        # Добавление в макет
        layout.addWidget(title)
        layout.addWidget(description)
        layout.addWidget(buttons_frame)
        layout.addStretch()
        layout.addWidget(close_button, 0, Qt.AlignCenter)
        
        # Стилизация диалога
        self.setStyleSheet("""
            QDialog {
                background-color: white;
                border-radius: 10px;
            }
        """)
    
    def openKofi(self):
        """Открыть Ko-fi страницу"""
        url = "https://ko-fi.com/kobyakov"
        QDesktopServices.openUrl(QUrl(url))
        self.accept()
    
    def openPayPal(self):
        """Открыть PayPal страницу"""
        # Замените на вашу реальную PayPal ссылку
        url = "https://paypal.me/kobyakov"  
        QDesktopServices.openUrl(QUrl(url))
        self.accept()
    
    def openGitHub(self):
        """Открыть GitHub Sponsors"""
        # Замените на вашу реальную GitHub Sponsors ссылку
        url = "https://github.com/sponsors/kobyakov"
        QDesktopServices.openUrl(QUrl(url))
        self.accept()


class CompactDonationWidget(QFrame):
    """Компактный виджет donation для встраивания"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка компактного интерфейса"""
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 4, 8, 4)
        layout.setSpacing(8)
        
        # Иконка и текст
        label = QLabel("☕ Support")
        label.setStyleSheet("""
            QLabel {
                color: #f45d22;
                font-weight: bold;
                font-size: 11px;
            }
        """)
        
        # Кнопка Ko-fi
        donate_button = QPushButton("Donate")
        donate_button.setFixedSize(60, 24)
        donate_button.setStyleSheet("""
            QPushButton {
                background-color: #f45d22;
                color: white;
                border: none;
                border-radius: 12px;
                font-weight: bold;
                font-size: 10px;
            }
            QPushButton:hover {
                background-color: #e55a1f;
            }
        """)
        donate_button.clicked.connect(self.openDonation)
        
        layout.addWidget(label)
        layout.addWidget(donate_button)
        layout.addStretch()
        
        # Стилизация
        self.setStyleSheet("""
            CompactDonationWidget {
                background-color: rgba(244, 93, 34, 0.1);
                border: 1px solid rgba(244, 93, 34, 0.3);
                border-radius: 6px;
            }
        """)
        self.setMaximumHeight(32)
    
    def openDonation(self):
        """Открыть диалог поддержки"""
        dialog = SimpleDonationDialog(self)
        dialog.exec_()


# Экспорт
__all__ = ['SimpleDonationDialog', 'CompactDonationWidget']
