v = ["a", "e", "i", "o", "u"]
r = input()
vogais = []
while not(len(r) <= 50):
    r = input()
for i , id in enumerate(r):
    if id in v:
        vogais.append(id)
if vogais == vogais[::-1]:
    print('S')
else:
    print('N')

