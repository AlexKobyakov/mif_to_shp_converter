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
from .gui import MifToShpDialog


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
        self.menu = 'MIF/TAB Converter'
        
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
        self.action = QAction(
            QIcon(icon_path),
            '🎯 MIF/TAB to SHP/GeoJSON Converter',
            self.iface.mainWindow()
        )
        
        # Подключение действия
        self.action.triggered.connect(self.run)
        self.action.setEnabled(True)
        self.action.setToolTip(translations.get_text('window_title'))
        self.action.setStatusTip(translations.get_text('window_title'))

        # Добавление в меню и панель инструментов
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToVectorMenu(self.menu, self.action)

    def unload(self):
        """Удаление плагина"""
        # Удаление из меню и панели инструментов
        self.iface.removePluginVectorMenu(self.menu, self.action)
        self.iface.removeToolBarIcon(self.action)
        
        # Очистка переводчика
        if self.translator:
            QCoreApplication.removeTranslator(self.translator)

    def run(self):
        """Запуск плагина"""
        # Создание диалога при первом запуске
        if self.dialog is None:
            self.dialog = MifToShpDialog()
        
        # Показ диалога
        result = self.dialog.exec_()
        
        # Обработка результата (при необходимости)
        if result:
            pass  # Диалог был принят
