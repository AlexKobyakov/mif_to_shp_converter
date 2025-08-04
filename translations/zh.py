# -*- coding: utf-8 -*-
"""
Chinese translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'MIF/TAB转SHP/GeoJSON转换器 - 批量转换器',
    'conversion_mode': '转换模式',
    'single_file': '单个文件',
    'batch_processing': '批量处理（文件夹）',
    'input_file': '输入文件：',
    'input_folder': '输入文件夹：',
    'output_folder': '输出文件夹：',
    'output_format': '输出格式：',
    'browse': '浏览...',
    'threading_settings': '多线程设置',
    'thread_count': '线程数：',
    'coordinate_system': '坐标系统',
    'crs_format_hint': '格式：EPSG:代码、PROJ4或WKT',
    'add_to_project': '将结果添加到QGIS项目',
    'progress': '进度：',
    'logs': '日志',
    'results': '结果',
    'start_conversion': '开始转换',
    'cancel': '取消',
    'clear_logs': '清除日志',
    'converting': '转换中...',
    'language': '语言：',
    'file': '文件',
    'status': '状态',
    'message': '消息',
    'success': '成功',
    'error': '错误',
    'select_input_file': '选择输入文件',
    'select_input_folder': '选择输入文件夹',
    'select_output_folder': '选择输出文件夹',
    'error_no_input_file': '请选择有效的输入文件',
    'error_no_input_folder': '请选择有效的文件夹',
    'error_no_files_found': '在选定文件夹中未找到支持的文件',
    'error_no_output_folder': '请指定输出文件夹',
    'error_no_crs': '请指定坐标系统',
    'conversion_cancelled': '正在取消转换...',
    'confirm_close': '转换正在进行中。停止并关闭？',
    'confirmation': '确认',
    'critical_error': '严重错误',
    'supported_formats': 'MIF/TAB文件 (*.mif *.tab)',
    'author_info': '作者：Кобяков Александр Викторович (Alex Kobyakov)\n邮箱：kobyakov@lesburo.ru\n创建年份：2025',
    'about_author': '关于作者',
    'settings': '设置',
    'input_output': '输入输出',
    'processing_options': '处理选项',
    
    # Donation dialog translations
    'donation_title': '☕ 支持开发',
    'donation_window_title': '☕ 支持插件开发',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 MIF/TAB to SHP/GeoJSON 转换器</b></p>
            <p>这个插件是<b>免费</b>开发和维护的！</p>
            <p>您的支持帮助更新和改进插件。</p>
            <p style="color: #7f8c8d; font-size: 13px;">每一杯咖啡都很重要！❤️</p>
        </div>''',
    'donation_kofi': '☕ 在 Ko-fi 上买咖啡',
    'donation_tbank': '💳 通过 T-Bank 捐款',
    'donation_github': '💖 在 GitHub 上赞助',
    'donation_maybe_later': '✅ 下次再说',
    'donation_support_development': '☕ 支持插件开发',
    'donation_plugin_info': '这个插件是免费开发和维护的！',
    'donation_help_improve': '您的支持帮助更新和改进插件。',
    'donation_every_coffee': '每一杯咖啡都很重要！❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': '坐标系统示例',
    'crs_examples_window_title': '坐标系统格式示例',
    'crs_examples_button': '坐标系统示例',
    'crs_examples_close': '关闭',
    'crs_examples_content': '''🌍 EPSG格式（推荐）：
   EPSG:4326    - WGS84（纬度/经度）
   EPSG:3857    - Web Mercator（Google Maps）
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93（法国）
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New（荷兰）

📝 PROJ4格式：
   +proj=longlat +datum=WGS84 +no_defs
   +proj=utm +zone=37 +datum=WGS84 +units=m +no_defs
   +proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m

🗂️ WKT格式（Well-Known Text）：
   GEOGCS["WGS 84",
     DATUM["WGS_1984",
       SPHEROID["WGS 84",6378137,298.257223563]],
     PRIMEM["Greenwich",0],
     UNIT["degree",0.0174532925199433]]

💡 建议：
   • 使用EPSG代码以简化操作
   • EPSG:4326 - 通用WGS84格式
   • 对于本地项目使用UTM区域
   • 转换前验证CRS的正确性

🔍 有用资源：
   • https://epsg.io/ - EPSG代码搜索
   • https://spatialreference.org/ - CRS数据库
   • QGIS Browser - 内置CRS搜索''',
    
    # Header buttons translations
    'header_support': '支持',
    'header_about_author': '关于作者'
}
