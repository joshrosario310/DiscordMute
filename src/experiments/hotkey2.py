# https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/

from time import sleep
from pynput.keyboard import HotKey, Key, KeyCode, Listener
import keyboard
import os
import asyncio
# import simpleobsws

# loop = asyncio.get_event_loop()

# ws = simpleobsws.obsws(host='127.0.0.1', port=4444, password='MYSecurePassword')

print("Ctrl-Alt-Shift-C to exit script\n")
print("Monitoring for Discord Mute foot pedal command Ctrl-Alt-Shift-Win-M")

async def discord_mute():
    print("Toggling Discord Mute")
    # make_request()

# async def make_request():
#     await ws.connect()
    # ws.connect()
#     # Get initial volume
#     data = {'source':'Discord', 'useDecibel':True}
#     result = await ws.call('GetVolume', data)
#     volumeStart = result['volume']
#     print("Starting Volume: {}dB".format(volumeStart))
#     await asyncio.sleep(3)
#     # Lower if by 6 (clamp to -100)
#     volumeTemp = volumeStart - 6.0
#     data = {'source':'Discord', 'volume': volumeTemp, 'useDecibel':True}
#     result = await ws.call('SetVolume', data)
#     data = {'source':'Discord', 'useDecibel':True}
#     result = await ws.call('GetVolume', data)
#     volume = result['volume']
#     print("Temporary Volume: {}dB".format(volume))
#     await asyncio.sleep(3)
#     # Return to original volume
#     data = {'source':'Discord', 'volume': volumeStart, 'useDecibel':True}
#     result = await ws.call('SetVolume', data)
#     data = {'source':'Discord', 'useDecibel':True}
#     result = await ws.call('GetVolume', data)
#     volume = result['volume']
#     print("Temporary Volume: {}dB".format(volume))
#     await ws.disconnect()

hotkey1 = HotKey(
    [Key.ctrl, Key.alt, Key.shift, Key.cmd_l, KeyCode(char='m')],
    # [Key.ctrl, Key.alt, Key.shift, Key.f1],
    # [Key.f1],
    discord_mute
)

hotkey2 = HotKey(
    [Key.ctrl, Key.alt, Key.shift, KeyCode(char='c')],
    quit
)

hotkeys = [hotkey1, hotkey2]

def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()

# loop.run_until_complete(make_request())