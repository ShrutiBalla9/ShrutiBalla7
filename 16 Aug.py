num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


   #Check whether an alphabet is vowel or consonant using if..else statement - a,b,e,o
ch = input("Enter a character: ")
if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

#Write programm to calculate monthly simple intrest and compound intrest(5%/Month) on amount - 161258/-

    p=161258
    t=30
    r=5
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
      
    si = (p * t * r)/100
      
    print('The Simple Interest is', si)

    #Write programm to calculate to calculate monthly simple interest compound interest and compound interest(5% Month)on amount
    -161258
    p=161258r=5t=1 si=p*r*t*0.01 print("Si : ",si) Amount = p * (pow((1 + r / 100), t))ci =
     Amount - p print("Compound interest is", ci)
baseprice = 34900 GST =0.18 * baseprice print("GST =",GST)


#Write program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-
emi=161258
emi3=emi/(12*3)
emi5=emi/(12*5)
#print("\n Emi after 3 year without interest",emi3)
#print("\n Emi after 5 years",emi5)
emin3=emi3+((5/100)*emi3)
emin5=emi5+((5/100)*emi5)
print("\n Emi after 3 year with interest",emin3)
print("\n Emi after 5 years with interest",emin5) 
