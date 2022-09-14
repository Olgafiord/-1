def bin(list, guess, start, stop) :
    if start > stop:
        return False
    else: 
        mid = (start + stop) //2
        if guess == list[mid]:
            return mid
        elif guess < list[mid]:
            return bin(list, guess, start, mid-1 )
        else:
            return bin(list, guess, mid+1, stop )
  
 

start = 1
stop = 101


list = range(start, stop)

guess = 4

prav = bin(list, guess, start, stop)

if prav == False:
    print ('num', guess, 'is not found')
else:
    print('num', guess, 'found')
