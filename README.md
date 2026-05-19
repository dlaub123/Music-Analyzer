# Music File Scrubber

A single file python GUI utility that cleans up music files so they're not skipped/ignored, play in the correct order and display properly with track # and title when copied from one OS to another.

## 🚀 Features

Music File Scrubber
- A lightweight, single-file Python utility designed to clean, standardize, and scrub audio file metadata and filenames for a pristine, seamless local media library. Tested and verified for compatibility with Volumio gapless playback servers.
- Features
  - Metadata Cleansing: Strips problematic, corrupt, or non-standard tags that cause indexing issues in local music players.
  - Smart Filename Renaming: Standardizes file naming conventions for clean sorting without breaking album structures.
  - Dry-Run Safety: Features a robust "Safe Mode" allowing you to verify exactly what changes will be made before a single file is altered on disk.
  - Volumio Tested: In extensive testing has not interrupted gapless playback sequences or triggered library scanning exceptions.
  - Quick Start
- Prerequisites
Python 3.10 or higher
- Installation & Run
Clone the repository and run the script directly from the root folder:
git clone https://github.com/yourusername/music-file-scrubber.git
cd music-file-scrubber
python main.py

- Real-World Example (32GB USB Drive Run)
To see exactly how the script behaves under pressure, check out the included sample_run_log.txt.
This log shows a real execution against a 32GB music library running in both modes:
Safe Mode: The initial dry-run assessment that generates a non-destructive preview of changes.
"Commit" Mode: The actual execution where the files are safely updated on disk based on the verified logs.
- Support the Project
- If this utility helped clean up your music library or saved you hours of manual tagging, consider supporting ongoing development:
Buy Me A Coffee
- License
This project is licensed under the MIT License - see the LICENSE file for details.

- Many modern media players, especially audiophile-focused gapless playback systems like Volumio, rely on pristine file integrity to map out audio buffers. Behind the scenes, various music ripping tools, download stores, and editing software inject non-standard metadata, hidden padding blocks, or corrupt ID3 frames into audio headers.
Leaving these unscrubbed causes subtle but frustrating issues:
Broken Gapless Playback: Hidden metadata chunks can confuse the audio decoder at the exact millisecond a track finishes, introducing a tiny pop, click, or a brief gap in live or concept albums.
Library Indexing Crashes: Corrupt or overly large cover art tags, invalid character encodings, and legacy metadata blocks can throw unhandled exceptions during background library scans, causing tracks or entire albums to completely vanish from your player's user interface.
Bloated Network Streams: Extraneous tag data unnecessarily inflates file header sizes, adding latency when streaming high-resolution audio over local Wi-Fi networks to your player.
This utility strips away that hidden digital "friction", leaving only the pure audio stream and the essential, standardized tags your player needs.

## 🛠️ Tech Stack

## 📦 Installation

Get the project up and running locally on your machine.

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
