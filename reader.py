def analyze(line):
  # if it begins with def it better end with :, else print an error message
  if line.startswith("def"):
     if not line[-1]==":":
        print("****** missing colon")



filepath = 'test.py'  
with open(filepath) as fp:  
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line))
       analyze(line)
       line = fp.readline()
       cnt += 1

