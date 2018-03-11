import random

lvl1 = "errrrrrbbbbbbww"
lvl2 = "errrrrrbbbbwwyy"
lvl3 = "errrrbbbbwwyygg"
lvl4 = "errrrbbwwyyggpp"
s = lvl4
s = ''.join(random.sample(s,len(s)))
print(s)



thefile = open('level4.txt', 'w')
length = 10
for index in range(0, length):
    s = (''.join(random.sample(s,len(s))))
    for i in range(len(s)):
        thefile.write(s[i] + ' ')
    thefile.write("\n")
