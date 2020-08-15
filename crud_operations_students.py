# CRUD - Create Read Update Delete
#         index       0,              1             2
student_names  = [ "Vasile Hugo", "Olga Einstein", "Iurie Hussein", "Osama Papuc", "Vladimir Dodon", "Klaus Dancila", "Igor Putin",  ]  # string values
student_specs  = [ "Science", "Scenography", "Languages", "Law", "History", "Chemistry", "Theology"   ]  # string values
student_grades = [ 9.576, 9.678, 8.267, 8.547, 5.765, 9.345, 5.104     ]  # float values


# R
# python string formatting -> templates
def read():
    for i in range(len(student_names)):
        # print( " > ", student_names[i], "( " + student_specs[i] + " )", student_grades[i] )
    
        print(f" > {student_names[i]:30s} ( {student_specs[i]:11s} )")
        # f"... {value:specifications} ..." - placeholder

def details():
    name = input( "Which student? > " ).lower().title()
    for i in range(len(student_names)):
        if name not in student_names:
            print( "STUDENT NOT FOUND!" )
            break
        if student_names[i] == name:
            print( "STUDENT FOUND!" )
            print(f" >>> {student_names[i]:30s} ( {student_specs[i]:11s} ) {student_grades[i]:4.1f}")

def delete():
    name = input( "Which student? > " ).lower().title()
    for i in range(len(student_names)):
        if name not in student_names:
            print( "STUDENT NOT FOUND!" )
            break
        if student_names[i] == name:
            print( "STUDENT DELETED!" )
            student_names.pop(i)   
            student_grades.pop(i)
            student_specs.pop(i)
            break
        
        
def edit():
    name = input( "Which student? > " ).lower().title()
    for i in range(len(student_names)):
        if student_names[i] == name:
            
            new_name  = input( " ENTER THE NEW STUDENT NAME > ")
            new_spec  = input( " ENTER THE NEW STUDENT SPECIALITY > ")
            new_grade = float(input( " ENTER THE NEW STUDENT SPECIALITY > "))
            
            if new_name == "":
                pass
            else:
                student_names[i]  = new_name
            if new_spec == "":
                pass
            else:
                student_specs[i]  = new_spec
            if new_grade == "":
                    pass
            else:
                student_grades[i] = new_grade
            print( "STUDENT EDITED!" )
        
       
    
    
        
def menu():
    option = -1
    while option != 0:
        print( "\n\n" )
        print( "########### MENU ###########" )
        print( "1. Show Student List" )
        print( "2. Show Student Details" )
        print( "3. Edit Student Details" )
        print( "4. Delete Student" )
        print( "0. Exit" )
        print( "############################" )
        print( "CHOOSE OPTION > ")
        
        option = int(input())
    
        if option == 1:
            read()
        if option == 2:
            details()
        if option == 3:
            edit()
        if option == 4:
            delete()

menu()
read()