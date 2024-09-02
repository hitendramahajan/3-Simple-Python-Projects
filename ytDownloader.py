from pytube import YouTube
import argparse

parser = argparse.ArgumentParser(
    description='A sample Argument Parser.'
)
parser.add_argument('-u',
                    '--url',
                    nargs='?',
                    # const='https://www.youtube.com/watch?v=Wnr8LRO7CiA',
                    default='https://www.youtube.com/watch?v=Wnr8LRO7CiA',
                    type=str
                    )

args = parser.parse_args()

print(args.url)

try:
    # Ask the user to input the YouTube URL
    # url = input("Enter the YouTube URL: ")
    url = args.url
    yt = YouTube(url)
    
    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()
    
    # Download the video to the current directory
    yd.download()
    
    print("Download complete.")
except Exception as e:
    print("An error occurred:", str(e))
