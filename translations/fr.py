# -*- coding: utf-8 -*-
"""
French translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'Convertisseur MIF/TAB vers SHP/GeoJSON - Convertisseur par Lots',
    'conversion_mode': 'Mode de Conversion',
    'single_file': 'Fichier Unique',
    'batch_processing': 'Traitement par Lots (Dossier)',
    'input_file': 'Fichier d\'Entrée:',
    'input_folder': 'Dossier d\'Entrée:',
    'output_folder': 'Dossier de Sortie:',
    'output_format': 'Format de Sortie:',
    'browse': 'Parcourir...',
    'threading_settings': 'Paramètres de Threading',
    'thread_count': 'Nombre de Threads:',
    'coordinate_system': 'Système de Coordonnées',
    'crs_format_hint': 'Format: EPSG:code, PROJ4 ou WKT',
    'add_to_project': 'Ajouter le résultat au projet QGIS',
    'progress': 'Progrès:',
    'logs': 'Journaux',
    'results': 'Résultats',
    'start_conversion': 'Démarrer la Conversion',
    'cancel': 'Annuler',
    'clear_logs': 'Effacer les Journaux',
    'converting': 'Conversion en cours...',
    'language': 'Langue:',
    'file': 'Fichier',
    'status': 'Statut',
    'message': 'Message',
    'success': 'Succès',
    'error': 'Erreur',
    'select_input_file': 'Sélectionner le fichier d\'entrée',
    'select_input_folder': 'Sélectionner le dossier d\'entrée',
    'select_output_folder': 'Sélectionner le dossier de sortie',
    'error_no_input_file': 'Sélectionner un fichier d\'entrée valide',
    'error_no_input_folder': 'Sélectionner un dossier valide',
    'error_no_files_found': 'Aucun fichier supporté trouvé dans le dossier sélectionné',
    'error_no_output_folder': 'Spécifier le dossier de sortie',
    'error_no_crs': 'Spécifier le système de coordonnées',
    'conversion_cancelled': 'Annulation de la conversion...',
    'confirm_close': 'Conversion en cours. Arrêter et fermer?',
    'confirmation': 'Confirmation',
    'critical_error': 'Erreur Critique',
    'supported_formats': 'Fichiers MIF/TAB (*.mif *.tab)',
    'author_info': 'Auteur: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nAnnée: 2025',
    'about_author': 'À Propos de l\'Auteur',
    'settings': 'Paramètres',
    'input_output': 'Entrée et Sortie',
    'processing_options': 'Options de Traitement',
    
    # Donation dialog translations
    'donation_title': '☕ Soutenir le Développement',
    'donation_window_title': '☕ Soutenir le Développement du Plugin',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Convertisseur MIF/TAB vers SHP/GeoJSON</b></p>
            <p>ce plugin est développé et maintenu <b>gratuitement</b> !</p>
            <p>Votre soutien aide à mettre à jour et améliorer le plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Chaque café compte ! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Acheter un Café sur Ko-fi',
    'donation_tbank': '💳 Faire un Don via T-Bank',
    'donation_github': '💖 Parrainer sur GitHub',
    'donation_maybe_later': '✅ Peut-être Plus Tard',
    'donation_support_development': '☕ Soutenir le Développement du Plugin',
    'donation_plugin_info': 'ce plugin est développé et maintenu gratuitement !',
    'donation_help_improve': 'Votre soutien aide à mettre à jour et améliorer le plugin.',
    'donation_every_coffee': 'Chaque café compte ! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'Exemples de Systèmes de Coordonnées',
    'crs_examples_window_title': 'Exemples de Formats de Systèmes de Coordonnées',
    'crs_examples_button': 'Exemples de Systèmes de Coordonnées',
    'crs_examples_close': 'Fermer',
    'crs_examples_content': '''🌍 FORMAT EPSG (recommandé):
   EPSG:4326    - WGS84 (latitude/longitude)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (France)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (Pays-Bas)

📝 FORMAT PROJ4:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ FORMAT WKT (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 RECOMMANDATIONS:
   • Utilisez les codes EPSG pour la simplicité
   • EPSG:4326 - format universel WGS84
   • Pour les projets locaux, utilisez les zones UTM
   • Vérifiez l'exactitude du CRS avant la conversion

🔍 RESSOURCES UTILES:
   • https://epsg.io/ - recherche de codes EPSG
   • https://spatialreference.org/ - base de données CRS
   • QGIS Browser - recherche CRS intégrée''',
    
    # Header buttons translations
    'header_support': 'Soutien',
    'header_about_author': 'À Propos de l\'Auteur'
}
