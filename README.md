# Music File Scrubber

A utility that cleans up music files so they're not skipped/ignored, play in the correct order and display properly with track # and title when copied from one OS to another.

## 🚀 Features

A lightweight, single-file Python utility designed to clean, standardize, and scrub audio file metadata and filenames for a pristine, seamless local media library. Tested and verified for compatibility with Volumio gapless playback servers.

* **Metadata Cleansing:** Strips problematic, corrupt, or non-standard tags that cause indexing issues in local music players.
* **Smart Filename Renaming:** Standardizes file naming conventions for clean sorting without breaking album structures.
* **Dry-Run Safety:** Features a robust "Safe Mode" allowing you to verify exactly what changes will be made before a single file is altered on disk.
* **Volumio Tested:** In extensive testing has not interrupted gapless playback sequences or triggered library scanning exceptions.

## 📊 Real-World Example (32GB USB Drive Run)

To see exactly how the script behaves under pressure, check out the execution logs:
* [Processing Log (Safe Mode)](ProcessingLogSafeMode.txt) - The initial dry-run assessment that generates a non-destructive preview of changes.
* [Processing Log (Commit Mode)](ProcessingLogChangeMode.txt) - The actual execution where the files are safely updated on disk based on the verified logs.

## 🖼️ Interface Preview

![Music File Scrubber GUI](Screenshot%202026-05-17%20173638.png)

## 🔍 Why This Matters

Many modern media players, especially audiophile-focused gapless playback systems like Volumio, rely on pristine file integrity to map out audio buffers. Behind the scenes, various music ripping tools, download stores, and editing software inject non-standard metadata, hidden padding blocks, or corrupt ID3 frames into audio headers.

This utility strips away that hidden digital "friction", leaving only the pure audio stream and the essential, standardized tags your player needs.

## 📦 How to Run (For Windows End Users)

No Python installation, command line tweaks, or virtual environments required. 

1. Go to the **[Releases](https://github.com/dlaub123/Music-Analyzer/releases)** section on the right side of this page.
2. Download the latest standalone binary: `MusicFileScrubber.exe`.
3. Move the executable to a folder of your choice, double-click to launch, and select your music directory!

---

## 🛠️ Tech Stack & Developer Setup for LINUX and Mac

If you want to modify the source code or build the executable yourself from scratch, use the following configuration:

### Dependencies
- Python 3.12
- `tkinter` (Standard GUI library)
- `mutagen` (Audio metadata tagging framework)

### Local Development Setup
```bash
# Clone the repository
git clone [https://github.com/dlaub123/Music-Analyzer.git](https://github.com/dlaub123/Music-Analyzer.git)
cd Music-Analyzer

# Install required dependencies locally
pip install mutagen pyinstaller

# Compiling a New Standalone Executable
To bundle the script into a single standalone binary on Linux or macOS, run the clean compilation command in your local terminal:
python -m PyInstaller --clean --onefile MusicFileScrubber.py
```

## ☕ Support the Project

If this utility helped clean up your music library or saved you hours of manual tagging, consider supporting ongoing development:

[Support me on Ko-fi](https://ko-fi.com/dmlsoftare) [or Paypal](https:/paypal.com/dmlaub123)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
