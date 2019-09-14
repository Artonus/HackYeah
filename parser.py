import re


clockwise_re = re.compile(r'^CLOCKWISE (\d{1,3})$', re.IGNORECASE)
counterclockwise_re = re.compile(r'^COUNTERCLOCKWISE (\d{1,3})$', re.IGNORECASE)
stop_re = re.compile(r'^STOP$', re.IGNORECASE)
speed_re = re.compile(r'^SPEED (\d{1,2})$', re.IGNORECASE)
pause_re = re.compile(r'^PAUSE (\d{1,5})$', re.IGNORECASE)
base_re = re.compile(r'^BASE$', re.IGNORECASE)
while True:
    user_input = input('> ')
    if clockwise_re.search(user_input):
        degrees = int(clockwise_re.search(user_input).group(1))
        print('clockwise {} degrees'.format(degrees))
    elif counterclockwise_re.search(user_input):
        degrees = int(counterclockwise_re.search(user_input).group(1))
        print('counterclockwise {} degrees'.format(degrees))
    elif stop_re.search(user_input):
        print('stop')
    elif speed_re.search(user_input):
        speed = int(speed_re.search(user_input).group(1))
        print('set speed {}'.format(speed))
    elif pause_re.search(user_input):
        pause = int(pause_re.search(user_input).group(1))
        print('pause {}'.format(pause))
    elif base_re.search(user_input):
        print('base')
    else:
        print('Unknown command')
