# Music File Scrubber

A utility that cleans up music files so they're not skipped/ignored, play in the correct order and display properly with track # and title when copied from one OS to another.

## 🚀 Features

Music File Scrubber
- A lightweight, single-file Python utility designed to clean, standardize, and scrub audio file metadata and filenames for a pristine, seamless local media library. Tested and verified for compatibility with Volumio gapless playback servers.
- Features
  - Metadata Cleansing: Strips problematic, corrupt, or non-standard tags that cause indexing issues in local music players.
  - Smart Filename Renaming: Standardizes file naming conventions for clean sorting without breaking album structures.
  - Dry-Run Safety: Features a robust "Safe Mode" allowing you to verify exactly what changes will be made before a single file is altered on disk.
  - Volumio Tested: In extensive testing has not interrupted gapless playback sequences or triggered library scanning exceptions.

- Real-World Example (32GB USB Drive Run)
To see exactly how the script behaves under pressure, check out the included sample_run_log.txt.
This log shows a real execution against a 32GB music library running in both modes:
Safe Mode: The initial dry-run assessment that generates a non-destructive preview of changes.
"Commit" Mode: The actual execution where the files are safely updated on disk based on the verified logs.
- Support the Project - If this utility helped clean up your music library or saved you hours of manual tagging, consider supporting ongoing development:
  xxx
- License: This project is licensed under the MIT License - see the LICENSE file for details.
- Screenshot of GUI: xxx
- Processing Log (Safe Mode): xxx
- Processing Log (Commit mode): xxx

- Many modern media players, especially audiophile-focused gapless playback systems like Volumio, rely on pristine file integrity to map out audio buffers. Behind the scenes, various music ripping tools, download stores, and editing software inject non-standard metadata, hidden padding blocks, or corrupt ID3 frames into audio headers.
- This utility strips away that hidden digital "friction", leaving only the pure audio stream and the essential, standardized tags your player needs.

## 🛠️ Tech Stack
Python 3.10 or higher

## 📦 Installation

Clone the repository and run the script directly from the root folder:
- git clone https://github.com/dlaub123/Music-Analyzer.git
- cd music-file-scrubber
- python MusicFileScrubber.py
