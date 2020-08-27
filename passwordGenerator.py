import random
import string

# populate lists and init variables
alpha_list = []
num_list = []
final_password = []
for i in range(len(string.ascii_lowercase)):
    alpha_list.append(string.ascii_lowercase[slice(i, i + 1)])
for i in range(10):
    num_list.append(i)
letterNum = 0
numberNum = 0
inWay = 1

#collect user input
while inWay == 1:
    passLength = int(input('How long would you like the password? (min 6)'))
    while passLength < 6:
        print('Error, not enough characters.')
        passLength = int(input('How long would you like the password? (min 6)'))

    letterNum = int(input('How many letters should the password contain?'))
    while letterNum > passLength:
        print('Error, too many letters')
        letterNum = int(input('How many letters should the password contain?'))

    numberNum = int(input('How many numbers should the password contain?'))
    while numberNum > passLength:
        print('Error, to many numbers')
        numberNum = int(input('How many numbers should the password contain?'))
    if numberNum + letterNum == passLength:
        inWay = 0
    else:
        print('The password cannot be made, restart and check values')

def check_exceed_length(list):
    if len(list) > passLength:
        list = list[:passLength]
    str1 = ''.join(str(e) for e in list)
    print(str1)

#less code with similar output
def quick_random(size = 7, chars = string.ascii_lowercase + string.digits +string.ascii_uppercase):
    print(''.join(random.choice(chars) for i in range(size)))

for i in range(letterNum):
    charCount = random.randint(0, len(alpha_list)-1)
    char = alpha_list[int(charCount)]
    final_password.insert(charCount, char)
for i in range(numberNum):
    NumaCount = random.randint(0, len(num_list)-1)
    Numa = num_list[int(NumaCount)]
    final_password.insert(NumaCount, Numa)

check_exceed_length(final_password)
quick_random() #quicker random with less control
quick_random(20)

