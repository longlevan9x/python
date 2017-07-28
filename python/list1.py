a = int(input("Nhap vao so phan tu mang "))
b = []
for i in range (0,a):
    print("a[",i,"] = ")
    b.append(int(input()))
print("Max = ",max(b))
print("Min = ",min(b))
print(b)
b.sort();
print(b)
b.reverse();
print(b)
c = 0
for i in range(0,len(b)-1):
    if (b[i] % 3 == 0):
        c  = c + b[i]
        print("So chia het cho 3",b[i])
print("Tông chia hét cho 3",c)
 
 
