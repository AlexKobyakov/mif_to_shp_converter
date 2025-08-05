# -*- coding: utf-8 -*-
"""
Russian translations for MIF/TAB to SHP/GeoJSON Converter Plugin
Русские переводы для плагина конвертации MIF/TAB в SHP/GeoJSON

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'MIF/TAB в SHP/GeoJSON Конвертер - Пакетный конвертер',
    'conversion_mode': 'Режим конвертации',
    'single_file': 'Один файл',
    'batch_processing': 'Пакетная обработка (папка)',
    'input_file': 'Входной файл:',
    'input_folder': 'Папка с файлами:',
    'output_folder': 'Выходная папка:',
    'output_format': 'Выходной формат:',
    'browse': 'Обзор...',
    'threading_settings': 'Настройки многопоточности',
    'thread_count': 'Количество потоков:',
    'coordinate_system': 'Система координат',
    'crs_format_hint': 'Формат: EPSG:код, PROJ4 или WKT',
    'add_to_project': 'Добавить результат в проект QGIS',
    'progress': 'Прогресс:',
    'logs': 'Логи',
    'results': 'Результаты',
    'start_conversion': 'Начать конвертацию',
    'cancel': 'Отмена',
    'clear_logs': 'Очистить логи',
    'converting': 'Конвертация...',
    'language': 'Язык:',
    'file': 'Файл',
    'status': 'Статус',
    'message': 'Сообщение',
    'success': 'Успешно',
    'error': 'Ошибка',
    'select_input_file': 'Выберите входной файл',
    'select_input_folder': 'Выберите папку с файлами',
    'select_output_folder': 'Выберите выходную папку',
    'error_no_input_file': 'Выберите корректный входной файл',
    'error_no_input_folder': 'Выберите корректную папку',
    'error_no_files_found': 'В выбранной папке не найдено поддерживаемых файлов',
    'error_no_output_folder': 'Укажите выходную папку',
    'error_no_crs': 'Укажите систему координат',
    'conversion_cancelled': 'Отмена конвертации...',
    'confirm_close': 'Конвертация в процессе. Остановить и закрыть?',
    'confirmation': 'Подтверждение',
    'critical_error': 'Критическая ошибка',
    'supported_formats': 'MIF/TAB файлы (*.mif *.tab)',
    'author_info': 'Автор: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nГод создания: 2025',
    'about_author': 'Об авторе',
    'settings': 'Настройки',
    'input_output': 'Входные и выходные данные',
    'processing_options': 'Параметры обработки',
    
    # Donation dialog translations
    'donation_title': '☕ Поддержка разработки',
    'donation_window_title': '☕ Поддержите разработку плагина',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 MIF/TAB to SHP/GeoJSON Converter</b></p>
            <p>этот плагин разрабатывается и поддерживается <b>бесплатно</b>!</p>
            <p>Ваша поддержка помогает обновлять и улучшать плагин.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Каждый кофе имеет значение! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Купить кофе на Ko-fi',
    'donation_tbank': '💳 Пожертвовать через Т Банк',
    'donation_github': '💖 Спонсировать на GitHub',
    'donation_maybe_later': '✅ Может быть позже',
    'donation_support_development': '☕ Поддержите разработку плагина',
    'donation_plugin_info': 'этот плагин разрабатывается и поддерживается бесплатно!',
    'donation_help_improve': 'Ваша поддержка помогает обновлять и улучшать плагин.',
    'donation_every_coffee': 'Каждый кофе имеет значение! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'Примеры систем координат',
    'crs_examples_window_title': 'Примеры форматов систем координат',
    'crs_examples_button': 'Примеры систем координат',
    'crs_examples_close': 'Закрыть',
    'crs_examples_content': '''🌍 ФОРМАТ EPSG (рекомендуемый):
   EPSG:4326    - WGS84 (широта/долгота)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (Франция)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (Нидерланды)

📝 ФОРМАТ PROJ4:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ ФОРМАТ WKT (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 РЕКОМЕНДАЦИИ:
   • Используйте EPSG коды для простоты
   • EPSG:4326 - универсальный формат WGS84
   • Для локальных проектов используйте UTM зоны
   • Проверьте корректность CRS перед конвертацией

🔍 ПОЛЕЗНЫЕ РЕСУРСЫ:
   • https://epsg.io/ - поиск EPSG кодов
   • https://spatialreference.org/ - база CRS
   • QGIS Browser - встроенный поиск CRS''',
    
    # Header buttons translations
    'header_support': 'Поддержка',
    'header_about_author': 'Об авторе',
    
    # Author dialog translations
    'version': 'Версия',
    'author': 'Автор',
    'contact': 'Контакт',
    'year': 'Год',
    'organization': 'Организация',
    'plugin_description': 'Профессиональный инструмент конвертации ГИС данных',
    'multilingual_support': 'Поддерживает множество языков и форматов'
}
