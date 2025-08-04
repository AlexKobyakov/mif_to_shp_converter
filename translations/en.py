# -*- coding: utf-8 -*-
"""
English translations for MIF/TAB to SHP/GeoJSON Converter Plugin
Английские переводы для плагина конвертации MIF/TAB в SHP/GeoJSON

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'MIF/TAB to SHP/GeoJSON Converter - Batch Converter',
    'conversion_mode': 'Conversion Mode',
    'single_file': 'Single File',
    'batch_processing': 'Batch Processing (Folder)',
    'input_file': 'Input File:',
    'input_folder': 'Input Folder:',
    'output_folder': 'Output Folder:',
    'output_format': 'Output Format:',
    'browse': 'Browse...',
    'threading_settings': 'Threading Settings',
    'thread_count': 'Thread Count:',
    'coordinate_system': 'Coordinate System',
    'crs_format_hint': 'Format: EPSG:code, PROJ4 or WKT',
    'add_to_project': 'Add result to QGIS project',
    'progress': 'Progress:',
    'logs': 'Logs',
    'results': 'Results',
    'start_conversion': 'Start Conversion',
    'cancel': 'Cancel',
    'clear_logs': 'Clear Logs',
    'converting': 'Converting...',
    'language': 'Language:',
    'file': 'File',
    'status': 'Status',
    'message': 'Message',
    'success': 'Success',
    'error': 'Error',
    'select_input_file': 'Select input file',
    'select_input_folder': 'Select input folder',
    'select_output_folder': 'Select output folder',
    'error_no_input_file': 'Select a valid input file',
    'error_no_input_folder': 'Select a valid folder',
    'error_no_files_found': 'No supported files found in selected folder',
    'error_no_output_folder': 'Specify output folder',
    'error_no_crs': 'Specify coordinate system',
    'conversion_cancelled': 'Cancelling conversion...',
    'confirm_close': 'Conversion in progress. Stop and close?',
    'confirmation': 'Confirmation',
    'critical_error': 'Critical Error',
    'supported_formats': 'MIF/TAB files (*.mif *.tab)',
    'author_info': 'Author: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nYear: 2025',
    'about_author': 'About Author',
    'settings': 'Settings',
    'input_output': 'Input & Output',
    'processing_options': 'Processing Options',
    
    # Donation dialog translations
    'donation_title': '☕ Support Development',
    'donation_window_title': '☕ Support Plugin Development',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 MIF/TAB to SHP/GeoJSON Converter</b></p>
            <p>this plugin is developed and maintained <b>for free</b>!</p>
            <p>Your support helps update and improve the plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Every coffee counts! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Buy Coffee on Ko-fi',
    'donation_tbank': '💳 Donate via T-Bank',
    'donation_github': '💖 Sponsor on GitHub',
    'donation_maybe_later': '✅ Maybe Later',
    'donation_support_development': '☕ Support Plugin Development',
    'donation_plugin_info': 'this plugin is developed and maintained for free!',
    'donation_help_improve': 'Your support helps update and improve the plugin.',
    'donation_every_coffee': 'Every coffee counts! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'Coordinate System Examples',
    'crs_examples_window_title': 'Coordinate System Format Examples',
    'crs_examples_button': 'Coordinate System Examples',
    'crs_examples_close': 'Close',
    'crs_examples_content': '''🌍 EPSG FORMAT (recommended):
   EPSG:4326    - WGS84 (latitude/longitude)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (France)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (Netherlands)

📝 PROJ4 FORMAT:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ WKT FORMAT (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 RECOMMENDATIONS:
   • Use EPSG codes for simplicity
   • EPSG:4326 - universal WGS84 format
   • For local projects use UTM zones
   • Verify CRS correctness before conversion

🔍 USEFUL RESOURCES:
   • https://epsg.io/ - EPSG code search
   • https://spatialreference.org/ - CRS database
   • QGIS Browser - built-in CRS search''',
    
    # Header buttons translations
    'header_support': 'Support',
    'header_about_author': 'About Author'
}
