from pydub import AudioSegment
from pydub.silence import split_on_silence
from inspector import lense
def get_silence_thresh(audio, min_silence_len):
    # Base threshold relative to average loudness
    base = audio.dBFS - 14

    # Longer silence → less aggressive threshold
    if min_silence_len <= 400:
        adjust = -6
    elif min_silence_len <= 800:
        adjust = -4
    elif min_silence_len <= 1200:
        adjust = -2
    else:
        adjust = 0

    return base + adjust
AUDIO_FILE = r'C:\Users\HP OMEN\OneDrive\Documents\Sound Recordings\RockFoundationFirst.wav'
AUDIO_FILE_SPLIT = AUDIO_FILE.split('\\')
AUDIO_FILE_SPLIT_len = len(AUDIO_FILE_SPLIT)-1
file_name = AUDIO_FILE_SPLIT[AUDIO_FILE_SPLIT_len]
file_name = f'pause_removed_{file_name}'
audio = AudioSegment.from_file(
    AUDIO_FILE,
    format='m4a'
)

min_silence_len_out = 200

chunks = split_on_silence(
    audio,
    min_silence_len=min_silence_len_out,
    silence_thresh=get_silence_thresh(audio, min_silence_len_out),
    keep_silence=100
)


output = AudioSegment.empty()
for chunk in chunks:
    output += chunk
print(file_name)
pause_removed_file = r'C:\Users\HP OMEN\OneDrive\Documents\CapCut\RockFoundationProject\audio'+f"\\{file_name}"
output.export(
    pause_removed_file,
    format="mp4",
    codec="aac"
)
