from youtube_transcript_api import YouTubeTranscriptApi
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and YouTube URL from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
url = os.getenv('YOUTUBE_URL')

print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

response = openai.ChatCompletion.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a database computer"},
    {"role": "assistant", "content": "data is stored in JSON {text:'', start:'', duration:''}"},
    {"role": "assistant", "content": str(transcript)},
    {"role": "user", "content": "what are the topics discussed in this video. Provide start time codes in seconds and also in minutes and seconds"}
  ]
)
timecode = response["choices"][0]["message"]["content"]

# Create output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Replace print statements with file writing
output_file = os.path.join(output_dir, "timecode_output.txt")
with open(output_file, "w") as f:
    f.write(f"URL: {url}\n")
    f.write(f"Video ID: {video_id}\n")
    f.write(f"Timecode:\n{timecode}\n")

print(f"Output written to {output_file}")