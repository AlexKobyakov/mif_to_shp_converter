# 🌍 Development Guide - MIF/TAB to SHP/GeoJSON Converter Plugin v3.6

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Development Setup](#development-setup)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [Testing](#testing)
- [Building](#building)
- [Best Practices](#best-practices)

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- QGIS 3.0+
- Qt/PyQt knowledge
- Git

### Setup
```bash
# Clone and setup
git clone https://github.com/AlexKobyakov/mif_to_shp_converter.git
cd mif_to_shp_converter
git checkout -b feature/your-feature

# Link to QGIS (Windows)
mklink /D "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\mif_dev" "."

# Install dev tools
pip install black isort flake8 pytest pytest-qt
```

---

## 💻 Development Setup

### IDE Configuration (VS Code)
```json
{
    "python.defaultInterpreterPath": "/path/to/qgis/python",
    "python.analysis.extraPaths": ["/path/to/QGIS/python/"]
}
```

### Debug Mode
```python
# Enable debugging
import logging
logging.basicConfig(level=logging.DEBUG)

# QGIS message log
from qgis.core import QgsMessageLog, Qgis
QgsMessageLog.logMessage("Debug message", "Plugin", Qgis.Info)
```

---

## 🏗️ Code Structure

```
mif_to_shp_converter_3.6/
├── 📄 mif_to_shp_converter.py       # Main plugin class
├── 📄 worker.py                     # Multi-threaded processing
├── 📄 translation_manager.py        # i18n system
├── 📁 gui/                          # GUI components
├── 📁 translations/                 # Language files (9 languages)
├── 📁 docs/                         # Documentation
└── 📁 tests/                        # Test suite
```

### Key Components
- **Main Plugin**: QGIS integration and lifecycle
- **Worker**: Multi-threaded file conversion
- **GUI**: Modular interface with event handling
- **Translations**: 9 languages with RTL support

---

## 🤝 Contributing

### Workflow
```bash
# 1. Create feature branch
git checkout -b feature/add-format-support

# 2. Make changes and test
black .
isort .
flake8 .
pytest

# 3. Commit and push
git commit -m "feat: add DXF format support"
git push origin feature/add-format-support

# 4. Create pull request
```

### Code Style
```python
# Good: Type hints and docstrings
def convert_file(input_path: str, output_path: str) -> bool:
    """Convert MapInfo file to target format."""
    pass

# Good: Error handling
try:
    result = process_file(file_path)
except FileNotFoundError:
    return False, "File not found"
except Exception as e:
    return False, f"Error: {e}"
```

### Commit Format
```
feat(scope): description
fix(scope): description
docs: update documentation
test: add unit tests
```

---

## 🧪 Testing

### Test Structure
```python
# tests/test_worker.py
import unittest
from mif_to_shp_converter.worker import ConversionWorker

class TestConversionWorker(unittest.TestCase):
    def setUp(self):
        self.worker = ConversionWorker(...)
    
    def test_initialization(self):
        self.assertIsNotNone(self.worker)
    
    def test_file_conversion(self):
        success, message = self.worker.convert_single_file(...)
        self.assertTrue(success)
```

### Run Tests
```bash
# All tests
pytest

# With coverage
pytest --cov=mif_to_shp_converter --cov-report=html

# GUI tests
QT_QPA_PLATFORM=offscreen pytest tests/test_gui.py
```

---

## 📦 Building

### Build Script
```bash
#!/bin/bash
# Clean and format
rm -rf build/ dist/
black .
isort .

# Test and build
pytest
python scripts/create_plugin_zip.py

echo "✅ Build complete: dist/mif_to_shp_converter_3.6.zip"
```

### Plugin ZIP Structure
```python
# scripts/create_plugin_zip.py
def create_plugin_zip():
    include = ["*.py", "*.txt", "*.md", "*.png", "gui/*.py", "translations/*.py"]
    exclude = ["__pycache__", "*.pyc", "tests/", "build/"]
    
    with zipfile.ZipFile("dist/plugin.zip", 'w') as zf:
        # Add files matching patterns
        pass
```

---

## 🌍 Adding Languages

### 1. Create Translation File
```python
# translations/new_lang.py
translations = {
    'window_title': 'Translated Title',
    'start_conversion': 'Start',
    'cancel': 'Cancel',
    # ... all keys from en.py
}
```

### 2. Update Manager
```python
# translation_manager.py
self.supported_languages = ['ru', 'en', 'zh', 'hi', 'es', 'ar', 'fr', 'pt', 'de', 'new']
```

### 3. Test Translation
```bash
pytest tests/test_translation.py::test_new_language_completeness
```

---

## ✨ Best Practices

### Code Quality
```python
# Good: Clear naming and documentation
class ConversionWorker(QObject):
    """Multi-threaded file conversion worker."""
    
    def __init__(self, files_list: List[str], output_dir: str):
        """Initialize worker with file list and output directory."""
        self.files_list = files_list
        self.output_dir = output_dir
        self.is_cancelled = False
    
    def convert_single_file(self, file_path: str) -> Tuple[bool, str]:
        """Convert single file with error handling."""
        try:
            # Conversion logic
            return True, "Success"
        except Exception as e:
            return False, f"Error: {e}"
```

### Performance
```python
# Monitor memory usage
import psutil

def monitor_conversion():
    process = psutil.Process()
    initial_memory = process.memory_info().rss
    
    # Conversion logic
    
    final_memory = process.memory_info().rss
    if (final_memory - initial_memory) > 100_000_000:  # 100MB
        print("Warning: High memory usage")
```

### Threading
```python
# Proper signal handling
class ConversionWorker(QObject):
    progress = pyqtSignal(int)
    finished = pyqtSignal()
    error = pyqtSignal(str)
    
    def run(self):
        try:
            for i, file_path in enumerate(self.files_list):
                if self.is_cancelled:
                    break
                
                # Process file
                self.progress.emit(int(i / len(self.files_list) * 100))
                
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()
```

---

## 🔧 Release Process

### Checklist
- [ ] Update version in `metadata.txt`
- [ ] Update changelog in `README.md`
- [ ] Run full test suite
- [ ] Build and test plugin ZIP
- [ ] Create GitHub release
- [ ] Submit to QGIS Plugin Repository

### Commands
```bash
# Prepare release
git checkout -b release/v3.7.0
vim metadata.txt  # Update version
vim README.md     # Update changelog

# Test and build
pytest --cov=mif_to_shp_converter
./scripts/build.sh

# Tag and push
git commit -am "chore: prepare release v3.7.0"
git tag -a v3.7.0 -m "Release v3.7.0"
git push origin release/v3.7.0 v3.7.0
```

---

## 📞 Support

### Getting Help
- **📧 Email**: [kobyakov@lesburo.ru](mailto:kobyakov@lesburo.ru)
- **💬 Telegram**: [@AKobyakov](https://t.me/AKobyakov)
- **🐙 GitHub Issues**: [Bug Reports](https://github.com/AlexKobyakov/mif_to_shp_converter/issues)
- **📚 Discussions**: [Development Questions](https://github.com/AlexKobyakov/mif_to_shp_converter/discussions)

### Resources
- [QGIS Plugin Development](https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/plugins/index.html)
- [PyQt5 Documentation](https://doc.qt.io/qtforpython/)
- [MapInfo Formats](https://www.mapinfo.com/support/documentation)

---

<div align="center">

**🌍 MIF/TAB to SHP/GeoJSON Converter Plugin Development Guide v3.6.0**

*Concise guide for developers and contributors*

[📖 User Manual](user-manual.md) | [🏗️ Architecture](architecture.md) | [📥 Installation](installation.md) | [🔧 API Docs](api.md)

**Made with ❤️ for the QGIS Developer Community**

</div>
