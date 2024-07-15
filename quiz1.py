
studentRecord=[["stdId","studentName","Standard","Age","Hindi",'English',"Maths","Science","Computer","Total"],
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

# for i in range(len(studentRecord)):
#     print(studentRecord[i])

data = studentRecord[1:]
print("Name of students whose marks in english is greater than 50")

for i in range(len(data)):
    if data[i][5] >50:
        print(data[i][1])

print("Name and age of top four scorer of maths")
maths=[]
for i in range(len(data)):
    temp=[]
    temp.append(data[i][1])
    temp.append(data[i][3])
    temp.append(data[i][6])
    maths.append(temp)

maths.sort(key=lambda x:x[2],reverse=True)
top_four = maths[:4]

for student in top_four:
    print(f"Name: {student[0]}, Age: {student[1]}")


print("Name and id of three lowest scorer of computer: ")

computer=[]
for i in range(len(data)):
    temp=[]
    temp.append(data[i][0])
    temp.append(data[i][1])
    temp.append(data[i][8])
    computer.append(temp)

computer.sort(key=lambda x:x[2])
low_three = computer[:3]

for student in low_three:
    print(f"Name: {student[0]}, Age: {student[1]}")

