#with open("adat.txt", "r") as file:
 #   my_list = []
  #  my_list.append(file.readlines())

with open("adat.txt", "r") as file:
    texts = file.readlines()
    my_list = []
    for i in texts:
        my_list.append(i.strip())

with open("fajl3adat.txt", "w") as file2:
    file2.write(str(my_list))

