def timkiem(word, letter):
    index=0
    while index < len(word):
        if word[index] == letter:
                print(index,"vi tri can tim")
        else:
            print(index,"khong xuat hien tu can tim")
        index=index+1
    else:
        print("ket thuc viec tim kiem")
if __name__ =='__main__':
    tiep=input("Co tiep tuc khong Y/N?")
    while tiep=="y":
        m=input("nhap chuoi:")
        n=input("nhap tu can tim:")
        timkiem(m,n)                                                                
        tiep=input("Co tiep tuc khong Y/N?")
    else:
        print(" khong tim kiem")
