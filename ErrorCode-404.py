



def analyze(code):
    code = code.strip()
    if code.startswith("def"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
    elif code.startswith("if"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
    elif code.startswith("else"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
    elif code.startswith("while"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
    elif code.startswith("for"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
    elif code.startswith("except"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")
    elif code.startswith("while"):
        if not (code[-1]==':'):
            print ("ERROR: Missing colon.")

# Par = parentheses
# Bra = brackets
# Cur = curly braces

    openPar = (code).count('(')
    closedPar = (code).count(')')
    openBra = (code).count('[')
    closedBra = (code).count(']')
    openCur = (code).count('{')
    closedCur = (code).count('}')

    open = openPar + openBra + openCur
    closed = closedPar + closedBra + closedCur

    if open > closed:
        print ("There are more open parentheses/brackets than closed parentheses/brackets.")
    elif open < closed:
        print ("There are more closed parentheses/brackets than open parentheses/brackets.")

    quotes = (code).count('"')

    if (quotes)%2!=0

filepath = input("Input program file name: ")

with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line))
       analyze(line)
       line = fp.readline()
       cnt += 1
