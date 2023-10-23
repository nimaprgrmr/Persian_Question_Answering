import requests
from timeit import default_timer as timer

audio_file_path = "farsi.mp3"

url = "http://127.0.0.1:8000/upload/"

start_time = timer()
with open(audio_file_path, 'rb') as f:
    response = requests.post(url, files={"file": f})
end_time = timer()

print(response.json(), (end_time - start_time))
