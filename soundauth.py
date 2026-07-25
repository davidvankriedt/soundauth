#!/usr/bin/env python3

import numpy as np
import sounddevice as sd
import sys

FS = 44100              # sample rate
RECORDING_DURATION = 5

# config

sd.default.samplerate = FS
sd.default.channels = 1


# mapping notes to frequencies (Hz)
NOTES = {
    'C4': 261.63,
    'E4': 329.63,
    'G4': 392.00,
    'C5': 523.25
}

def decode_melody(recording):
    """Returns notes detected in given recording"""

    # ensure data is 1D
    recording = recording.flatten()

    # converting data from time domain to frequency domain + removing complex numbers
    fft_data = np.abs(np.fft.rfft(recording))

    # creating Hz array for mapping fft_data amplitudes
    frequencies = np.fft.rfftfreq(len(recording), 1/FS)

    # filter low frequencies below 200 (noise)
    valid_range = frequencies >= 200
    fft_data[~valid_range] = 0

    # Normalising magnitudes (0 is quiet, 1 is max loudness)
    max_val = np.max(fft_data)
    if max_val > 0:
        fft_data = fft_data / max_val

    detected_notes = []

    for note_name, target_freq in NOTES.items():
        # allow 1 semitone deviation
        window = (frequencies >= target_freq - 12) & (frequencies <= target_freq + 12)
        
        if np.any(window):
            peak_val = np.max(fft_data[window])
            # checking if peak volume in this window is at least 30% of max volume in recording
            if peak_val > 0.3:
                detected_notes.append(note_name)

    return detected_notes

def main():
    print("------- DEVICE LOCKED -------")
    print("Unlock through secret melody: ")

    # indefinite loop checking for melody
    while True:
        command = input("Enter 's' to start recording: ")
        if command == 's':
            recording = sd.rec(int(RECORDING_DURATION * FS))
            sd.wait()

            notes_found = decode_melody(recording)
            expected_key = ['C4', 'E4', 'G4', 'C5']

            if set(expected_key) == set(notes_found):
                print('Correct melody. Device unlocked.')
                sys.exit(0)
            else:
                print('Incorrect melody. Try again.')  

    

if __name__ == "__main__":
    main()