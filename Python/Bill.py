# program to input quantity and print out bill

print("Chirstmas Tree: 1,200 \n Fairy Lights: 350 \n Santa hats: 150 \n Gift Boxes: 500 \n Candles: 200 \n Decorative Balls: 250")

try: 
    nC = int(input("Enter the number of chemistry: ")) #stores the number of chirstmas tree
    nF = int(input("Enter the number of fairy lights: ")) #stores the number of fairy lights
    nS = int(input("Enter the number of santa hats: ")) #stores the number of santa hats 
    nG = int(input("Enter the number of gift boxes: ")) #stores the number of gift boxes 
    nCd = int(input("Enter the number of candles: ")) #stores the number of candles 
    nD = int(input("Enter the number of Decorative Balls: ")) #stores the number of decorative balls 

except:
    print("Invalid input")

Total_Bill = ((1200*nC)+(350*nF)+(150*nS)+(500*nG)+(200*nCd)+(250*nD))

if Total_Bill<=5000:
    print("No discount allowed")
    print(f"Total bill to be payed:{Total_Bill}")
elif Total_Bill>5000 and Total_Bill<=10000:
    print("Discount allowed:5%")
    print(f"Total Bill:{Total_Bill-0.05*Total_Bill}") 
elif Total_Bill>10000 and Total_Bill<=15000:
    print("Discount allowed:10%")
    print(f"Total Bill:{Total_Bill-0.1*Total_Bill}")
elif Total_Bill>15000:
    print("Discount allowed:15%")
    print(f"Total Bill:{Total_Bill-0.15*Total_Bill}")
