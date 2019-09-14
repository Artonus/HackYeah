import re

class Parser:
    clockwise_re = re.compile(r'^CLOCKWISE (\d{1,3})$', re.IGNORECASE)
    counterclockwise_re = re.compile(r'^COUNTERCLOCKWISE (\d{1,3})$', re.IGNORECASE)
    stop_re = re.compile(r'^STOP$', re.IGNORECASE)
    speed_re = re.compile(r'^SPEED (\d{1,2})$', re.IGNORECASE)
    pause_re = re.compile(r'^PAUSE (\d{1,5})$', re.IGNORECASE)
    base_re = re.compile(r'^BASE$', re.IGNORECASE)

    def parse_file(file_path):
        with open(file_path, 'r') as f:
            commands = f.readlines()
            for command in commands:
                __parse_user_input(command)
                
    def __parse_user_input(user_input):
        if self.clockwise_re.search(user_input):
                degrees = int(self.clockwise_re.search(user_input).group(1))
                print('clockwise {} degrees'.format(degrees))
        elif self.counterclockwise_re.search(user_input):
            degrees = int(self.counterclockwise_re.search(user_input).group(1))
            print('counterclockwise {} degrees'.format(degrees))
        elif self.stop_re.search(user_input):
            print('bye')
            break
        elif self.speed_re.search(user_input):
            speed = int(self.speed_re.search(user_input).group(1))
            print('set speed {}'.format(speed))
        elif self.pause_re.search(user_input):
            pause = int(self.pause_re.search(user_input).group(1))
            print('pause {}'.format(pause))
        elif self.base_re.search(user_input):
            print('base')
        else:
            print('Unknown command')

    def start(self):
        while True:
            user_input = input('> ')
            self.__parse_user_input(user_input)
    
if __name__ == '__main__':
    parser = Parser()
    parser.start()
