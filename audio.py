import pydub


def merge_audio_files(audio_files, output_file):
    audio_files = [pydub.AudioSegment.from_file(file) for file in audio_files]
    combined = audio_files[0]
    for audio in audio_files[1:]:
        combined = combined.append(audio, crossfade=0)
    combined.export(output_file, format="wav")
    print("Audio files merged successfully!")
    return True


# if __name__ == "__main__":
#     audio_files = ["D:\Projects\GoPro Vids Merger\GX010060.WAV", "D:\Projects\GoPro Vids Merger\GX020060.WAV"]
#     output_file = "D:\Projects\GoPro Vids Merger\output.WAV"
#     merge_audio_files(audio_files, output_file)