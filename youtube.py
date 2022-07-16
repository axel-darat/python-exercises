from pytube import YouTube

video_url = input("Insert the URL:")
youtube = pytube.YouTube(video_url)
video = youtube.streams.first()
video.download('Downloads')