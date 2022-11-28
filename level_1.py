import string
# string module - for number and ascii values
letter = string.ascii_lowercase
s = string.punctuation

change_string = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. 
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

# abcdefghijklmnopqrstuvwxyz
alphabet = dict()
swap = {}
punch = {}

# enumerate - it give the count and values
for count, values in enumerate(letter, start=1):
    alphabet[count]=values
    swap[values]=count

for count, values in enumerate(s, start=100):
    punch[count] = values

print(punch)


alphabet[200] = ' '
swap[200] = ' '

number = list()
for letter in change_string:
    if letter in swap:
        number.append(swap[letter]+2)
    elif letter in punch:
        number.append(swap[letter])
    else:
        number.append(200)


# print(number)
# print(alphabet)
# print(swap)

for name in number:
    if name == 200:
        print(alphabet[name], end='')
    elif name >= 100:
        print(punch[name], end='')
    elif name >= 26 and name < 100:
        name = name - 26
        print(alphabet[name], end='')
    else:
        print(alphabet[name], end='')

# check = 'udayakumarz'

# abcdefghijklmnopqrstuvwxyz
