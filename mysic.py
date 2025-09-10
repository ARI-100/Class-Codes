import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Global variables
playlist = []
current_index = 0
is_paused = False

def add_songs():
    global playlist
    files = filedialog.askopenfilenames(
        title="Select Songs",
        filetypes=[("MP3 Files", "*.mp3")]
    )
    for file in files:
        playlist.append(file)
        playlist_box.insert(tk.END, os.path.basename(file))

def play_song():
    global current_index, is_paused
    if playlist:
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
            status_label.config(text="Resumed: " + os.path.basename(playlist[current_index]))
        else:
            song = playlist[current_index]
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            status_label.config(text="Playing: " + os.path.basename(song))

def pause_song():
    global is_paused
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
        is_paused = True
        status_label.config(text="Paused")

def stop_song():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

def next_song():
    global current_index
    if playlist:
        current_index = (current_index + 1) % len(playlist)
        play_song()

def prev_song():
    global current_index
    if playlist:
        current_index = (current_index - 1) % len(playlist)
        play_song()

# GUI Setup
root = tk.Tk()
root.title("Python Music Player")
root.geometry("500x400")

playlist_box = tk.Listbox(root, width=60, height=10)
playlist_box.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

tk.Button(btn_frame, text="Add Songs", command=add_songs, width=10).grid(row=0, column=0, padx=2)
tk.Button(btn_frame, text="Play", command=play_song, width=10).grid(row=0, column=1, padx=2)
tk.Button(btn_frame, text="Pause", command=pause_song, width=10).grid(row=0, column=2, padx=2)
tk.Button(btn_frame, text="Stop", command=stop_song, width=10).grid(row=0, column=3, padx=2)
tk.Button(btn_frame, text="Prev", command=prev_song, width=10).grid(row=0, column=4, padx=2)
tk.Button(btn_frame, text="Next", command=next_song, width=10).grid(row=0, column=5, padx=2)

status_label = tk.Label(root, text="Welcome to Music Player", relief=tk.SUNKEN, anchor="w")
status_label.pack(fill=tk.X, pady=5)

root.mainloop()