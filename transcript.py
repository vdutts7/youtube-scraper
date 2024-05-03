import os
from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()

# Get the URL from the environment variable
url = os.getenv('YOUTUBE_URL')

if not url:
    print("Error: YOUTUBE_URL environment variable is not set.")
    exit(1)

video_id = url.replace('https://www.youtube.com/watch?v=', '')

transcript = YouTubeTranscriptApi.get_transcript(video_id)

output = ''
for entry in transcript:
    sentence = entry['text']
    output += f'{sentence}\n'

# Create the output folder if it doesn't exist
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

# Write the output to a file in the output folder
output_file = os.path.join(output_folder, f'{video_id}_transcript.txt')
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(output)

print(f"Transcript has been saved to {output_file}")