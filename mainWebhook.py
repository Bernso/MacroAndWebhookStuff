import customtkinter as ctk
import requests

def send_to_discord(webhook_url, message):
    try:
        payload = {
            "content": f"{message}"
        }
        requests.post(webhook_url, json=payload)

        # Log Discord webhook message
        print("Message sent to Discord webhook.")
    except Exception as e:
        print(e)

webhook_url = "https://discord.com/api/webhooks/1236361210354597898/ntwpwERJ6nVJsoDQ8gfFgc3_ltZ2ls4SkYaHQVqtyNmp4F5BsIRuCvkg-ss4-m8ZmkkN"
def send_data():
    main_message = user_message.get("1.0", "end")
    for i in range(1, 11):
        message = f"{main_message} {i}"
        send_to_discord(webhook_url, message)
        
app = ctk.CTk()
app.geometry("500x350")
app.title("Discord Webhook Test")

user_message = ctk.CTkTextbox(app, scrollbar_button_color='black', scrollbar_button_hover_color='blue', activate_scrollbars=True, width=400)
user_message.pack(pady = 10)

send_button = ctk.CTkButton(app, text="Send Messages", command=send_data)
send_button.pack(padx=20, pady=20)

if __name__ == "__main__":
    app.mainloop()