# 🔧 ИСПРАВЛЕНИЕ ОШИБОК КОНСТАНТ Qt

## ❌ ПРОБЛЕМА
При запуске плагина возникает ошибка:
```
AttributeError: type object 'Qt' has no attribute 'ScrollBarNever'
```

## ✅ РЕШЕНИЕ

### 🎯 Исправленные константы:

1. **ScrollBar константы** в `gui_main.py`:
   - `Qt.ScrollBarNever` → `Qt.ScrollBarAlwaysOff`
   - `Qt.ScrollBarAsNeeded` остается без изменений

2. **Layout Direction константы** в `gui_handlers.py`:
   - `setLayoutDirection(1)` → `setLayoutDirection(Qt.RightToLeft)`
   - `setLayoutDirection(0)` → `setLayoutDirection(Qt.LeftToRight)`

### 🔧 Исправленные импорты:

1. **В `gui_handlers.py`:**
   ```python
   # До:
   from qgis.PyQt.QtCore import QThread
   from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox
   from qgis.PyQt.QtGui import QColor
   from qgis.PyQt.QtWidgets import QTableWidgetItem

   # После:
   from qgis.PyQt.QtCore import QThread, Qt
   from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox, QTableWidgetItem
   from qgis.PyQt.QtGui import QColor
   ```

2. **В `gui_main.py`:**
   ```python
   # Строка 109 исправлена:
   self.settings_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
   ```

## 🎉 СТАТУС
✅ **ВСЕ ОШИБКИ ИСПРАВЛЕНЫ**
✅ **ПЛАГИН ГОТОВ К ЗАПУСКУ**

Дата исправления: 27 июля 2025
Автор: Кобяков Александр Викторович
