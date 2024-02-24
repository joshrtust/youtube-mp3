import youtube_dl
from youtube_dl.utils import RegexNotFoundError

def download_video(link, output_path):
    options = {
    'format': 'bestaudio',
    'outtmpl': output_path + '/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,  # Set quiet to False for more verbose output
    'headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    },
    #'youtube_include_dash_manifest': False,  # Add this line to disable DASH manifest
    #'no_check_certificate': True,  # Add this line to disable SSL certificate verification
}

    with youtube_dl.YoutubeDL(options) as ydl:
        try:
            ydl.download([link])
        except RegexNotFoundError as e:
            print(f"RegexNotFoundError: {e}. Continuing with the download.")

def main():
    link = input("Enter the YouTube video link: ")
    output_path = input("Enter the output directory (leave blank for the current directory): ") or '.'

    try:
        download_video(link, output_path)
        print("Download complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()