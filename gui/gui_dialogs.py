# -*- coding: utf-8 -*-
"""
Dialog Components
Компоненты диалоговых окон

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

from qgis.PyQt.QtCore import Qt
from qgis.PyQt.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QLabel, QTextEdit, QPushButton


class AuthorInfoDialog(QMessageBox):
    """Диалог информации об авторе"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        self.setWindowTitle('👤 Author Information')
        self.setTextFormat(Qt.RichText)
        self.setText("""
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
        self.setStandardButtons(QMessageBox.Ok)


class CrsExamplesDialog(QDialog):
    """Диалог примеров систем координат"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        from ..translation_manager import translations
        
        self.setWindowTitle(f'📋 {translations.get_text("crs_examples_title")}')
        self.setMinimumSize(600, 500)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        from ..translation_manager import translations
        
        layout = QVBoxLayout(self)
        
        # Заголовок
        title = QLabel(f'📋 {translations.get_text("crs_examples_window_title")}')
        title.setStyleSheet("""
            QLabel {
                font-size: 16px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
                background: #ecf0f1;
                border-radius: 6px;
                margin-bottom: 10px;
            }
        """)
        
        # Текст с примерами
        examples_text = QTextEdit()
        examples_text.setReadOnly(True)
        examples_text.setStyleSheet("""
            QTextEdit {
                background-color: white;
                border: 2px solid #bdc3c7;
                border-radius: 6px;
                padding: 15px;
                font-family: 'Consolas', 'Monaco', monospace;
                font-size: 12px;
            }
        """)
        
        examples_text.setPlainText(translations.get_text('crs_examples_content'))
        
        # Кнопка закрытия
        close_button = QPushButton(f'✅ {translations.get_text("crs_examples_close")}')
        close_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #3498db, stop:1 #2980b9);
                color: white;
                border: none;
                border-radius: 6px;
                padding: 10px 20px;
                font-weight: bold;
                font-size: 12px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #5dade2, stop:1 #3498db);
            }
        """)
        close_button.clicked.connect(self.accept)
        
        layout.addWidget(title)
        layout.addWidget(examples_text)
        layout.addWidget(close_button, 0, Qt.AlignCenter)


class ProgressDialog(QDialog):
    """Диалог прогресса для длительных операций"""
    
    def __init__(self, title="Выполнение операции...", parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setModal(True)
        self.setMinimumSize(400, 150)
        self.setupUi()
    
    def setupUi(self):
        """Настройка интерфейса"""
        from .gui_components import ModernProgressBar
        
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Сообщение
        self.message_label = QLabel("Инициализация...")
        self.message_label.setStyleSheet("""
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                padding: 10px;
            }
        """)
        
        # Прогресс-бар
        self.progress_bar = ModernProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        
        # Кнопка отмены
        self.cancel_button = QPushButton('❌ Отмена')
        self.cancel_button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #e74c3c, stop:1 #c0392b);
                color: white;
                border: none;
                border-radius: 6px;
                padding: 8px 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 #ec7063, stop:1 #e74c3c);
            }
        """)
        self.cancel_button.clicked.connect(self.reject)
        
        layout.addWidget(self.message_label)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.cancel_button, 0, Qt.AlignCenter)
    
    def update_progress(self, value, message=""):
        """Обновление прогресса"""
        self.progress_bar.setValue(value)
        if message:
            self.message_label.setText(message)


class ErrorDialog(QMessageBox):
    """Стилизованный диалог ошибки"""
    
    def __init__(self, title="Ошибка", message="Произошла ошибка", parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Critical)
        self.setWindowTitle(f'❌ {title}')
        self.setText(f'🔥 {message}')
        self.setStandardButtons(QMessageBox.Ok)
        
        # Стилизация
        self.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QMessageBox QLabel {
                color: #2c3e50;
                font-size: 12px;
            }
        """)


class WarningDialog(QMessageBox):
    """Стилизованный диалог предупреждения"""
    
    def __init__(self, title="Предупреждение", message="Внимание!", parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle(f'⚠️ {title}')
        self.setText(f'⚠️ {message}')
        self.setStandardButtons(QMessageBox.Ok)
        
        # Стилизация
        self.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QMessageBox QLabel {
                color: #2c3e50;
                font-size: 12px;
            }
        """)


class SuccessDialog(QMessageBox):
    """Стилизованный диалог успеха"""
    
    def __init__(self, title="Успех", message="Операция выполнена успешно!", parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle(f'🎉 {title}')
        self.setText(f'✅ {message}')
        self.setStandardButtons(QMessageBox.Ok)
        
        # Стилизация
        self.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QMessageBox QLabel {
                color: #2c3e50;
                font-size: 12px;
            }
        """)


class ConfirmationDialog(QMessageBox):
    """Стилизованный диалог подтверждения"""
    
    def __init__(self, title="Подтверждение", message="Вы уверены?", parent=None):
        super().__init__(parent)
        self.setIcon(QMessageBox.Question)
        self.setWindowTitle(f'❓ {title}')
        self.setText(f'🤔 {message}')
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.setDefaultButton(QMessageBox.No)
        
        # Стилизация
        self.setStyleSheet("""
            QMessageBox {
                background-color: #f8f9fa;
            }
            QMessageBox QLabel {
                color: #2c3e50;
                font-size: 12px;
            }
        """)
