def calculate_average(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

def classify_student(media):
      if media >= 7:
           return("Approved")
      else :
           return("Failed")


student_average = calculate_average(8,7,9)

student_status = classify_student(student_average)

print(f"Average: {student_average} - Status: {student_status}")