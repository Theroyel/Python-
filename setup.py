from pytube import YouTube

def download_youtube_video():
    raw_url = input("Enter YouTube video URL: ").strip()
    url = raw_url.split('&')[0].split('?')[0]  # clean URL

    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print("Downloading...")

        stream = yt.streams.get_highest_resolution()
        stream.download()
        print("✅ Download completed!")

    except Exception as e:
        print("❌ An error occurred:", e)

download_youtube_video()

