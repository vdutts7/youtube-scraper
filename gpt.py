import os
from youtube_transcript_api import YouTubeTranscriptApi
import openai

openai.api_key = os.getenv('OPENAI_API_KEY')

url = os.getenv('YOUTUBE_URL')
if not url:
    raise ValueError("YOUTUBE_URL environment variable is not set")
print(url)

video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

output=''
for x in transcript:
  sentence = x['text']
  output += f' {sentence}\n'

response = openai.ChatCompletion.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a journalist."},
    {"role": "assistant", "content": "write a 100 word summary of this video"},
    {"role": "user", "content": output}
  ]
)
summary = response["choices"][0]["message"]["content"]

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a journalist."},
    {"role": "assistant", "content": "output a list of tags for this blog post in a python list such as ['item1', 'item2','item3']"},
    {"role": "user", "content": output}
  ]
)
tag = response["choices"][0]["message"]["content"]

print('>>>SUMMARY:')
print(summary)
print('>>>TAGS:')
print(tag)
print('>>>OUTPUT:')
#print(output)

#print(transcript)