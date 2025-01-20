import re
import argparse

def classify_youtube_link(link):
    video_pattern = r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)"
    channel_pattern = r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/channel\/([a-zA-Z0-9_-]+)"
    playlist_pattern = r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/playlist\?list=([a-zA-Z0-9_-]+)"
    
    video_match = re.match(video_pattern, link)
    channel_match = re.match(channel_pattern, link)
    playlist_match = re.match(playlist_pattern, link)
    
    if video_match:
        return "video", video_match.group(1)
    elif channel_match:
        return "channel", channel_match.group(1)
    elif playlist_match:
        return "playlist", playlist_match.group(1)
    else:
        return "unknown", None

def main():
    parser = argparse.ArgumentParser(description="Classify YouTube links and extract their IDs.")
    parser.add_argument("link", nargs='?', help="The YouTube link to classify.")
    args = parser.parse_args()

    if args.link:
        link = args.link
    else:
        link = input("Enter a YouTube link: ")

    link_type, link_id = classify_youtube_link(link)
    print(f"Link: {link}\nType: {link_type}\nID: {link_id}")

if __name__ == "__main__":
    main()