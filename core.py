import logging
import log
import com_slack
import csv_reader
import sys

logg = logging.getLogger('botlogger')


def main():
    logg.info('Start Bot')
    logg.info('read csv')
    in_logins = csv_reader.parse_email()
    logg.info('request all users in slack')
    all_users = com_slack.list_of_users()
    logg.info('request all users in channel')
    chanel_logins = com_slack.users_in_channel()
    logg.info('search unknown users')
    list_of_unknown_users = [x for x in in_logins if x not in [item[1] for item in all_users]]
    invite_users = [x for x in in_logins if (x not in chanel_logins) and (x not in list_of_unknown_users)]
    if invite_users == []:
        logg.info('no new user')
        print('no new user')
    else:
        logg.info('invite new users')
        com_slack.invite_to_channel([inv[0] for inv in all_users if inv[1] in invite_users])
    logg.info('Off Bot')
    sys.exit()


if __name__ == '__main__':
    main()
