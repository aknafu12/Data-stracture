#implementation of stack using list
in_put = int(input('enter size of list :'))
#out_data = int(input('how many elemet do u want delete : '))


stack = []
for i in range(in_put):
    #push data to stack
    stack.append(i)

print('pushed',stack)
#pop or delet from stack
for j in range(1,in_put-1):
    remv = stack.pop()
    print(f"poped {j} element {remv}")

print(' the remain elements after poped',stack)
    
