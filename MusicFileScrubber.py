import os

#import tkinter as tk
#from tkinter import filedialog, messagebox, ttk

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog

ttk.BooleanVar = tk.BooleanVar
ttk.StringVar = tk.StringVar

from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
from mutagen.flac import FLAC
from mutagen.oggvorbis import OggVorbis

class MusicScrubberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Audio Metadata & File Scrubber")
        self.root.geometry("650x500")
        self.root.minsize(550, 400)

        # Variables
        self.selected_folder = tk.StringVar()
        self.safe_mode = tk.BooleanVar(value=True)  # Safe Mode defaults to ON
        
        # Metadata Toggles
        self.clean_title = tk.BooleanVar(value=False)
        self.clean_artist = tk.BooleanVar(value=False)
        self.clean_album = tk.BooleanVar(value=False)
        self.clean_genre = tk.BooleanVar(value=False)
        
        # Filename Toggles
        self.replace_spaces = tk.BooleanVar(value=False)
        self.lowercase_names = tk.BooleanVar(value=False)
        self.remove_special = tk.BooleanVar(value=False)

        self.setup_ui()

    def setup_ui(self):
        # --- Folder Selection ---
        folder_frame = tk.LabelFrame(self.root, text=" 1. Select Music Folder ", padx=10, pady=10)
        folder_frame.pack(fill="x", padx=15, pady=10)

        tk.Entry(folder_frame, textvariable=self.selected_folder, width=50).pack(side="left", expand=True, fill="x", padx=(0, 10))
        tk.Button(folder_frame, text="Browse...", command=self.browse_folder).pack(side="right")

        # --- Options Frame ---
        options_frame = tk.Frame(self.root)
        options_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # Metadata Options
        meta_frame = tk.LabelFrame(options_frame, text=" 2. Metadata Scrubbing (Wipe Fields) ", padx=10, pady=10)
        meta_frame.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        tk.Checkbutton(meta_frame, text="Wipe Title", variable=self.clean_title).pack(anchor="w", pady=2)
        tk.Checkbutton(meta_frame, text="Wipe Artist", variable=self.clean_artist).pack(anchor="w", pady=2)
        tk.Checkbutton(meta_frame, text="Wipe Album", variable=self.clean_album).pack(anchor="w", pady=2)
        tk.Checkbutton(meta_frame, text="Wipe Genre/Others", variable=self.clean_genre).pack(anchor="w", pady=2)

        # Filename Options
        file_frame = tk.LabelFrame(options_frame, text=" 3. Filename Cleaning ", padx=10, pady=10)
        file_frame.pack(side="right", fill="both", expand=True, padx=(5, 0))

        tk.Checkbutton(file_frame, text="Replace Spaces with Under_scores", variable=self.replace_spaces).pack(anchor="w", pady=2)
        tk.Checkbutton(file_frame, text="Convert to lowercase", variable=self.lowercase_names).pack(anchor="w", pady=2)
        tk.Checkbutton(file_frame, text="Remove Special Characters", variable=self.remove_special).pack(anchor="w", pady=2)

        # --- Execution & Mode Controls ---
        control_frame = tk.LabelFrame(self.root, text=" 4. Mode & Execution ", padx=10, pady=10)
        control_frame.pack(fill="x", padx=15, pady=15)

        # Safe Mode Toggle Configuration
        safe_mode_cb = tk.Checkbutton(
            control_frame, 
            text="SAFE MODE (Simulation Only - No files will be modified)", 
            variable=self.safe_mode,
            font=("Arial", 10, "bold"),
            fg="darkgreen"
        )
        safe_mode_cb.pack(anchor="w", pady=5)
        
        # Visual indicator listener for safe mode
        self.safe_mode.trace_add("write", self.update_mode_style)
        self.safe_mode_label = tk.Label(control_frame, text="Status: Ready to simulate.", fg="green")
        self.safe_mode_label.pack(anchor="w", pady=(0, 5))

        # Run Button
        self.run_btn = tk.Button(control_frame, text="RUN SCRUBBER", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), padx=5, pady=5, command=self.process_files)
        self.run_btn.pack(fill="x", pady=5)

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder.set(folder)

    def update_mode_style(self, *args):
        if self.safe_mode.get():
            self.safe_mode_label.config(text="Status: Ready to simulate.", fg="green")
            self.run_btn.config(text="RUN SIMULATION (SAFE MODE)", bg="#4CAF50")
        else:
            self.safe_mode_label.config(text="WARNING: Live mode selected. Changes will be permanent!", fg="red")
            self.run_btn.config(text="COMMIT ACTUAL CHANGES", bg="#d32f2f")

    def clean_filename(self, filename):
        name, ext = os.path.splitext(filename)
        
        if self.replace_spaces.get():
            name = name.replace(" ", "_")
        if self.lowercase_names.get():
            name = name.lower()
        if self.remove_special.get():
            # Keeps alphanumeric characters, underscores, and hyphens
            name = "".join(c for c in name if c.isalnum() or c in ('_', '-'))
            
        return f"{name}{ext}"

    def scrub_metadata(self, file_path):
        # Supported extensions by mutagen handlers used here
        ext = os.path.splitext(file_path)[1].lower()
        try:
            if ext == '.mp3':
                try:
                    audio = EasyID3(file_path)
                except Exception:
                    # If no ID3 tag exists, create one
                    audio = MP3(file_path, ID3=EasyID3)
                    audio.add_tags()
            elif ext == '.flac':
                audio = FLAC(file_path)
            elif ext in ['.ogg', '.oga']:
                audio = OggVorbis(file_path)
            else:
                return False # Unsupported format
            
            # Wipe tags if checkboxes are checked
            if self.clean_title.get() and 'title' in audio: del audio['title']
            if self.clean_artist.get() and 'artist' in audio: del audio['artist']
            if self.clean_album.get() and 'album' in audio: del audio['album']
            if self.clean_genre.get():
                for tag in ['genre', 'date', 'tracknumber', 'comment']:
                    if tag in audio: del audio[tag]
            
            if not self.safe_mode.get():
                audio.save()
            return True
        except Exception as e:
            print(f"Error processing metadata for {file_path}: {e}")
            return False

    def process_files(self):
        dir_path = self.selected_folder.get()
        if not dir_path or not os.path.isdir(dir_path):
            messagebox.showerror("Error", "Please select a valid directory first.")
            return

        is_safe = self.safe_mode.get()
        log_report = []
        files_processed = 0

        # Supported audio formats
        valid_extensions = ('.mp3', '.flac', '.ogg', '.oga')

        for root_dir, _, files in os.walk(dir_path):
            for file in files:
                if file.lower().endswith(valid_extensions):
                    files_processed += 1
                    current_path = os.path.join(root_dir, file)
                    
                    # 1. Metadata updates
                    meta_status = self.scrub_metadata(current_path)
                    
                    # 2. Filename updates
                    new_name = self.clean_filename(file)
                    new_path = os.path.join(root_dir, new_name)
                    
                    rename_happened = False
                    if new_name != file:
                        rename_happened = True
                        if not is_safe:
                            os.rename(current_path, new_path)
                    
                    # Log the actions
                    action_desc = f"File: {file}\n"
                    if meta_status:
                        action_desc += "   - Metadata Wiped (matching settings)\n"
                    if rename_happened:
                        action_desc += f"   - Renamed to: {new_name}\n"
                    if not meta_status and not rename_happened:
                        action_desc += "   - No changes required.\n"
                        
                    log_report.append(action_desc)

        if files_processed == 0:
            messagebox.showinfo("Done", "No compatible music files found (.mp3, .flac, .ogg).")
            return

        # Show results window
        report_window = tk.Toplevel(self.root)
        report_window.title("Simulation Report" if is_safe else "Execution Report")
        report_window.geometry("500x400")
        
        title_text = f"--- {'SIMULATION ONLY' if is_safe else 'ACTUAL CHANGES COMMITTED'} ---"
        tk.Label(report_window, text=title_text, font=("Arial", 12, "bold"), fg="blue" if is_safe else "red").pack(pady=10)
        
        text_area = tk.Text(report_window, wrap="word")
        scroll = tk.Scrollbar(report_window, command=text_area.yview)
        text_area.configure(yscrollcommand=scroll.set)
        
        scroll.pack(side="right", fill="y")
        text_area.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        
        text_area.insert("end", f"Total music files analyzed: {files_processed}\n\n")
        text_area.insert("end", "\n".join(log_report))
        text_area.configure(state="disabled") # Make read-only

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicScrubberApp(root)
    root.mainloop()