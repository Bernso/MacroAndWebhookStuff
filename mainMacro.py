from pynput.keyboard import Key, Listener
import threading
import time
from pynput.mouse import Listener as MouseListener

pressed_keys = {}

def on_press(key):
    try:
        # Record the time when the key is pressed
        pressed_keys[key] = time.time()
        print(f'Key pressed: {key.char}')
    except AttributeError:
        print(f'Special key pressed: {key}')

def on_release(key):
    if key == Key.esc:
        return False  # If the key 'esc' is pressed, stop the program

    if key in pressed_keys:
        # Calculate the duration the key was pressed
        duration = time.time() - pressed_keys[key]
        print(f'Key {key} pressed for {duration:.2f} seconds')

# Define mouse click handler (unchanged)
def on_click(x, y, button, pressed):
    if pressed:
        print(f'Mouse clicked at ({x}, {y}) with button {button}')

# Function to start keyboard listener
def start_keyboard_listener():
    with Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
        keyboard_listener.join()

# Start listening for mouse clicks (unchanged)
mouse_listener = MouseListener(on_click=on_click)
mouse_listener.start()

# Start keyboard listener in a separate thread
keyboard_thread = threading.Thread(target=start_keyboard_listener)
keyboard_thread.start()

# Keep the main thread alive
keyboard_thread.join()
