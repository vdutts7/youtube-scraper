import os
from youtube_transcript_api import YouTubeTranscriptApi
import openai
from dotenv import load_dotenv

load_dotenv()


openai.api_key = os.getenv('OPENAI_API_KEY')

url = os.getenv('YOUTUBE_URL')


video_id = url.replace('https://www.youtube.com/watch?v=', '')
print(video_id)

transcript = YouTubeTranscriptApi.get_transcript(video_id)

output=''
for x in transcript:
  sentence = x['text']
  output += f' {sentence}\n'

response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {"role": "system", "content": "You are a journalist."},
    {"role": "assistant", "content": "write a 100 word summary of this video"},
    {"role": "user", "content": output}
  ]
)
summary = response["choices"][0]["message"]["content"]

response = openai.ChatCompletion.create(
  model="gpt-4",
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

# Create output folder if it doesn't exist
output_folder = 'output'
os.makedirs(output_folder, exist_ok=True)

# Write output to a file in the output folder
output_file = os.path.join(output_folder, f'{video_id}_output.txt')
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('>>>SUMMARY:\n')
    f.write(summary + '\n\n')
    f.write('>>>TAGS:\n')
    f.write(tag + '\n\n')
    f.write('>>>OUTPUT:\n')
    f.write(output)

print(f'Output has been saved to {output_file}')

#print(transcript)