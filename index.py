import os
from googleapiclient.discovery import build

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("No API key provided. Please set the YOUTUBE_API_KEY environment variable.")

def get_channel_id_from_video_id(video_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    
    if "items" in response and len(response["items"]) > 0:
        channel_id = response["items"][0]["snippet"]["channelId"]
        return channel_id
    else:
        raise ValueError("No video found with the provided video ID.")

video_id = "YOUR_VIDEO_ID_HERE"  # Replace with your video ID
channel_id = get_channel_id_from_video_id(video_id)
print(f"Channel ID: {channel_id}")