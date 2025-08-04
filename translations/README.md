# Modular Translation System for MIF/TAB to SHP/GeoJSON Converter

## Overview
This directory contains the modular translation system for the QGIS plugin. Each language is stored in a separate Python module for better maintainability and extensibility.

## Structure
```
translations/
├── __init__.py          # Package initialization
├── ru.py               # Russian translations
├── en.py               # English translations
├── zh.py               # Chinese translations
├── hi.py               # Hindi translations
├── es.py               # Spanish translations
├── ar.py               # Arabic translations
├── fr.py               # French translations
├── pt.py               # Portuguese translations
├── de.py               # German translations
└── README.md           # This file
```

## Supported Languages
- 🇷🇺 Russian (ru) - Primary language
- 🇺🇸 English (en) - Fallback language
- 🇨🇳 Chinese (zh)
- 🇮🇳 Hindi (hi)
- 🇪🇸 Spanish (es)
- 🇸🇦 Arabic (ar)
- 🇫🇷 French (fr)
- 🇧🇷 Portuguese (pt)
- 🇩🇪 German (de)

## How it works
1. The main `TranslationManager` class is located in `../translations.py`
2. Each language file contains a `translations` dictionary with all translation keys
3. The manager loads language modules dynamically
4. If a translation key is not found in the current language, it falls back to English
5. If not found in English, it falls back to Russian
6. If still not found, it returns the key itself

## Adding a New Language

1. Create a new file `[language_code].py` in this directory
2. Add the language code to the `supported_languages` list in `../translations.py`
3. Add the language flag and name to the GUI language selector
4. Follow the template below:

```python
# -*- coding: utf-8 -*-
"""
[Language Name] translations for MIF/TAB to SHP/GeoJSON Converter Plugin

Author: Кобяков Александр Викторович (Alex Kobyakov)
Email: kobyakov@lesburo.ru
Year: 2025
"""

translations = {
    # Main interface translations
    'window_title': '[Translated title]',
    'conversion_mode': '[Translated text]',
    # ... add all required keys
    
    # Donation dialog translations
    'donation_title': '[Translated text]',
    # ... add all donation keys
}
```

## Translation Keys

All language files must contain the following keys:

### Main Interface
- `window_title`
- `conversion_mode`
- `single_file`
- `batch_processing`
- `input_file`
- `input_folder`
- `output_folder`
- `output_format`
- `browse`
- `threading_settings`
- `thread_count`
- `coordinate_system`
- `crs_format_hint`
- `add_to_project`
- `progress`
- `logs`
- `results`
- `start_conversion`
- `cancel`
- `clear_logs`
- `converting`
- `language`
- `file`
- `status`
- `message`
- `success`
- `error`
- `select_input_file`
- `select_input_folder`
- `select_output_folder`
- `error_no_input_file`
- `error_no_input_folder`
- `error_no_files_found`
- `error_no_output_folder`
- `error_no_crs`
- `conversion_cancelled`
- `confirm_close`
- `confirmation`
- `critical_error`
- `supported_formats`
- `author_info`
- `about_author`
- `settings`
- `input_output`
- `processing_options`

### Donation Dialog
- `donation_title`
- `donation_window_title`
- `donation_description`
- `donation_kofi`
- `donation_tbank`
- `donation_github`
- `donation_maybe_later`
- `donation_support_development`
- `donation_plugin_info`
- `donation_help_improve`
- `donation_every_coffee`

## Usage in Code

```python
from translations import translations

# Get translated text
text = translations.get_text('window_title')

# Change language
translations.set_language('en')

# Update GUI after language change
self.updateLanguage()
```

## Maintenance Notes

- Always keep all translation files in sync with new keys
- Test all languages after adding new features
- Use proper character encodings (UTF-8)
- Consider RTL (right-to-left) languages like Arabic
- Keep translation keys consistent across all languages

## Author

Created by: Кобяков Александр Викторович (Alex Kobyakov)  
Email: kobyakov@lesburo.ru  
Year: 2025
