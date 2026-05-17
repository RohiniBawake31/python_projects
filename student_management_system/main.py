students=[]

# Add students data 
def add_student():
   name=input("Enter your name : ")
   age=input ("Enter age: ")
   course=input("Enter course:")
   student={"name":name,
             "age":age,
             "course":course}     
   students.append(student)
   print("student added successfully")
   print(students)

# search students data
def search_student():
  search_name=input("Enter student name for search: ")
  for student in students:
    if student['name'].lower() == search_name.lower():
         print("name:",student['name'])
         print("age:",student['age'])
         print("course:",student['course'])
        
    else:    
        print("student not found")

# Delete students data
def delete_student():
    search_name = input("Enter student name to delete: ")

    for student in students:
        if student["name"].lower() == search_name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            print(students)
        else:
            print("Student not found")
        break


if __name__=="__main__":
  add_student()
  search_student()
  delete_student()


