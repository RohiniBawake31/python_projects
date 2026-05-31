students=[]

# Add students data 
def add_student(name,age,course):
   student={"name":name,
             "age":age,
             "course":course}     
   students.append(student)
   print("student added successfully")
   print(students)

# search students data
def search_student(student_name):
  for student in students:
    if student['name'].lower() == student_name.lower():
         print("name:",student['name'])
         print("age:",student['age'])
         print("course:",student['course'])
        
    else:    
        print("student not found")

# Delete students data
def delete_student(student_name):
    for student in students:
        if student["name"].lower() == student_name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            print(students)
        else:
            print("Student not found")
        break


if __name__=="__main__":
  add_student("sai",30,"BSC")
  search_student("sai")
  delete_student("sai")


