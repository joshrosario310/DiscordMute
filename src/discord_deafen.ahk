; Discord Deafen
; v0.2 Jan 20, 2022
; Josh Rosario https://github.com/joshrosario310
; Purpose: To send default Deafen command (Ctrl-Shift-D) to Discord without window focus
; Usage: Compile into executable and then use as executable action on a trigger,
;        ex. Bome's MIDI translator, USB Foot Switch, etc.
; Issues: Can't figure out why ControlSend won't send to Discord.exe without focus, also
;         won't work if Discord is in the system tray or on a different virtual desktop
;         (must be a window in the active desktop)
; Workaround: This will instead change focus to Discord and then back to original window,
;             Works fine if for example OBS has focus and Discord is behind it
;             However, if playing a fullscreen game and activating the script, keys being
;             pressed for the game will be momentarily sent to Discord which could cause 
;             garbage text or possibly commands


WinGet, nDiscordPID, PID, ahk_exe discord.exe
WinGet, nCurrentPID, PID, A

WinActivate, ahk_pid %nDiscordPID%

Send, ^+D

WinActivate, ahk_pid %nCurrentPID%

Return