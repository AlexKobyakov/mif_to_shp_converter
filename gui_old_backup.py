output_format')}")
        
        self.input_file_button.setText(f"📂 {translations.get_text('browse')}")
        self.input_folder_button.setText(f"📂 {translations.get_text('browse')}")
        self.output_folder_button.setText(f"📂 {translations.get_text('browse')}")
        
        self.threading_group.setTitle(f"⚡ {translations.get_text('threading_settings')}")
        self.thread_count_label.setText(f"🧵 {translations.get_text('thread_count')}")
        
        self.crs_group.setTitle(f"🌍 {translations.get_text('coordinate_system')}")
        self.crs_hint_label.setText(f"📝 {translations.get_text('crs_format_hint')}")
        self.add_to_project_cb.setText(f"✅ {translations.get_text('add_to_project')}")
        
        self.progress_label.setText(f"📊 {translations.get_text('progress')}")
        
        # Обновление табов
        self.tab_widget.setTabText(0, f"📋 {translations.get_text('logs')}")
        self.tab_widget.setTabText(1, f"📈 {translations.get_text('results')}")
        
        # Обновление заголовков таблицы
        self.results_table.setHorizontalHeaderLabels([
            f"📄 {translations.get_text('file')}",
            f"📊 {translations.get_text('status')}",
            f"💬 {translations.get_text('message')}"
        ])
        
        # Обновление кнопок
        if 'Converting' in self.convert_button.text() or 'Конвертация' in self.convert_button.text():
            self.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        else:
            self.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
            
        self.cancel_button.setText(f"❌ {translations.get_text('cancel')}")
        self.clear_log_button.setText(f"🧹 {translations.get_text('clear_logs')}")

    def showAuthorInfo(self):
        """Показать информацию об авторе"""
        author_dialog = QMessageBox()
        author_dialog.setWindowTitle('👤 Author Information')
        author_dialog.setTextFormat(Qt.RichText)
        author_dialog.setText(f"""
        <div style="text-align: center; padding: 20px;">
            <h2 style="color: #3498db;">🎯 MIF/TAB to SHP/GeoJSON Converter</h2>
            <hr style="border: 1px solid #bdc3c7;">
            <p><b>👨‍💻 Author:</b> Кобяков Александр Викторович<br>
            <i>(Alex Kobyakov)</i></p>
            <p><b>📧 Email:</b> <a href="mailto:kobyakov@lesburo.ru">kobyakov@lesburo.ru</a></p>
            <p><b>📅 Year:</b> 2025</p>
            <p><b>🏢 Organization:</b> Lesburo</p>
            <hr style="border: 1px solid #bdc3c7;">
            <p style="color: #7f8c8d; font-style: italic;">
            Professional GIS data conversion tool<br>
            Supporting multiple languages and formats
            </p>
        </div>
        """)
        author_dialog.setStandardButtons(QMessageBox.Ok)
        author_dialog.exec_()

    def onModeChanged(self):
        """Обработка смены режима конвертации"""
        is_batch = self.batch_mode.isChecked()
        self.single_widget.setVisible(not is_batch)
        self.batch_widget.setVisible(is_batch)

    def selectInputFile(self):
        """Выбор входного файла"""
        filename, _ = QFileDialog.getOpenFileName(
            self, translations.get_text('select_input_file'), '', 
            translations.get_text('supported_formats'))
        if filename:
            self.input_file_line.setText(filename)
            if not self.output_folder_line.text():
                self.output_folder_line.setText(os.path.dirname(filename))

    def selectInputFolder(self):
        """Выбор входной папки"""
        folder = QFileDialog.getExistingDirectory(self, translations.get_text('select_input_folder'))
        if folder:
            self.input_folder_line.setText(folder)
            if not self.output_folder_line.text():
                self.output_folder_line.setText(folder)

    def selectOutputFolder(self):
        """Выбор выходной папки"""
        folder = QFileDialog.getExistingDirectory(self, translations.get_text('select_output_folder'))
        if folder:
            self.output_folder_line.setText(folder)

    def startConversion(self):
        """Запуск процесса конвертации"""
        # Сбор файлов для обработки
        files_to_process = []
        
        if self.single_mode.isChecked():
            input_file = self.input_file_line.text()
            if not input_file or not os.path.exists(input_file):
                QMessageBox.warning(self, 'Error', translations.get_text('error_no_input_file'))
                return
            files_to_process = [input_file]
        else:
            input_folder = self.input_folder_line.text()
            if not input_folder or not os.path.exists(input_folder):
                QMessageBox.warning(self, 'Error', translations.get_text('error_no_input_folder'))
                return
            
            # Поиск всех поддерживаемых файлов в папке (MIF и TAB)
            mif_pattern = os.path.join(input_folder, '*.mif')
            tab_pattern = os.path.join(input_folder, '*.tab')
            files_to_process = glob.glob(mif_pattern) + glob.glob(tab_pattern)
            
            if not files_to_process:
                QMessageBox.warning(self, 'Error', translations.get_text('error_no_files_found'))
                return
        
        output_folder = self.output_folder_line.text()
        if not output_folder:
            QMessageBox.warning(self, 'Error', translations.get_text('error_no_output_folder'))
            return
        
        # Создание выходной папки если не существует
        os.makedirs(output_folder, exist_ok=True)
        
        crs_text = self.crs_text.toPlainText().strip()
        if not crs_text:
            QMessageBox.warning(self, 'Error', translations.get_text('error_no_crs'))
            return
        
        # Получение выходного формата
        output_format = 'GeoJSON' if 'GeoJSON' in self.output_format_combo.currentText() else 'ESRI Shapefile'
        
        # Очистка результатов
        self.results_table.setRowCount(0)
        self.log_message(f"🚀 === {translations.get_text('start_conversion')} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        
        # Настройка UI для процесса конвертации
        self.progress_bar.setVisible(True)
        self.progress_bar.setValue(0)
        self.convert_button.setEnabled(False)
        self.convert_button.setText(f"⏳ {translations.get_text('converting')}")
        
        # Создание и запуск воркера
        max_workers = self.threads_spinbox.value()
        self.worker = ConversionWorker(files_to_process, output_folder, crs_text, output_format, max_workers)
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
        """Отмена конвертации"""
        if self.worker:
            self.worker.cancel()
            self.log_message(f"⚠️ {translations.get_text('conversion_cancelled')}")

    def clearLogs(self):
        """Очистка логов и результатов"""
        self.log_text.clear()
        self.results_table.setRowCount(0)
        self.log_message("🧹 Logs and results cleared")

    def onFileCompleted(self, filename, success, message):
        """Обработка завершения файла"""
        # Добавление результата в таблицу
        row = self.results_table.rowCount()
        self.results_table.insertRow(row)
        
        # Файл
        file_item = QTableWidgetItem(filename)
        file_item.setToolTip(filename)
        self.results_table.setItem(row, 0, file_item)
        
        # Статус с иконками
        status_text = f"✅ {translations.get_text('success')}" if success else f"❌ {translations.get_text('error')}"
        status_item = QTableWidgetItem(status_text)
        
        if success:
            status_item.setBackground(QColor('#d5f4e6'))  # Светло-зеленый
            status_item.setForeground(QColor('#27ae60'))  # Темно-зеленый текст
        else:
            status_item.setBackground(QColor('#fadbd8'))  # Светло-красный
            status_item.setForeground(QColor('#e74c3c'))  # Темно-красный текст
            
        self.results_table.setItem(row, 1, status_item)
        
        # Сообщение
        message_item = QTableWidgetItem(message)
        message_item.setToolTip(message)
        self.results_table.setItem(row, 2, message_item)
        
        # Автоматическая прокрутка к последней строке
        self.results_table.scrollToBottom()

    def onConversionFinished(self):
        """Обработка завершения конвертации"""
        self.progress_bar.setValue(100)
        self.convert_button.setEnabled(True)
        self.convert_button.setText(f"🚀 {translations.get_text('start_conversion')}")
        self.log_message(f"🎉 === Conversion completed {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===")
        
        # Статистика
        total_files = self.results_table.rowCount()
        success_count = 0
        error_count = 0
        
        for row in range(total_files):
            status_item = self.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                success_count += 1
            else:
                error_count += 1
        
        self.log_message(f"📊 Statistics: {success_count} successful, {error_count} errors out of {total_files} files")
        
        # Добавление результата в проект если нужно
        if self.add_to_project_cb.isChecked() and success_count > 0:
            self.addResultsToProject()
        
        # Очистка воркера
        if self.worker_thread:
            self.worker_thread.quit()
            self.worker_thread.wait()
            self.worker_thread = None
            self.worker = None
        
        # Уведомление о завершении
        if success_count == total_files:
            QMessageBox.information(self, '🎉 Success', 
                                  f'All {total_files} files converted successfully!')
        elif success_count > 0:
            QMessageBox.warning(self, '⚠️ Partial Success', 
                              f'{success_count} files converted successfully, {error_count} failed.')
        else:
            QMessageBox.critical(self, '❌ Error', 
                               'No files were converted successfully.')

    def onConversionError(self, error_message):
        """Обработка критической ошибки"""
        self.log_message(f"🔥 CRITICAL ERROR: {error_message}")
        QMessageBox.critical(self, translations.get_text('critical_error'), error_message)
        self.onConversionFinished()

    def addResultsToProject(self):
        """Добавление успешно конвертированных файлов в проект"""
        output_folder = self.output_folder_line.text()
        crs_text = self.crs_text.toPlainText().strip()
        output_format = 'GeoJSON' if 'GeoJSON' in self.output_format_combo.currentText() else 'ESRI Shapefile'
        
        # Создание CRS объекта
        crs = QgsCoordinateReferenceSystem()
        if crs_text.startswith('EPSG:'):
            epsg_code = int(crs_text.split(':')[1])
            crs.createFromId(epsg_code)
        else:
            crs.createFromString(crs_text)
        
        added_count = 0
        for row in range(self.results_table.rowCount()):
            status_item = self.results_table.item(row, 1)
            if status_item and '✅' in status_item.text():
                filename = self.results_table.item(row, 0).text()
                
                if output_format == 'GeoJSON':
                    # Для GeoJSON файлов
                    if filename.lower().endswith('.mif'):
                        output_file = os.path.join(output_folder, filename.replace('.mif', '.geojson'))
                        layer_name = filename.replace('.mif', '')
                    else:  # .tab
                        output_file = os.path.join(output_folder, filename.replace('.tab', '.geojson'))
                        layer_name = filename.replace('.tab', '')
                else:
                    # Для Shapefile
                    if filename.lower().endswith('.mif'):
                        output_file = os.path.join(output_folder, filename.replace('.mif', '.shp'))
                        layer_name = filename.replace('.mif', '')
                    else:  # .tab
                        output_file = os.path.join(output_folder, filename.replace('.tab', '.shp'))
                        layer_name = filename.replace('.tab', '')
                
                if os.path.exists(output_file):
                    layer = QgsVectorLayer(output_file, layer_name, "ogr")
                    if layer.isValid():
                        layer.setCrs(crs)
                        QgsProject.instance().addMapLayer(layer)
                        added_count += 1
        
        if added_count > 0:
            self.log_message(f"📁 Added to project: {added_count} layers")

    def log_message(self, message):
        """Добавление сообщения в лог с цветовой раскраской"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        
        # Определение цвета на основе типа сообщения
        if message.startswith('🚀') or message.startswith('🎉'):
            color = '#2ecc71'  # Зеленый для успеха
        elif message.startswith('⚠️'):
            color = '#f39c12'  # Оранжевый для предупреждений
        elif message.startswith('🔥') or message.startswith('❌'):
            color = '#e74c3c'  # Красный для ошибок
        elif message.startswith('✅'):
            color = '#27ae60'  # Темно-зеленый для успешных файлов
        elif message.startswith('✗'):
            color = '#c0392b'  # Темно-красный для ошибок файлов
        elif message.startswith('📊') or message.startswith('📁'):
            color = '#3498db'  # Синий для информации
        else:
            color = '#ecf0f1'  # Белый для обычных сообщений
        
        formatted_message = f'<span style="color: #95a5a6;">[{timestamp}]</span> <span style="color: {color};">{message}</span>'
        self.log_text.append(formatted_message)
        
        # Автопрокрутка к концу
        cursor = self.log_text.textCursor()
        cursor.movePosition(cursor.End)
        self.log_text.setTextCursor(cursor)

    def closeEvent(self, event):
        """Обработка закрытия окна"""
        if self.worker and self.worker_thread and self.worker_thread.isRunning():
            reply = QMessageBox.question(
                self, 
                translations.get_text('confirmation'), 
                translations.get_text('confirm_close'),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
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
