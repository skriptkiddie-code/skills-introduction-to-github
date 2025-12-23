#!/usr/bin/env python3
"""
Song Lyrics Display Program

This program displays song lyrics line by line with configurable resting intervals
and stopping time.
"""

import time
import sys


class SongLyricsDisplay:
    """
    A class to display song lyrics with timing control.
    """
    
    def __init__(self, lyrics, rest_interval=1.0, stop_time=None):
        """
        Initialize the lyrics display.
        
        Args:
            lyrics (list or str): Song lyrics as a list of lines or a single string
            rest_interval (float): Time in seconds to wait between displaying lines
            stop_time (float): Optional total time in seconds after which to stop displaying
        
        Raises:
            TypeError: If lyrics is not a string or list
            ValueError: If rest_interval or stop_time is negative
        """
        # Validate lyrics input
        if isinstance(lyrics, str):
            self.lyrics = lyrics.strip().split('\n')
        elif isinstance(lyrics, list):
            self.lyrics = lyrics
        else:
            raise TypeError("lyrics must be a string or list")
        
        # Validate rest_interval
        if rest_interval < 0:
            raise ValueError("rest_interval must be non-negative")
        self.rest_interval = rest_interval
        
        # Validate stop_time
        if stop_time is not None and stop_time < 0:
            raise ValueError("stop_time must be non-negative or None")
        self.stop_time = stop_time
    
    def display(self):
        """
        Display the song lyrics with the configured timing.
        
        Returns:
            int: Number of lines displayed
        """
        start_time = time.time()
        lines_displayed = 0
        
        for line in self.lyrics:
            # Check if we've exceeded the stop time
            if self.stop_time is not None:
                elapsed_time = time.time() - start_time
                if elapsed_time >= self.stop_time:
                    print(f"\n[Stopped after {elapsed_time:.2f} seconds]")
                    break
            
            # Display the line
            print(line)
            lines_displayed += 1
            
            # Wait for the rest interval before displaying the next line
            # (unless it's the last line)
            if lines_displayed < len(self.lyrics):
                time.sleep(self.rest_interval)
        
        return lines_displayed


def main():
    """
    Main function to demonstrate the song lyrics display.
    """
    # Sample song lyrics (Public Domain: "Twinkle, Twinkle, Little Star" by Jane Taylor, 1806)
    sample_lyrics = """Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, twinkle, little star,
How I wonder what you are!"""

    print("=" * 60)
    print("Song Lyrics Display Demo")
    print("=" * 60)
    print()
    
    # Example 1: Display with 1 second rest interval
    print("Example 1: Display with 1 second rest interval")
    print("-" * 60)
    displayer = SongLyricsDisplay(sample_lyrics, rest_interval=1.0)
    lines = displayer.display()
    print(f"\nDisplayed {lines} lines")
    print()
    
    # Example 2: Display with 0.5 second rest interval and 5 second stop time
    print("\nExample 2: Display with 0.5 second rest interval and 5 second stop time")
    print("-" * 60)
    displayer2 = SongLyricsDisplay(sample_lyrics, rest_interval=0.5, stop_time=5.0)
    lines2 = displayer2.display()
    print(f"\nDisplayed {lines2} lines")
    print()
    
    # Example 3: Display with custom lyrics (Public Domain: "Row, Row, Row Your Boat", traditional nursery rhyme)
    print("\nExample 3: Display with custom lyrics (2 second interval)")
    print("-" * 60)
    custom_lyrics = [
        "Row, row, row your boat,",
        "Gently down the stream.",
        "Merrily, merrily, merrily, merrily,",
        "Life is but a dream."
    ]
    displayer3 = SongLyricsDisplay(custom_lyrics, rest_interval=2.0)
    lines3 = displayer3.display()
    print(f"\nDisplayed {lines3} lines")
    print()
    
    print("=" * 60)
    print("Demo completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()
