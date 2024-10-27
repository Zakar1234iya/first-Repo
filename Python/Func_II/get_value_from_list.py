students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]



def printInfo(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

printInfo('first_name', students)


def printInfo(key_name, some_list):
    for dictionary in some_list:
        print(dictionary[key_name])

printInfo('last_name', students)


