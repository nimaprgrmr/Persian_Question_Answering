
from huggingsound import SpeechRecognitionModel
from timeit import default_timer as timer
from parsivar import SpellCheck
# from google_spell_checker import GoogleSpellChecker
# from pydub import AudioSegment


corrector_text = SpellCheck()
# google_spell_check = GoogleSpellChecker(lang="fa")

model = SpeechRecognitionModel("jonatasgrosman/wav2vec2-large-xlsr-53-persian")
audio_paths = ["farsi.mp3", "audio1.mp3"]


def spell_check(text):
    correct_text = (corrector_text.spell_corrector(text))
    sentence = correct_text.replace("\200c", " ")
    return sentence


def converter_with_corrector(audio):
    path = [audio]
    start_time = timer()
    transcript = model.transcribe(path)
    sentence = spell_check(transcript[0]['transcription'])
    end_time = timer()
    return sentence, (int(end_time - start_time))


def converter(audio):
    path = [audio]
    start_time = timer()
    transcript = model.transcribe(path)
    sentence = transcript[0]['transcription']
    end_time = timer()
    return sentence, (int(end_time - start_time))


# Recognize voice 1
# start_time_1 = timer()
# # audio1 = audio_paths[0]
# transcript1 = model.transcribe(["farsi.mp3"])
# end_time_1 = timer()
# time1 = int(end_time_1-start_time_1)
# #take sentence from transcribe dict
# sentence1 = transcript1[0]['transcription']
#
# #Recognize voice 2
# start_time_2 = timer()
# # audio2 = audio_paths[1]
# transcript2 = model.transcribe(["audio1.mp3"])
# end_time_2 = timer()
# time2 = int(start_time_2-end_time_2)
# sentence2 = transcript2[0]['transcription']
#
# print(f"{audio_paths[0]} Recognition: {sentence1}  in {time1} Seconds")
# print(f"{audio_paths[1]} Recognition: {sentence2}  in {time2} Seconds")
#
# print(f"first corrected text = {parsivar.spell_corrector(sentence1)}")
# print(f"first corrected text = {parsivar.spell_corrector(sentence2)}")

# print(f"first corrected text = {google_spell_check.check(sentence2)}")
# print(f"first corrected text = {google_spell_check.check(sentence2)}")

# def change_type(audio_path):
#     audio_name = audio_path.split(".")[1]
#     audio_format = audio_path.split(".")[-1]
#     wav_audio = AudioSegment.from_file(audio_path, format=audio_format)
#     raw_audio = AudioSegment.from_file(audio_path, format=audio_format,
#                                        frame_rate=44100, channels=2, sample_width=2)
#
#     wav_audio.export(audio_name+".mp3", format="mp3")