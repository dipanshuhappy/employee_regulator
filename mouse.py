import pickle
def write_to_file(positions):
    with open('mouse_activity.txt','wb') as mouse_file:
        pickle.dump(positions,mouse_file)
def get_total_mouse_moves():
    with open('mouse_activity.txt','rb') as mouse_file:
        positions:list=pickle.load(mouse_file)
        return len(positions)
