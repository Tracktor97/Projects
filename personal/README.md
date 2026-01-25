# Date Machine Tool

The Date Machine Tool is a lightweight Python program that randomly selects
a unique date-night activity using weighted rarity and optional modifiers.
Activities are sourced from an Excel spreadsheet and tracked to prevent
unwanted repetition.

This project uses random number generation to determine a date-night activity
based on rarity tiers defined in an Excel spreadsheet. Once a rarity is selected,
the program samples an activity from the corresponding category using pandas.
An additional modifier is selected from a separate sheet to add variety.

Non-repeatable activities are logged to a CSV file to prevent reuse.
Final results are printed to the user upon completion.

## Features
- Weighted rarity-based activity selection
- Modifier system for added variety
- Non-repeatable activity tracking via CSV logging
- Excel sheet parsing using pandas
- Easily customizable activity and modifier lists

## Purpose
This project was my solution to a recurring problem after my wife expressed
interest in having dedicated date nights on Saturdays. I wanted to build a
tool that could remove decision fatigue while still keeping date nights fun,
varied, and occasionally challenging through the use of modifiers.

## Limitations
- This program was developed without a main execution wrapper and is therefore
  less modular than some of my other projects
- The tool requires a specifically formatted Excel spreadsheet with two sheets
  ("Main" and "Extras")
- In its current state, the program assumes local file paths and hard-coded values
- The primary limitation of this tool is user creativity — any activity or modifier
  can be implemented

## Future Improvements
- Refactor into a modular structure with a main execution function
- Add command-line arguments for user input
- Improve error handling for missing or malformed Excel files
- Optional GUI or web-based interface
