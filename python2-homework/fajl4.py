with open("adat.txt", "r") as file:
    my_list = []
    for line in file:
        my_list.append(line)


with open("fajl4adat.txt", "w") as file2:
    file2.write(str(my_list))
