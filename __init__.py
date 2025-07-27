# -*- coding: utf-8 -*-
"""
MIF/TAB to SHP/GeoJSON Converter Plugin
"""

def classFactory(iface):
    from .mif_to_shp_converter import MifToShpConverter
    return MifToShpConverter(iface)