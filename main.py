import mido
import struct

def read_lyrics(lyric_filename):
    with open(lyric_filename, "r", encoding="latin-1") as f:
        lines = f.readlines()
    title = lines[0].strip()
    artist = lines[1].strip()
    lyrics = [line.strip() for line in lines[4:]]
    return title, artist, lyrics

def read_cursor(cursor_filename, ticks_per_beat):
    timestamps = []
    with open(cursor_filename, "rb") as f:
        previous_absolute_timestamp = 0
        while True:
            bytes_read = f.read(2)
            if not bytes_read:
                break
            absolute_timestamp = struct.unpack("<H", bytes_read)[0]
            absolute_timestamp *= (ticks_per_beat / 24)
            if absolute_timestamp < previous_absolute_timestamp:
                absolute_timestamp = previous_absolute_timestamp  # ป้องกันไม่ให้ค่าเวลาย้อนกลับ
            relative_timestamp = int(absolute_timestamp - previous_absolute_timestamp)
            timestamps.append(relative_timestamp)
            previous_absolute_timestamp = absolute_timestamp
    return timestamps

def combine_to_kar(midi_filename, lyric_filename, cursor_filename, kar_filename):
    title, artist, lyrics = read_lyrics(lyric_filename)

    midi = mido.MidiFile(midi_filename)
    ticks_per_beat = midi.ticks_per_beat
    karaoke_track = mido.MidiTrack()
    midi.tracks.append(karaoke_track)

    karaoke_track.append(mido.MetaMessage('text', text=f"@T{title}", time=0))
    karaoke_track.append(mido.MetaMessage('text', text=f"@T{artist}", time=0))

    timestamps = read_cursor(cursor_filename, ticks_per_beat)

    previous_time = 0
    line_idx = 0
    for line in lyrics:
        line_with_slash = f"/{line}"
        for char in line_with_slash:
            if line_idx < len(timestamps):
                delta_time = timestamps[line_idx]
            else:
                delta_time = 0
            karaoke_track.append(mido.MetaMessage('lyrics', text=char, time=delta_time))
            previous_time += delta_time
            line_idx += 1

    midi.save(kar_filename)
    print(f"บันทึกไฟล์ .kar เสร็จสิ้น: {kar_filename}")

combine_to_kar("song.mid", "song.lyr", "song.cur", "output.kar")
