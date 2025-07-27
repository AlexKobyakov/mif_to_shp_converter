# -*- coding: utf-8 -*-
"""
🌟 MIF/TAB to SHP/GeoJSON Converter Plugin
Professional multilingual converter with modern UI
Supporting 9 world languages

👨‍💻 Author: Кобяков Александр Викторович (Alex Kobyakov)
📧 Email: kobyakov@lesburo.ru
🏢 Organization: Lesburo
📅 Year: 2025
"""

def classFactory(iface):
    from .mif_to_shp_converter import MifToShpConverter
    return MifToShpConverter(iface)
