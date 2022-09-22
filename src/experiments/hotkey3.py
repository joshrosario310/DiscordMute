# Listen for special Hotkeys (Ctrl-Shift-Alt-F1/F2) from footswitch and control OBS & Discord
# F1 will enable "Chat Mode" which mutes Discord Mic, turns down Discord Vox in OBS, then reverts

# Note: In Discord, we need to create "custom" keybinds for Mute & Deafen which are the 
# same as the defaults overriding them, this allows Discord to listen for the hotkey (Still doesn't seem to override OBS Admin)

# So for now we have to run OBS as NOT Admin for any of this to work as OBS overrides all hotkeys

# Footswitch is configured for Ctrl-Shift-Alt-F1 and -F2

# https://github.com/IRLToolkit/simpleobsws/tree/0.0.7
# Had to install with pip install simpleobsws==0.0.7
# Using obs-websocket==4.9.1
# https://github.com/obsproject/obs-websocket/blob/4.9.1/docs/generated/protocol.md#requests

import keyboard
import asyncio
import simpleobsws

loop = asyncio.get_event_loop()
ws = simpleobsws.obsws(host='127.0.0.1', port=4444, loop=loop)

bChatMode = False
volumeStart = 0

async def test():
    print("test")
    await asyncio.sleep(2)
    print("complete")

async def lower_vol():
    # print("connecting to obs websocket")
    await ws.connect()
    print("connected to obs websocket")
    # Get initial volume
    data = {'source':'Discord', 'useDecibel':True}
    result = await ws.call('GetVolume', data)
    global volumeStart
    volumeStart = result['volume']
    print("volumeStart {}".format(volumeStart))
    print("Starting Volume: {}dB".format(volumeStart))
    # Lower if by 6dB
    volumeTemp = volumeStart - 6.0
    data = {'source':'Discord', 'volume': volumeTemp, 'useDecibel':True}
    result = await ws.call('SetVolume', data)
    data = {'source':'Discord', 'useDecibel':True}
    result = await ws.call('GetVolume', data)
    volume = result['volume']
    print("Temporary Volume: {}dB".format(volume))
    await ws.disconnect()
    # print("disconnected from obs websocket")

async def raise_vol():
    # print("connecting to obs websocket")
    await ws.connect()
    print("connected to obs websocket")
    print("volumeStart {}".format(volumeStart))
    # Return to original volume
    data = {'source':'Discord', 'volume': volumeStart, 'useDecibel':True}
    result = await ws.call('SetVolume', data)
    data = {'source':'Discord', 'useDecibel':True}
    result = await ws.call('GetVolume', data)
    volume = result['volume']
    print("Temporary Volume: {}dB".format(volume))
    await ws.disconnect()
    # print("disconnected from obs websocket")

def toggle_chat_mode():
    # Toggle the discord mute
    print("mute command")
    keyboard.press_and_release("ctrl+shift+m")
    # asyncio.run(make_request())
    global bChatMode
    if bChatMode == False:
        loop.run_until_complete(lower_vol())
        bChatMode = True
    else:
        loop.run_until_complete(raise_vol())
        bChatMode = False


def toggle_deafen():
    # Toggle the discord deafen
    print("deafen command")
    keyboard.press_and_release("ctrl+shift+d")

def main():
    print("setting hotkeys")

    # print("Enter desired shortcut: ")
    # shortcut_mute = keyboard.read_hotkey()
    # print("Shortcut: ", shortcut_mute)
    shortcut_mute = "ctrl+alt+shift+f1"
    shortcut_deafen = "ctrl+alt+shift+f2"

    keyboard.add_hotkey(shortcut_mute, toggle_chat_mode)
    keyboard.add_hotkey(shortcut_deafen, toggle_deafen)

    # print("esc to exit")
    # keyboard.wait("esc")
    input("Press Enter to end")

if __name__ == "__main__":
    main()