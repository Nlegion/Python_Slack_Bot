import com_slack
import csv_reader

incom_logins = csv_reader.parse_email()
all_users = com_slack.list_of_users()
chanel_logins = com_slack.users_in_channel()
list_of_unknown_users = [x for x in incom_logins if x not in [item[1] for item in all_users]]
invite_users = [x for x in incom_logins if (x not in chanel_logins) and (x not in list_of_unknown_users)]
com_slack.invite_to_channel([inv[0] for inv in all_users if inv[1] in invite_users])
