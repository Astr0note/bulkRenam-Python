
log_file = 'rename.log'

def log(msg):
    with open(log_file, 'a') as f:
        f.write(msg + '\n')