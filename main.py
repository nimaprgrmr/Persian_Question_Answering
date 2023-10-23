import time
import pyaudio  # You might need to install this library
from huggingsound import SpeechRecognitionModel


# Initialize the model and audio recorder
model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-persian")

def converter_with_corrector(audio):
    path = [audio]
    transcript = model.transcribe(path)
    sentence = transcript[0]['transcription']
    return sentence


def real_time_transcription():
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=16000,  # Adjust this rate to match your audio source
                    input=True,
                    frames_per_buffer=1024)  # Adjust buffer size as needed

    print("Start speaking...")

    try:
        while True:
            audio_data = stream.read(1024)  # Adjust buffer size
            sentence = converter_with_corrector(audio_data)
            print(f"Transcription: {sentence}")

    except KeyboardInterrupt:
        print("Recording stopped.")
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    real_time_transcription()


# import time
# import pyaudio
# import tempfile
# from huggingsound import SpeechRecognitionModel
#
# # Initialize the model
# model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-persian")
#
# def converter_with_corrector(audio_path):
#     path = [audio_path]
#     transcript = model.transcribe(path)
#     sentence = transcript[0]['transcription']
#     return sentence
#
# def real_time_transcription():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16,
#                     channels=1,
#                     rate=16000,  # Adjust this rate to match your audio source
#                     input=True,
#                     frames_per_buffer=1024)  # Adjust buffer size as needed
#
#     print("Start speaking...")
#
#     try:
#         temp_audio_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         audio_file_path = temp_audio_file.name
#
#         while True:
#             audio_data = stream.read(1024)  # Adjust buffer size
#             temp_audio_file.write(audio_data)
#             sentence = converter_with_corrector(audio_file_path)
#             print(f"Transcription: {sentence}")
#
#     except KeyboardInterrupt:
#         print("Recording stopped.")
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#         temp_audio_file.close()
#
# if __name__ == "__main__":
#     real_time_transcription()


#  IF ITS NOT WORK THEN:

# import time
# import pyaudio
# import wave
# import tempfile
#
# # Initialize the model and audio recorder
# model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-persian")
#
# def converter_with_corrector(audio_path):
#     path = [audio_path]
#     transcript = model.transcribe(path)
#     sentence = transcript[0]['transcription']
#     return sentence
#
# def real_time_transcription():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16,
#                     channels=1,
#                     rate=44100,  # Adjust this rate to match your audio source
#                     input=True,
#                     frames_per_buffer=1024)  # Adjust buffer size as needed
#
#     print("Start speaking...")
#
#     try:
#         temp_audio_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         with wave.open(temp_audio_file.name, 'wb') as audio_file:
#             audio_file.setnchannels(1)
#             audio_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
#             audio_file.setframerate(44100)  # Adjust this rate
#             while True:
#                 audio_data = stream.read(1024)  # Adjust buffer size
#                 audio_file.writeframes(audio_data)
#                 sentence = converter_with_corrector(temp_audio_file.name)
#                 print(f"Transcription: {sentence}")
#
#     except KeyboardInterrupt:
#         print("Recording stopped.")
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#         temp_audio_file.close()
#
# if __name__ == "__main__":
#     real_time_transcription()


# if its not work again
# import time
# import pyaudio
# import wave
# import tempfile
# import os
#
# # Initialize the model and audio recorder
# model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-persian")
#
# def converter_with_corrector(audio_path):
#     path = [audio_path]
#     transcript = model.transcribe(path)
#     sentence = transcript[0]['transcription']
#     return sentence
#
# def real_time_transcription():
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16,
#                     channels=1,
#                     rate=44100,  # Adjust this rate to match your audio source
#                     input=True,
#                     frames_per_buffer=1024)  # Adjust buffer size as needed
#
#     print("Start speaking...")
#
#     try:
#         temp_audio_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
#         audio_file_path = temp_audio_file.name
#         audio_file = wave.open(audio_file_path, 'wb')
#         audio_file.setnchannels(1)
#         audio_file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
#         audio_file.setframerate(44100)  # Adjust this rate
#         audio_frames = []
#
#         while True:
#             audio_data = stream.read(1024)  # Adjust buffer size
#             audio_frames.append(audio_data)
#             audio_file.writeframes(audio_data)
#             sentence = converter_with_corrector(audio_file_path)
#             print(f"Transcription: {sentence}")
#
#     except KeyboardInterrupt:
#         print("Recording stopped.")
#         stream.stop_stream()
#         stream.close()
#         p.terminate()
#         audio_file.close()
#         os.remove(audio_file_path)
#
# if __name__ == "__main__":
#     real_time_transcription()
