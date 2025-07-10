import requests
import time

def set_discord_status(token, status):
    url = "https://discord.com/api/v9/users/@me/settings" # Use https://discord.com/api/v8/users/@me/settings to use the v8 api
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    data = {
        "status": visibility,
        "custom_status": {
            "text": status,
        },
        "show_current_game": game_status
    }
    response = requests.patch(url, headers=headers, json=data)
    
    if response.status_code == 200:
        print(f"Status Updated: {status} - {visibility} - Game Activity {game_status}")
    else:
        print(f"Failed to update status... Error Code: {response.status_code} - {response.text}")

token = "token" # Put your token here
status = "Hello World!"
game_status = True # Set to true to show current game
visibility = "online"  # Can be 'idle', 'dnd', 'invisible', or 'online'

set_discord_status(token, status)
