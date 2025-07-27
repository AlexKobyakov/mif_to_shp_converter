 starten'}
        }
    
    def get_text(self, key):
        return self.translations.get(self.current_language, {}).get(key, key)
    
    def set_language(self, language):
        if language in self.translations:
            self.current_language = language


# Глобальный объект переводов
translations = Translations()


class ConversionWorker(QObject):
    """Worker класс для многопоточной обработки"""
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    log_message = pyqtSignal(str)
    file_completed = pyqtSignal(str, bool, str)

    def __init__(self, files_list, output_dir, crs_text, output_format, max_workers=4):
        super().__init__()
        self.files_list = files_list
        self.output_dir = output_dir
        self.crs_text = crs_text
        self.output_format = output_format
        self.max_workers = max_workers
        self.is_cancelled = False
        
    def cancel(self):
        self.is_cancelled = True
        
    def run(self):
        try:
            total_files = len(self.files_list)
            completed = 0
            
            self.log_message.emit(f"Starting conversion of {total_files} files...")
            self.log_message.emit(f"Using {self.max_workers} threads")
            
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
        try:
            filename = os.path.basename(input_file)
            
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
            
            layer = QgsVectorLayer(input_file, "temp_layer", "ogr")
            if not layer.isValid():
                return False, f"Failed to load {filename}"
            
            layer.setCrs(crs)
            
            save_options = QgsVectorFileWriter.SaveVectorOptions()
            save_options.driverName = driver_name
            save_options.fileEncoding = "UTF-8"
            
            error = QgsVectorFileWriter.writeAsVectorFormatV3(
                layer, output_file, QgsProject.instance().transformContext(), save_options)
            
            if error[0] == QgsVectorFileWriter.NoError:
                return True, f"Successfully converted to {os.path.basename(output_file)}"
            else:
                return False, f"Write error: {error[1]}"
                
        except Exception as e:
            return False, f"Processing error: {str(e)}"


class MifToShpConverter:
    """Основной класс плагина"""
    
    def __init__(self, iface):
        self.iface = iface
        self.plugin_dir = os.path.dirname(__file__)
        
        # Инициализация переводов
        locale = QSettings().value('locale/userLocale')[0:2]
        if locale in ['en', 'zh', 'hi', 'es', 'ar', 'fr', 'pt', 'de']:
            translations.set_language(locale)
        else:
            translations.set_language('ru')

        self.actions = []
        self.menu = self.tr('&MIF/TAB to SHP/GeoJSON Converter')
        self.first_start = None

    def tr(self, message):
        return QCoreApplication.translate('MifToShpConverter', message)

    def add_action(self, icon_path, text, callback, enabled_flag=True,
                   add_to_menu=True, add_to_toolbar=True, status_tip=None,
                   whats_this=None, parent=None):
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)
        return action

    def initGui(self):
        icon_path = ':/plugins/mif_to_shp_converter/icon.png'
        self.add_action(
            icon_path,
            text=self.tr('Convert MIF/TAB to SHP/GeoJSON'),
            callback=self.run,
            parent=self.iface.mainWindow())

        self.first_start = True

    def unload(self):
        for action in self.actions:
            self.iface.removePluginMenu(self.tr('&MIF/TAB to SHP/GeoJSON Converter'), action)
            self.iface.removeToolBarIcon(action)

    def run(self):
        if self.first_start:
            self.first_start = False
            self.dlg = MifToShpDialog()

        self.dlg.show()
        result = self.dlg.exec_()


class MifToShpDialog(QDialog):
    """Главное диалоговое окно плагина с современным дизайном"""
    
    def __init__(self):
        super().__init__()
        self.worker = None
        self.worker_thread = None
        self.setupUi()
        self.connectSignals()

    def setupUi(self):
        self.setWindowTitle('MIF/TAB to SHP/GeoJSON Converter v2.3.0')
        self.setMinimumSize(900, 700)
        
        # Применение современных стилей
        self.setStyleSheet("""
            QDialog {
                background-color: #f8f9fa;
                font-family: 'Segoe UI', Arial, sans-serif;
            }
            QGroupBox {
                font-weight: bold;
                border: 2px solid #dee2e6;
                border-radius: 8px;
                margin-top: 1ex;
                padding-top: 10px;
                background-color: #ffffff;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 8px 0 8px;
                color: #495057;
            }
            QPushButton {
                background-color: #007bff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 6px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QLineEdit, QTextEdit, QComboBox, QSpinBox {
                border: 2px solid #ced4da;
                border-radius: 6px;
                padding: 8px;
                background-color: #ffffff;
            }
            QLineEdit:focus, QTextEdit:focus, QComboBox:focus, QSpinBox:focus {
                border-color: #007bff;
            }
            QProgressBar {
                border: 2px solid #ced4da;
                border-radius: 8px;
                text-align: center;
                font-weight: bold;
                background-color: #e9ecef;
            }
            QProgressBar::chunk {
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0,
                    stop: 0 #007bff, stop: 1 #28a745);
                border-radius: 6px;
            }
        """)
        
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Заголовок
        title_label = QLabel("🗺️ MIF/TAB to SHP/GeoJSON Converter v2.3.0")
        title_label.setStyleSheet("""
            QLabel {
                color: #495057;
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
                background-color: #ffffff;
                border-radius: 10px;
                border: 2px solid #dee2e6;
            }
        """)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Выбор языка
        lang_layout = QHBoxLayout()
        lang_layout.addWidget(QLabel('🌐 Language:'))
        self.lang_combo = QComboBox()
        self.lang_combo.addItems([
            '🇷🇺 Русский', '🇺🇸 English', '🇨🇳 中文', '🇮🇳 हिंदी', 
            '🇪🇸 Español', '🇸🇦 العربية', '🇫🇷 Français', 
            '🇧🇷 Português', '🇩🇪 Deutsch'
        ])
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()
        
        author_button = QPushButton('👤 About Author')
        author_button.clicked.connect(self.showAuthorInfo)
        lang_layout.addWidget(author_button)
        
        main_layout.addLayout(lang_layout)
        
        # Настройки конвертации
        settings_group = QGroupBox("⚙️ Conversion Settings")
        settings_layout = QVBoxLayout()
        
        # Режим конвертации
        mode_layout = QHBoxLayout()
        self.single_mode = QRadioButton("📄 Single File")
        self.batch_mode = QRadioButton("📁 Batch Processing")
        self.single_mode.setChecked(True)
        mode_layout.addWidget(self.single_mode)
        mode_layout.addWidget(self.batch_mode)
        mode_layout.addStretch()
        settings_layout.addLayout(mode_layout)
        
        # Входные данные
        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel('📥 Input:'))
        self.input_line = QLineEdit()
        self.input_button = QPushButton('Browse...')
        input_layout.addWidget(self.input_line)
        input_layout.addWidget(self.input_button)
        settings_layout.addLayout(input_layout)
        
        # Выходные данные
        output_layout = QHBoxLayout()
        output_layout.addWidget(QLabel('📤 Output:'))
        self.output_line = QLineEdit()
        self.output_button = QPushButton('Browse...')
        output_layout.addWidget(self.output_line)
        output_layout.addWidget(self.output_button)
        settings_layout.addLayout(output_layout)
        
        # Формат вывода
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel('📋 Format:'))
        self.format_combo = QComboBox()
        self.format_combo.addItems(['🗺️ ESRI Shapefile', '🌐 GeoJSON'])
        format_layout.addWidget(self.format_combo)
        format_layout.addStretch()
        settings_layout.addLayout(format_layout)
        
        # Система координат
        crs_layout = QHBoxLayout()
        crs_layout.addWidget(QLabel('🌍 CRS:'))
        self.crs_line = QLineEdit()
        self.crs_line.setText('EPSG:4326')
        crs_layout.addWidget(self.crs_line)
        settings_layout.addLayout(crs_layout)
        
        # Настройки потоков
        thread_layout = QHBoxLayout()
        thread_layout.addWidget(QLabel('⚡ Threads:'))
        self.threads_spinbox = QSpinBox()
        self.threads_spinbox.setMinimum(1)
        self.threads_spinbox.setMaximum(16)
        self.threads_spinbox.setValue(4)
        thread_layout.addWidget(self.threads_spinbox)
        thread_layout.addStretch()
        settings_layout.addLayout(thread_layout)
        
        settings_group.setLayout(settings_layout)
        main_layout.addWidget(settings_group)
        
        # Прогресс
        self.progress_bar = QProgressBar()
        self.progress_bar.setVisible(False)
        main_layout.addWidget(self.progress_bar)
        
        # Логи и результаты
        results_group = QGroupBox("📊 Results & Logs")
        results_layout = QVBoxLayout()
        
        self.results_tabs = QTabWidget()
        
        # Логи
        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        self.log_text.setMaximumHeight(200)
        self.log_text.setStyleSheet("""
            QTextEdit {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-family: 'Consolas', monospace;
            }
        """)
        self.results_tabs.addTab(self.log_text, "📋 Logs")
        
        # Таблица результатов
        self.results_table = QTableWidget()
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(['File', 'Status', 'Message'])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_tabs.addTab(self.results_table, "📈 Results")
        
        results_layout.addWidget(self.results_tabs)
        results_group.setLayout(results_layout)
        main_layout.addWidget(results_group)
        
        # Кнопки управления
        button_layout = QHBoxLayout()
        self.convert_button = QPushButton('🚀 Start Conversion')
        self.convert_button.setStyleSheet("""
            QPushButton {
                background-color: #28a745;
                font-size: 16px;
                padding: 12px 24px;
            }
            QPushButton:hover {
                background-color: #218838;
            }
        """)
        self.cancel_button = QPushButton('❌ Cancel')
        self.clear_button = QPushButton('🧹 Clear')
        
        button_layout.addWidget(self.convert_button)
        button_layout.addWidget(self.cancel_button)
        button_layout.addWidget(self.clear_button)
        button_layout.addStretch()
        
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

    def connectSignals(self):
        self.input_button.clicked.connect(self.selectInput)
        self.output_button.clicked.connect(self.selectOutput)
        self.convert_button.clicked.connect(self.startConversion)
        self.cancel_button.clicked.connect(self.cancelConversion)
        self.clear_button.clicked.connect(self.clearResults)
        self.lang_combo.currentTextChanged.connect(self.changeLanguage)
        self.single_mode.toggled.connect(self.updateMode)

    def showAuthorInfo(self):
        QMessageBox.information(self, '👤 Author Information', 
                              'Author: Кобяков Александр Викторович (Alex Kobyakov)\n'
                              'Email: kobyakov@lesburo.ru\n'
                              'Organization: Lesburo\n'
                              'Year: 2025\n\n'
                              '🌐 Supporting 9 languages worldwide\n'
                              '🚀 Professional GIS data conversion tool')

    def changeLanguage(self, text):
        lang_map = {
            '🇷🇺 Русский': 'ru', '🇺🇸 English': 'en', '🇨🇳 中文': 'zh',
            '🇮🇳 हिंदी': 'hi', '🇪🇸 Español': 'es', '🇸🇦 العربية': 'ar',
            '🇫🇷 Français': 'fr', '🇧🇷 Português': 'pt', '🇩🇪 Deutsch': 'de'
        }
        if text in lang_map:
            translations.set_language(lang_map[text])
            if lang_map[text] == 'ar':
                self.setLayoutDirection(Qt.RightToLeft)
            else:
                self.setLayoutDirection(Qt.LeftToRight)

    def updateMode(self):
        is_single = self.single_mode.isChecked()
        # Здесь можно добавить логику переключения режимов

    def selectInput(self):
        if self.single_mode.isChecked():
            file_path, _ = QFileDialog.getOpenFileName(
                self, 'Select MIF/TAB file', '', 'MIF/TAB files (*.mif *.tab)')
            if file_path:
                self.input_line.setText(file_path)
                if not self.output_line.text():
                    self.output_line.setText(os.path.dirname(file_path))
        else:
            folder = QFileDialog.getExistingDirectory(self, 'Select folder with MIF/TAB files')
            if folder:
                self.input_line.setText(folder)
                if not self.output_line.text():
                    self.output_line.setText(folder)

    def selectOutput(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select output folder')
        if folder:
            self.output_line.setText(folder)

    def startConversion(self):
        input_path = self.input_line.text()
        output_path = self.output_line.text()
        crs_text = self.crs_line.text()
        
        if not input_path or not output_path or not crs_text:
            QMessageBox.warning(self, 'Error', 'Please fill all required fields')
            return
        
        # Сбор файлов для обработки
        files_to_process = []
        if self.single_mode.isChecked():
            if os.path.exists(input_path):
                files_to_process = [input_path]
        else:
            if os.path.exists(input_path):
                mif_files = glob.glob(os.path.join(input_path, '*.mif'))
                tab_files = glob.glob(os.path.join(input_path, '*.tab'))
                files_to_process = mif_files + tab_files
        
        if not files_to_process:
            QMessageBox.warning(self, 'Error', 'No supported files found')
            return
        
        # Создание выходной папки
        os.makedirs(output_path, exist_ok=True)
        
        # Определение формата вывода
        output_format = 'GeoJSON' if 'GeoJSON' in self.format_combo.currentText() else 'ESRI Shapefile'
        
        # Настройка UI
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.convert_button.setEnabled(False)
        self.convert_button.setText('⏳ Converting...')
        
        # Очистка результатов
        self.results_table.setRowCount(0)
        self.log_message("🚀 Starting conversion...")
        
        # Создание и запуск worker
        max_workers = self.threads_spinbox.value()
        self.worker = ConversionWorker(files_to_process, output_path, crs_text, output_format, max_workers)
        self.worker_thread = QThread()
        self.worker.moveToThread(self.worker_thread)
        
        # Подключение сигналов
        self.worker_thread.started.connect(self.worker.run)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.log_message.connect(self.log_message)
        self.worker.file_completed.connect(self.onFileCompleted)
        self.worker.finished.connect(self.onConversionFinished)
        self.worker.error.connect(self.onConversionError)
        
        # Запуск
        self.worker_thread.start()

    def cancelConversion(self):
        if self.worker:
            self.worker.cancel()
            self.log_message("⚠️ Cancelling conversion...")

    def clearResults(self):
        self.log_text.clear()
        self.results_table.setRowCount(0)
        self.log_message("🧹 Results cleared")

    def onFileCompleted(self, filename, success, message):
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        
        self.results_table.setItem(row, 0, QTableWidgetItem(filename))
        status_text = "✅ Success" if success else "❌ Error"
        status_item = QTableWidgetItem(status_text)
        if success:
            status_item.setBackground(QColor('#d4edda'))
        else:
            status_item.setBackground(QColor('#f8d7da'))
        self.results_table.setItem(row, 1, status_item)
        self.results_table.setItem(row, 2, QTableWidgetItem(message))

    def onConversionFinished(self):
        self.progress_bar.setValue(100)
        self.convert_button.setEnabled(True)
        self.convert_button.setText('🚀 Start Conversion')
        self.log_message("🎉 Conversion completed!")
        
        # Подсчет статистики
        total_files = self.results_table.rowCount()
        success_count = 0
        for row in range(total_files):
            status_item = self.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                success_count += 1
        
        self.log_message(f"📊 Statistics: {success_count}/{total_files} files converted successfully")
        
        # Уведомление
        if success_count == total_files:
            QMessageBox.information(self, '🎉 Success', f'All {total_files} files converted successfully!')
        elif success_count > 0:
            QMessageBox.warning(self, '⚠️ Partial Success', 
                              f'{success_count} of {total_files} files converted successfully.')
        else:
            QMessageBox.critical(self, '❌ Error', 'No files were converted successfully.')
        
        # Очистка worker
        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.worker = None

    def onConversionError(self, error_message):
        self.log_message(f"🔥 CRITICAL ERROR: {error_message}")
        QMessageBox.critical(self, 'Critical Error', error_message)
        self.onConversionFinished()

    def log_message(self, message):
        timestamp = datetime.now().strftime('%H:%M:%S')
        formatted_message = f'<span style="color: #95a5a6;">[{timestamp}]</span> {message}'
        self.log_text.append(formatted_message)
        
        # Автопрокрутка
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)

    def closeEvent(self, event):
        if self.worker and self.worker_thread and self.worker_thread.isRunning():
            reply = QMessageBox.question(self, 'Confirmation', 
                                       'Conversion in progress. Stop and close?',
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.cancelConversion()
                if self.worker_thread:
                    self.worker_thread.quit()
                    self.worker_thread.wait()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
