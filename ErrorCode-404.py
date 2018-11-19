



def analyze(code):
    code = code.strip()
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



filepath = input("Input program file name: ")

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line))
       analyze(line)
       line = fp.readline()
       cnt += 1
