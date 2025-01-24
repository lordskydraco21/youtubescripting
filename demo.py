# Replace with your YouTube Data API key
import re
import requests
import json
import os
import time
from tqdm import tqdm  # For progress bars

# Replace with your YouTube Data API key
API_KEY = "AIzaSyDi-LpZo5ULSVY3ZcS9gb8Errn-JCgrugQ"

# Base URL for YouTube Data API v3
BASE_URL = "https://www.googleapis.com/youtube/v3/"

# Output directory to save JSON files
OUTPUT_DIR = "youtube_data"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_video_id(video_url):
    """
    Extract the video ID from a YouTube video link using regex.
    """
    # Regex to match YouTube video URLs
    regex = r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/watch\?v=|youtu\.be\/)([a-zA-Z0-9_-]{11})"
    match = re.search(regex, video_url)
    if match:
        return match.group(1)
    else:
        raise ValueError("Invalid YouTube video URL")

def fetch_data(endpoint, params):
    """
    Fetch data from the YouTube Data API.
    """
    url = BASE_URL + endpoint
    params["key"] = API_KEY
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def save_data(data, filename):
    """
    Save JSON data to a file.
    """
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {filepath}")

def get_channel_id(video_id):
    """
    Fetch the channel ID associated with a video using the YouTube Data API.
    """
    params = {
        "part": "snippet",
        "id": video_id
    }
    data = fetch_data("videos", params)
    if data and data["items"]:
        return data["items"][0]["snippet"]["channelId"]
    else:
        raise ValueError("No video found with the given ID")

def fetch_channel_videos(channel_id):
    """
    Fetch all videos from a channel using the uploads playlist.
    """
    # Fetch uploads playlist ID
    channel_params = {
        "part": "contentDetails",
        "id": channel_id
    }
    channel_data = fetch_data("channels", channel_params)
    if not channel_data or not channel_data["items"]:
        raise ValueError("No channel found with the given ID")

    uploads_playlist_id = channel_data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    # Fetch all videos from the uploads playlist
    videos = []
    next_page_token = None
    total_videos = 0

    print("Fetching video list from the uploads playlist...")
    start_time = time.time()

    with tqdm(desc="Fetching videos", unit="videos") as pbar:
        while True:
            playlist_params = {
                "part": "snippet",
                "playlistId": uploads_playlist_id,
                "maxResults": 50,  # Maximum allowed by API
                "pageToken": next_page_token
            }
            playlist_data = fetch_data("playlistItems", playlist_params)
            if not playlist_data:
                break

            videos.extend(playlist_data["items"])
            total_videos = len(videos)
            pbar.update(len(playlist_data["items"]))
            next_page_token = playlist_data.get("nextPageToken")

            if not next_page_token:
                break

    elapsed_time = time.time() - start_time
    print(f"Fetched {total_videos} videos in {elapsed_time:.2f} seconds.")

    save_data(videos, "channel_videos.json")

    # Fetch detailed information for each video
    fetch_video_details(videos)

def fetch_video_details(videos):
    """
    Fetch details for a list of videos.
    """
    video_ids = [item["snippet"]["resourceId"]["videoId"] for item in videos]
    video_details = []
    total_videos = len(video_ids)

    print("Fetching detailed information for each video...")
    start_time = time.time()

    with tqdm(total=total_videos, desc="Fetching video details", unit="videos") as pbar:
        for i in range(0, total_videos, 50):  # Process 50 videos at a time (API limit)
            batch = video_ids[i:i + 50]
            video_params = {
                "part": "snippet,statistics,contentDetails",
                "id": ",".join(batch)
            }
            video_data = fetch_data("videos", video_params)
            if video_data:
                video_details.extend(video_data["items"])
            pbar.update(len(batch))

    elapsed_time = time.time() - start_time
    print(f"Fetched details for {total_videos} videos in {elapsed_time:.2f} seconds.")

    save_data(video_details, "video_details.json")

if __name__ == "__main__":
    # Input: YouTube video link
    video_link = input("Enter YouTube video link: ")

    try:
        # Step 1: Extract video ID from the link
        video_id = extract_video_id(video_link)
        print(f"Video ID: {video_id}")

        # Step 2: Fetch channel ID using the YouTube Data API
        channel_id = get_channel_id(video_id)
        print(f"Channel ID: {channel_id}")

        # Step 3: Fetch all videos from the channel
        fetch_channel_videos(channel_id)
    except Exception as e:
        print(f"Error: {e}")