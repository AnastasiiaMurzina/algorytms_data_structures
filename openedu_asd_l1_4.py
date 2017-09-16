with open('input.txt','r') as f:
    length = int(f.readline())
    array = list(map(lambda x: float(x),f.read().split()))
array = [ [array[j-1],j] for j in range(1, length+1)]
# print(array)
for i in range(length-1):
    j = i+1
    while j>0 and array[j][0]<array[j-1][0]:
        tmp = array[j]
        array[j]=array[j-1]
        array[j-1]=tmp
        j-=1
with open('output.txt','w') as f1:
    f1.write(str(array[0][1])+' '+str(array[length//2][1])+' '+str(array[-1][1]))
