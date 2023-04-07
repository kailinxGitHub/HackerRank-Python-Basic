list = []
command = str(input())
split_command = command.split()
if split_command[0] == "insert":
    vari = int(split_command[1])
    vare = int(split_command[2])
    list.insert(vari, vare)
    print(list)