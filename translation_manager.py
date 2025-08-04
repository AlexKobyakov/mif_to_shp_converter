# -*- coding: utf-8 -*-
"""
Translation Manager for MIF/TAB to SHP/GeoJSON Converter Plugin
Менеджер переводов для плагина конвертации MIF/TAB в SHP/GeoJSON

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

import os
import sys

class TranslationManager:
    """Менеджер переводов с поддержкой модульной архитектуры"""
    
    def __init__(self):
        self.current_language = 'ru'
        self.fallback_language = 'en'
        self.loaded_languages = {}
        
        # Список поддерживаемых языков
        self.supported_languages = ['ru', 'en', 'zh', 'hi', 'es', 'ar', 'fr', 'pt', 'de']
        
        # Загружаем язык по умолчанию
        self._load_language(self.current_language)
        if self.current_language != self.fallback_language:
            self._load_language(self.fallback_language)
    
    def _load_language(self, language_code):
        """Загружает переводы для указанного языка"""
        if language_code in self.loaded_languages:
            return True
            
        if language_code not in self.supported_languages:
            return False
            
        try:
            # Динамически импортируем модуль языка из пакета translations
            if language_code == 'ru':
                from .translations import ru as module
            elif language_code == 'en':
                from .translations import en as module
            elif language_code == 'zh':
                from .translations import zh as module
            elif language_code == 'hi':
                from .translations import hi as module
            elif language_code == 'es':
                from .translations import es as module
            elif language_code == 'ar':
                from .translations import ar as module
            elif language_code == 'fr':
                from .translations import fr as module
            elif language_code == 'pt':
                from .translations import pt as module
            elif language_code == 'de':
                from .translations import de as module
            else:
                return False
            
            if hasattr(module, 'translations'):
                self.loaded_languages[language_code] = module.translations
                return True
            else:
                print(f"Warning: Module {language_code} does not have 'translations' dictionary")
                return False
                
        except ImportError as e:
            print(f"Warning: Could not load translations for {language_code}: {e}")
            return False
        except Exception as e:
            print(f"Error loading translations for {language_code}: {e}")
            return False
    
    def set_language(self, language_code):
        """Устанавливает текущий язык"""
        if language_code in self.supported_languages:
            if self._load_language(language_code):
                self.current_language = language_code
                return True
        return False
    
    def get_text(self, key, language=None):
        """Получает переведенный текст по ключу с fallback механизмом"""
        # Определяем язык для поиска
        lang = language or self.current_language
        
        # Пытаемся найти в текущем языке
        if lang in self.loaded_languages:
            translations = self.loaded_languages[lang]
            if key in translations:
                return translations[key]
        
        # Пытаемся найти в резервном языке
        if self.fallback_language in self.loaded_languages and lang != self.fallback_language:
            translations = self.loaded_languages[self.fallback_language]
            if key in translations:
                return translations[key]
        
        # Возвращаем ключ, если перевод не найден
        return key
    
    def get_current_language(self):
        """Возвращает код текущего языка"""
        return self.current_language
    
    def get_supported_languages(self):
        """Возвращает список поддерживаемых языков"""
        return self.supported_languages.copy()
    
    def is_language_loaded(self, language_code):
        """Проверяет, загружен ли язык"""
        return language_code in self.loaded_languages
    
    def reload_language(self, language_code):
        """Перезагружает переводы для языка"""
        if language_code in self.loaded_languages:
            del self.loaded_languages[language_code]
        return self._load_language(language_code)


# Глобальный объект переводов
translations = TranslationManager()
