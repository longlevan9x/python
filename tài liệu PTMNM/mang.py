#nhap mang
n=int(input("Nhap so phan tu cua mang n="))
a=[]
for i in range(0,n):
          print("a[",i,"]=")
          a.append(int(input()))
print("mang a=",a)
#sap xep tang dan
a.sort()
print("mang sap xep theo thu tu tang dan a=",a)
#sap xep giam dan
a.reverse()
print("mang sap xep theo thu tu giam dan a=",a)
#phan tu lon nhat
print("phan tu lon nhat =",max(a))
#phan tu nho nhat
print("phan tu nho nhat =",min(a))
#tong (tich) cac so chan(le).v.v.
s=0
for i in range(0,n):
           if (a[i]%2)==0:
                      s=s+a[i]
print("tong cac so chan =",s)
#so ngyen to cach 1
for i in range(0,n):
           dem=0
           for j in range(1,a[i]+1):
                      if ((a[i]%j)==0):
                                 dem=dem+1
           if(dem==2):
                      print(a[i])
# so nguyen to cach 2
def sont(x):
           if(x==2):
                      return 1
           elif(x>2):
                      for i in range(2,x):
                                 if(x%i==0):
                                            return 0
                                            break
                      return 1
           else:
                      return 0
for i in range(0,n):
           if (sont(a[i])==1):
                      print(a[i])

#xoa phan tu trung nhau
a=set(a)
print("mang da xoa phan tu giong nhau =",a)
