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
        "https://youtu.be/v4sCCVinN-U",
        "https://youtu.be/owe9cPEdm7k",
        "https://youtu.be/PJYWANz2-fA",
        "https://youtube.com/playlist?list=PLP1Z3Rf9MJpD55AHHGXgfKwmiKB6dUzRo",
        "https://youtube.com/playlist?list=PLP1Z3Rf9MJpCPL2jm8uZ-uzt51eJOYoF8",
        "https://youtube.com/playlist?list=PLZdXRHYAVxTIVkiqT5N9IHcX5I4y7vCNp",
        "https://youtube.com/c/WhatIfScienceShow",
        "https://youtube.com/channel/UCJ_dsa5WPjwNGK8PLnB18Bw",
        "https://youtube.com/c/WatchDataVerified",
        "https://youtube.com/c/TallyStat",
        "https://youtube.com/c/reigarw",
        "https://youtube.com/channel/UC1wjrBtYqZtC3HeQydqZscA",
        "https://www.youtube.com/watch?v=aKOJGzNEnlc",
        "https://www.youtube.com/watch?v=AhAay4FT-nE",
        "https://www.youtube.com/watch?v=B1ouIlaGlQg",
        "https://www.youtube.com/watch?v=7qz9E4KUJ4w",
        "https://www.youtube.com/watch?v=DVQ29IkEmM0",
        "https://www.youtube.com/playlist?list=PLXXRE-F0fw2XVppL6w1g2f_m1h9Wy7rX8",
        "https://www.youtube.com/playlist?list=PLP1Z3Rf9MJpA2qFI3nCK3kca7upsRI1ZE",
        "https://www.youtube.com/channel/UCJ_dsa5WPjwNGK8PLnB18Bw",
        "https://www.youtube.com/channel/UCL2hOcfXAxD44bGz0JIf-dA",
        "https://www.youtube.com/channel/UC4R8DWoMoI7CAwX8_LjQHig",
        "https://www.youtube.com/watch?v=LHqvDyC1uVQ&list=PLXXRE-F0fw2XVppL6w1g2f_m1h9Wy7rX8",
        "https://www.youtube.com/watch?v=62o7Qwnnnh0&list=PLP1Z3Rf9MJpA2qFI3nCK3kca7upsRI1ZE"
    ]

    for link in links:
        link_type, link_id = classify_youtube_link(link)
        print(f"Link: {link}\nType: {link_type}\nID: {link_id}\n")

if __name__ == "__main__":
    main()