import slack, os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('../bot') / '.env'
load_dotenv(dotenv_path=env_path)

client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
# client.chat_postMessage(channel='#test__2', text='Hello Wolrd!')

channel_id = 'C03RNUN0ELB'
result = client.conversations_members(channel=channel_id)
addname = []
for user in result['members']:
    info = client.users_info(user=user).data
    # print(info)
    if 'real_name' in info['user']['profile'].keys():
        addname.append(info['user']['profile']['real_name'])
print(addname)
