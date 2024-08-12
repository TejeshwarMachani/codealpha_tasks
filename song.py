import random
from music21 import stream, note, chord, instrument

# Define a scale (C major scale)
scale = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Function to generate a random note or chord
def generate_note_or_chord():
    choice = random.choice([0, 1])
    if choice == 0:
        # Generate a random note
        n = random.choice(scale)
        return note.Note(n)
    else:
        # Generate a random chord
        n1, n2, n3 = random.choices(scale, k=3)
        return chord.Chord([n1, n2, n3])

# Create a stream (a sequence of notes/chords)
music_stream = stream.Stream()

# Add an instrument to the stream
music_stream.append(instrument.Piano())

# Generate 50 random notes or chords
for _ in range(50):
    n = generate_note_or_chord()
    music_stream.append(n)

# Save the generated music to a MIDI file
music_stream.write('midi', fp='random_music.mid')
