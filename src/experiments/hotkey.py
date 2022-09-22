# https://nitratine.net/blog/post/how-to-make-hotkeys-in-python/

from math import comb
from pynput import keyboard


COMBINATIONS = [
    {keyboard.Key.shift, keyboard.KeyCode(vk=65)}, # Shift-A
    {keyboard.Key.shift, keyboard.KeyCode(vk=66)} # Shift-B
]

def execute():
    print("Do something")

pressed_vks = set()

def get_vk(key):
    return key.vk if hasattr(key, 'vk') else key.value.vk

def is_combination_pressed(combination):
    return all([get_vk(key) in pressed_vks for key in combination])

def on_press(key):
    vk = get_vk(key)
    pressed_vks.add(vk)

    for combination in COMBINATIONS:
        if is_combination_pressed(combination):
            execute()
            break

def on_release(key):
    vk = get_vk(key)
    pressed_vks.remove(vk)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()