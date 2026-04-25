#student marks analysis
'''
n=int(input("Enter number of students:"))
marks=list(map(int,input("enter marks").split()))
if len(marks)!=n:
    print("not sufficient length")
else:    
    for i in range(n):
        print(f"student-{i+1}: {marks[i]}")
    print(f"Total marks:{sum(marks)}")
    print(f"Maximum marks:{max(marks)}")
    print(f"minimum marks:{min(marks)}")
    print(f"Average marks for class:{sum(marks)/n}")'''


#or
'''
n=int(input("Enter number of students:"))
marks=[]
for i in range(n):
    mark=int(input("enter marks:"))
    marks.append(mark)
for i in marks:
    print(i,end=" ")
    
print("\nStudent Marks Analysis Report......")
print("The heighest marks is",max(marks))
print("The Lowest marks is ",min(marks))
print("The total marks is",sum(marks))
print("The average marks is",sum(marks)/n)

'''
