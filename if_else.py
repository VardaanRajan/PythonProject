lst = []
string = ""
for temp in range(5,12):
    print(temp)
    string += str(temp) + " "
    lst.append(temp)
print(string)

#' '.join(lst)
# result = " ".join(map(str,lst))
# print(result)

a = int(input("enter a number: "))
print("Positive")  if a > 0 else print("Negative")
# git and github pe account create