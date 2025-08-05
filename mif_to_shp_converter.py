# -*- coding: utf-8 -*-
"""
MIF/TAB to SHP/GeoJSON Converter Plugin for QGIS
Упрощенный основной класс плагина с модульной архитектурой

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import configparser

from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QAction

from qgis.core import QgsApplication
from qgis.utils import iface

from .translation_manager import translations
# Не импортируем gui здесь, чтобы избежать проблем с импортом
# from .gui import MifToShpDialog


class MifToShpConverter:
    """Основной класс плагина конвертера MIF/TAB в SHP/GeoJSON"""

    def __init__(self, iface):
        """Конструктор плагина"""
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        
        # Инициализация переводов
        self.translator = None
        self.initTranslator()
        
        # Действие плагина
        self.action = None
        self.menu = 'MIF/TAB Converter'  # Короткое название для меню
        
        # Диалог
        self.dialog = None
    
    @staticmethod
    def get_plugin_version():
        """Чтение версии плагина из metadata.txt"""
        try:
            plugin_dir = os.path.dirname(__file__)
            metadata_file = os.path.join(plugin_dir, 'metadata.txt')
            
            if os.path.exists(metadata_file):
                config = configparser.ConfigParser()
                config.read(metadata_file, encoding='utf-8')
                
                if 'general' in config and 'version' in config['general']:
                    return config['general']['version']
            
            return "Unknown"
        except Exception as e:
            print(f"Error reading plugin version: {e}")
            return "Unknown"
    
    @staticmethod
    def get_plugin_info():
        """Получение полной информации о плагине из metadata.txt"""
        try:
            plugin_dir = os.path.dirname(__file__)
            metadata_file = os.path.join(plugin_dir, 'metadata.txt')
            
            if os.path.exists(metadata_file):
                config = configparser.ConfigParser()
                config.read(metadata_file, encoding='utf-8')
                
                if 'general' in config:
                    return {
                        'name': config['general'].get('name', 'MIF/TAB to SHP/GeoJSON Converter'),
                        'version': config['general'].get('version', 'Unknown'),
                        'author': config['general'].get('author', 'Unknown'),
                        'email': config['general'].get('email', ''),
                        'description': config['general'].get('description', '')
                    }
            
            return {
                'name': 'MIF/TAB to SHP/GeoJSON Converter',
                'version': 'Unknown',
                'author': 'Unknown',
                'email': '',
                'description': ''
            }
        except Exception as e:
            print(f"Error reading plugin info: {e}")
            return {
                'name': 'MIF/TAB to SHP/GeoJSON Converter',
                'version': 'Unknown',
                'author': 'Unknown',
                'email': '',
                'description': ''
            }

    def initTranslator(self):
        """Инициализация переводов"""
        # Определение языка системы
        locale = QSettings().value('locale/userLocale')[0:2]
        
        # Установка языка в translations
        translations.set_language(locale)
        
        # Загрузка переводчика Qt
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            f'MifToShpConverter_{locale}.qm'
        )

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)
            QCoreApplication.installTranslator(self.translator)

    def initGui(self):
        """Создание GUI плагина"""
        # Создание действия
        icon_path = os.path.join(self.plugin_dir, 'icon.png')
        
        # Получаем переведенное название
        plugin_name = translations.get_text('window_title') or 'MIF/TAB to SHP/GeoJSON Converter'
        
        self.action = QAction(
            QIcon(icon_path),
            f'🎯 {plugin_name}',
            self.iface.mainWindow()
        )
        
        # Подключение действия
        self.action.triggered.connect(self.run)
        self.action.setEnabled(True)
        self.action.setToolTip(plugin_name)
        self.action.setStatusTip(plugin_name)

        # Добавление в меню Vector и панель инструментов
        # Пробуем разные способы добавления в меню
        try:
            # Метод 1: Добавление через addPluginToVectorMenu
            self.iface.addPluginToVectorMenu(self.menu, self.action)
            print(f"Successfully added plugin '{self.menu}' to Vector menu using addPluginToVectorMenu")
        except Exception as e:
            print(f"Method 1 failed: {e}")
            
            try:
                # Метод 2: Прямое добавление в меню Vector
                vector_menu = self.iface.vectorMenu()
                if vector_menu:
                    vector_menu.addAction(self.action)
                    print(f"Successfully added plugin using direct vector menu access")
                else:
                    print("Vector menu not found")
            except Exception as e2:
                print(f"Method 2 also failed: {e2}")
                
                try:
                    # Метод 3: Добавление в общее меню плагинов
                    self.iface.addPluginToMenu(self.menu, self.action)
                    print(f"Successfully added plugin '{self.menu}' to Plugins menu using addPluginToMenu")
                except Exception as e3:
                    print(f"All methods failed. Last error: {e3}")
        
        # Добавление на панель инструментов (это работает)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        """Удаление плагина"""
        try:
            # Удаление с панели инструментов (всегда работает)
            self.iface.removeToolBarIcon(self.action)
            
            # Пробуем разные способы удаления из меню
            try:
                # Метод 1: Удаление через removePluginVectorMenu
                self.iface.removePluginVectorMenu(self.menu, self.action)
                print(f"Successfully removed plugin '{self.menu}' from Vector menu")
            except Exception as e:
                print(f"removePluginVectorMenu failed: {e}")
                
                try:
                    # Метод 2: Прямое удаление из меню Vector
                    vector_menu = self.iface.vectorMenu()
                    if vector_menu:
                        vector_menu.removeAction(self.action)
                        print(f"Successfully removed plugin using direct vector menu access")
                except Exception as e2:
                    print(f"Direct vector menu removal failed: {e2}")
                    
                    try:
                        # Метод 3: Удаление из общего меню плагинов
                        self.iface.removePluginMenu(self.menu, self.action)
                        print(f"Successfully removed plugin '{self.menu}' from Plugins menu")
                    except Exception as e3:
                        print(f"All removal methods failed. Last error: {e3}")
            
        except Exception as e:
            print(f"Error during plugin unload: {e}")
        
        # Очистка переводчика
        if self.translator:
            QCoreApplication.removeTranslator(self.translator)

    def run(self):
        """Запуск плагина"""
        try:
            # Создание диалога при первом запуске
            if self.dialog is None:
                from .gui import MifToShpDialog
                self.dialog = MifToShpDialog()
                print("Dialog created successfully")
            
            # Показ диалога
            result = self.dialog.exec_()
            
            # Обработка результата (при необходимости)
            if result:
                pass  # Диалог был принят
        
        except Exception as e:
            print(f"Error running plugin: {e}")
            # Показываем ошибку пользователю
            from qgis.PyQt.QtWidgets import QMessageBox
            QMessageBox.critical(self.iface.mainWindow(), 'Ошибка плагина', f'Ошибка при запуске плагина:\n{str(e)}')
