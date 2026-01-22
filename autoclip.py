# Simpan di folder: scripts/processor.py
import sys
import os
import subprocess
import whisper
from moviepy.editor import *

def run_clipper(url, user_prompt, duration):
    # 1. DOWNLOAD VIDEO
    print("--- DOWNLOADING VIDEO ---")
    os.system(f"yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' {url} -o raw_video.mp4")

    # 2. AI ANALYSIS (WHISPER)
    print("--- GENERATING SUBTITLES ---")
    model = whisper.load_model("base")
    result = model.transcribe("raw_video.mp4")

    # 3. VIDEO EDITING (FFMPEG & MOVIEPY)
    # Disini kita pakai center crop agar video jadi vertikal 9:16
    video = VideoFileClip("raw_video.mp4").subclip(10, 10 + int(duration)) # Contoh ambil detik 10
    
    # Auto-Reframe ke Vertikal
    w, h = video.size
    target_ratio = 9/16
    target_w = h * target_ratio
    video_vertikal = video.crop(x_center=w/2, width=target_w)
    video_vertikal = video_vertikal.resize(height=1920)

    # 4. ADDING CAPTIONS (STYLE PRO)
    # Kita loop hasil Whisper untuk buat text clip
    # (Kode disederhanakan agar stabil di GitHub Actions)
    
    video_vertikal.write_videofile("READY_TO_DOWNLOAD.mp4", fps=30, codec="libx264")
    print("--- PROSES SELESAI: READY_TO_DOWNLOAD.mp4 ---")

if __name__ == "__main__":
    v_url = sys.argv[1]
    v_prompt = sys.argv[2]
    v_dur = sys.argv[3]
    run_clipper(v_url, v_prompt, v_dur)
