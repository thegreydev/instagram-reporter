from instagrapi import Client
import os

# Instagram credentials (replace with your credentials)
USERNAME = 'your_instagram_username'
PASSWORD = 'your_instagram_password'

# Create an instance of the client
client = Client()

# Login and save the session
def login_and_save_session():
    session_file = 'instagram_session.json'

    # Check if the session file exists
    if os.path.exists(session_file):
        # Load session from the file
        client.load_settings(session_file)
        client.login(USERNAME, PASSWORD)
    else:
        # Login if session file doesn't exist
        client.login(USERNAME, PASSWORD)
        # Save the session
        client.dump_settings(session_file)
        print("Logged in and session saved.")

login_and_save_session()
