#ReadMe.txt, Pg 227 Q7.
#Saatvik Kambhampati
#17/10/2020

OTP = list(input("Please input the One-Time Pad: "))
PlainText = list(input("Please input the plaintext: "))

#Converting each character of plaintext into it's UTF counter part, then into Binary.
for i in range(len(PlainText)):
  UTF = int(ord(PlainText[i])) 
  Binary = str(bin(UTF))[2:] #The "[2:] removes the first 2 chars in the string, so it removes "0b" from the binary number.
  PlainText[i] = int(Binary)

#This for loop does the same thing as above, only with the OTP list.
for i in range(len(OTP)):
  UTF = int(ord(OTP[i]))
  Binary = str(bin(UTF))[2:]
  OTP[i] = int(Binary)
