import slack, os, ssl, certifi
from pathlib import Path
from dotenv import load_dotenv
from slack.errors import SlackApiError

# global
ssl_context = ssl.create_default_context(cafile=certifi.where())
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)
all_users_store = {}


def users_in_chanel():
    channel_id = 'C03RNUN0ELB'
    result = client.conversations_members(channel=channel_id)
    addname = []
    for user in result['members']:
        info = client.users_info(user=user).data
        if 'real_name' in info['user']['profile'].keys():
            addname.append(info['user']['profile']['real_name'])
    return addname


def save_users(users_array):
    for user in users_array:
        user_id = user["id"]
        all_users_store[user_id] = user


def get_all_users():
    try:
        result = client.users_list()
        save_users(result["members"])
    except SlackApiError as e:
        f'Error creating conversation: {e}'
    return all_users_store


def list_of_users():
    get_all_users()
    mykeys = ['id', 'real_name']
    list_of_users = []
    for item in all_users_store.keys():
        mydict = all_users_store.get(item)
        list_of_users.append([mydict[k] for k in mykeys if k in mydict])
    return list_of_users
