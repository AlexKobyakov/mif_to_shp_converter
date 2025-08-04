# -*- coding: utf-8 -*-
"""
German translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'MIF/TAB zu SHP/GeoJSON Konverter - Batch Konverter',
    'conversion_mode': 'Konvertierungsmodus',
    'single_file': 'Einzelne Datei',
    'batch_processing': 'Stapelverarbeitung (Ordner)',
    'input_file': 'Eingabedatei:',
    'input_folder': 'Eingabeordner:',
    'output_folder': 'Ausgabeordner:',
    'output_format': 'Ausgabeformat:',
    'browse': 'Durchsuchen...',
    'threading_settings': 'Threading-Einstellungen',
    'thread_count': 'Thread-Anzahl:',
    'coordinate_system': 'Koordinatensystem',
    'crs_format_hint': 'Format: EPSG:Code, PROJ4 oder WKT',
    'add_to_project': 'Ergebnis zu QGIS-Projekt hinzufügen',
    'progress': 'Fortschritt:',
    'logs': 'Protokolle',
    'results': 'Ergebnisse',
    'start_conversion': 'Konvertierung starten',
    'cancel': 'Abbrechen',
    'clear_logs': 'Protokolle löschen',
    'converting': 'Konvertierung läuft...',
    'language': 'Sprache:',
    'file': 'Datei',
    'status': 'Status',
    'message': 'Nachricht',
    'success': 'Erfolg',
    'error': 'Fehler',
    'select_input_file': 'Eingabedatei auswählen',
    'select_input_folder': 'Eingabeordner auswählen',
    'select_output_folder': 'Ausgabeordner auswählen',
    'error_no_input_file': 'Gültige Eingabedatei auswählen',
    'error_no_input_folder': 'Gültigen Ordner auswählen',
    'error_no_files_found': 'Keine unterstützten Dateien im ausgewählten Ordner gefunden',
    'error_no_output_folder': 'Ausgabeordner angeben',
    'error_no_crs': 'Koordinatensystem angeben',
    'conversion_cancelled': 'Konvertierung wird abgebrochen...',
    'confirm_close': 'Konvertierung läuft. Stoppen und schließen?',
    'confirmation': 'Bestätigung',
    'critical_error': 'Kritischer Fehler',
    'supported_formats': 'MIF/TAB-Dateien (*.mif *.tab)',
    'author_info': 'Autor: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nJahr: 2025',
    'about_author': 'Über den Autor',
    'settings': 'Einstellungen',
    'input_output': 'Eingabe und Ausgabe',
    'processing_options': 'Verarbeitungsoptionen',
    
    # Donation dialog translations
    'donation_title': '☕ Entwicklung Unterstützen',
    'donation_window_title': '☕ Plugin-Entwicklung Unterstützen',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 MIF/TAB zu SHP/GeoJSON Konverter</b></p>
            <p>dieses Plugin wird <b>kostenlos</b> entwickelt und gepflegt!</p>
            <p>Ihre Unterstützung hilft, das Plugin zu aktualisieren und zu verbessern.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Jeder Kaffee zählt! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Kaffee auf Ko-fi Kaufen',
    'donation_tbank': '💳 Spenden via T-Bank',
    'donation_github': '💖 Auf GitHub Sponsern',
    'donation_maybe_later': '✅ Vielleicht Später',
    'donation_support_development': '☕ Plugin-Entwicklung Unterstützen',
    'donation_plugin_info': 'dieses Plugin wird kostenlos entwickelt und gepflegt!',
    'donation_help_improve': 'Ihre Unterstützung hilft, das Plugin zu aktualisieren und zu verbessern.',
    'donation_every_coffee': 'Jeder Kaffee zählt! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'Koordinatensystem-Beispiele',
    'crs_examples_window_title': 'Koordinatensystem-Format-Beispiele',
    'crs_examples_button': 'Koordinatensystem-Beispiele',
    'crs_examples_close': 'Schließen',
    'crs_examples_content': '''🌍 EPSG-FORMAT (empfohlen):
   EPSG:4326    - WGS84 (Breiten-/Längengrad)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (Frankreich)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (Niederlande)

📝 PROJ4-FORMAT:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ WKT-FORMAT (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 EMPFEHLUNGEN:
   • Verwenden Sie EPSG-Codes für Einfachheit
   • EPSG:4326 - universelles WGS84-Format
   • Für lokale Projekte verwenden Sie UTM-Zonen
   • Überprüfen Sie die CRS-Korrektheit vor der Konvertierung

🔍 NÜTZLICHE RESSOURCEN:
   • https://epsg.io/ - EPSG-Code-Suche
   • https://spatialreference.org/ - CRS-Datenbank
   • QGIS Browser - eingebaute CRS-Suche''',
    
    # Header buttons translations
    'header_support': 'Unterstützung',
    'header_about_author': 'Über den Autor'
}
