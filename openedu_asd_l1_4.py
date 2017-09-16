with open('input.txt','r') as f:
    length = int(f.readline())
    array = list(map(lambda x: float(x),f.read().split()))
positions=[i for i in range(1,length+1)]
for i in range(length-1):
    j = i+1
    while j>0 and array[j]<array[j-1]:
        tmp = array[j]
        array[j]=array[j-1]
        array[j-1]=tmp
        tmp_extra = positions[j]
        positions[j]=positions[j-1]
        positions[j-1]=tmp_extra
        j-=1
with open('output.txt','w') as f1:
    f1.write(str(positions[0])+' '+str(positions[length//2])+' '+str(positions[-1]))
