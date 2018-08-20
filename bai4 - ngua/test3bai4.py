from collections import defaultdict
import matplotlib.pyplot as plt
from datetime import datetime
import math

#read data and divine it into dictionary with key is the id of horse

horse_by_id = defaultdict(list)
f = open('ZebraBotswana.txt' , 'r')
for x in f:
    horse = x.split(",")
    horse[0] = datetime.fromtimestamp(float(horse[0])).strftime('%Y-%m-%d') 
    id = horse[3]                           
    horse_by_id[id].append(horse) 

# ve ban do duong di cua moi con ngua
color = ['r','b','g','k','c','y','m']
index = 0
for key in horse_by_id.keys():
    x, y = [], []
    index -= 1
    c =  color[index] 
    for i in horse_by_id[key]:
        x.append(float(i[1]))
        y.append(float(i[2]))    
    sorted(x)
    sorted(y)
    plt.plot(x, y, c = c, label = key)
plt.legend()
plt.show()






