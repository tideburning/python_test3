import matplotlib.pyplot as plt
import numpy as np
from collections import defaultdict
import math
from datetime import datetime

# Tinh khoang cach gan nhat giua 2 ngay 
def min_dis_of_day(day1, day2):
    dis = 1000000
    for data1 in day1:
        for data2 in day2:
            #each position of a day is considered as a point
            disTemp = float(math.sqrt( (float(data2[0]) - float(data1[0]))**2 + (float(data2[1]) - float(data1[1]))**2  ) )
            if(disTemp < dis): dis = disTemp
    return dis

# find two day with the min distance
def min_dis_of_horse(horse):
    final_distance = 1000000000
    day1, day2 = 0, 0
    key = list(horse.keys())
    for i in range(len(key)- 1):
        day1 = key[i]
        for j in range(i):       
            day2 = key[j]
            disTemp = min_dis_of_day(horse[day1], horse[day2])
            if(disTemp < final_distance): 
                final_distance = disTemp
    return final_distance, day1, day2     


f1 = open ('output4.txt', 'w')


#read data and divine it into dictionary with key is the id of horse

horse_by_id = defaultdict(list)
#f = open('ZebraBotswana.txt' , 'r')
f = open('input.txt' , 'r')
for x in f:
    horse = x.split(",")
    horse[0] = datetime.fromtimestamp(float(horse[0])).strftime('%Y-%m-%d') 
    id = horse[3]                           
    horse_by_id[id].append(horse) 


# for each bt_id horse, divine each horse_by_time a position (long, latt) of a horse
for key in horse_by_id:
    horse_by_time = defaultdict(list)
    for horse in horse_by_id[key]:  
        viTri = [horse[1], horse[2]]
        time = horse[0]
        horse_by_time[time].append(viTri)
    #caculate the day that has the min distance
    lengh, day1, day2 = min_dis_of_horse(horse_by_time)
    result = str(key) + "//" +str(day1) + "/" +str(day2) + "/" + str(lengh) + "\n" +"=============================" + "\n"
    f1.write(result)


print("Done")