code = input("Input your code ")
print("Your program is:")
print(code)

if (code[0:2]=='def') or (code[0:1]=='if') or (code[0:3]=='else'):
    if (code[-1]==':'):
        print ("Nothing is wrong with line one")
    else:
        print ("you might be missing a colon in line one")
else:
    print("Nothing is wrong with line one")
