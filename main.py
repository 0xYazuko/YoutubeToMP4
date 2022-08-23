# Dev By 0xYazuko

from pytube import YouTube # module pytube pour installer la musique

url = input("Insérer un lien youtube: ")


def on_download_progress(stream, chunk, bytes_remaining):
    bytes_downloaded = stream.filesize - bytes_remaining
    percent = bytes_downloaded * 100 / stream.filesize

    print(f"Progression du téléchargement {int(percent)}%")



youtube_video = YouTube(url)

youtube_video.register_on_progress_callback(on_download_progress)

print("TITRE: " + youtube_video.title)
print("NB VUES:", youtube_video.views)

print("STREAMS")
for stream in youtube_video.streams.fmt_streams:
    print("  ", stream)

# stream = youtube_video.streams.get_by_itag(18)
stream = youtube_video.streams.get_highest_resolution() # obtiens la plus haute résolution possible
print("Steam vidéo: ", stream)
print("Téléchargement...")
stream.download()
print(youtube_video.title + "a bien été installée")
