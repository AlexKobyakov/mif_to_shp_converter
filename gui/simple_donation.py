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
from ..translation_manager import translations


class SimpleDonationDialog(QDialog):
    """Простой диалог поддержки разработки"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(translations.get_text('donation_title'))
        self.setFixedSize(500, 400)  # Увеличиваем размеры
        self.setModal(True)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(25, 25, 25, 25)  # Увеличены отступы
        layout.setSpacing(20)  # Увеличено расстояние
        
        # Заголовок
        title = QLabel(translations.get_text('donation_window_title'))
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
        description = QLabel(translations.get_text('donation_description'))
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
        kofi_button = QPushButton(translations.get_text('donation_kofi'))
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
        
        # Т Банк кнопка
        tbank_button = QPushButton(translations.get_text('donation_tbank'))
        tbank_button.setStyleSheet("""
            QPushButton {
                background-color: #ffdd2d;
                color: #333;
                border: none;
                border-radius: 8px;
                padding: 15px 20px;  /* Увеличен padding */
                font-weight: bold;
                font-size: 14px;
                min-height: 20px;  /* Минимальная высота */
            }
            QPushButton:hover {
                background-color: #f5d000;
                transform: translateY(-1px);
            }
        """)
        tbank_button.clicked.connect(self.openTBank)
        
        # GitHub Sponsors кнопка
        github_button = QPushButton(translations.get_text('donation_github'))
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
        buttons_layout.addWidget(tbank_button)
        buttons_layout.addWidget(github_button)
        
        # Кнопка закрытия
        close_button = QPushButton(translations.get_text('donation_maybe_later'))
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
    
    def openTBank(self):
        """Открыть страницу доната Т Банка"""
        url = "https://www.tinkoff.ru/rm/r_nCoENhHIfi.KBsuiKmOgJ/ggPSE72306"
        QDesktopServices.openUrl(QUrl(url))
        self.accept()
    
    def openGitHub(self):
        """Открыть GitHub Sponsors"""
        # Замените на вашу реальную GitHub Sponsors ссылку
        url = "https://github.com/sponsors/AlexKobyakov"
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
        label = QLabel(translations.get_text('donation_title'))
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
