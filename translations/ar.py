# -*- coding: utf-8 -*-
"""
Arabic translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'محول MIF/TAB إلى SHP/GeoJSON - محول مجموعة',
    'conversion_mode': 'وضع التحويل',
    'single_file': 'ملف واحد',
    'batch_processing': 'معالجة مجموعة (مجلد)',
    'input_file': 'ملف الإدخال:',
    'input_folder': 'مجلد الإدخال:',
    'output_folder': 'مجلد الإخراج:',
    'output_format': 'تنسيق الإخراج:',
    'browse': 'تصفح...',
    'threading_settings': 'إعدادات الخيوط',
    'thread_count': 'عدد الخيوط:',
    'coordinate_system': 'نظام الإحداثيات',
    'crs_format_hint': 'التنسيق: EPSG:رمز، PROJ4 أو WKT',
    'add_to_project': 'إضافة النتيجة إلى مشروع QGIS',
    'progress': 'التقدم:',
    'logs': 'السجلات',
    'results': 'النتائج',
    'start_conversion': 'بدء التحويل',
    'cancel': 'إلغاء',
    'clear_logs': 'مسح السجلات',
    'converting': 'جاري التحويل...',
    'language': 'اللغة:',
    'file': 'ملف',
    'status': 'الحالة',
    'message': 'رسالة',
    'success': 'نجح',
    'error': 'خطأ',
    'select_input_file': 'اختر ملف الإدخال',
    'select_input_folder': 'اختر مجلد الإدخال',
    'select_output_folder': 'اختر مجلد الإخراج',
    'error_no_input_file': 'اختر ملف إدخال صالح',
    'error_no_input_folder': 'اختر مجلد صالح',
    'error_no_files_found': 'لم يتم العثور على ملفات مدعومة في المجلد المحدد',
    'error_no_output_folder': 'حدد مجلد الإخراج',
    'error_no_crs': 'حدد نظام الإحداثيات',
    'conversion_cancelled': 'إلغاء التحويل...',
    'confirm_close': 'التحويل قيد التقدم. إيقاف وإغلاق؟',
    'confirmation': 'تأكيد',
    'critical_error': 'خطأ حرج',
    'supported_formats': 'ملفات MIF/TAB (*.mif *.tab)',
    'author_info': 'المؤلف: Кобяков Александр Викторович (Alex Kobyakov)\nالبريد الإلكتروني: kobyakov@lesburo.ru\nالسنة: 2025',
    'about_author': 'حول المؤلف',
    'settings': 'الإعدادات',
    'input_output': 'الإدخال والإخراج',
    'processing_options': 'خيارات المعالجة',
    
    # Donation dialog translations
    'donation_title': '☕ دعم التطوير',
    'donation_window_title': '☕ دعم تطوير المكون الإضافي',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 محول MIF/TAB إلى SHP/GeoJSON</b></p>
            <p>هذا المكون الإضافي يتم تطويره وصيانته <b>مجانًا</b>!</p>
            <p>دعمك يساعد في تحديث وتحسين المكون الإضافي.</p>
            <p style="color: #7f8c8d; font-size: 13px;">كل قهوة مهمة! ❤️</p>
        </div>''',
    'donation_kofi': '☕ شراء قهوة على Ko-fi',
    'donation_tbank': '💳 التبرع عبر T-Bank',
    'donation_github': '💖 الرعاية على GitHub',
    'donation_maybe_later': '✅ ربما لاحقًا',
    'donation_support_development': '☕ دعم تطوير المكون الإضافي',
    'donation_plugin_info': 'هذا المكون الإضافي يتم تطويره وصيانته مجانًا!',
    'donation_help_improve': 'دعمك يساعد في تحديث وتحسين المكون الإضافي.',
    'donation_every_coffee': 'كل قهوة مهمة! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'أمثلة أنظمة الإحداثيات',
    'crs_examples_window_title': 'أمثلة تنسيقات أنظمة الإحداثيات',
    'crs_examples_button': 'أمثلة أنظمة الإحداثيات',
    'crs_examples_close': 'إغلاق',
    'crs_examples_content': '''🌍 تنسيق EPSG (موصى به):
   EPSG:4326    - WGS84 (خط العرض/خط الطول)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (فرنسا)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (هولندا)

📝 تنسيق PROJ4:
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ تنسيق WKT (Well-Known Text):
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 التوصيات:
   • استخدم رموز EPSG للبساطة
   • EPSG:4326 - تنسيق WGS84 عالمي
   • للمشاريع المحلية استخدم مناطق UTM
   • تحقق من صحة CRS قبل التحويل

🔍 موارد مفيدة:
   • https://epsg.io/ - بحث رموز EPSG
   • https://spatialreference.org/ - قاعدة بيانات CRS
   • QGIS Browser - بحث CRS مدمج''',
    
    # Header buttons translations
    'header_support': 'دعم',
    'header_about_author': 'حول المؤلف'
}
