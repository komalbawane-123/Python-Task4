## Example 1 Of Functions

def Student(Name,Age,Subject,Test_marks):
    print(f'S_Name={Name}')
    print(f'S_Age={Age}')
    print(f'S_Subject={Subject}')
    print(f'S_Test_marks{Test_marks}')
    return'--Urgent'
print('---')
print(f'Student_1{Student('Revati',16,'English',80)}')
print('---')
print(f'Student_2{Student('Juhi',25,'Maths',100)}')
print('---')

## Example 2 of Function

def LinkedinAccount(id,IdType,Followers_count,Time_spent):
    print(f'LinkedinId={id}')
    print(f'Type_id ={IdType}')
    print(f'No_Of_Followers = {Followers_count}') 
    print(f'Time_spent_on_Instagram = {Time_spent}')
    
    return{
        'LinkedinId':id,
        'Type_id':IdType,
        'No_Of_Followers':Followers_count,
        'Time_spent_on_Instagram':Time_spent
    }
print('---')
id1=LinkedinAccount('Lavanay@official','Private','100k','6 Hours')
print('---')
id2=LinkedinAccount('SathiRaju@unofficial','Public','2k','8 Hours')
print('---')

## Example 3 of Function

def add(a, b):
 return a + b

result = add(7, 10)
print(result)

## Example 4 of Function

def greet(name):
    print(f"Hello, {name}!")

greet("Rudra")

