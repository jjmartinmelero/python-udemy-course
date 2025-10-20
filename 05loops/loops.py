
MAX_VALUE = 5
index = 0

# while
while index <= MAX_VALUE:
    print(index)
    index+=1


# for
for index in range(5):
    print(index)

# iterate str
str = "Hello world !"

for character in str:
    print(character)


# for - accumulated sum

total = 0

for index in range(6):
    print(total, index)
    total += index

print(total)