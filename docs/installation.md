# 📥 Installation Guide - MIF/TAB to SHP/GeoJSON Converter Plugin v3.6

## 📋 Table of Contents
- [System Requirements](#system-requirements)
- [Installation Methods](#installation-methods)
- [Verification](#verification)
- [Configuration](#configuration)
- [Troubleshooting](#troubleshooting)
- [Uninstallation](#uninstallation)
- [Advanced Installation](#advanced-installation)

---

## 💻 System Requirements

### 🎯 Minimum Requirements

| Component | Requirement | Notes |
|-----------|-------------|-------|
| **QGIS** | 3.0+ | QGIS 3.4+ recommended |
| **Python** | 3.9+ | Included with QGIS |
| **Qt** | 5.15+ | Included with QGIS |
| **RAM** | 4 GB | 8 GB+ for large files |
| **Storage** | 50 MB | Additional space for conversions |
| **CPU** | Dual-core | Multi-core for better performance |

### 🖥️ Supported Operating Systems

#### ✅ Windows
- **Windows 10** (1903+) - Fully supported
- **Windows 11** - Fully supported
- **Windows Server 2019/2022** - Supported

#### ✅ Linux
- **Ubuntu 20.04 LTS+** - Fully tested
- **Fedora 35+** - Supported
- **openSUSE Leap 15.3+** - Supported
- **Debian 11+** - Supported
- **CentOS 8+** - Supported

#### ✅ macOS
- **macOS 10.15 Catalina+** - Fully supported
- **macOS 11 Big Sur+** - Fully supported
- **macOS 12 Monterey+** - Fully supported
- **macOS 13 Ventura+** - Fully supported

### 🔧 QGIS Version Compatibility

| QGIS Version | Plugin Support | Notes |
|--------------|----------------|-------|
| **3.34 LTR** | ✅ Full | Recommended |
| **3.28 LTR** | ✅ Full | Stable |
| **3.22 LTR** | ✅ Full | Legacy support |
| **3.16 LTR** | ⚠️ Limited | Basic features only |
| **3.4-3.15** | ⚠️ Limited | Compatibility mode |
| **< 3.4** | ❌ Not supported | Upgrade required |

---

## 📦 Installation Methods

### Method 1: 🏪 QGIS Plugin Repository (Recommended)

This is the easiest and safest installation method.

#### Step 1: Open Plugin Manager
1. Launch **QGIS**
2. Go to **Plugins** → **Manage and Install Plugins...**
3. The Plugin Manager window will open

#### Step 2: Search for Plugin
1. Click on the **All** tab
2. In the search box, type: `MIF TAB Converter`
3. The plugin should appear in the results list

#### Step 3: Install Plugin
1. Click on **MIF/TAB to SHP/GeoJSON Converter** in the list
2. Click the **Install Plugin** button
3. Wait for the installation to complete
4. The plugin is now installed and activated

### Method 2: 📁 Manual Installation from ZIP

Use this method if the plugin isn't available in the repository yet.

#### Step 1: Download Plugin
1. Go to [GitHub Releases](https://github.com/AlexKobyakov/mif_to_shp_converter/releases)
2. Download the latest `mif_to_shp_converter_3.6.zip` file
3. Save it to your Downloads folder

#### Step 2: Install from ZIP
1. Open QGIS Plugin Manager (**Plugins** → **Manage and Install Plugins...**)
2. Click on **Install from ZIP** tab
3. Click the **...** button to browse for the ZIP file
4. Select the downloaded ZIP file
5. Click **Install Plugin**
6. Wait for installation completion

### Method 3: 🔧 Manual Extraction

For advanced users or custom installations.

#### Step 1: Locate QGIS Plugins Directory

**Windows:**
```
%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\
```
Full path example:
```
C:\Users\[Username]\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins\
```

**Linux:**
```
~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```
Full path example:
```
/home/[username]/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
```

**macOS:**
```
~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/
```
Full path example:
```
/Users/[username]/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/
```

#### Step 2: Extract Plugin
1. Download and extract the plugin ZIP file
2. Copy the `mif_to_shp_converter_3.6` folder to the plugins directory
3. Ensure the folder structure is correct:
```
plugins/
└── mif_to_shp_converter_3.6/
    ├── __init__.py
    ├── mif_to_shp_converter.py
    ├── metadata.txt
    └── [other files...]
```

#### Step 3: Restart and Activate
1. Restart QGIS completely
2. Go to **Plugins** → **Manage and Install Plugins...**
3. Click on **Installed** tab
4. Find **MIF/TAB to SHP/GeoJSON Converter**
5. Check the checkbox to activate it

### Method 4: 🐙 Git Clone (Developers)

For developers who want to work with the source code.

#### Prerequisites
- Git installed on your system
- Command line access
- QGIS plugins directory located

#### Installation Steps
```bash
# Navigate to QGIS plugins directory
cd /path/to/qgis/plugins/

# Clone the repository
git clone https://github.com/AlexKobyakov/mif_to_shp_converter.git

# Checkout the latest version
cd mif_to_shp_converter
git checkout v3.6-stable

# For development
git checkout main
```

**Platform-specific commands:**

**Windows (Command Prompt):**
```cmd
cd %APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\
git clone https://github.com/AlexKobyakov/mif_to_shp_converter.git
```

**Linux/macOS (Terminal):**
```bash
cd ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
git clone https://github.com/AlexKobyakov/mif_to_shp_converter.git
```

---

## ✅ Verification

### 🔍 Check Installation Success

After installation, verify the plugin is working correctly:

#### Visual Verification
1. **Toolbar Icon**: Look for the 🎯 plugin icon in the QGIS toolbar
2. **Menu Item**: Check **Vector** → **MIF/TAB Converter** menu item
3. **Plugin List**: Confirm plugin appears in **Plugins** → **Manage and Install Plugins** → **Installed**

#### Functional Test
1. Click the plugin icon or menu item
2. The plugin dialog should open without errors
3. Try switching languages in the header
4. All interface elements should display correctly

### 🧪 Test Conversion

Perform a quick test to ensure everything works:

1. **Download Sample Data**:
   - Create a simple MIF file for testing
   - Or use existing MapInfo data

2. **Test Single File Conversion**:
   - Open the plugin
   - Select single file mode
   - Choose your test MIF file
   - Set output folder
   - Click "Start Conversion"

3. **Verify Results**:
   - Check output folder for created files
   - Verify files open correctly in QGIS
   - Check logs for any errors

### 📊 Performance Test

Test threading and performance:

1. **Thread Count**: Verify thread selector shows appropriate range (1-32)
2. **Multi-file Test**: Try batch processing with multiple files
3. **Progress Display**: Confirm progress bar updates during conversion
4. **Language Test**: Switch between different languages

---

## ⚙️ Configuration

### 🌍 Language Configuration

The plugin automatically detects your QGIS language setting, but you can change it:

1. **Automatic Detection**:
   - Plugin uses QGIS locale setting
   - Falls back to English if language not supported

2. **Manual Selection**:
   - Use language dropdown in plugin header
   - Changes apply immediately
   - Setting persists between sessions

### 🔧 Default Settings

The plugin comes with optimized defaults:

| Setting | Default Value | Customizable |
|---------|---------------|--------------|
| **Thread Count** | Auto-detected | Yes (1-32) |
| **Output Format** | Shapefile | Yes (SHP/GeoJSON) |
| **CRS** | Source file CRS | Yes (Any valid CRS) |
| **Add to Project** | Disabled | Yes |
| **Language** | System locale | Yes |

### 📁 Folder Permissions

Ensure proper permissions for plugin operation:

**Windows:**
- Output folders: Write access required
- QGIS plugins folder: Full control for updates
- Temp folders: System manages automatically

**Linux/macOS:**
- Output folders: `chmod 755` or higher
- Plugin folder: User read/write access
- Use `sudo` only if necessary for system-wide installation

---

## 🛠️ Troubleshooting

### ❌ Common Installation Issues

#### Issue 1: "Plugin not found in repository"
**Symptoms**: Plugin doesn't appear in QGIS Plugin Manager
**Causes**:
- Plugin not yet published to official repository
- Repository refresh needed
- Network connectivity issues

**Solutions**:
1. **Refresh Repository**:
   ```
   Plugins → Manage and Install Plugins → Settings → Reload repository
   ```

2. **Check Network Connection**:
   - Verify internet connectivity
   - Check proxy settings in QGIS
   - Try manual download method

3. **Use Alternative Installation**:
   - Use Method 2 (Manual ZIP installation)
   - Contact support for direct download link

#### Issue 2: "Installation failed" error
**Symptoms**: Error during ZIP installation
**Causes**:
- Corrupted download file
- Insufficient permissions
- Plugin folder conflicts

**Solutions**:
1. **Re-download Plugin**:
   - Delete corrupted ZIP file
   - Download fresh copy from GitHub
   - Verify file integrity

2. **Check Permissions**:
   ```bash
   # Linux/macOS
   chmod -R 755 ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/
   
   # Windows: Run QGIS as Administrator
   ```

3. **Clear Plugin Cache**:
   - Close QGIS completely
   - Delete plugin folder if partially installed
   - Restart QGIS and try again

#### Issue 3: "Plugin won't activate"
**Symptoms**: Plugin installs but won't activate
**Causes**:
- Missing dependencies
- Python path issues
- Conflicting plugins

**Solutions**:
1. **Check QGIS Version**:
   - Verify QGIS 3.0+ requirement
   - Update QGIS if necessary

2. **Review Error Messages**:
   - Check QGIS Log Messages panel
   - Look for Python import errors
   - Note specific error details

3. **Clean Reinstall**:
   - Uninstall plugin completely
   - Restart QGIS
   - Reinstall using Method 1

#### Issue 4: "Missing menu items"
**Symptoms**: Plugin activates but no menu items appear
**Causes**:
- Menu integration issues
- QGIS interface customization
- Plugin initialization errors

**Solutions**:
1. **Check Toolbar**:
   - Look for plugin icon in toolbar
   - Right-click toolbar to customize

2. **Reset QGIS Interface**:
   ```
   Settings → Options → General → Reset default interface
   ```

3. **Check Alternative Menus**:
   - Look in **Plugins** menu
   - Search in **Processing** toolbox

### 🔧 Advanced Troubleshooting

#### Debug Mode Installation
For developers or advanced troubleshooting:

1. **Enable Debug Logging**:
   ```python
   # Add to QGIS Python Console
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **Manual Plugin Loading**:
   ```python
   # QGIS Python Console
   import sys
   sys.path.append('/path/to/plugin/directory')
   from mif_to_shp_converter import MifToShpConverter
   ```

3. **Check Dependencies**:
   ```python
   # Verify required modules
   import qgis.core
   import qgis.PyQt
   print("All dependencies available")
   ```

---

## 🗑️ Uninstallation

### Complete Removal

#### Method 1: Plugin Manager
1. Open **Plugins** → **Manage and Install Plugins...**
2. Click **Installed** tab
3. Find **MIF/TAB to SHP/GeoJSON Converter**
4. Click **Uninstall Plugin**
5. Confirm removal

#### Method 2: Manual Removal
1. Close QGIS completely
2. Navigate to plugins directory:
   - Windows: `%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\`
   - Linux: `~/.local/share/QGIS/QGIS3/profiles/default/python/plugins/`
   - macOS: `~/Library/Application Support/QGIS/QGIS3/profiles/default/python/plugins/`
3. Delete the `mif_to_shp_converter_3.6` folder
4. Restart QGIS

### Clean Removal (Advanced)
Remove all plugin traces:

1. **Remove Plugin Files**: Delete plugin directory
2. **Clear Settings**: 
   ```python
   # QGIS Python Console
   from qgis.core import QgsSettings
   settings = QgsSettings()
   settings.remove('mif_to_shp_converter')
   ```
3. **Clear Cache**: Remove any cached plugin data
4. **Restart QGIS**: Complete clean restart

---

## 🚀 Advanced Installation

### 🏢 Enterprise Deployment

For organizations deploying to multiple users:

#### Network Installation
1. **Shared Plugin Directory**:
   ```
   \\server\qgis\plugins\mif_to_shp_converter_3.6\
   ```

2. **Custom Installation Script**:
   ```batch
   @echo off
   REM Windows batch script for enterprise deployment
   xcopy "\\server\qgis\plugins\mif_to_shp_converter_3.6" "%APPDATA%\QGIS\QGIS3\profiles\default\python\plugins\" /E /I /Y
   echo Plugin installed successfully
   ```

3. **Group Policy Deployment** (Windows):
   - Package plugin as MSI
   - Deploy via Active Directory
   - Configure automatic updates

#### Linux Package Management
```bash
# Create DEB package (Debian/Ubuntu)
dpkg-deb --build mif-to-shp-converter-qgis-plugin_3.6.0_all.deb

# Create RPM package (RedHat/Fedora)
rpmbuild -ba mif-to-shp-converter-qgis-plugin.spec
```

### 🐳 Docker Installation

For containerized QGIS environments:

```dockerfile
FROM qgis/qgis:latest

# Install plugin
COPY mif_to_shp_converter_3.6 /usr/share/qgis/python/plugins/mif_to_shp_converter_3.6

# Set permissions
RUN chmod -R 755 /usr/share/qgis/python/plugins/mif_to_shp_converter_3.6

# Configure QGIS
ENV QGIS_PLUGINPATH=/usr/share/qgis/python/plugins
```

### 🔧 Custom Profile Installation

For specific QGIS profiles:

1. **Identify Profile Path**:
   ```python
   # QGIS Python Console
   from qgis.core import QgsApplication
   print(QgsApplication.qgisSettingsDirPath())
   ```

2. **Install to Custom Profile**:
   ```bash
   # Copy to specific profile
   cp -r mif_to_shp_converter_3.6 ~/.local/share/QGIS/QGIS3/profiles/[profile_name]/python/plugins/
   ```

---

## 📞 Installation Support

### 🆘 Getting Help

If you encounter installation issues:

#### 📧 Contact Support
- **Email**: [kobyakov@lesburo.ru](mailto:kobyakov@lesburo.ru)
- **Telegram**: [@AKobyakov](https://t.me/AKobyakov)
- **GitHub Issues**: [Report Installation Problems](https://github.com/AlexKobyakov/mif_to_shp_converter/issues)

#### 📋 Information to Include
When requesting installation help, please provide:

1. **System Information**:
   - Operating System and version
   - QGIS version and build
   - Python version (if known)

2. **Installation Method**:
   - Which method you tried
   - Steps completed successfully
   - Where the process failed

3. **Error Messages**:
   - Complete error text
   - Screenshots of error dialogs
   - QGIS log messages

4. **Environment Details**:
   - Antivirus software
   - Network restrictions
   - Administrative privileges

### 🔍 Self-Diagnosis Tools

#### QGIS System Information
```python
# Run in QGIS Python Console
from qgis.core import QgsApplication
from qgis.PyQt.QtCore import QT_VERSION_STR
from qgis.PyQt.Qt import PYQT_VERSION_STR

print(f"QGIS Version: {QgsApplication.version()}")
print(f"Qt Version: {QT_VERSION_STR}")
print(f"PyQt Version: {PYQT_VERSION_STR}")
print(f"Python Version: {sys.version}")
print(f"Platform: {sys.platform}")
```

#### Plugin Directory Check
```python
# Verify plugin directories exist
import os
from qgis.core import QgsApplication

plugin_path = os.path.join(QgsApplication.qgisSettingsDirPath(), 'python', 'plugins')
print(f"Plugin directory: {plugin_path}")
print(f"Directory exists: {os.path.exists(plugin_path)}")
print(f"Directory writable: {os.access(plugin_path, os.W_OK)}")
```

---

## 🎉 Post-Installation

### 🎯 Next Steps

After successful installation:

1. **📖 Read User Manual**: Review [user-manual.md](user-manual.md) for usage instructions
2. **🧪 Test Plugin**: Try converting sample files to verify functionality  
3. **🌍 Set Language**: Choose your preferred interface language
4. **⚙️ Configure Settings**: Optimize thread count and default folders
5. **⭐ Rate Plugin**: Leave feedback in QGIS Plugin Repository

### 🚀 Quick Start

Ready to start converting? Follow these steps:

1. **Launch Plugin**: Click toolbar icon or use Vector menu
2. **Select Mode**: Choose single file or batch processing
3. **Pick Files**: Browse for MIF/TAB files to convert
4. **Set Output**: Choose destination folder and format
5. **Start**: Click "Start Conversion" and monitor progress

### 📚 Learn More

- **📖 User Manual**: Complete usage guide
- **🏗️ Architecture**: Technical details for developers
- **🔧 API Documentation**: Programming interface details
- **🌍 Development Guide**: Contribution and extension guide

---

<div align="center">

**🎯 Installation Complete!**

*Ready to convert your MapInfo files with professional-grade performance*

[📖 User Manual](user-manual.md) | [🏗️ Architecture](architecture.md) | [🔧 API Docs](api.md) | [🌍 Development](development.md)

**Made with ❤️ for the QGIS Community**

</div>
