# -*- coding: utf-8 -*-
"""
Hindi translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'MIF/TAB से SHP/GeoJSON कन्वर्टर - बैच कन्वर्टर',
    'conversion_mode': 'रूपांतरण मोड',
    'single_file': 'एकल फ़ाइल',
    'batch_processing': 'बैच प्रोसेसिंग (फ़ोल्डर)',
    'input_file': 'इनपुट फ़ाइल:',
    'input_folder': 'इनपुट फ़ोल्डर:',
    'output_folder': 'आउटपुट फ़ोल्डर:',
    'output_format': 'आउटपुट प्रारूप:',
    'browse': 'ब्राउज़...',
    'threading_settings': 'थ्रेडिंग सेटिंग्स',
    'thread_count': 'थ्रेड गिनती:',
    'coordinate_system': 'समन्वय प्रणाली',
    'crs_format_hint': 'प्रारूप: EPSG:कोड, PROJ4 या WKT',
    'add_to_project': 'QGIS प्रोजेक्ट में परिणाम जोड़ें',
    'progress': 'प्रगति:',
    'logs': 'लॉग',
    'results': 'परिणाम',
    'start_conversion': 'रूपांतरण शुरू करें',
    'cancel': 'रद्द करें',
    'clear_logs': 'लॉग साफ़ करें',
    'converting': 'रूपांतरित कर रहा है...',
    'language': 'भाषा:',
    'file': 'फ़ाइल',
    'status': 'स्थिति',
    'message': 'संदेश',
    'success': 'सफल',
    'error': 'त्रुटि',
    'select_input_file': 'इनपुट फ़ाइल चुनें',
    'select_input_folder': 'इनपुट फ़ोल्डर चुनें',
    'select_output_folder': 'आउटपुट फ़ोल्डर चुनें',
    'error_no_input_file': 'एक वैध इनपुट फ़ाइल चुनें',
    'error_no_input_folder': 'एक वैध फ़ोल्डर चुनें',
    'error_no_files_found': 'चयनित फ़ोल्डर में कोई समर्थित फ़ाइल नहीं मिली',
    'error_no_output_folder': 'आउटपुट फ़ोल्डर निर्दिष्ट करें',
    'error_no_crs': 'समन्वय प्रणाली निर्दिष्ट करें',
    'conversion_cancelled': 'रूपांतरण रद्द कर रहा है...',
    'confirm_close': 'रूपांतरण प्रगति में है। रोकें और बंद करें?',
    'confirmation': 'पुष्टि',
    'critical_error': 'गंभीर त्रुटि',
    'supported_formats': 'MIF/TAB फ़ाइलें (*.mif *.tab)',
    'author_info': 'लेखक: Кобяков Александр Викторович (Alex Kobyakov)\nईमेल: kobyakov@lesburo.ru\nवर्ष: 2025',
    'about_author': 'लेखक के बारे में',
    'settings': 'सेटिंग्स',
    'input_output': 'इनपुट आउटपुट',
    'processing_options': 'प्रसंस्करण विकल्प',
    
    # Donation dialog translations
    'donation_title': '☕ विकास का समर्थन',
    'donation_window_title': '☕ प्लगइन विकास का समर्थन',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 MIF/TAB to SHP/GeoJSON कन्वर्टर</b></p>
            <p>यह प्लगइन <b>मुफ़्त में</b> विकसित और बनाए रखा गया है!</p>
            <p>आपका समर्थन प्लगइन को अपडेट और सुधारने में मदद करता है।</p>
            <p style="color: #7f8c8d; font-size: 13px;">हर कॉफी मायने रखती है! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Ko-fi पर कॉफी खरीदें',
    'donation_tbank': '💳 T-Bank के माध्यम से दान',
    'donation_github': '💖 GitHub पर स्पॉन्सर करें',
    'donation_maybe_later': '✅ शायद बाद में',
    'donation_support_development': '☕ प्लगइन विकास का समर्थन',
    'donation_plugin_info': 'यह प्लगइन मुफ़्त में विकसित और बनाए रखा गया है!',
    'donation_help_improve': 'आपका समर्थन प्लगइन को अपडेट और सुधारने में मदद करता है।',
    'donation_every_coffee': 'हर कॉफी मायने रखती है! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'समन्वय प्रणाली उदाहरण',
    'crs_examples_window_title': 'समन्वय प्रणाली प्रारूप उदाहरण',
    'crs_examples_button': 'समन्वय प्रणाली उदाहरण',
    'crs_examples_close': 'बंद करें',
    'crs_examples_content': '''🌍 EPSG प्रारूप (सुझाया गया):
   EPSG:4326    - WGS84 (अक्षांश/देशांतर)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (फ्रांस)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (नीदरलैंड)

📝 PROJ4 प्रारूप:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ WKT प्रारूप (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 सिफारिशें:
   • सरलता के लिए EPSG कोड का उपयोग करें
   • EPSG:4326 - सार्वभौमिक WGS84 प्रारूप
   • स्थानीय परियोजनाओं के लिए UTM क्षेत्र का उपयोग करें
   • रूपांतरण से पहले CRS की सहीता की जांच करें

🔍 उपयोगी संसाधन:
   • https://epsg.io/ - EPSG कोड खोज
   • https://spatialreference.org/ - CRS डेटाबेस
   • QGIS Browser - बिल्ट-इन CRS खोज''',
    
    # Header buttons translations
    'header_support': 'समर्थन',
    'header_about_author': 'लेखक के बारे में'
}
