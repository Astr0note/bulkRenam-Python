import os
import sys
import logger


pad = 0
args = sys.argv
nbrimg = 1

for i in range(0, len(args)):
    arg= args[i]
    print(arg)
    if arg == '-i':
        if i + 1 < len(args):
            path = args[i + 1]
            print(f'path= {path}')
            #If there is the "-i" argument, then we check if it is a correct path

        else:
            print('Something went wrong :( please enter a directory with file to rename')

    elif arg == '-p':
        if i + 1 < len(args):
            pad = int(args [i + 1])
            #If there is the "-p" argument, then we convert the next argument as an int to get a padding

        else:
            print('Something went wrong :( please enter a correct padding')

"""

Getting the necessary argument for the cli
param args = what the user will enter in the command line
param arg = treating the argument no matter is place on the command line


"""


for file in os.listdir(path):
    try:
        src = path + '/' + file  #We are getting into the folder with the file to rename in it
        dst = path + '/' + 'Art ' + str(nbrimg).zfill(pad) + '.jpg'  #We rename one file
        os.rename(src, dst)
        nbrimg += 1  #We pass to the next file
        print(src)
        print(dst)
        logger.log((f'file rename = {dst}'))
    except NameError as e:
        print('il manque quelque chose.')
    """
    Changing the name of the file in the directory
    :param file: image folder where all the file need to be rename
    :param os.listdir(): putting all file of the folder in a list
    """