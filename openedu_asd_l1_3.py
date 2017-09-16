with open('input.txt','r') as f:
    length = int(f.readline())
    array = list(map(lambda x: int(x),f.read().split()))
positions=[1]
for i in range(length-1):
    j = i+1
    while j>0 and array[j]<array[j-1]:
        tmp = array[j]
        array[j]=array[j-1]
        array[j-1]=tmp
        j-=1
    positions.append(j+1)

with open('output.txt','w') as f1:
    f1.write(' '.join([str(i) for i in positions]))
    f1.write('\n')
    f1.write(' '.join([str(i) for i in array]))