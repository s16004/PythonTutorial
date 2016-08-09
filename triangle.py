
h = int(input('高さを出力してください'))
"""
h
for i in range(1, h + 1):
    print('*' * i)
"""

for vertical in range(h + 1):
    for horizontal in range(vertical):
        if horizontal == 0 or horizontal == vertical - 1\
                or vertical == h:
            print('*', end='')
        else:
            print('+', end='')

    print()
