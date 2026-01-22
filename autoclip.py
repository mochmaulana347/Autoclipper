# Simpan sebagai: scripts/autoclip.py
import os
import subprocess

def process_video(url):
    print(f"Men-download video dari: {url}")
    # 1. Download video pakai yt-dlp
    os.system(f"yt-dlp -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4' {url} -o input_video.mp4")

    # 2. Proses potong & crop jadi Vertikal (9:16) pakai FFmpeg
    # Mengambil detik ke 30 selama 15 detik sebagai contoh
    cmd = [
        'ffmpeg', '-i', 'input_video.mp4',
        '-ss', '00:00:30', '-t', '15',
        '-vf', "crop=ih*(9/16):ih,scale=1080:1920",
        '-c:v', 'libx264', '-crf', '23', 'output_reels.mp4'
    ]
    subprocess.run(cmd)
    print("Video berhasil dibuat!")

if __name__ == "__main__":
    # URL diambil dari input GitHub Action
    import sys
    video_url = sys.argv[1]
    process_video(video_url)