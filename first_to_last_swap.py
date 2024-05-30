import sys
input = sys.stdin.readline
gi = lambda: list(map(int, input().split()))
gs = lambda: list(input().split())

t = int(input().strip()) 
for _ in range(t):
    n = int(input().strip()) 
    a = gi()  
    a[0],a[n-1] = a[n-1],a[0]
    print(' '.join(map(str, a)))  

#--------------Approach-1-----------
# def swapList(l):
#     a, *b, c = l
#     l = [c, *b, a]
#     return l
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))


#--------------Approach-2-----------
# def swapList(list):
#     first = list.pop(0)   
#     last = list.pop(-1)
#     list.insert(0, last)  
#     list.append(first)   
    
#     return list
    
# # Driver code
# newList = [12, 35, 9, 56, 24]
# print(swapList(newList))

#--------------Approach-3-----------
# def swapPositions(lis, pos1, pos2):
#     for i, x in enumerate(lis):
#         if i==pos1:
#             elem1 = x
#         if i == pos2:
#             elem2 = x
#     lis[pos1] = elem2
#     lis[pos2] = elem1
#     return lis

# List = [23, 65, 19, 90]
# pos1, pos2 = 1, 3
# print(swapPositions(List, pos1-1, pos2-1))