import yt_dlp

urls = []

output_path = ''


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'outtmpl': output_path + '%(title)s.%(ext)s',
    'quiet': True,
    'ffmpeg_location': r'C:\Users\vale3\OneDrive\Desktop\dataset\chocolatey\bin',
}

failed = []
success = []

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in urls:
        try:
            ydl.download([url])
            print("Downloaded:", url)
            success.append(url)
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            failed.append(url)

print("Download failed:", failed)
print("Successfully downloaded:", success)
