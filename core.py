import csv_reader, slack_reader,slack_user_invite

incom_logins = csv_reader.parse_email()
all_users = slack_reader.list_of_users()
chanel_logins = slack_reader.users_in_chanel()
list_of_unknown_users = [x for x in incom_logins if x not in [item[1] for item in all_users]]
invite_users = [x for x in incom_logins if (x not in chanel_logins) and (x not in list_of_unknown_users)]
slack_user_invite.invite_to_chanel([inv[0] for inv in all_users if inv[1] in invite_users])
