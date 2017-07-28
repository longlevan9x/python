def khoitao():
    a=[]
    return a
def xuat(s,a = []):
    for i in range(0,s):
        print("a[",i,"]=")
        s = input()
        while s.isnumeric() == False:
            print("a[",i,"]=")
            s = input()
            continue
        a.append(int(s))
    return a

def nhap():
    s = input("Nhap vao so phan tu mang: ")
    while s.isnumeric() == False:
        s = input("Nhap lai so phan tu mang: ")
        continue
    return int(s)
def giatrimax(a = []):
    print("GT lon nhat = ",max(a),", Vi tri cua gia tri lon nhat = ",a.index(max(a)))
def tinhTong(a = []):
    tongLe = 0
    tongChan = 0
    chia2 = 0
    chia3 = 0
    for i in range(0,len(a)):
        if a[i] % 2 == 0:
            tongChan = tongChan + a[i]
        else:
            tongLe = tongLe + a[i]
        if a[i] % 3 == 0:
            chia3 += a[i]
    print("Tong so chan: ",tongChan)
    print("Tong so le: ",tongLe)
    print("Tong so chia het cho 3: ",chia3)
def tinhTich(a = []):
    tichLe = 1
    tichChan = 1
    chia3 = 1
    for i in range(0,len(a)):
        if a[i] % 2 == 0:
            tichChan = tichChan * a[i]
        else:
            tichLe = tichLe * a[i]
        if a[i] % 3 == 0:
            chia3 *= a[i]
    print("Tich so chan: ",tichChan)
    print("Tich so le: ",tichLe)
    print("Tich so chia het cho 3: ",chia3)
def sont(a = []):
    soChan = 0
    soLe = 0
    for i in range(0,len(a)):
        if a[i] < 2:
            continue
        if i > 0:
            if a[i] % i == 0:
                continue
            else:
                print(a[i])
                if a[i] % 2 == 0:
                    soChan += a[i]
                else:
                    soLe += a[i]
    print(soChan)
    print(soLe)
def main():
    a = khoitao()
    s = nhap()
    c = xuat(s,a)
    giatrimax(c)
    tinhTong(c)
    tinhTich(c)
    sont(c)
if __name__ == '__main__':
    main()
