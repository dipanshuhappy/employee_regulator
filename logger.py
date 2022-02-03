from pynput.keyboard import Key, Listener
count=0
keys=[]
numbers_of_clicks=0

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
    global numbers_of_clicks
    with open("file.txt", "w") as f:
        for key in keys:
            numbers_of_clicks+=1
            f.write(str(numbers_of_clicks))

def release(key):
    if key==Key.esc:
        return False
def listen_to_keyboard():
    listener=Listener(on_press=clicked,on_release=release)
    listener.start()
def get_total_keyboard_clicks():
    with open("file.txt",'r') as f:
        return int(f.read())

