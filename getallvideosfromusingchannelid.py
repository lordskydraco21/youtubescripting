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

def get_all_videos_from_channel(channel_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )
    response = request.execute()
    log_response(response)
    
    videos = []
    while request is not None:
        response = request.execute()
        log_response(response)
        videos += response.get("items", [])
        request = youtube.search().list_next(request, response)
    
    return videos

channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Replace with your channel ID
videos = get_all_videos_from_channel(channel_id)
print(f"Total videos found: {len(videos)}")
for video in videos:
    if video["id"]["kind"] == "youtube#video":
        print(f"Title: {video['snippet']['title']}, Video ID: {video['id']['videoId']}")