# -*- coding: utf-8 -*-
"""
Тест импортов модульного GUI
Test file for modular GUI imports

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

def test_imports():
    """Тестирование всех импортов GUI модулей"""
    try:
        print("🔄 Тестирование импортов модульного GUI...")
        
        # Тест базовых компонентов
        from .gui.gui_components import ModernGroupBox, ModernButton, ModernProgressBar
        print("✅ gui_components импортирован успешно")
        
        # Тест виджетов
        from .gui.gui_widgets import HeaderWidget, ConversionModeWidget, InputDataWidget
        print("✅ gui_widgets импортирован успешно")
        
        # Тест диалогов  
        from .gui.gui_dialogs import AuthorInfoDialog, CrsExamplesDialog
        print("✅ gui_dialogs импортирован успешно")
        
        # Тест обработчиков
        from .gui.gui_handlers import GuiEventHandlers
        print("✅ gui_handlers импортирован успешно")
        
        # Тест главного окна
        from .gui.gui_main import MifToShpDialog
        print("✅ gui_main импортирован успешно")
        
        # Тест пакета GUI
        from .gui import MifToShpDialog as DialogFromPackage
        print("✅ gui package импортирован успешно")
        
        print("🎉 Все импорты успешно прошли тестирование!")
        return True
        
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        return False
    except Exception as e:
        print(f"❌ Неожиданная ошибка: {e}")
        return False

if __name__ == "__main__":
    test_imports()
