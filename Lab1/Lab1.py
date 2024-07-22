# Ques 1-----------------------------------------

# with open("abc.txt","r") as file:
#     data=file.readlines()
#     for i in data:
#         print(i,end="")

# Ques 2---------------------------
# count=1
# with open("abc.txt","r") as file:
#         for i in file:
#             for j in i:
#                 if j == " ": 
#                     count+=1
#         print(count)
#     

# Ques 3 ---------------------------
# count=0
# with open("abc.txt","r") as file:
#     for line in file:
#         for i in line:
#             if i.isupper():
#                 count+=1

# print(count)

# Ques 4 -----------------------------
# file=open("abc.txt","r")


# def display_words(file):
#     for i in file:
#         l=i.split()
#         for i in l:
#             if len(i)<4:
#                 print(i)

# display_words(file)