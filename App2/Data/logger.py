import logging

logging.basicConfig(
            level=logging.INFO,
            format='%(message)s: %(asctime)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename='Data/app.log',
            filemode='a'
        )

def log_change(user, change):
    logging.info(f'{user}: {change}')