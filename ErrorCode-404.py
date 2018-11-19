code = str(input("Input your code: "))
print("Your program is:")
print(code)

def analyze(code):
    if code.startswith("def"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    elif code.startswith("if"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    elif code.startswith("else"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    elif code.startswith("while"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    elif code.startswith("for"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    elif code.startswith("except"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    elif code.startswith("while"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
        else:
            print ("No colon errors detected.")
    else:
        print ("No colon errors detected.")
