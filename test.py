s = input()
q = input()

for qi in range(q):
    command = input().split()

    if command[0] == 'print':
        a = int(command[1])
        b = int(command[2])
        print(s[a:b + 1])
    elif command[0] == 'reverse':
        s = s[:a] + s[a:b + 1][::-1] + s[b + 1:]
    else:
        p = command[3]
        s = 
