import os
import ssl
from pathlib import Path

import certifi
import slack
from dotenv import load_dotenv
from slack.errors import SlackApiError

# global
ssl_context = ssl.create_default_context(cafile=certifi.where())
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'], ssl=ssl_context)
all_users_store = {}
channel_id = 'C03RNUN0ELB'


# get a list of users in channel
def users_in_channel():
    try:
        result = client.conversations_members(channel=channel_id)
        addname = []
        for user in result['members']:
            info = client.users_info(user=user).data
            if 'real_name' in info['user']['profile'].keys():
                addname.append(info['user']['profile']['real_name'])
        return addname
    except SlackApiError as e:
        print(f'Error fetching conversations: {e}')


# save all users in workspace to the dic
def save_users(users_array):
    for user in users_array:
        user_id = user["id"]
        all_users_store[user_id] = user


# get list of all users
def get_all_users():
    try:
        result = client.users_list()
        save_users(result["members"])
        return all_users_store
    except SlackApiError as e:
        print(f'Error creating conversation: {e}')


# dict of all users to the list
def list_of_users():
    get_all_users()
    mykeys = ['id', 'real_name']
    list_of_users = []
    for item in all_users_store.keys():
        mydict = all_users_store.get(item)
        list_of_users.append([mydict[k] for k in mykeys if k in mydict])
    return list_of_users


# invite Users fron incom list
def invite_to_channel(users):
    try:
        response = client.conversations_invite(
            channel=channel_id,
            users=users)
        return print(f'Success! {len(users)} user added.')
    except SlackApiError as e:
        print(f'Error invite users of list: {e}')
