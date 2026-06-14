# Music File Scrubber

A utility that cleans up music files so they're not skipped/ignored when copied from one OS to another.

## 🚀 Features

A lightweight, single-file Python utility designed to clean, standardize, and scrub audio file metadata and filenames for a pristine local media library. Tested and verified for compatibility with Volumio gapless playback servers.

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

## 📦 How to Run (For Windows & Linux Mint for Intel End Users)

No Python installation, command line tweaks, or virtual environments required.  Simply download the executable. 

1. Go to the **[Releases](https://github.com/dlaub123/Music-Analyzer/releases)** section on the right side of this page.
2. Download the latest standalone binary: `MusicFileScrubber.exe` for Windows or `MusicFileScrubber` for Linux Mint (note after downloading the Linux mint version you may have to run chmod +x on the executable)
3. Move the executable to a folder of your choice, double-click to launch, and select your music directory!
4. If Windows displays a "Protected your PC" warning, click "More Info" and then "Run Anyway."

---

## 🛠️ Tech Stack & Developer Setup for LINUX and Mac (and Windows fans of command line tools)

If you want to modify the source code or build the executable yourself use the following configuration:

### Dependencies
- Python 3.12
- `tkinter` (Standard GUI library)
- `mutagen` (Audio metadata tagging framework)

## Prerequisites

If you are starting from scratch, you will need Python installed on your system. 

1. **Install Python:** Download it from [python.org](https://www.python.org/downloads/) or your system's package manager.
2. **Ensure `pip` is installed:** Pip is Python's package manager. It usually comes with Python, but you can verify by running:
   `pip --version` (or `pip3 --version` on Linux/Mac)

## Linux Environments e.g. Mint / Ubuntu-Based Setup (For most Linux installs this is pre-installed)

If you are running Linux Mint, Ubuntu, or a similar Debian-based distribution, you may need to install the underlying UI framework (`tkinter`) at the system level before building the app. If you skip this, the script might run, but the executable will crash with a `ModuleNotFoundError`.

Run this in your terminal:
`sudo apt-get install python3-tk`

*(Note: You may also need to install pip directly if your distro didn't include it: `sudo apt install python3-pip`)*

## Building the Executable

```bash
# Clone the repository
git clone https://github.com/dlaub123/Music-Analyzer.git
cd Music-Analyzer

# Install required dependencies locally (For most Linux installs this is pre-installed)
pip install mutagen pyinstaller

# Compiling a New Standalone Executable
To bundle the script into a single standalone binary on Linux or macOS, run the clean compilation command in your local terminal:
python3 -m PyInstaller --clean --onefile MusicFileScrubber.py
```

## ☕ Support the Project

This utility was partially generated using AI tools. If this utility helped clean up your music library or saved you hours of manual tagging, consider supporting ongoing development:

* **[Support me on Ko-fi](https://ko-fi.com/dmlsoftware)**  (dmlsoftware)
* **[Support me on PayPal](https://www.paypal.me/dmlaub123)** (dmlaub123)

Note this is not a perfect utility - 1) removing accent marks misspells words but that's far better than having tracks not play at all 2) Kanji characters remain unchanged - if you use FooBar2000 for ripping you can use advanced features in it to Romanize these artist names (like Eiji Oue) - but these advanced Foobar features don't "fix" Cyrillic names (like Rachmaninoff) 3) for a final level of scrubbing the utility MP3tag still remains invaluable for true outliers. 4) You may still have issues with long file names and special characters in directory names. 5) This utility is currently restrict to FLAC & MP3 files only. 6) This project is a collaboration between human & AI sources.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
