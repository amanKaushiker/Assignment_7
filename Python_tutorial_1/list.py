marks = [1,2,3,4,5,6,7, "aman"]
print("marks : ", marks)
print("negative index : ", marks[-1])
print("BEtween range : ", marks[1:3])

for score in marks:
    print(score)
    
    
print(3 in marks)      #check whether the 3 exists in list or not    

print(len(marks))

# marks.clear()

# print(marks)

for mark in marks:
    if mark == 3:
        break;
    print(mark)
    