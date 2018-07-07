

def log(message, mode='a+', file='log.txt'):
    with open(file, mode) as f:
        print(message, file=f)
