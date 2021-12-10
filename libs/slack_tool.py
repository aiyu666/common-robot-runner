import fire
import logging
from slack_sdk import WebClient

logging.basicConfig(level=logging.INFO)


class slackWebClientTool:
    def __init__(self, bot_token: str):
        self.client = WebClient(token=bot_token)

    def post_message(self, channel_id: str, message: str):
        _ = self.client.chat_postMessage(channel=channel_id, text=message)
        logging.info(f"Post message to channel {channel_id}")

    def get_channel_id_by_name(self, channel_name: str):
        resp = self.client.conversations_list()
        channel = [ch for ch in resp["channels"] if ch["name"] == channel_name]
        logging.debug(channel)
        if len(channel) > 1:
            raise ValueError(
                f"""Get more than one result when search with name:
                {channel_name}"""
            )
        elif channel:
            return channel[0]["id"]
        else:
            raise ValueError(f"Cound not find channel name: {channel_name} ")


if __name__ == "__main__":
    fire.Fire(slackWebClientTool)
