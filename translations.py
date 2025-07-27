# -*- coding: utf-8 -*-
"""
Translations module for MIF/TAB to SHP/GeoJSON Converter Plugin
Модуль переводов для плагина конвертации MIF/TAB в SHP/GeoJSON

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

class Translations:
    """Класс для управления переводами на 9 языков"""
    
    def __init__(self):
        self.current_language = 'ru'
        self.translations = {
            'ru': {
                'window_title': 'MIF/TAB в SHP/GeoJSON Конвертер',
                'start_conversion': 'Начать конвертацию',
                'cancel': 'Отмена',
                'clear_logs': 'Очистить логи',
                'converting': 'Конвертация...',
                'browse': 'Обзор...',
                'success': 'Успешно',
                'error': 'Ошибка',
                'single_file': 'Один файл',
                'batch_processing': 'Пакетная обработка',
                'input': 'Вход',
                'output': 'Выход',
                'format': 'Формат',
                'crs': 'CRS',
                'threads': 'Потоки',
                'add_to_project': 'Добавить в проект QGIS'
            },
            'en': {
                'window_title': 'MIF/TAB to SHP/GeoJSON Converter',
                'start_conversion': 'Start Conversion',
                'cancel': 'Cancel',
                'clear_logs': 'Clear Logs',
                'converting': 'Converting...',
                'browse': 'Browse...',
                'success': 'Success',
                'error': 'Error',
                'single_file': 'Single File',
                'batch_processing': 'Batch Processing',
                'input': 'Input',
                'output': 'Output',
                'format': 'Format',
                'crs': 'CRS',
                'threads': 'Threads',
                'add_to_project': 'Add to QGIS project'
            },
            'zh': {
                'window_title': 'MIF/TAB转SHP/GeoJSON转换器',
                'start_conversion': '开始转换',
                'cancel': '取消',
                'clear_logs': '清除日志',
                'converting': '转换中...',
                'browse': '浏览...',
                'success': '成功',
                'error': '错误',
                'single_file': '单个文件',
                'batch_processing': '批量处理',
                'input': '输入',
                'output': '输出',
                'format': '格式',
                'crs': '坐标系',
                'threads': '线程',
                'add_to_project': '添加到QGIS项目'
            },
            'hi': {
                'window_title': 'MIF/TAB से SHP/GeoJSON कन्वर्टर',
                'start_conversion': 'रूपांतरण शुरू करें',
                'cancel': 'रद्द करें',
                'clear_logs': 'लॉग साफ़ करें',
                'converting': 'रूपांतरित कर रहा है...',
                'browse': 'ब्राउज़...',
                'success': 'सफल',
                'error': 'त्रुटि',
                'single_file': 'एकल फ़ाइल',
                'batch_processing': 'बैच प्रोसेसिंग',
                'input': 'इनपुट',
                'output': 'आउटपुट',
                'format': 'प्रारूप',
                'crs': 'सीआरएस',
                'threads': 'थ्रेड',
                'add_to_project': 'QGIS प्रोजेक्ट में जोड़ें'
            },
            'es': {
                'window_title': 'Convertidor MIF/TAB a SHP/GeoJSON',
                'start_conversion': 'Iniciar Conversión',
                'cancel': 'Cancelar',
                'clear_logs': 'Limpiar Registros',
                'converting': 'Convirtiendo...',
                'browse': 'Examinar...',
                'success': 'Éxito',
                'error': 'Error',
                'single_file': 'Archivo Único',
                'batch_processing': 'Procesamiento por Lotes',
                'input': 'Entrada',
                'output': 'Salida',
                'format': 'Formato',
                'crs': 'CRS',
                'threads': 'Hilos',
                'add_to_project': 'Agregar al proyecto QGIS'
            },
            'ar': {
                'window_title': 'محول MIF/TAB إلى SHP/GeoJSON',
                'start_conversion': 'بدء التحويل',
                'cancel': 'إلغاء',
                'clear_logs': 'مسح السجلات',
                'converting': 'جاري التحويل...',
                'browse': 'تصفح...',
                'success': 'نجح',
                'error': 'خطأ',
                'single_file': 'ملف واحد',
                'batch_processing': 'معالجة مجموعة',
                'input': 'إدخال',
                'output': 'إخراج',
                'format': 'تنسيق',
                'crs': 'نظام الإحداثيات',
                'threads': 'خيوط',
                'add_to_project': 'إضافة لمشروع QGIS'
            },
            'fr': {
                'window_title': 'Convertisseur MIF/TAB vers SHP/GeoJSON',
                'start_conversion': 'Démarrer la Conversion',
                'cancel': 'Annuler',
                'clear_logs': 'Effacer les Journaux',
                'converting': 'Conversion en cours...',
                'browse': 'Parcourir...',
                'success': 'Succès',
                'error': 'Erreur',
                'single_file': 'Fichier Unique',
                'batch_processing': 'Traitement par Lots',
                'input': 'Entrée',
                'output': 'Sortie',
                'format': 'Format',
                'crs': 'CRS',
                'threads': 'Threads',
                'add_to_project': 'Ajouter au projet QGIS'
            },
            'pt': {
                'window_title': 'Conversor MIF/TAB para SHP/GeoJSON',
                'start_conversion': 'Iniciar Conversão',
                'cancel': 'Cancelar',
                'clear_logs': 'Limpar Logs',
                'converting': 'Convertendo...',
                'browse': 'Navegar...',
                'success': 'Sucesso',
                'error': 'Erro',
                'single_file': 'Arquivo Único',
                'batch_processing': 'Processamento em Lote',
                'input': 'Entrada',
                'output': 'Saída',
                'format': 'Formato',
                'crs': 'CRS',
                'threads': 'Threads',
                'add_to_project': 'Adicionar ao projeto QGIS'
            },
            'de': {
                'window_title': 'MIF/TAB zu SHP/GeoJSON Konverter',
                'start_conversion': 'Konvertierung starten',
                'cancel': 'Abbrechen',
                'clear_logs': 'Protokolle löschen',
                'converting': 'Konvertierung läuft...',
                'browse': 'Durchsuchen...',
                'success': 'Erfolg',
                'error': 'Fehler',
                'single_file': 'Einzelne Datei',
                'batch_processing': 'Stapelverarbeitung',
                'input': 'Eingabe',
                'output': 'Ausgabe',
                'format': 'Format',
                'crs': 'CRS',
                'threads': 'Threads',
                'add_to_project': 'Zu QGIS-Projekt hinzufügen'
            }
        }
    
    def get_text(self, key):
        return self.translations.get(self.current_language, {}).get(key, key)
    
    def set_language(self, language):
        if language in self.translations:
            self.current_language = language


# Глобальный объект переводов
translations = Translations()
