



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

open = (code).count('(')
closed = (code).count(')')

if open == closed:
    print ("No parentheses/brackets errors deteced.")
elif open > closed:
    print ("There are more open parentheses/brackets than closed parentheses/brackets.")
elif open < closed:
    print ("There are more closed parentheses/brackets than open parentheses/brackets.")

filepath = input("Input program file name: ")

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line))
       analyze(line)
       line = fp.readline()
       cnt += 1
