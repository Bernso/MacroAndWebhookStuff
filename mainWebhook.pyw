import customtkinter as ctk
import requests

def send_to_discord():
    try:
        main_message = user_message.get("1.0", "end")
        webhook_url = webhook_url_entry.get()
        payload = {
            "content": f"{main_message}"
        }
        requests.post(webhook_url, json=payload)

        # Log Discord webhook message
        print("Message sent to Discord webhook.")
    except Exception as e:
        print(e)



        
app = ctk.CTk()
app.geometry("500x350")
app.title("Discord Webhook Test")

user_message = ctk.CTkTextbox(app, scrollbar_button_color='black', scrollbar_button_hover_color='blue', activate_scrollbars=True, width=400)
user_message.pack(pady = 10)

webhook_url_entry = ctk.CTkEntry(app, placeholder_text='Webhook URL')
webhook_url_entry.pack(pady = 10)

send_button = ctk.CTkButton(app, text="Send Messages", command=send_to_discord)
send_button.pack(padx=20, pady=20)

if __name__ == "__main__":
    app.mainloop()