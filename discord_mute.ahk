; Discord Mute
; v0.1
; Dec 17, 2021 - Josh Rosario https://github.com/joshrosario310
; Purpose: To send default Mute command (Ctrl-Shift-M) to Discord without window focus
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

; TESTING
;^+t::
;ControlSend,, {CtrlDown}{ShiftDown}M{ShiftUp}{CtrlUp}, ahk_exe discord.exe ; Works only if window is focused
;ControlSend,, ^!M, ahk_exe discord.exe ; Also works, only when window focused
;Send, {CtrlDown}{ShiftDown}M{ShiftUp}{CtrlUp} ; Does work when window focused
;;Send, ^!M ; Doesn't work
;ControlSendRaw,, {CtrlDown}{ShiftDown}M{ShiftUp}{CtrlUp}, ahk_exe discord.exe ; Just types it out in focused window
;ControlSendRaw,, ^!M, ahk_exe discord.exe ; Also just types it out in focused window
; END TESTING

WinGet, nDiscordPID, PID, ahk_exe discord.exe
WinGet, nCurrentPID, PID, A
;MsgBox, Discord PID is %nDiscordPID%
;MsgBox, Current PID is %nCurrentPID%
WinActivate, ahk_pid %nDiscordPID%
Send, {CtrlDown}{ShiftDown}M{ShiftUp}{CtrlUp}
WinActivate, ahk_pid %nCurrentPID%

Return