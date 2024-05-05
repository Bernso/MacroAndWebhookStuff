import time
import os
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

if os.path.exists('input.txt'):
    input("Input file already exists.\nPress enter to continue...")
else:
    open('input.txt', 'w').close()
    input('Input file created.\nPlease go and edit it manually for your macro.')
    quit()

def simulate_actions(file_path):
    keyboard = KeyboardController()
    mouse = MouseController()

    with open(file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Ignore empty lines
                if line.lower() == 'click':
                    mouse.click(Button.left)
                else:
                    parts = line.split()
                    if len(parts) == 2:
                        key, duration = parts
                        keyboard.press(key)
                        print(f"Pressed key: {key}")
                        time.sleep(float(duration))
                        print(f"Waited for {duration} seconds")
                        keyboard.release(key)
                        print(f"Released key: {key}")
                    else:
                        try:
                            duration = float(line)
                            time.sleep(duration)
                            print(f"Waited for {duration} seconds")
                        except ValueError:
                            print(f"Ignoring line: {line} - Invalid format")

if __name__ == "__main__":
    file_path = 'input.txt'  
    
    time.sleep(3)
    start = time.time()
    
    for i in range(10):
        simulate_actions(file_path)
    end = time.time()
    
    print(f"Total time taken: {end - start} seconds")