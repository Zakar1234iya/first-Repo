x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def change_x(num):
     x[1][0] = num
     print([x]) 
change_x(15)

def change_name(new_name1):
     students[0]['last_name']= new_name1

     print([students])

change_name('Bryant')  

def change_sport(new_name2):
     sports_directory['soccer'][0] = new_name2
     print([sports_directory]) 
change_sport('Andres')

def change_z(num2):
     z[0]['y'] = num2
     print([z]) 
change_z(30)