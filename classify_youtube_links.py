import re

def classify_youtube_link(link):
    video_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:m\.)?youtube\.com\/watch\?v=([a-zA-Z0-9_-]+)"
    short_video_pattern = r"(?:https?:\/\/)?(?:www\.)?youtu\.be\/([a-zA-Z0-9_-]+)"
    playlist_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:m\.)?youtube\.com\/playlist\?list=([a-zA-Z0-9_-]+)"
    channel_pattern = r"(?:https?:\/\/)?(?:www\.)?(?:m\.)?youtube\.com\/channel\/([a-zA-Z0-9_-]+)"
    custom_channel_pattern = r"(?:https?:\/\/)?(?:www\.)?youtube\.com\/c\/([a-zA-Z0-9_-]+)"

    video_match = re.match(video_pattern, link)
    short_video_match = re.match(short_video_pattern, link)
    playlist_match = re.match(playlist_pattern, link)
    channel_match = re.match(channel_pattern, link)
    custom_channel_match = re.match(custom_channel_pattern, link)

    if video_match:
        return "video", video_match.group(1)
    elif short_video_match:
        return "video", short_video_match.group(1)
    elif playlist_match:
        return "playlist", playlist_match.group(1)
    elif channel_match:
        return "channel", channel_match.group(1)
    elif custom_channel_match:
        return "channel", custom_channel_match.group(1)
    else:
        return "unknown", None

def main():
    links = [
        "https://m.youtube.com/watch?v=TV2F06Pd-Dg",
        "https://m.youtube.com/watch?v=s1J-DB2P4uU",
        "https://m.youtube.com/watch?v=sW9npZVpiMI",
        "https://m.youtube.com/playlist?list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK",
        "https://m.youtube.com/playlist?list=PLdPBL8cOjdzWQOdmxe6jhA5bhiKtxW0Oj",
        "https://m.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg",
        "https://m.youtube.com/channel/UCCWp4CCmI2JmIaoAuv0ocEA",
        "https://m.youtube.com/channel/UCOsM-xMGrGH0RHffLIznrUA",
        "https://m.youtube.com/channel/UCMrs06HEf3eTsPQBNAYa9qQ",
        "https://m.youtube.com/watch?v=k9TUPpGqYTo&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=2",
        "https://m.youtube.com/watch?v=Ozrduu2W9B8&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=1",
        "https://m.youtube.com/watch?v=2Rf01wfbQLk&list=PL4cUxeGkcC9idu6GZ8EU_5B6WpKTdYZbK&index=29",
        "https://m.youtube.com/watch?v=mqhxxeeTbu0&list=PLdPBL8cOjdzWQOdmxe6jhA5bhiKtxW0Oj&index=11",
        "https://youtu.be/dRcs98Zmfi4",
        "https://youtu.be/4EgOR8ALCHE",
        "https://youtu.be/Mpf4ntp0YJs",
        "https://youtu.be/v4sCCVinN-"
    ]
link = str(input("Enter a YouTube link: "))
link_type, link_id = classify_youtube_link(link)
print(f"Link: {link}\nType: {link_type}\nID: {link_id}\n")

if __name__ == "__main__":
    main()