# DiscordMute
Executable mute/deafen commands for when Discord is not in focus

v0.1 Dec 17, 2021

## Purpose
To send default Deafen/Mute commands (Default Ctrl-Shift-D/M) to Discord without window focus

## My Use-Case
Playing games on PS5 with a capture card to OBS, don't want to focus Discord and use keyboard shortcuts but instead want to trigger from an iOS Stream-Deck style app

## Usage
Download .exe files and target them to execute from some trigger ex. Bome's MIDI translator, USB Foot Switch, Streamdeck, etc.  
To build, install AutoHotKey and use context shell to compile into exe

## Issues
Can't figure out why ControlSend won't send to Discord.exe without focus, also won't work if Discord is in the system tray or on a different virtual desktop (must be a window in the active desktop)

## Workaround
This will instead change focus to Discord and then back to original window, works fine if for example OBS has focus and Discord is behind it  
However, if playing a fullscreen game and activating the script, keys being pressed for the game will be momentarily sent to Discord which could cause garbage text or possibly commands
