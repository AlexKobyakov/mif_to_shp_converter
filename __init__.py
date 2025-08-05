# -*- coding: utf-8 -*-
"""
MIF/TAB to SHP/GeoJSON Converter Plugin
Professional multilingual converter with modern UI supporting 9 languages

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Organization: Lesburo
Year: 2025
Version: 3.6.0

Modular Architecture:
- mif_to_shp_converter.py: Main plugin class
- gui.py: GUI components and design
- translations.py: Multi-language support (9 languages)
- worker.py: File processing and multithreading
"""

def classFactory(iface):
    """
    Точка входа для QGIS плагина
    
    Args:
        iface: QGIS interface object
        
    Returns:
        MifToShpConverter: Экземпляр основного класса плагина
    """
    from .mif_to_shp_converter import MifToShpConverter
    return MifToShpConverter(iface)
