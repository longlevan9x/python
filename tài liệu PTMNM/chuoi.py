s=input("nhap chuoi s=")
#nhap chuoi ho ten va in moi ten tren 1 dong
s3=s.split()
for i in range(0,len(s3)):
           if (s3[i]!=" "):
                     print(s3[i])
           else:
                      print("\n")           
#dao chuoi
dt=s[::-1]
print("chuoi dao:",dt)
#xoa khoang trang dau dong
s=s.lstrip()
print("xoa khoang trang dau dong:",s)
#xoa khoang trang cuoi dong
s=s.rstrip()
print("xoa khoang trang cuoi dong:",s)
#xoa khoang trang dau va cuoi dong
s=s.strip()
print("Xoa khoang trang dau va cuoi dong:",s)
# kiem tra s1 co trong s=????
s1=input("nhap chuoi s1=")
st=s.find(s1,0,len(s))
if st==-1:
   print("khong co s1 trong s")
else:
   print("chuoi'", s1,"'xuat hien tai vi tri",st,"trong chuoi'", s,"'")
#xoa tat cac khoang trang trong chuoi s(cach 1)
s2=""
for i in range(0,len(s)):
           if (s[i]!=" "):
                      s2=s2+s[i]
s=s2
print(s)
#xoa tat cac khoang trang trong chuoi s(cach 2)
s=s.replace(" ","")
print(s)
#chuyen chuoi s thanh chu hoa
ch=s.upper()
print("CHUOI S HOA:",ch)
#chuyen chuoi s thanh chu thuong
ct=s.lower()
print("chuoi s thuong:",ct)
#chuyen chu cai i bat ky trong chuoi s thanh chu hoa
      

