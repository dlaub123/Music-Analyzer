# Music File Scrubber

A utility that cleans up music files so they're not skipped/ignored, play in the correct order and display properly with track # and title when copied from one OS to another.

## 🚀 Features

A lightweight, single-file Python utility designed to clean, standardize, and scrub audio file metadata and filenames for a pristine, seamless local media library. Tested and verified for compatibility with Volumio gapless playback servers.

* **Metadata Cleansing:** Strips problematic, corrupt, or non-standard tags that cause indexing issues in local music players.
* **Smart Filename Renaming:** Standardizes file naming conventions for clean sorting without breaking album structures.
* **Dry-Run Safety:** Features a robust "Safe Mode" allowing you to verify exactly what changes will be made before a single file is altered on disk.
* **Volumio Tested:** In extensive testing has not interrupted gapless playback sequences or triggered library scanning exceptions.

### 📊 Real-World Example (32GB USB Drive Run)
To see exactly how the script behaves under pressure, check out the execution logs:
* [Processing Log (Safe Mode)](ProcessingLogSafeMode.txt) - The initial dry-run assessment that generates a non-destructive preview of changes.
* [Processing Log (Commit Mode)](ProcessingLogChangeMode.txt) - The actual execution where the files are safely updated on disk based on the verified logs.

### 🖼️ Interface Preview
![Music File Scrubber GUI](Screenshot%202026-05-17%20173638.png)

---

### 🔍 Why This Matters
Many modern media players, especially audiophile-focused gapless playback systems like Volumio, rely on pristine file integrity to map out audio buffers. Behind the scenes, various music ripping tools, download stores, and editing software inject non-standard metadata, hidden padding blocks, or corrupt ID3 frames into audio headers.

This utility strips away that hidden digital "friction", leaving only the pure audio stream and the essential, standardized tags your player needs.

---

## 🛠️ Tech Stack

* Python 3.10 or higher

## 📦 Installation

Clone the repository and run the script directly from the root folder:

```bash
git clone [https://github.com/dlaub123/Music-Analyzer.git](https://github.com/dlaub123/Music-Analyzer.git)
cd Music-Analyzer
python MusicFileScrubber.py

