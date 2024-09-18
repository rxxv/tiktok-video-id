import requests
import re

def link(shortened_link: str) -> str:
    try:
        response = requests.head(shortened_link, allow_redirects=True)
        
        full_link = response.url
        return full_link
    except requests.RequestException as e:
        return f"Error resolving link: {e}"

def extract(full_link: str) -> str:
    """
    Extracts the video ID from the full TikTok web link.
    """
    match = re.search(r'/video/(\d+)', full_link)
    if match:
        return match.group(1)
    else:
        return "Video ID not found in the link."

mobile_link = input("Enter TikTok link: ")

full_link = link(mobile_link)

video_id = extract(full_link)
print("Video ID/Aweme ID:", video_id)
