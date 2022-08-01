import logging

log = logging.getLogger('botlogger')
settings = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")
filehandler = logging.FileHandler('slackbot.log', encoding='utf-8')
filehandler.setFormatter(settings)
log.addHandler(filehandler)
log.setLevel(logging.INFO)

if __name__ == '__main__':
    stream = logging.StreamHandler()
    stream.setFormatter(settings)
    log.addHandler(stream)
    # Test message
    log.info('Отладочное сообщение')
