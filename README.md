# Audio Visualizer with Pygame

This Python script creates a simple audio visualizer that displays a graphical representation of an audio waveform using Pygame and librosa. Though it is not anywhere near accurate, but does something ^^

## Prerequisites

Before running the script, ensure you have the following libraries installed:

- Python (3.x recommended)
- Pygame
- librosa
- numpy

You can install these libraries using pip:

```bash
pip install pygame librosa numpy
```

## Usage

1. Run the script by executing `visualizer.py` in your terminal or IDE.

2. When prompted, enter the path to the audio file you want to visualize.

3. The audio visualizer window will appear, and the audio will start playing. You will see a graphical representation of the audio waveform.

4. Close the window to stop the visualization and exit the program.

## Customization

You can customize various aspects of the visualizer by modifying the script:

- Adjust the `SCREEN_WIDTH`, `SCREEN_HEIGHT`, `BAR_WIDTH`, and `BAR_SPACING` constants to change the size and spacing of the bars in the visualizer.

- Modify the `BACKGROUND_COLOR` to change the background color of the visualizer.

- You can customize the color gradient of the bars by changing the `color` variable inside the main loop. The color is determined by the amplitude of each frequency band in the audio spectrum.

- You can also adjust the frame rate by changing the argument to `clock.tick()` inside the main loop.

## References


- [Pygame](https://www.pygame.org/): creating the graphical user interface.
- [Librosa](https://librosa.org/): audio processing and visualization.

### Feel free to use and modify this script to create your own audio visualizer projects
~~Maybe a better one~~
