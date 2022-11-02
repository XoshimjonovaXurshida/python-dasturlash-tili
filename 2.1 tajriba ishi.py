n=int(input("n-qiymatini kiriting "))
if(n<100 or n>999):
    print("Kiritilgan son 3 xonali emas!")
else:
    a2=n//100
    a1=(n%100)//10
    a0=n%10
    if(a2>a1 and a2>a0 and a1>a0): print("Berilgan son raqamlari o'zaro kamayuvchi")
    elif(a2<a1 and a2<a0 and a1<a0): print("Berilgan son raqamlari o'zaro o'suvchi")
    elif(a2==a1 and a2==a0 and a1==a0): print("Berilgan son raqamlari o'zaro teng")
    else: print("Berilgan son raqamlari o'suvchi ham kamayuvchi ham emas")