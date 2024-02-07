import random
 
def calc(): 
     
    sampleList = [1,2]
 
    randomList = random.choices(
  sampleList, weights=(9,1), k=1)
    if randomList[0] == 1: 
        return 'No'
    elif randomList[0] == 2: 
        return 'Si'
    else: 
        return 'No'
