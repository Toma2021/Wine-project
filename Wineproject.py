import csv

with open("data.csv", "r") as csv_file:
    my_file = csv_file.read()
    my_list = my_file.splitlines()
    list_columns = []
    my_data = []
    for i in range(len(my_list)):
        if i == 0:
            list_columns = my_list[0].split(',')
        else:
            l = {
                list_columns[0]: my_list[i].split(',')[0],
                list_columns[1]: my_list[i].split(',')[1],
                list_columns[2]: my_list[i].split(',')[2],
                list_columns[3]: my_list[i].split(',')[3],
                list_columns[4]: my_list[i].split(',')[4],
                list_columns[5]: my_list[i].split(',')[5]
            }
            my_data.append(l)


class Person:
    def __init__(self, name, age, event, liked):
        self.name = name
        self.age = age
        self.event = event
        self.liked = liked

    def drink(self):
        print(f"{self.name}is drinking")


for user in my_data:
    for other in my_data:
        if user[list_columns[0]] == other[list_columns[0]] and user[list_columns[1]] == other[list_columns[1]] and user[list_columns[5]] != other[list_columns[5]]:
            print(f"User {user[list_columns[0]]} {user[list_columns[1]]} is already in list")
