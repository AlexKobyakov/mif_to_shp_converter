# -*- coding: utf-8 -*-
"""
Portuguese translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': 'Conversor MIF/TAB para SHP/GeoJSON - Conversor em Lote',
    'conversion_mode': 'Modo de Conversão',
    'single_file': 'Arquivo Único',
    'batch_processing': 'Processamento em Lote (Pasta)',
    'input_file': 'Arquivo de Entrada:',
    'input_folder': 'Pasta de Entrada:',
    'output_folder': 'Pasta de Saída:',
    'output_format': 'Formato de Saída:',
    'browse': 'Navegar...',
    'threading_settings': 'Configurações de Threading',
    'thread_count': 'Contagem de Threads:',
    'coordinate_system': 'Sistema de Coordenadas',
    'crs_format_hint': 'Formato: EPSG:código, PROJ4 ou WKT',
    'add_to_project': 'Adicionar resultado ao projeto QGIS',
    'progress': 'Progresso:',
    'logs': 'Logs',
    'results': 'Resultados',
    'start_conversion': 'Iniciar Conversão',
    'cancel': 'Cancelar',
    'clear_logs': 'Limpar Logs',
    'converting': 'Convertendo...',
    'language': 'Idioma:',
    'file': 'Arquivo',
    'status': 'Status',
    'message': 'Mensagem',
    'success': 'Sucesso',
    'error': 'Erro',
    'select_input_file': 'Selecionar arquivo de entrada',
    'select_input_folder': 'Selecionar pasta de entrada',
    'select_output_folder': 'Selecionar pasta de saída',
    'error_no_input_file': 'Selecionar um arquivo de entrada válido',
    'error_no_input_folder': 'Selecionar uma pasta válida',
    'error_no_files_found': 'Nenhum arquivo suportado encontrado na pasta selecionada',
    'error_no_output_folder': 'Especificar pasta de saída',
    'error_no_crs': 'Especificar sistema de coordenadas',
    'conversion_cancelled': 'Cancelando conversão...',
    'confirm_close': 'Conversão em andamento. Parar e fechar?',
    'confirmation': 'Confirmação',
    'critical_error': 'Erro Crítico',
    'supported_formats': 'Arquivos MIF/TAB (*.mif *.tab)',
    'author_info': 'Autor: Кобяков Александр Викторович (Alex Kobyakov)\nEmail: kobyakov@lesburo.ru\nAno: 2025',
    'about_author': 'Sobre o Autor',
    'settings': 'Configurações',
    'input_output': 'Entrada e Saída',
    'processing_options': 'Opções de Processamento',
    
    # Donation dialog translations
    'donation_title': '☕ Apoiar o Desenvolvimento',
    'donation_window_title': '☕ Apoiar o Desenvolvimento do Plugin',
    'donation_description': '''<div style="text-align: center; line-height: 1.6;">
            <p><b>🎯 Conversor MIF/TAB para SHP/GeoJSON</b></p>
            <p>este plugin é desenvolvido e mantido <b>gratuitamente</b>!</p>
            <p>Seu apoio ajuda a atualizar e melhorar o plugin.</p>
            <p style="color: #7f8c8d; font-size: 13px;">Cada café conta! ❤️</p>
        </div>''',
    'donation_kofi': '☕ Comprar Café no Ko-fi',
    'donation_tbank': '💳 Doar via T-Bank',
    'donation_github': '💖 Patrocinar no GitHub',
    'donation_maybe_later': '✅ Talvez Mais Tarde',
    'donation_support_development': '☕ Apoiar o Desenvolvimento do Plugin',
    'donation_plugin_info': 'este plugin é desenvolvido e mantido gratuitamente!',
    'donation_help_improve': 'Seu apoio ajuda a atualizar e melhorar o plugin.',
    'donation_every_coffee': 'Cada café conta! ❤️',
    
    # CRS Examples dialog translations
    'crs_examples_title': 'Exemplos de Sistemas de Coordenadas',
    'crs_examples_window_title': 'Exemplos de Formatos de Sistemas de Coordenadas',
    'crs_examples_button': 'Exemplos de Sistemas de Coordenadas',
    'crs_examples_close': 'Fechar',
    'crs_examples_content': '''🌍 FORMATO EPSG (recomendado):
   EPSG:4326    - WGS84 (latitude/longitude)
   EPSG:3857    - Web Mercator (Google Maps)
   EPSG:32637   - UTM Zone 37N
   EPSG:2154    - RGF93 / Lambert-93 (França)
   EPSG:3395    - World Mercator
   EPSG:4269    - NAD83
   EPSG:28992   - Amersfoort / RD New (Holanda)

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

💡 RECOMENDAÇÕES:
   • Use códigos EPSG para simplicidade
   • EPSG:4326 - formato universal WGS84
   • Para projetos locais use zonas UTM
   • Verifique a correção do CRS antes da conversão

🔍 RECURSOS ÚTEIS:
   • https://epsg.io/ - busca de códigos EPSG
   • https://spatialreference.org/ - banco de dados CRS
   • QGIS Browser - busca integrada de CRS''',
    
    # Header buttons translations
    'header_support': 'Suporte',
    'header_about_author': 'Sobre o Autor'
}
