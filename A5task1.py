students_marks = {'Ishika' : 90 , 'John' : 75 , 'Alice' : 80 , 'abcd': 45}
name = input("Enter a name: ")
if name in students_marks:
    print(f"Marks of {name} : {students_marks[name]}")
else:
    print("Student not found in the record")

