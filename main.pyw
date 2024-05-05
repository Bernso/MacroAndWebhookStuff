import tkinter as tk, os, time, webbrowser, requests
from tkinter import messagebox, ttk
from pynput.keyboard import Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController





def edit_macro_file():
    if not os.path.exists('macro.exe'):
        with open('macro.exe', 'w') as f:
            f.write("# Edit your macro here\n# Each line should contain a key and its duration separated by a space\n# Example: a 0.5\n# To simulate a mouse click, use 'click'\n")
            f.close() # To avoid data leak
            os.system('notepad.exe macro.exe')
    else:
        os.system('notepad.exe macro.exe')


def start_macro():
    keyboard = KeyboardController()
    mouse = MouseController()
    file_path = 'macro.exe'
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        file.close()  # To avoid data leak
        buttons = ['backspace', 'tab', 'enter', 'escape', 'delete', 'home', 'end', 'insert', 'left', 'right', 'down', 'up', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'shift', 'ctrl', 'alt', 'pause', 'caps_lock','scroll_lock', 'page_up', 'page_down', 'num_lock', 'print_screen']

        for line in lines:
            line = line.strip()  # Remove leading/trailing whitespace
            if line:  # Ignore empty lines
                if line.lower() == 'click':
                    mouse.click(Button.left)
                    
                elif line.lower() == 'right-click':
                    mouse.click(Button.right)
                    
                elif line.lower() == 'double-click':
                    mouse.click(Button.left, Button.left)
                    
                elif line.lower() == 'triple-click':
                    mouse.click(Button.left, Button.left, Button.left)
                    
                elif line.lower() =='scroll-up':
                    mouse.scroll(0, 1)  # Scrolling up, so dy is positive
                    
                elif line.lower() =='scroll-down':
                    mouse.scroll(0, -1)  # Scrolling down, so dy is negative
                    
                elif any(btn in line.lower() for btn in buttons):
                    parts = line.split()
                    if len(parts) == 2:
                        key, duration = parts
                        keyboard.press(key)
                        time.sleep(float(duration))
                        keyboard.release(key)
                    else:
                        try:
                            duration = float(line)
                            time.sleep(duration)
                        except ValueError:
                            print(f"Ignoring line: {line} - Invalid format")
                else:
                    parts = line.split()
                    if len(parts) == 2:
                        key, duration = parts
                        keyboard.press(key)
                        time.sleep(float(duration))
                        keyboard.release(key)
                    else:
                        try:
                            duration = float(line)
                            time.sleep(duration)
                        except ValueError:
                            print(f"Ignoring line: {line} - Invalid format")
                            
                            
def full_macro():
    try:
        num_times = int(timesToComplete.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input for number of times.")
        return

    if num_times <= 0:
        messagebox.showerror("Error", "Number of times should be a positive integer.")
        return

    confirmation = messagebox.askyesno("Confirmation", f"Start macro {num_times} times?")
    if not confirmation:
        return

    else:
        start_button.configure(text='Running macro...')
        for i in range(num_times):
            print(f"Running macro {i + 1} of {num_times}")
            
            start_macro()
            print(f"Finished macro {i + 1} of {num_times}")
        send_to_discord(times=i+1)
        start_button.configure(text='Start Macro')
        messagebox.showinfo("Macro", "Macro process completed.")


def open_discord(event):
    webbrowser.open("https://discord.com/invite/k5HBFXqtCB")


def send_to_discord(times):
    try:
        payload = {
            "content": f"Your macro has been successfully ran {times} times"
        }
        
        if os.path.exists('discordWebhook.exe'):
            webhook = open('discordWebhook.exe', 'r')
            discordWebhookURL = webhook.read()
            webhook.close()
            print('webhook found')
            
        else:
            discordWebhookURL = webhookURL.get()
            
        requests.post(discordWebhookURL, json=payload)
        print("Test message sent to Discord.")
        
    except Exception as e:
        print(e)


def send_to_discord_test():
    try:
        payload = {
            "content": f"This is a test message"
        }
        
        if os.path.exists('discordWebhook.exe'):
            webhook = open('discordWebhook.exe', 'r')
            discordWebhookURL = webhook.read()
            webhook.close()
            print('webhook found')
            
        else:
            discordWebhookURL = webhookURL.get()
            
        requests.post(discordWebhookURL, json=payload)
        print("Test message sent to Discord.")
        
    except Exception as e:
        print(e)


def helpMe():
    buttons = ['backspace', 'tab', 'enter', 'escape', 'delete', 'home', 'end', 'insert', 'left', 'right', 'down', 'up', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'shift', 'ctrl', 'alt', 'pause', 'caps_lock','scroll_lock', 'page_up', 'page_down', 'num_lock', 'print_screen']
    messagebox.showinfo("Help Message", f"Keybinds:\n\n{buttons}")


def save_discord_webhook():
    try:
        toSave = webhookURL.get()
        if toSave == '':
            messagebox.showerror("Error", "Discord webhook cannot be empty.")
            return
        
        else:
            if not toSave.startswith("https://discord.com/api/webhooks/"):
                messagebox.showerror("Error", "Enter a valid Discord webhook URL.")
                return
            
            else:
                with open('discordWebhook.exe', 'w') as f:
                    f.write(toSave)
                saveDiscordWebhookButton.configure(text="Discord webhook saved")
                
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Error saving Discord webhook.")


# Create the main window
app = tk.Tk()
app.geometry("290x230")
app.title("Macro Manager by Bernso")


# Create a Notebook (tabs)
notebook = ttk.Notebook(app)
notebook.pack(fill="both", expand=True)

# Create tabs
macro_tab = ttk.Frame(notebook)
discord_tab = ttk.Frame(notebook)

# Add tabs to the Notebook
notebook.add(macro_tab, text="Macro")
notebook.add(discord_tab, text="Discord")

# Macro tab
mainLabel = tk.Label(macro_tab, text="Main Features")
mainLabel.grid(column=0, row=0, padx=10, pady=10, sticky="w")

helpButton = tk.Button(macro_tab, text="Help", command=helpMe)
helpButton.place(x=180, y=15, width=100, height=20)

edit_button = tk.Button(macro_tab, text="Edit Macro", command=edit_macro_file)
edit_button.grid(column=0, row=1, padx=10, pady=10, sticky="ew")

numberOfTimesToRunLabel = tk.Label(macro_tab, text="Number of times to run macro")
numberOfTimesToRunLabel.grid(column=0, row=2, padx=10, pady=0, sticky='w')

timesToComplete = tk.Entry(macro_tab, textvariable="Number of times for macro to run", width=45)
timesToComplete.grid(column=0, row=3, padx=10, pady=10, sticky="ew")

start_button = tk.Button(macro_tab, text="Start Macro", command=full_macro)
start_button.grid(column=0, row=4, padx=10, pady=10, sticky="ew")


# Discord tab
discordLabel = tk.Label(discord_tab, text="Discord Webhook URL")
discordLabel.grid(column=0, row=0, padx=10, pady=10, sticky="w")

webhookURL = tk.Entry(discord_tab, textvariable="Your Discord Webhook URL", width = 45)
webhookURL.grid(column=0, row=1, padx=10, pady=10, sticky="ew")

sendTestMessageButton = tk.Button(discord_tab, text="Send Test Message", command=send_to_discord_test)
sendTestMessageButton.grid(column=0, row=2, padx=10, pady=10, sticky="ew")

saveDiscordWebhookButton = tk.Button(discord_tab, text="Save Discord Webhook", command=save_discord_webhook)
saveDiscordWebhookButton.grid(column=0, row=3, padx=10, sticky='ew')

discordHelp = tk.Label(discord_tab, text="Join the discord for help: (click the link)\ndiscord.gg/k5HBFXqtCB")
discordHelp.bind("<Button-1>", open_discord)
discordHelp.grid(column=0, row=4, padx=10, pady=10, sticky="snew")

if __name__ == "__main__":
    app.mainloop()