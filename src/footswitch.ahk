; Footswitch
; v0.3 Oct 26, 2022
; Josh Rosario https://github.com/joshrosario310
; Purpose: To take keys generated by footswitch (Ctrl-Alt-Shift-F1/2/3) and mute different apps
; Usage: Compile into executable and then run in admin mode while waiting for keystrokes from footswitch
; Variant: This version needs to be run to stay in task bar, then will be triggered by a ridiculous 
;          keystroke, needed because my dumb footswitch can only trigger keystrokes
; Issues: OBS runs in Admin mode and disables global hotkeys for apps
; Workaround: This will instead change focus to app and then back to original window,
;             Works fine if for example OBS has focus and Discord is behind it
;             However, if playing a fullscreen game and activating the script, keys being
;             pressed for the game will be momentarily sent to Discord which could cause 
;             garbage text or possibly commands

; Ctrl-Alt-Shift-F1 Mutes Discord (Ctrl-Shift-M)
^!+F1::

WinGet, nDiscordPID, PID, ahk_exe discord.exe
WinGet, nCurrentPID, PID, A

WinActivate, ahk_pid %nDiscordPID%

Send, ^+M

WinActivate, ahk_pid %nCurrentPID%

Return

; Ctrl-Alt-Shift-F2 Deafens Discord (Ctrl-Shift-M)
^!+F2::

WinGet, nDiscordPID, PID, ahk_exe discord.exe
WinGet, nCurrentPID, PID, A

WinActivate, ahk_pid %nDiscordPID%

Send, ^+D

WinActivate, ahk_pid %nCurrentPID%

Return

; Ctrl-Alt-Shift-F3 Mutes strip 1 in Voicemeeter as a global mute (Ctrl-F3)
; NOTE: Voicemeeter Macro button needs to be running and programmed with Ctrl-F3 to mute with Exclusive,
; Voicemeeter needs to be open
^!+F3::

WinGet, nVoicemeeterPID, PID, ahk_exe voicemeeter8x64.exe
WinGet, nCurrentPID, PID, A

WinActivate, ahk_pid %nVoicemeeterPID%

Sleep, 100
Send, ^{F3}

WinActivate, ahk_pid %nCurrentPID%

Return