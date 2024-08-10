print("Grade Calculator")
subject = input("Enter the name of the subject: ")
max = int(input("Enter the maximum marks: "))
marks = int(input("Enter the marks you got: ")) #Int is used for whole numbers
percentage = (marks/max)*100
percentage = round(percentage,2) #rounding off to 2 decimal places 
if percentage >= 90:
  print("You got",percentage,"% in",subject,"which is an A+")  
elif percentage >= 80:
  print("You got",percentage,"% in",subject,"which is an A") 
elif percentage >= 70:
  print("You got",percentage,"% in",subject,"which is a B")
elif percentage >= 60:
  print("You got",percentage,"% in",subject,"which is a C")
elif percentage >= 50:
  print("You got",percentage,"% in",subject,"which is a D")
elif percentage >= 40:
  print("You got",percentage,"% in",subject,"which is an U")
elif percentage < 40:
  print("You got",percentage,"% in",subject,"which is an Ungraded") #You are ungraded
else:
  print("I don't know what you got")