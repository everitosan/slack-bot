"""
This is the main module
"""

# Python
from pathlib import Path
from os import environ

# Slack
from slackclient import SlackClient

# Dotenv
from dotenv import load_dotenv

load_dotenv()


def main():
    slack_token = environ.get("TOKEN")
    slack_client = SlackClient(slack_token)
    slack_client.api_call("chat.postMessage", channel="general", text="Hi")


if __name__ == "__main__":
    main()
