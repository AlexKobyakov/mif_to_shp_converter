# 📖 User Manual - MIF/TAB to SHP/GeoJSON Converter Plugin v3.6

## 📋 Table of Contents
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Interface Overview](#interface-overview)
- [Step-by-Step Usage](#step-by-step-usage)
- [Advanced Features](#advanced-features)
- [Troubleshooting](#troubleshooting)
- [FAQ](#faq)
- [Support](#support)

---

## 🚀 Quick Start

The MIF/TAB to SHP/GeoJSON Converter is a powerful QGIS plugin that converts MapInfo files to standard GIS formats with professional-grade performance and multilingual support.

### ⚡ 3-Step Quick Conversion

1. **📂 Select Files**: Choose your MIF/MID or TAB files
2. **🎯 Set Output**: Choose destination folder and format
3. **🚀 Convert**: Click "Start Conversion" and wait for results

---

## 📥 Installation

### Method 1: QGIS Plugin Repository (Recommended)
1. Open QGIS
2. Go to `Plugins` → `Manage and Install Plugins`
3. Search for "MIF/TAB to SHP/GeoJSON Converter"
4. Click `Install Plugin`
5. Activate the plugin in the list

### Method 2: Manual Installation
1. Download the plugin from [GitHub Releases](https://github.com/AlexKobyakov/mif_to_shp_converter/releases)
2. Extract to QGIS plugins directory:
   - **Windows**: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - **Linux**: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - **macOS**: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Restart QGIS
4. Enable the plugin in `Plugins` → `Manage and Install Plugins`

### ✅ Verification
After installation, you should see:
- 🎯 Plugin icon in the toolbar
- Menu item in `Vector` → `MIF/TAB Converter`

---

## 🖥️ Interface Overview

### 📱 Main Window Layout

```
┌─────────────────────────────────────────────────────────────┐
│  🌍 Language | ☕ Support | 👤 Author      [Header Bar]    │
├─────────────────────────────────────────────────────────────┤
│                  Settings Tabs                             │
│  ┌─────────────────┐ ┌─────────────────┐                   │
│  │📥📤 Input/Output│ │⚙️ Processing   │                   │
│  │                 │ │                 │                   │
│  │ • File Selection│ │ • Threading     │                   │
│  │ • Mode Toggle   │ │ • Coordinate    │                   │
│  │ • Output Format │ │   System        │                   │
│  └─────────────────┘ └─────────────────┘                   │
├─────────────────────────────────────────────────────────────┤
│        [🚀 Start] [❌ Cancel] [🧹 Clear]  [Control Bar]   │
├─────────────────────────────────────────────────────────────┤
│  📊 Progress: ████████████░░░░░ 75%                        │
│  ┌─────────────────┐ ┌─────────────────┐                   │
│  │📋 Logs         │ │📈 Results       │                   │
│  │                 │ │                 │                   │
│  │ Conversion logs │ │ File status     │                   │
│  │ with timestamps │ │ table           │                   │
│  └─────────────────┘ └─────────────────┘                   │
└─────────────────────────────────────────────────────────────┘
```

### 🎛️ Interface Components

#### 📊 Header Bar
- **🌍 Language Selector**: Switch between 9 supported languages
- **☕ Support Button**: Access donation and support options
- **👤 Author Button**: Contact information and credits

#### ⚙️ Settings Area
- **📥📤 Input/Output Tab**: File selection and format options
- **⚙️ Processing Tab**: Advanced settings and performance options

#### 🎮 Control Bar (Always Visible)
- **🚀 Start Conversion**: Begin the conversion process
- **❌ Cancel**: Stop ongoing conversion
- **🧹 Clear Logs**: Clear log messages

#### 📊 Results Area
- **Progress Bar**: Real-time conversion progress
- **📋 Logs Tab**: Detailed processing messages
- **📈 Results Tab**: File-by-file conversion status

---

## 📚 Step-by-Step Usage

### 🎯 Single File Conversion

#### Step 1: Select Conversion Mode
1. Open the plugin via `Vector` → `MIF/TAB Converter` or toolbar icon
2. In the **Input/Output** tab, select **📄 Single File** mode

#### Step 2: Choose Input File
1. Click **📂 Browse** next to "Input File"
2. Navigate to your MIF or TAB file
3. Select the file and click **Open**

**Supported Input Formats:**
- `.mif` + `.mid` files (MapInfo Interchange Format)
- `.tab` files (MapInfo native format with associated files)

#### Step 3: Set Output Options
1. Click **📂 Browse** next to "Output Folder"
2. Choose destination directory
3. Select output format from dropdown:
   - **🗺️ Shapefile (.shp)** - Standard ESRI format
   - **🌐 GeoJSON (.geojson)** - Web-friendly format

#### Step 4: Configure Processing (Optional)
1. Switch to **⚙️ Processing** tab
2. Adjust **Thread Count** (1-32, auto-detected optimal)
3. Set **Coordinate System** if needed:
   - Use `EPSG:4326` for WGS84
   - Use `EPSG:3857` for Web Mercator
   - Click **📋 Examples** for more CRS options

#### Step 5: Start Conversion
1. Click **🚀 Start Conversion**
2. Monitor progress in the progress bar
3. Watch logs for detailed information
4. Check results in the **📈 Results** tab

### 📁 Batch Processing

#### Step 1: Select Batch Mode
1. In the **Input/Output** tab, select **📁 Batch Processing** mode
2. The interface will adapt for folder selection

#### Step 2: Choose Input Folder
1. Click **📂 Browse** next to "Input Folder"
2. Select folder containing multiple MIF/TAB files
3. All compatible files will be processed automatically

#### Step 3: Configure and Convert
1. Follow steps 3-5 from single file conversion
2. Monitor progress for multiple files
3. Each file's status appears in the results table

---

## 🎛️ Advanced Features

### ⚡ Performance Optimization

#### Thread Configuration
- **Automatic Detection**: Plugin detects optimal thread count
- **Manual Override**: Adjust from 1-32 threads based on:
  - CPU cores available
  - System memory
  - File sizes
  - Other running processes

**Recommended Settings:**
- **Small files (<1MB)**: 4-8 threads
- **Medium files (1-10MB)**: 8-16 threads  
- **Large files (>10MB)**: 16-32 threads

#### Memory Management
- Plugin automatically manages memory usage
- Large files processed in chunks
- Garbage collection optimized for performance

### 🌍 Coordinate Reference Systems

#### Common CRS Examples
- **EPSG:4326** - WGS84 (Geographic, degrees)
- **EPSG:3857** - Web Mercator (Web mapping)
- **EPSG:2154** - RGF93 / Lambert-93 (France)
- **EPSG:25832** - ETRS89 / UTM zone 32N (Central Europe)
- **EPSG:32637** - WGS 84 / UTM zone 37N (Eastern Europe)

#### Custom CRS Input
You can specify CRS in multiple formats:
```
EPSG:4326
PROJ:+proj=longlat +datum=WGS84 +no_defs
WKT:GEOGCS["WGS 84",DATUM["WGS_1984",...]]
```

### 🎨 Interface Customization

#### Language Support
**Available Languages:**
- 🇷🇺 **Русский (Russian)** - Native interface language
- 🇺🇸 **English** - International standard
- 🇨🇳 **中文 (Chinese)** - Simplified Chinese
- 🇮🇳 **हिंदी (Hindi)** - Devanagari script
- 🇪🇸 **Español (Spanish)** - Latin American/European
- 🇸🇦 **العربية (Arabic)** - RTL support
- 🇫🇷 **Français (French)** - European French
- 🇧🇷 **Português (Portuguese)** - Brazilian Portuguese
- 🇩🇪 **Deutsch (German)** - Standard German

**Language Switching:**
1. Click language dropdown in header
2. Select desired language
3. Interface updates immediately
4. No restart required

#### RTL Language Support
- **Arabic**: Complete right-to-left interface support
- **UI Mirroring**: Buttons and layouts adapt automatically
- **Text Direction**: Proper text rendering and alignment

---

## 📊 Understanding Results

### 📈 Results Table Columns

| Column | Description | Values |
|--------|-------------|---------|
| **📄 File** | Source filename | `example.mif`, `data.tab` |
| **📊 Status** | Conversion result | `✅ Success`, `❌ Failed` |
| **💬 Message** | Detailed information | Success/error details |

### 📋 Log Message Types

#### Success Messages (Green 🟢)
- `🚀 Starting conversion...` - Process initiated
- `✅ file.mif: Converted successfully` - File completed
- `🎉 Conversion completed` - All files finished

#### Information Messages (Blue 🔵)
- `📊 Processing 15 files...` - Batch information
- `📁 Using 8 threads` - Configuration details
- `📄 Loading example.mif...` - File processing

#### Warning Messages (Orange 🟠)
- `⚠️ CRS not specified, using default` - Missing settings
- `⚠️ Large file detected` - Performance warning

#### Error Messages (Red 🔴)
- `❌ File not found: example.mif` - Missing file
- `🔥 Invalid coordinate system` - Configuration error
- `❌ Conversion failed: Memory error` - Processing error

---

## 🛠️ Troubleshooting

### Common Issues and Solutions

#### ❌ "Plugin not found in Vector menu"
**Cause**: QGIS version compatibility or installation issue
**Solution**:
1. Check QGIS version (requires 3.0+)
2. Reinstall plugin from Plugin Manager
3. Restart QGIS
4. Look for plugin in `Plugins` menu as fallback

#### 🔥 "Invalid coordinate system" error
**Cause**: Incorrect CRS format or unsupported system
**Solution**:
1. Use standard EPSG codes: `EPSG:4326`
2. Click **📋 Examples** for valid formats
3. Verify CRS exists in QGIS CRS database
4. Leave empty to use file's original CRS

#### ⚠️ "Conversion failed: Permission denied"
**Cause**: Write permissions or file locks
**Solution**:
1. Check output folder permissions
2. Close files in other applications
3. Run QGIS as administrator (Windows)
4. Select different output location

#### 📊 Slow performance with large files
**Cause**: Insufficient threading or memory
**Solution**:
1. Increase thread count in Processing tab
2. Process files in smaller batches
3. Close other applications
4. Use SSD storage for better I/O

#### 🌍 Text not displaying correctly
**Cause**: Font or encoding issues
**Solution**:
1. Switch to English language temporarily
2. Update QGIS to latest version
3. Check system language settings
4. Restart QGIS after language change

#### 📁 "No files found" in batch mode
**Cause**: No compatible files in selected folder
**Solution**:
1. Verify folder contains .mif or .tab files
2. Check file extensions (case sensitive on Linux)
3. Ensure files are not corrupted
4. Try single file mode for testing

---

## ❓ FAQ

### General Questions

**Q: What file formats are supported?**
A: **Input**: MIF/MID and TAB files. **Output**: Shapefile (.shp) and GeoJSON (.geojson).

**Q: Can I convert multiple files at once?**
A: Yes! Use **📁 Batch Processing** mode to convert entire folders.

**Q: Does the plugin work on all operating systems?**
A: Yes, it works on Windows, Linux, and macOS with QGIS 3.0+.

**Q: Are the converted files automatically added to QGIS?**
A: Only if you check **✅ Add to Project** in Processing options.

### Technical Questions

**Q: How many threads should I use?**
A: The plugin auto-detects optimal settings. For manual tuning:
- **4-8 threads**: Small files, older computers
- **8-16 threads**: Medium files, modern computers  
- **16-32 threads**: Large files, high-end systems

**Q: What coordinate systems are supported?**
A: All CRS supported by QGIS, including EPSG codes, PROJ strings, and WKT definitions.

**Q: Can I preserve custom attributes?**
A: Yes, all attributes from MIF/TAB files are preserved in the output.

**Q: What's the maximum file size supported?**
A: No hard limit, but performance depends on available system memory.

### Language and Interface

**Q: How do I change the interface language?**
A: Use the language dropdown in the header bar. Changes apply immediately.

**Q: Is Arabic text properly supported?**
A: Yes, with complete right-to-left (RTL) interface support.

**Q: Can I add new language translations?**
A: Yes! See the [Translation Guide](translations/README.md) for instructions.

---

## 📞 Support

### 🆘 Getting Help

#### 📧 Direct Contact
- **Email**: [kobyakov@lesburo.ru](mailto:kobyakov@lesburo.ru)
- **Telegram**: [@AKobyakov](https://t.me/AKobyakov)

#### 🌐 Online Resources
- **GitHub Issues**: [Report bugs and request features](https://github.com/AlexKobyakov/mif_to_shp_converter/issues)
- **Documentation**: [Complete plugin documentation](https://github.com/AlexKobyakov/mif_to_shp_converter/docs)
- **Discussions**: [Community discussions](https://github.com/AlexKobyakov/mif_to_shp_converter/discussions)

#### ☕ Support Development
If this plugin helps you, consider supporting its development:
- **Ko-fi**: [Buy me a coffee](https://ko-fi.com/kobyakov)
- **PayPal**: [Donation via PayPal](https://paypal.me/kobyakov)
- **GitHub**: [Sponsor on GitHub](https://github.com/sponsors/kobyakov)

### 🐛 Reporting Issues

When reporting issues, please include:

1. **System Information**:
   - QGIS version
   - Operating system
   - Plugin version

2. **Problem Description**:
   - What you were trying to do
   - What happened instead
   - Error messages (if any)

3. **Steps to Reproduce**:
   - Detailed steps to recreate the issue
   - Sample files (if possible)
   - Screenshots (if relevant)

4. **Log Information**:
   - Copy relevant log messages
   - Include full error stack traces

### 📋 Feature Requests

We welcome suggestions for new features! Please:
1. Check existing issues first
2. Describe the use case clearly
3. Explain the expected behavior
4. Consider implementation complexity

---

## 🎓 Tips and Best Practices

### 🚀 Performance Tips

1. **Batch Processing**:
   - Group similar-sized files together
   - Process during low system usage
   - Monitor memory usage for very large batches

2. **Thread Optimization**:
   - Start with auto-detected settings
   - Increase threads for I/O bound operations
   - Decrease threads if system becomes unresponsive

3. **Storage Considerations**:
   - Use SSDs for better performance
   - Ensure sufficient free space (3x input size)
   - Avoid network drives for large files

### 🎯 Workflow Optimization

1. **File Organization**:
   - Keep MIF/MID pairs together
   - Use consistent naming conventions
   - Organize by project or region

2. **Quality Control**:
   - Test with small samples first
   - Verify CRS settings before large batches
   - Check results in QGIS after conversion

3. **Project Integration**:
   - Use "Add to Project" for immediate use
   - Set consistent output naming
   - Document conversion parameters

### 🌍 Multi-language Usage

1. **Team Collaboration**:
   - Standardize on one language for consistency
   - Train users on interface basics
   - Create local documentation if needed

2. **International Projects**:
   - Use appropriate CRS for region
   - Consider cultural UI preferences
   - Test interface in target languages

---

## 📝 Version History

### 🎯 Current Version: 3.6.0
- **🔗 QGIS Plugin Repository compliance** with complete metadata
- **📋 Enhanced menu integration** with robust fallback methods
- **💬 Telegram contact integration** for direct support
- **🎯 Always-visible control buttons** for better UX
- **🌍 Complete translation coverage** including all dialogs

### 🏆 Major Milestones
- **v3.5.0**: UI visibility improvements and fixed button layout
- **v3.4.0**: Complete translation coverage and enhanced header design
- **v3.2.0**: Ultimate performance optimization (60% faster)
- **v3.0.0**: Major architectural overhaul with modern UI
- **v2.0.0**: Batch processing and multithreading introduction
- **v1.0.0**: Initial release with basic MIF to SHP conversion

---

## 📄 License and Credits

### 📜 License
This plugin is released under the **MIT License**. See [LICENSE](../LICENSE) file for details.

### 👨‍💻 Author
**Кобяков Александр Викторович (Alex Kobyakov)**
- 🏢 Organization: Lesburo
- 📧 Email: kobyakov@lesburo.ru
- 💬 Telegram: [@AKobyakov](https://t.me/AKobyakov)
- 🐙 GitHub: [@AlexKobyakov](https://github.com/AlexKobyakov)

### 🙏 Acknowledgments
- QGIS Development Team for the excellent platform
- MapInfo for the MIF/TAB format specifications
- Community contributors for translations and feedback
- Users who provided bug reports and feature suggestions

---

<div align="center">

**🎯 MIF/TAB to SHP/GeoJSON Converter Plugin v3.6.0**

*Professional multilingual converter with enterprise-grade performance*

**Made with ❤️ for the QGIS Community**

[⭐ Star on GitHub](https://github.com/AlexKobyakov/mif_to_shp_converter) | [🐛 Report Issues](https://github.com/AlexKobyakov/mif_to_shp_converter/issues) | [💬 Discussions](https://github.com/AlexKobyakov/mif_to_shp_converter/discussions)

</div>
