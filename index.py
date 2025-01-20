import os
from googleapiclient.discovery import build
import json

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("No API key provided. Please set the YOUTUBE_API_KEY environment variable.")

def log_response(response):
    with open("log.txt", "a") as log_file:
        log_file.write(json.dumps(response, indent=4))
        log_file.write("\n")

def get_channel_id_from_video_id(video_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.videos().list(part="snippet", id=video_id)
    response = request.execute()
    log_response(response)
    
    if "items" in response and len(response["items"]) > 0:
        channel_id = response["items"][0]["snippet"]["channelId"]
        return channel_id
    else:
        raise ValueError("No video found with the provided video ID.")

video_id = "dQw4w9WgXcQ"  # Replace with your video ID
channel_id = get_channel_id_from_video_id(video_id)
print(f"Channel ID: {channel_id}")