from yt_dlp import YoutubeDL

def get_playlist_videos(url):
    if "list=" not in url:
        print("URL inválida")
        return []

    playlist_id = url.split("list=")[1].split("&")[0]

    ydl_opts = {
        "quiet": True,
        "extract_flat": True
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)

    return [entry["id"] for entry in info["entries"]]