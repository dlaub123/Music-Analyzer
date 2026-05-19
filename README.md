# Music File Scrubber

A brief, one-sentence description of what this project does and who it's for.

## 🚀 Features

Why Scrubbing Hidden Tags Matters
Many modern media players, especially audiophile-focused gapless playback systems like Volumio, rely on pristine file integrity to map out audio buffers. Behind the scenes, various music ripping tools, download stores, and editing software inject non-standard metadata, hidden padding blocks, or corrupt ID3 frames into audio headers.
Leaving these unscrubbed causes subtle but frustrating issues:
Broken Gapless Playback: Hidden metadata chunks can confuse the audio decoder at the exact millisecond a track finishes, introducing a tiny pop, click, or a brief gap in live or concept albums.
Library Indexing Crashes: Corrupt or overly large cover art tags, invalid character encodings, and legacy metadata blocks can throw unhandled exceptions during background library scans, causing tracks or entire albums to completely vanish from your player's user interface.
Bloated Network Streams: Extraneous tag data unnecessarily inflates file header sizes, adding latency when streaming high-resolution audio over local Wi-Fi networks to your player.
This utility strips away that hidden digital friction, leaving only the pure audio stream and the essential, standardized tags your player needs.


- **User Authentication:** Secure login and signup.
- **Dark Mode:** Easy on the eyes for night owl developers.
- **Responsive Design:** Works flawlessly on mobile and desktop.

## 🛠️ Tech Stack

**Client:** React, Tailwind CSS
**Server:** Node.js, Express
**Database:** MongoDB

## 📦 Installation

Get the project up and running locally on your machine.

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
