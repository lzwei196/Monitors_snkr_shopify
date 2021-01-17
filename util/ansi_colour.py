def magenta(msg):
    return f'\033[35m{msg}\033[0m'

def red(msg):
    return f'\033[31m{msg}\033[0m'

def green(msg):
    return f'\033[32m{msg}\033[0m'

def yellow(msg):
    return f'\033[33m{msg}\033[0m'

def blue(msg):
    return f'\033[34m{msg}\033[0m'

def cyan(msg):
    return f'\033[36m{msg}\033[0m'

def bright_blue(msg):
    return f'\033[94m{msg}\033[0m'

def test(msg):
    return f'\033[94m{msg}\033[0m'

if __name__ =='__main__':
    print(test('msg'))
    print(red('msg'))
