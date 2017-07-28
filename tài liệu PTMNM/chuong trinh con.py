def khoitao():
        a=[]
        return a
def sopt():
        s = input("Nhap vao so phan tu mang: ")
        while s.isnumeric() == False:
                s = input("Nhap lai so phan tu mang: ")
                continue
        return int(s)
def nhapgt(a,n):
        for i in range(0,n):
                print("a[",i,"]=")
                n = input()
                while n.isnumeric() == False:
                    print("a[",i,"]=")
                    n = input()
                    continue
                a.append(int(n))
        return a
def ingt(a):
        return print(a)
def sont():
        for i in range(0,n):
                dem=0
                for j in range(1,a[i]+1):
                        if ((a[i]%j)==0):
                                dem=dem+1
                if(dem==2):
                        #if (a[i]%10)==3:
                        print(a[i])


def gtln():
        return print("GTLN=",max(a))
def tongchan():
        s=0
        for i in range(0,n):
           if (a[i]%2)==0:
                      s=s+a[i]
        return print("Tong chan=",s)
def main():
        a=khoitao()
        n=sopt()
        nhapgt(a,n)
        ingt(a)
        sont()
        gtln()
        tongchan()
if __name__=='__main__':
           main()
           

           
