import slack, os, ssl, certifi
from pathlib import Path
from dotenv import load_dotenv


def invite_to_chanel(users):
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)
    channel_id = 'C03RNUN0ELB'
    response = client.conversations_invite(
        channel=channel_id,
        users=users)
