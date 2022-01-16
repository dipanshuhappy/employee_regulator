import pickle
from turtle import position
def write_to_file(positions):
    with open('mouse_activity.txt','wb') as mouse_file:
        pickle.dump(positions,mouse_file)
positions:set=pickle.load(open('mouse_activity.txt','rb'))
print(len(positions))