userValidated = True
userlen = 0
Alphalist = [("0",2),("1",3),("2",5),("3",7),("4",11),("5",13),("6",17),("7",19),("8",23),("9",29),("a",31),("b",37),("c",41),("d",43),("e",47),("f",53),("g",59),("h",61),("i",67),("j",71),("k",73),("l",79),("m",83),("n",97),("o",101),("p",103),("q",107),("r",109),("s",113),("t",127),("u",131),("v",137),("w",139),("x",149),("y",151),("z",157),("-",163),("_",167),("!",173),("£",179),("$",181),("%",191),("^",193),("&",197),("*",199),("#",211),(",",223),(";",227),(".",229),("@",233),(":",239)]
userIntList = []
validList = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","-","_","!","£","$","%","^","&","*","#",",",";",".","@",":"]
userPosXCharList = []

#Below this block of code acts as valiation for a username, where a username must be between 10 and 15 characters long, and can only contain alphanumeric characters(no symbols)

while userValidated == True:
    inuser = str(input("Please input a username "))
    username = inuser.lower()
    for char in range(0,len(username)):
        if username[char] not in validList:
            print("please put in a valid username")
            break
        elif len(username) < 10 or len(username) > 15:
            print("please put in a username that is in between 10 and 15 characters")
            break
        else:
            userlen += 1
    if userlen == len(username):
        userValidated = False
#Below the code goes through each character of the username, and converts it into its numeric value, using the list "Alphalist".
for char in range(0, len(username)):
    for string in range(0,len(Alphalist)):
        if username[char] == Alphalist[string][0]:
            userIntList.append(Alphalist[string][1])
        else:
            continue
#Multipling each character's value by it's position in the list plus one, adding to userPosXCharList.
position = 1
for integer in range(0,len(userIntList)):
    hexval = userIntList[integer] * position
    userPosXCharList.append(hexval)
    position += 1
# Sums up all of the new values for each character, and converts that number into a hexidecimal.
userdenint = sum(userPosXCharList)
userfinalhex = hex(userdenint)
print(username, userIntList, userPosXCharList, userdenint,userfinalhex)


passValidated = True
passlen = 0
passIntList = []
passPosXCharList = []
#validation, the password must be made of characters and valid numbers, and must be in btween 10 and 15 characters long
while passValidated == True:
    inpass = str(input("Please Input a password that is in between 10 and 15 characters "))
    password = inpass.lower()
    for char in range(0,len(password)):
        if password[char] not in validList:
            print("please put in a valid password")
            break
        elif len(password) < 10 or len(password) > 15:
            print("please put in a password that is in between 10 and 15 characters")
            break
        else:
            passlen += 1
    if passlen == len(password):
        passValidated = False
#turning character into assorted numbers
for char in range(0, len(password)):
    for string in range(0,len(Alphalist)):
        if password[char] == Alphalist[string][0]:
            passIntList.append(Alphalist[string][1])
        else:
            continue
#Multipling the char value by it's position in the list plus one, adding to passPosXCharList.
position = 1
for integer in range(0,len(passIntList)):
    hexval = passIntList[integer] * position
    passPosXCharList.append(hexval)
    position += 1
#adding all of the hexvalues in the list together to get a singular number., then converting taht into a hexadecimal
passdenint = sum(passPosXCharList)
passfinalhex = hex(passdenint)
print(password, passIntList, passPosXCharList, passdenint,passfinalhex)