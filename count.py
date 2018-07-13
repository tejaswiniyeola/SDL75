def word_count(str):
    count= dict()
    w= str. split()
    for a in w:
        if a in count:
            count[a]+= 1
        else:
            count[a]= 1
    return count

string1 = input("ENTER A STRING :: ")
check = word_count(string1)

print("\n ")
print(check)
