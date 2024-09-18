def students(Marks):
    if (Marks<50):
     print("fail")
    else:
     print("pass")
def main():
  x = int(input("Enter student 1 marks:"))
  print(students(x))
  y = int(input("Enter marks student 2:"))
  print(students(y))
main()
