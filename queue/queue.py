#implementaton of queue using list
queue = []

#add new elements 
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('b')

print('pused elements :', queue)

#remove exist element
queue.pop(0) #remove first element
queue.pop(0) #remove second element

print('after the first two elements removed ', queue)
