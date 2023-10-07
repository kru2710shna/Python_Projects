from pytube import YouTube

# Create a YouTube object by providing the video URL
link = "https://www.youtube.com/watch?v=Z_ikDlimN6A"

youtube_1 = YouTube(link)

#print(youtube_1.title)
# Choose the stream (resolution and format) you want to download
#print(youtube_1.thumbnail_url)
videos = youtube_1.streams.all() # all format
#videos = youtube_1.streams.filter(only_audio = True)
vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter: "))
videos[strm].download()
print("Video downloaded successfully!")
