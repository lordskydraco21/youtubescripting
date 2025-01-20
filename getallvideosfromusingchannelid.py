import os
from googleapiclient.discovery import build
import json
from datetime import datetime

API_KEY = os.getenv("YOUTUBE_API_KEY")

if not API_KEY:
    raise ValueError("No API key provided. Please set the YOUTUBE_API_KEY environment variable.")

def log_response(response, log_file_name):
    with open(log_file_name, "a") as log_file:
        log_file.write(json.dumps(response, indent=4))
        log_file.write("\n")

def get_channel_name(channel_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.channels().list(part="snippet", id=channel_id)
    response = request.execute()
    if "items" in response and len(response["items"]) > 0:
        return response["items"][0]["snippet"]["title"]
    else:
        raise ValueError("No channel found with the provided channel ID.")

def get_all_videos_from_channel(channel_id):
    youtube = build("youtube", "v3", developerKey=API_KEY)
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=50,
        order="date"
    )
    videos = []
    while request is not None:
        response = request.execute()
        videos += response.get("items", [])
        request = youtube.search().list_next(request, response)
    
    return videos

channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Replace with your channel ID
channel_name = get_channel_name(channel_id)
videos = get_all_videos_from_channel(channel_id)
video_count = len(videos)
current_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file_name = f"logs/{channel_name}_{video_count}_{current_datetime}.txt"

os.makedirs("logs", exist_ok=True)
log_response({"videos": videos}, log_file_name)

print(f"Total videos found: {video_count}")
for video in videos:
    if video["id"]["kind"] == "youtube#video":
        print(f"Title: {video['snippet']['title']}, Video ID: {video['id']['videoId']}")