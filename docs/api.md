# 🔧 API Documentation - MIF/TAB to SHP/GeoJSON Converter Plugin v3.6

## 📋 Table of Contents
- [Overview](#overview)
- [Core API](#core-api)
- [GUI API](#gui-api)
- [Worker API](#worker-api)
- [Translation API](#translation-api)
- [Event System](#event-system)
- [Extension Points](#extension-points)
- [Code Examples](#code-examples)
- [Integration Guide](#integration-guide)

---

## 📊 Overview

The MIF/TAB to SHP/GeoJSON Converter Plugin v3.6 provides a comprehensive API for programmatic access to conversion functionality, GUI components, and extension capabilities. The API is designed for:

- **🔌 Plugin Integration**: Integrate conversion capabilities into other QGIS plugins
- **🤖 Automation**: Batch processing and scripted conversions
- **🎨 GUI Customization**: Custom interfaces and workflows
- **🔧 Extension Development**: Adding new formats and processing options

### 🎯 API Design Principles

- **🏗️ Modular Architecture**: Clear separation between core logic and GUI
- **📡 Signal-based Communication**: Qt signals for decoupled component interaction
- **🛡️ Error Handling**: Comprehensive exception handling and validation
- **🌍 Internationalization**: Full i18n support for custom interfaces
- **⚡ Performance**: Multi-threaded processing with progress tracking

---

## 🏛️ Core API

### 📦 Main Plugin Class

```python
class MifToShpConverter:
    """Main plugin class providing QGIS integration and core functionality"""
    
    def __init__(self, iface):
        """Initialize plugin with QGIS interface"""
        
    def initGui(self) -> None:
        """Initialize plugin GUI elements"""
        
    def unload(self) -> None:
        """Clean plugin unload"""
        
    def run(self) -> None:
        """Execute plugin main functionality"""
        
    @staticmethod
    def get_plugin_version() -> str:
        """Get plugin version from metadata.txt"""
        
    @staticmethod  
    def get_plugin_info() -> Dict[str, str]:
        """Get complete plugin information from metadata"""
```

---

## ⚡ Worker API

### 🔄 ConversionWorker Class

```python
class ConversionWorker(QObject):
    """Multi-threaded file conversion worker with progress tracking"""
    
    # Signals
    progress = pyqtSignal(int)                    # Progress percentage (0-100)
    finished = pyqtSignal()                       # Processing completed
    error = pyqtSignal(str)                       # Critical error occurred
    log_message = pyqtSignal(str)                 # Log message for display
    file_completed = pyqtSignal(str, bool, str)   # File, success, message
    
    def __init__(self, files_list: List[str], output_dir: str, 
                 crs_text: str, output_format: str, max_workers: int = 4):
        """Initialize conversion worker"""
        
    def run(self) -> None:
        """Main processing method (called by QThread)"""
        
    def convert_single_file(self, input_file: str, crs) -> Tuple[bool, str]:
        """Convert individual file"""
        
    def cancel(self) -> None:
        """Request graceful cancellation"""
```

#### 🔧 Usage Example

```python
# Create and configure worker
files = ['file1.mif', 'file2.tab']
worker = ConversionWorker(
    files_list=files,
    output_dir='/path/to/output',
    crs_text='EPSG:4326',
    output_format='Shapefile',
    max_workers=8
)

# Connect signals
worker.progress.connect(lambda p: print(f"Progress: {p}%"))
worker.file_completed.connect(lambda f, s, m: print(f"{f}: {s} - {m}"))
worker.finished.connect(lambda: print("Processing complete"))

# Run in thread
thread = QThread()
worker.moveToThread(thread)
thread.started.connect(worker.run)
thread.start()
```

---

## 🌍 Translation API

### 🗣️ TranslationManager Class

```python
class TranslationManager:
    """Dynamic translation system with modular language support"""
    
    def set_language(self, language_code: str) -> bool:
        """Set active interface language"""
        
    def get_text(self, key: str, language: str = None) -> str:
        """Get translated text with fallback support"""
        
    def get_supported_languages(self) -> List[str]:
        """Get list of supported language codes"""
        
    def reload_language(self, language_code: str) -> bool:
        """Hot-reload language translations"""
```

#### 🌐 Global Translation Instance

```python
# Global translation manager instance
from translation_manager import translations

# Usage examples
current_lang = translations.get_current_language()      # Get active language
available = translations.get_supported_languages()      # List available languages
title = translations.get_text('window_title')           # Get translated text
success = translations.set_language('de')               # Switch to German
```

### 📝 Common Translation Keys

```python
TRANSLATION_KEYS = {
    # Window and main interface
    'window_title': 'Main window title',
    'conversion_mode': 'Conversion mode label',
    'single_file': 'Single file mode',
    'batch_processing': 'Batch processing mode',
    
    # File operations
    'input_file': 'Input file label',
    'output_folder': 'Output folder label',
    'browse': 'Browse button text',
    
    # Actions and controls
    'start_conversion': 'Start conversion button',
    'cancel': 'Cancel button',
    'clear_logs': 'Clear logs button',
    
    # Results and feedback
    'progress': 'Progress label',
    'logs': 'Logs tab title',
    'results': 'Results tab title',
}
```

---

## 📡 Event System

### 🎛️ GuiEventHandlers Class

```python
class GuiEventHandlers:
    """Centralized event handling system for GUI components"""
    
    def __init__(self, dialog: MifToShpDialog):
        """Initialize event handlers"""
        
    def onLanguageChanged(self, index: int) -> None:
        """Handle language selection change"""
        
    def onModeChanged(self, batch_mode: bool) -> None:
        """Handle conversion mode toggle"""
        
    def selectInputFile(self) -> None:
        """Handle input file selection"""
        
    def selectOutputFolder(self) -> None:
        """Handle output folder selection"""
        
    def startConversion(self) -> None:
        """Handle conversion start request"""
        
    def cancelConversion(self) -> None:
        """Handle conversion cancellation"""
```

---

## 🔌 Extension Points

### 🎯 Format Extension API

```python
class FormatHandler(ABC):
    """Abstract base class for format handlers"""
    
    @abstractmethod
    def can_handle(self, file_path: str) -> bool:
        """Check if handler can process file"""
        
    @abstractmethod
    def get_file_info(self, file_path: str) -> Dict[str, Any]:
        """Get file metadata and information"""
        
    @abstractmethod
    def convert_file(self, input_path: str, output_path: str, 
                    options: Dict[str, Any]) -> Tuple[bool, str]:
        """Convert file to target format"""

# Example implementation
class DXFHandler(FormatHandler):
    """Handler for AutoCAD DXF files"""
    
    def can_handle(self, file_path: str) -> bool:
        return file_path.lower().endswith('.dxf')
```

---

## 💡 Code Examples

### 🤖 Programmatic Conversion

```python
from mif_to_shp_converter.worker import ConversionWorker
from PyQt5.QtCore import QThread

def convert_files_programmatically():
    """Example: Convert files without GUI"""
    
    # File list to convert
    files_to_convert = [
        '/path/to/file1.mif',
        '/path/to/file2.tab',
        '/path/to/file3.mif'
    ]
    
    # Create worker
    worker = ConversionWorker(
        files_list=files_to_convert,
        output_dir='/path/to/output',
        crs_text='EPSG:4326',
        output_format='GeoJSON',
        max_workers=4
    )
    
    # Create thread
    thread = QThread()
    worker.moveToThread(thread)
    
    # Connect signals
    def on_progress(percentage):
        print(f"Progress: {percentage}%")
    
    def on_file_completed(filename, success, message):
        status = "✅" if success else "❌"
        print(f"{status} {filename}: {message}")
    
    def on_finished():
        print("🎉 Conversion completed!")
        thread.quit()
        thread.wait()
    
    # Connect signals
    worker.progress.connect(on_progress)
    worker.file_completed.connect(on_file_completed)
    worker.finished.connect(on_finished)
    
    # Start processing
    thread.started.connect(worker.run)
    thread.start()
    
    return worker, thread
```

### 🎨 Custom GUI Integration

```python
from qgis.PyQt.QtWidgets import QDialog, QVBoxLayout, QPushButton
from mif_to_shp_converter.gui import MifToShpDialog

class CustomConverterDialog(QDialog):
    """Example: Custom dialog integrating converter functionality"""
    
    def __init__(self):
        super().__init__()
        self.setupUi()
        
    def setupUi(self):
        layout = QVBoxLayout(self)
        
        # Custom controls
        self.quick_convert_btn = QPushButton("Quick Convert")
        self.batch_convert_btn = QPushButton("Batch Convert")
        self.settings_btn = QPushButton("Settings")
        
        layout.addWidget(self.quick_convert_btn)
        layout.addWidget(self.batch_convert_btn)
        layout.addWidget(self.settings_btn)
        
        # Connect signals
        self.quick_convert_btn.clicked.connect(self.quick_convert)
        self.batch_convert_btn.clicked.connect(self.batch_convert)
        self.settings_btn.clicked.connect(self.show_settings)
    
    def quick_convert(self):
        """Quick conversion with default settings"""
        dialog = MifToShpDialog()
        dialog.mode_widget.single_mode.setChecked(True)
        dialog.exec_()
```

### 🌍 Translation Integration

```python
from mif_to_shp_converter.translation_manager import translations

def create_multilingual_message():
    """Example: Create message box with current language"""
    
    # Get translated text
    title = translations.get_text('window_title')
    message = translations.get_text('conversion_completed')
    
    # Use in message box or other UI elements
    print(f"Title: {title}")
    print(f"Message: {message}")

def switch_language_example():
    """Example: Dynamic language switching"""
    
    # Available languages
    languages = translations.get_supported_languages()
    print(f"Available languages: {languages}")
    
    # Switch to different languages
    for lang in ['en', 'ru', 'zh', 'ar']:
        if translations.set_language(lang):
            title = translations.get_text('window_title')
            print(f"{lang}: {title}")
```

---

## 🔗 Integration Guide

### 📦 Plugin Dependencies

To integrate the converter into your plugin:

```python
# In your plugin's __init__.py or main module
try:
    from mif_to_shp_converter.worker import ConversionWorker
    from mif_to_shp_converter.translation_manager import translations
    CONVERTER_AVAILABLE = True
except ImportError:
    CONVERTER_AVAILABLE = False
    print("MIF/TAB Converter plugin not available")

class YourPlugin:
    def __init__(self, iface):
        self.iface = iface
        self.converter_available = CONVERTER_AVAILABLE
    
    def convert_files(self, files):
        if not self.converter_available:
            self.iface.messageBar().pushMessage(
                "Error", "MIF/TAB Converter plugin required",
                level=Qgis.Critical
            )
            return
        
        # Use converter functionality
        worker = ConversionWorker(
            files_list=files,
            output_dir='/output/path',
            crs_text='EPSG:4326',
            output_format='Shapefile'
        )
```

---

## 📊 API Reference Summary

### 🎯 Core Classes

| Class | Purpose | Key Methods |
|-------|---------|-------------|
| `MifToShpConverter` | Main plugin class | `initGui()`, `run()`, `unload()` |
| `ConversionWorker` | File processing | `run()`, `convert_single_file()`, `cancel()` |
| `MifToShpDialog` | Main GUI dialog | `updateLanguage()`, `log_message()` |
| `TranslationManager` | I18n support | `set_language()`, `get_text()` |
| `GuiEventHandlers` | Event handling | `startConversion()`, `onLanguageChanged()` |

### 🔧 Key Signals

| Signal | Source | Parameters | Purpose |
|--------|---------|------------|---------|
| `progress` | ConversionWorker | `int` (0-100) | Progress updates |
| `file_completed` | ConversionWorker | `str, bool, str` | File completion |
| `finished` | ConversionWorker | None | Processing done |
| `error` | ConversionWorker | `str` | Error occurred |

### 🌍 Translation Categories

| Category | Example Keys | Purpose |
|----------|--------------|---------|
| Interface | `window_title`, `conversion_mode` | Main UI elements |
| Actions | `start_conversion`, `cancel`, `browse` | Button labels |
| Messages | `conversion_started`, `error_occurred` | Status messages |
| Options | `thread_count`, `coordinate_system` | Settings labels |

---

## 📞 API Support

### 🆘 Getting Help

For API-related questions and support:

- **📧 Email**: [kobyakov@lesburo.ru](mailto:kobyakov@lesburo.ru)
- **💬 Telegram**: [@AKobyakov](https://t.me/AKobyakov)
- **🐙 GitHub Issues**: [API Questions](https://github.com/AlexKobyakov/mif_to_shp_converter/issues)
- **📚 Documentation**: [GitHub Wiki](https://github.com/AlexKobyakov/mif_to_shp_converter/wiki)

### 📋 Contributing to API

To contribute API improvements:

1. **Fork Repository**: Create your own fork on GitHub
2. **Create Feature Branch**: `git checkout -b feature/api-improvement`
3. **Implement Changes**: Add new API methods or improve existing ones
4. **Add Tests**: Include unit tests for new functionality
5. **Update Documentation**: Update this API documentation
6. **Submit Pull Request**: Create PR with detailed description

### 🔧 API Versioning

The API follows semantic versioning:

- **Major**: Breaking changes to existing API
- **Minor**: New features, backward compatible
- **Patch**: Bug fixes, no API changes

Current API version: **3.6.0**

---

<div align="center">

**🔧 MIF/TAB to SHP/GeoJSON Converter Plugin API v3.6.0**

*Comprehensive API for professional MapInfo file conversion*

[📖 User Manual](user-manual.md) | [🏗️ Architecture](architecture.md) | [📥 Installation](installation.md) | [🌍 Development](development.md)

**Made with ❤️ for the QGIS Developer Community**

</div>
