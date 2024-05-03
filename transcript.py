from youtube_transcript_api import YouTubeTranscriptApi

url = 'https://www.youtube.com/watch?v=vEd-LqBCONg'
video_id = url.replace('https://www.youtube.com/watch?v=', '')

transcript = YouTubeTranscriptApi.get_transcript(video_id)

output = ''
for entry in transcript:
    sentence = entry['text']
    output += f'{sentence}\n'

# Write the output to a file
with open(f'{video_id}_transcript.txt', 'w', encoding='utf-8') as file:
    file.write(output)

print(f"Transcript has been saved to {video_id}_transcript.txt")