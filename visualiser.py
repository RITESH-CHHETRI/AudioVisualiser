import pygame
import librosa.display
import numpy as np

# Initialize Pygame
pygame.init()

#Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400
BAR_WIDTH = 5
BAR_SPACING = 2
NUM_BARS = SCREEN_WIDTH // (BAR_WIDTH + BAR_SPACING)

#BG color
BACKGROUND_COLOR = (0, 0, 0)

# Create a Pygame window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Audio Visualizer")

# Load the audio file and extract its waveform and sample rate
audio_file = input("Enter the path to an audio file: ")
y, sr = librosa.load(audio_file)

# Clock to control the frame rate
clock = pygame.time.Clock()

#Pygame mixer for playing audio
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(0)


running = True
t = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the FFT of the audio signal
    start = int((t / sr) * len(y))
    end = start + int((1 / NUM_BARS) * len(y))
    fft = np.abs(np.fft.fft(y[start:end]))

    # Normalize the FFT values
    fft /= np.max(fft)

    screen.fill(BACKGROUND_COLOR)

    # Draw the audio visualizer bars with a color gradient
    for i in range(NUM_BARS):
        amplitude = fft[i]
        color = (
            int(255 * amplitude),    # Red component
            0,                       # Green component
            int(255 * (1 - amplitude))  # Blue component
        )
        bar_height = int(amplitude * SCREEN_HEIGHT)
        x = i * (BAR_WIDTH + BAR_SPACING)
        pygame.draw.rect(screen, color, (x, SCREEN_HEIGHT - bar_height, BAR_WIDTH, bar_height))

    # Update display
    pygame.display.flip()

    # Increment time for the next frame
    t += 1

    #frame rate
    clock.tick(30)

pygame.quit()
