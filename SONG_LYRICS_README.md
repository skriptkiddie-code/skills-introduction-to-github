# Song Lyrics Display Program

A Python program that displays song lyrics line by line with configurable resting intervals and stopping time.

## Features

- Display song lyrics line by line
- Configurable rest interval between lines (in seconds)
- Optional stopping time to limit display duration
- Support for both string and list input formats
- Clean, object-oriented design

## Usage

### Basic Usage

Run the demo program:

```bash
python3 song_lyrics_display.py
```

### Using as a Library

```python
from song_lyrics_display import SongLyricsDisplay

# Example 1: Display lyrics with 1 second rest interval
# Note: "Amazing Grace" is in the public domain (John Newton, 1772)
lyrics = """Amazing grace, how sweet the sound
That saved a wretch like me
I once was lost, but now I'm found
Was blind, but now I see"""

displayer = SongLyricsDisplay(lyrics, rest_interval=1.0)
displayer.display()

# Example 2: Display with stop time
displayer = SongLyricsDisplay(lyrics, rest_interval=0.5, stop_time=3.0)
displayer.display()

# Example 3: Use list format
lyrics_list = [
    "Line 1 of the song",
    "Line 2 of the song",
    "Line 3 of the song"
]
displayer = SongLyricsDisplay(lyrics_list, rest_interval=2.0)
displayer.display()
```

## Class: SongLyricsDisplay

### Constructor Parameters

- `lyrics` (list or str): Song lyrics as a list of lines or a single string
- `rest_interval` (float): Time in seconds to wait between displaying lines (default: 1.0)
- `stop_time` (float): Optional total time in seconds after which to stop displaying (default: None)

### Methods

- `display()`: Display the lyrics with the configured timing. Returns the number of lines displayed.

## Examples

The program includes three demo examples:

1. **Example 1**: Display complete lyrics with 1 second rest interval
2. **Example 2**: Display lyrics with 0.5 second rest interval and 5 second stop time (demonstrates early stopping)
3. **Example 3**: Display custom lyrics with 2 second rest interval

## Requirements

- Python 3.x
- No external dependencies required (uses only standard library)

## Copyright Notice

The example lyrics used in this program ("Twinkle, Twinkle, Little Star", "Row, Row, Row Your Boat", and "Amazing Grace") are all in the public domain. When using this program with your own lyrics, please ensure you have the appropriate rights or permissions to use the lyrics.

## License

MIT License
