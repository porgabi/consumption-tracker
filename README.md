18/09 update -- starting to crack the puzzle at last, restored some basic functionality. Grinding away at PyQt signals/slots and their implementation, more commits to come in the next few days methinks.



This version is a WIP and not currently functional. One could reasonably suggest it is a bit of an awful mess, and such statement would only barely miss the mark. Yet, progress is being made on the improved software structure, though it has proven to be quite a difficult task to figure out.

Rest assured that it is, indeed, being pierced together.

![Alt Text](https://i.imgur.com/mXnNxoN.gif)

# Consumption Tracker

Consumption Tracker is a program that tracks daily water and calories consumption through simple user input.

This is a practice project made by a beginner with 3-4 months of learning experience. Treat it as such.

![Alt Text](https://i.imgur.com/21M3Xrf.gif)

## Features:

* Management of consumption via several buttons of varying values
* Simple and straightforward display of current values
* Widget to log meal times (max 6 at once)
* Adjustable maximum values for water and calories to reasonable extents
* Option to auto-reset all values and meal times in the morning
* Selectable male/female body figures
* Function to manually reset all values and meal times
* Function to save a screenshot of the current state of application
* Light/dark mode

## Before running the program:
* Unzip **CT_1.0.0** and all its content
* Make sure **CT_icons** is in the same folder as **CT.exe** (otherwise images in the application will not be displayed)

## Built with:
* [Python 3.6.0](https://www.python.org/downloads/release/python-360/)
* [PyQt5 5.13.0](https://pypi.org/project/PyQt5/)

## Additional notes:
* v1.0.0 source code has a severe case of spaghetto. This will likely be improved in a future release.
* CT was tested only on Windows 10, no guarantee it will work properly on other OS.
* Default folder for saved screenshots is C:\Users\User\CT_screenshots.
* The minimize to tray function is janky even by beginner standards. Will hopefully be improved later on.
