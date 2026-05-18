import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog
import unicodedata
from mutagen.flac import FLAC
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

def clean_text(text):
    """Removes accents/umlauts and flattens special characters to root values (e.g., ü -> u)"""
    if not text:
        return ""
    normalized = unicodedata.normalize('NFD', text)
    return "".join([c for c in normalized if unicodedata.category(c) != 'Mn'])

def safe_open_path(path):
    """Bypasses Windows 260-character path limit (MAX_PATH)"""
    abs_path = os.path.abspath(path)
    if os.name == 'nt' and not abs_path.startswith('\\\\?\\'):
        return '\\\\?\\' + abs_path
    return abs_path

class MusicScrubberApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Music File Scrubber")
        self.root.geometry("750x650")
        
        # Track State Variables
        self.selected_folder = tk.StringVar()
        self.safe_mode = tk.BooleanVar(value=True)
        
        # Section 2: Targeted Metadata Cleaning Options
        self.clean_garbage_tags = tk.BooleanVar(value=True)
        self.flatten_metadata_accents = tk.BooleanVar(value=False)
        
        # Section 3: Filename Cleaning Options
        self.clean_filename_accents = tk.BooleanVar(value=False)
        self.replace_spaces_with_underscores = tk.BooleanVar(value=False)
        
        self.setup_ui()

    def setup_ui(self):
        # 1. Folder Selection Frame
        folder_frame = tk.LabelFrame(self.root, text=" 1. Select Music Folder ", padx=10, pady=10)
        folder_frame.pack(fill="x", padx=15, pady=10)
        
        tk.Entry(folder_frame, textvariable=self.selected_folder, width=60).pack(side="left", padx=5, expand=True, fill="x")
        tk.Button(folder_frame, text="Browse...", command=self.browse_folder).pack(side="left", padx=5)

        # Main Options Splitter
        options_frame = tk.Frame(self.root)
        options_frame.pack(fill="both", expand=True, padx=15, pady=5)

        # 2. Metadata Cleaning Frame
        meta_frame = tk.LabelFrame(options_frame, text=" 2. Metadata Optimization ", padx=10, pady=10)
        meta_frame.pack(fill="x", pady=5)
        
        tk.Checkbutton(meta_frame, text="Scrub hidden tracking, encoder signatures, & comments", variable=self.clean_garbage_tags).pack(anchor="w", pady=2)
        tk.Checkbutton(meta_frame, text="Flatten special characters/umlauts inside tags", variable=self.flatten_metadata_accents).pack(anchor="w", pady=2)

        # 3. Filename Cleaning Frame
        file_frame = tk.LabelFrame(options_frame, text=" 3. Filename Cleaning ", padx=10, pady=10)
        file_frame.pack(fill="x", pady=10)
        
        tk.Checkbutton(file_frame, text="Flatten special characters/umlauts in filenames", variable=self.clean_filename_accents).pack(anchor="w", pady=2)
        tk.Checkbutton(file_frame, text="Replace spaces with Underscores", variable=self.replace_spaces_with_underscores).pack(anchor="w", pady=2)

        # Bottom Control Frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", padx=15, pady=5)
        
        tk.Checkbutton(control_frame, text="Safe Mode (Simulate without changing files)", variable=self.safe_mode, fg="darkgreen", font=("Arial", 10, "bold")).pack(side="left", pady=5)
        
        self.run_btn = tk.Button(control_frame, text="RUN SCRUBBER", bg="#4CAF50", fg="white", font=("Arial", 11, "bold"), padx=5, pady=5, command=self.process_files)
        self.run_btn.pack(side="right", pady=5)

        # Console Output Box with Added Scrollbar
        log_frame = tk.LabelFrame(self.root, text=" Processing Log ")
        log_frame.pack(fill="both", expand=True, padx=15, pady=10)
        
        # 1. Create the scrollbar widget inside the frame
        scrollbar = tk.Scrollbar(log_frame)
        
        # 2. Pack the scrollbar first, filling the vertical Y axis on the right side
        scrollbar.pack(side="right", fill="y")
        
        # 3. Pack the log box next, filling the remaining space on the left
        self.log_box = tk.Text(log_frame, wrap="word", height=14, bg="#1e1e1e", fg="#ffffff", font=("Consolas", 10), yscrollcommand=scrollbar.set)
        self.log_box.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        # 4. Tie them together dynamically
        scrollbar.config(command=self.log_box.yview)
 
        # Setup custom color tags for text formatting
        self.log_box.tag_config('album_header', foreground='#61AFEF', font=('Consolas', 10, 'bold')) # Blue
        self.log_box.tag_config('change_alert', foreground='#E06C75', font=('Consolas', 10, 'bold')) # Red
        self.log_box.tag_config('safe_header', foreground='#98C379', font=('Consolas', 10, 'bold')) # Dark Green
        self.log_box.tag_config('file_line', foreground='#ABB2BF') # Subdued gray

    def browse_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder.set(folder)

    def log_message(self, message, tag=None):
        if tag:
            self.log_box.insert(tk.END, message + "\n", tag)
        else:
            self.log_box.insert(tk.END, message + "\n")
        self.log_box.see(tk.END)
        self.root.update_idletasks()

    def process_files(self):
        target_dir = self.selected_folder.get()
        if not target_dir or not os.path.exists(target_dir):
            messagebox.showerror("Error", "Please select a valid folder first.")
            return

        self.log_box.delete("1.0", tk.END)
        is_safe = self.safe_mode.get()
        
        if is_safe:
            self.log_message("=== RUNNING IN SAFE MODE (No changes will be saved) ===\n", 'safe_header')
        else:
            self.log_message("=== LIVE RUN STARTED ===\n", 'change_alert')

        do_garbage_scrub = self.clean_garbage_tags.get()
        do_meta_flatten = self.flatten_metadata_accents.get()
        do_file_flatten = self.clean_filename_accents.get()
        do_underscores = self.replace_spaces_with_underscores.get()

        last_album_dir = None

        for root_dir, _, files in os.walk(target_dir):
            # Check if we have audio files in this directory before printing a header
            has_audio = any(f.lower().endswith(('.mp3', '.flac', '.m4a', '.ogg', '.wma')) for f in files)
            
            if has_audio and root_dir != last_album_dir:
                # Print a clean layout breaking line separating the new album track path
                self.log_message(f"\n📁 ALBUM DIRECTORY: {root_dir}", 'album_header')
                self.log_message("-" * len(f"📁 ALBUM DIRECTORY: {root_dir}"), 'album_header')
                last_album_dir = root_dir

            for file in files:
                if not file.lower().endswith(('.mp3', '.flac', '.m4a', '.ogg', '.wma')):
                    continue
                
                original_file_path = os.path.join(root_dir, file)
                safe_path = safe_open_path(original_file_path)
                self.log_message(f"  📄 Track: {file}", 'file_line')

                # --- METADATA SCRUBBING ---
                try:
                    modified_tags = False
                    log_entries = []
                    
                    if file.lower().endswith('.flac') and (do_garbage_scrub or do_meta_flatten):
                        audio = FLAC(safe_path)
                        
                        if do_garbage_scrub:
                            for junk_tag in ['comment', 'encoder', 'vendor', 'description', 'copyright']:
                                if junk_tag in audio:
                                    del audio[junk_tag]
                                    modified_tags = True
                                    log_entries.append(f"     [Meta] Removed tracking tag: {junk_tag}")
                                    
                        if do_meta_flatten:
                            for tag in list(audio.keys()):
                                original_vals = list(audio[tag])
                                cleaned_vals = [clean_text(val) for val in original_vals]
                                if cleaned_vals != original_vals:
                                    audio[tag] = cleaned_vals
                                    modified_tags = True
                                    log_entries.append(f"     [Meta Tag '{tag}'] Flatten conversion: '{''.join(original_vals)}' -> '{''.join(cleaned_vals)}'")
                                
                        if modified_tags:
                            for entry in log_entries:
                                self.log_message(entry, 'change_alert')
                            if not is_safe:
                                audio.save()

                    elif file.lower().endswith('.mp3') and (do_garbage_scrub or do_meta_flatten):
                        audio = EasyID3(safe_path)
                        
                        if do_garbage_scrub:
                            for junk_tag in ['comment', 'encodedby', 'website', 'copyright']:
                                if junk_tag in audio:
                                    del audio[junk_tag]
                                    modified_tags = True
                                    log_entries.append(f"     [Meta] Removed tracking tag: {junk_tag}")
                                    
                        if do_meta_flatten:
                            for tag in list(audio.keys()):
                                original_vals = list(audio[tag])
                                cleaned_vals = [clean_text(val) for val in original_vals]
                                if cleaned_vals != original_vals:
                                    audio[tag] = cleaned_vals
                                    modified_tags = True
                                    log_entries.append(f"     [Meta Tag '{tag}'] Flatten conversion: '{''.join(original_vals)}' -> '{''.join(cleaned_vals)}'")
                                
                        if modified_tags:
                            for entry in log_entries:
                                self.log_message(entry, 'change_alert')
                            if not is_safe:
                                audio.save()

                except Exception as e:
                    self.log_message(f"     ❌ Metadata Error: {e}", 'change_alert')

                # --- FILENAME CLEANING WITH VISIBLE TRANSFORMS ---
                new_name = file
                if do_file_flatten:
                    new_name = clean_text(new_name)
                if do_underscores:
                    new_name = new_name.replace(" ", "_")

                if new_name != file:
                    self.log_message(f"     [Rename Target] Cleaned name layout:", 'change_alert')
                    self.log_message(f"     ↳ Before: {file}", 'change_alert')
                    self.log_message(f"     ↳ After:  {new_name}", 'change_alert')
                    
                    if not is_safe:
                        new_file_path = os.path.join(root_dir, new_name)
                        safe_new_path = safe_open_path(new_file_path)
                        try:
                            os.rename(safe_path, safe_new_path)
                        except Exception as e:
                            self.log_message(f"     ❌ Rename Error: {e}", 'change_alert')

        self.log_message("\n=== Processing Complete! ===")
        messagebox.showinfo("Finished", "Scrubber run completed successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicScrubberApp(root)
    root.mainloop()