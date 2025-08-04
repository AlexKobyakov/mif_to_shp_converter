# -*- coding: utf-8 -*-
"""
Spanish translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'Convertidor MIF/TAB a SHP/GeoJSON - Convertidor por Lotes',
    'conversion_mode': 'Modo de Conversión',
    'single_file': 'Archivo Único',
    'batch_processing': 'Procesamiento por Lotes (Carpeta)',
    'input_file': 'Archivo de Entrada:',
    'input_folder': 'Carpeta de Entrada:',
    'output_folder': 'Carpeta de Salida:',
    'output_format': 'Formato de Salida:',
    'browse': 'Examinar...',
    'threading_settings': 'Configuración de Hilos',
    'thread_count': 'Cantidad de Hilos:',
    'coordinate_system': 'Sistema de Coordenadas',
    'crs_format_hint': 'Formato: EPSG:código, PROJ4 o WKT',
    'add_to_project': 'Agregar resultado al proyecto QGIS',
    'progress': 'Progreso:',
    'logs': 'Registros',
    'results': 'Resultados',
    'start_conversion': 'Iniciar Conversión',
    'cancel': 'Cancelar',
    'clear_logs': 'Limpiar Registros',
    'converting': 'Convirtiendo...',
    'language': 'Idioma:',
    'file': 'Archivo',
    'status': 'Estado',
    'message': 'Mensaje',
    'success': 'Éxito',
    'error': 'Error',
    'select_input_file': 'Seleccionar archivo de entrada',
    'select_input_folder': 'Seleccionar carpeta de entrada',
    'select_output_folder': 'Seleccionar carpeta de salida',
    'error_no_input_file': 'Seleccionar un archivo de entrada válido',
    'error_no_input_folder': 'Seleccionar una carpeta válida',
    'error_no_files_found': 'No se encontraron archivos compatibles en la carpeta seleccionada',
    'error_no_output_folder': 'Especificar carpeta de salida',
    'error_no_crs': 'Especificar sistema de coordenadas',
    'conversion_cancelled': 'Cancelando conversión...',
    'confirm_close': '¿Conversión en progreso. Detener y cerrar?',
    'confirmation': 'Confirmación',
    'critical_error': 'Error Crítico',
    'supported_formats': 'Archivos MIF/TAB (*.mif *.tab)',
    'author_info': 'Autor: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nAño: 2025',
    'about_author': 'Acerca del Autor',
    'settings': 'Configuración',
    'input_output': 'Entrada y Salida',
    'processing_options': 'Opciones de Procesamiento',
    
    # Donation dialog translations
    'donation_title': '☕ Apoyar el Desarrollo',
    'donation_window_title': '☕ Apoyar el Desarrollo del Plugin',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Convertidor MIF/TAB a SHP/GeoJSON</b></p>
            <p>¡este plugin es desarrollado y mantenido <b>gratuitamente</b>!</p>
            <p>Su apoyo ayuda a actualizar y mejorar el plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">¡Cada café cuenta! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Comprar Café en Ko-fi',
    'donation_tbank': '💳 Donar via T-Bank',
    'donation_github': '💖 Patrocinar en GitHub',
    'donation_maybe_later': '✅ Tal vez Más Tarde',
    'donation_support_development': '☕ Apoyar el Desarrollo del Plugin',
    'donation_plugin_info': '¡este plugin es desarrollado y mantenido gratuitamente!',
    'donation_help_improve': 'Su apoyo ayuda a actualizar y mejorar el plugin.',
    'donation_every_coffee': '¡Cada café cuenta! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'Ejemplos de Sistemas de Coordenadas',
    'crs_examples_window_title': 'Ejemplos de Formatos de Sistemas de Coordenadas',
    'crs_examples_button': 'Ejemplos de Sistemas de Coordenadas',
    'crs_examples_close': 'Cerrar',
    'crs_examples_content': '''🌍 FORMATO EPSG (recomendado):
   EPSG:4326    - WGS84 (latitud/longitud)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (Francia)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (Países Bajos)

📝 FORMATO PROJ4:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ FORMATO WKT (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 RECOMENDACIONES:
   • Use códigos EPSG para simplicidad
   • EPSG:4326 - formato universal WGS84
   • Para proyectos locales use zonas UTM
   • Verifique la corrección del CRS antes de la conversión

🔍 RECURSOS ÚTILES:
   • https://epsg.io/ - búsqueda de códigos EPSG
   • https://spatialreference.org/ - base de datos CRS
   • QGIS Browser - búsqueda integrada de CRS''',
    
    # Header buttons translations
    'header_support': 'Soporte',
    'header_about_author': 'Acerca del Autor'
}
