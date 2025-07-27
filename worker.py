# -*- coding: utf-8 -*-
"""
Worker module for MIF/TAB to SHP/GeoJSON Converter Plugin
Модуль обработки для плагина конвертации

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from qgis.PyQt.QtCore import QObject, pyqtSignal
from qgis.core import (QgsVectorLayer, QgsCoordinateReferenceSystem,
                       QgsVectorFileWriter, QgsProject)


class ConversionWorker(QObject):
    """Worker класс для многопоточной обработки файлов"""
    
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    log_message = pyqtSignal(str)
    file_completed = pyqtSignal(str, bool, str)  # filename, success, message

    def __init__(self, files_list, output_dir, crs_text, output_format, max_workers=4):
        super().__init__()
        self.files_list = files_list
        self.output_dir = output_dir
        self.crs_text = crs_text
        self.output_format = output_format
        self.max_workers = max_workers
        self.is_cancelled = False
        
    def cancel(self):
        """Отмена обработки"""
        self.is_cancelled = True
        
    def run(self):
        """Основной метод обработки файлов"""
        try:
            total_files = len(self.files_list)
            completed = 0
            
            self.log_message.emit(f"Starting conversion of {total_files} files...")
            self.log_message.emit(f"Using {self.max_workers} threads")
            self.log_message.emit(f"Output format: {self.output_format}")
            
            # Создание CRS объекта
            crs = QgsCoordinateReferenceSystem()
            if self.crs_text.startswith('EPSG:'):
                epsg_code = int(self.crs_text.split(':')[1])
                crs.createFromId(epsg_code)
            else:
                crs.createFromString(self.crs_text)
            
            if not crs.isValid():
                self.error.emit('Invalid coordinate system')
                return
            
            # Многопоточная обработка
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                future_to_file = {
                    executor.submit(self.convert_single_file, file_path, crs): file_path 
                    for file_path in self.files_list
                }
                
                for future in as_completed(future_to_file):
                    if self.is_cancelled:
                        break
                        
                    file_path = future_to_file[future]
                    try:
                        success, message = future.result()
                        self.file_completed.emit(os.path.basename(file_path), success, message)
                        
                        if success:
                            self.log_message.emit(f"✓ {os.path.basename(file_path)}: {message}")
                        else:
                            self.log_message.emit(f"✗ {os.path.basename(file_path)}: {message}")
                            
                    except Exception as e:
                        self.log_message.emit(f"✗ {os.path.basename(file_path)}: Error - {str(e)}")
                        self.file_completed.emit(os.path.basename(file_path), False, str(e))
                    
                    completed += 1
                    progress_value = int((completed / total_files) * 100)
                    self.progress.emit(progress_value)
            
            if not self.is_cancelled:
                self.log_message.emit(f"Conversion completed. Processed files: {completed}")
            else:
                self.log_message.emit("Conversion cancelled by user")
                
        except Exception as e:
            self.error.emit(f"Critical error: {str(e)}")
        finally:
            self.finished.emit()
    
    def convert_single_file(self, input_file, crs):
        """Конвертация одного файла"""
        try:
            filename = os.path.basename(input_file)
            
            # Определение выходного файла
            if self.output_format == 'GeoJSON':
                if filename.lower().endswith('.mif'):
                    output_file = os.path.join(self.output_dir, filename.replace('.mif', '.geojson'))
                else:
                    output_file = os.path.join(self.output_dir, filename.replace('.tab', '.geojson'))
                driver_name = "GeoJSON"
            else:
                if filename.lower().endswith('.mif'):
                    output_file = os.path.join(self.output_dir, filename.replace('.mif', '.shp'))
                else:
                    output_file = os.path.join(self.output_dir, filename.replace('.tab', '.shp'))
                driver_name = "ESRI Shapefile"
            
            # Загрузка слоя
            layer = QgsVectorLayer(input_file, "temp_layer", "ogr")
            if not layer.isValid():
                return False, f"Failed to load {filename}"
            
            # Установка CRS
            layer.setCrs(crs)
            
            # Настройки записи
            save_options = QgsVectorFileWriter.SaveVectorOptions()
            save_options.driverName = driver_name
            save_options.fileEncoding = "UTF-8"
            
            # Запись файла
            error = QgsVectorFileWriter.writeAsVectorFormatV3(
                layer, output_file, QgsProject.instance().transformContext(), save_options)
            
            if error[0] == QgsVectorFileWriter.NoError:
                return True, f"Successfully converted to {os.path.basename(output_file)}"
            else:
                return False, f"Write error: {error[1]}"
                
        except Exception as e:
            return False, f"Processing error: {str(e)}"
