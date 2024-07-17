studentRecord = [["stdId","studentName","Standard","Age","Hindi",'English',"Maths","Science","Computer","Total"],
                 ["std01","Ashish Kumar","10th",15,67,89,87,89,90,422],
                 ["std02","Abhishek Kumar","10th",14,85,45,48,90,45,313],
                 ["std03","Aman","10th",15,23,56,78,78,67,302],
                 ["std04","Rahul","10th",14,45,67,45,45,56,258],
                 ["std05","Ruby","10th",13,89,67,89,93,65,403],
                 ["std06","Suman","10th",13,90,46,67,67,67,337],
                 ["std07","Saurabh","10th",15,45,23,34,45,34,181],
                 ["std08","Sumit","10th",14,23,45,67,78,90,303],
                 ["std09","Kamlesh","10th",15,45,56,78,99,67,345],
                 ["std10","Rohan","10th",15,34,12,24,45,56,171]]

headers = studentRecord[0]
data = studentRecord[1:]

# Convert to dictionary
# student_dict = [dict(zip(headers, student)) for student in data]
# print(student_dict)

student_dict=[]
for i in data:
    temp={}
    a=0
    for k in i:
        temp[headers[a]]=k
        a=a+1
    student_dict.append(temp)

print(student_dict)
    


# Print dictionary in tabular form
from tabulate import tabulate
print(tabulate(student_dict, headers="keys", tablefmt="pretty"))



# 1. Name of students whose marks in English is greater than 50
print("\nName of students whose marks in English is greater than 50")
for student in student_dict:
    if student["English"] > 50:
        print(student["studentName"])
    
# 2. Name and age of top four scorers in Maths
print("\nName and age of top four scorers in Maths")
maths_sorted = sorted(student_dict, key=lambda x: x["Maths"], reverse=True)[:4]
for student in maths_sorted:
    print(f"Name: {student['studentName']}, Age: {student['Age']}")

# 3. Name and id of three lowest scorers in Computer
print("\nName and ID of three lowest scorers in Computer")
computer_sorted = sorted(student_dict, key=lambda x: x["Computer"])[:3]
for student in computer_sorted:
    print(f"Name: {student['studentName']}, ID: {student['stdId']}")


