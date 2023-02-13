import youtube_dl


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}


def download_music(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
