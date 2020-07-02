from string import ascii_lowercase

NUM_LETTERS = len(ascii_lowercase)

print(ascii_lowercase)
print(NUM_LETTERS)

def count(string):
    ord_a = ord('a')

    freqs = [0]*NUM_LETTERS

    for c in string:
        freqs[ord(c) - ord_a] += 1

    result = []

    for spot in range(NUM_LETTERS-1):
        result.extend([chr(spot+ord_a)]*freqs[spot])

    print(freqs)
    print(result)
count("racecar")

string = "w' a"
print(len(string))

a = int('100110',2)
b = int('010001',2)
c = int('001001',2)

print(a&(b^c)==0)
print(a|b>32)
print(10/20)
# print(a)