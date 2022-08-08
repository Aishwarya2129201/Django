UIN = input("Enter the string of numbers:")
array = list(map(int, list(UIN)))
sum = 0
sumD = []
for i in range(0,len(array)):
    
    if i % 2 == 0:
        array[i] *= 3

for i in array:     
    sumValue = 0       
    for digit in str(i):
        sumValue += int(digit)
    sumD.append(sumValue)
for i in range(len(sumD)):
    sum += sumD[i]
    
if sum %10 == 0:
    print("True")
else:
    print("False")
