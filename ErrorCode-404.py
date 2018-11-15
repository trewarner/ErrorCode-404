code = input("Input your code with triple quotes: ")
print("Example:  \"\"\"if 2>0:\"\"\"")

x = "def f(a)"

>>> a

>>> x

'def f(a)'

>>> x[-1:]

')'

>>> if (x[-1]==':'):

...   print("yay")

...

>>> x = """def f(n):

...   return n*n

... """

>>> x

'def f(n):\n  return n*n\n'

>>> print(x)

def f(n):

  return n*n



>>> x

'def f(n):\n  return n*n\n'

>>> x.indexOf('/n')

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

AttributeError: 'str' object has no attribute 'indexOf'

>>> x.index('/n')

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: substring not found

>>> x

'def f(n):\n  return n*n\n'

>>> x.index(":")

8

>>> x.index("\n")

9

>>> x[x.index("\n"]-1)

  File "<stdin>", line 1

    x[x.index("\n"]-1)

                  ^

SyntaxError: invalid syntax

>>> x[x.index["\n"]-1)

  File "<stdin>", line 1

    x[x.index["\n"]-1)

                     ^

SyntaxError: invalid syntax

>>> x[x.index["\n"]-1]

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'

>>> pos = x.index('/n')

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: substring not found

>>> pos = x.index("/n")

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

ValueError: substring not found

>>> x

'def f(n):\n  return n*n\n'

>>> pos = x.index("\n")

>>> pos

9

>>> x(pos)

Traceback (most recent call last):

  File "<stdin>", line 1, in <module>

TypeError: 'str' object is not callable

>>> x[pos]

'\n'

>>> x[pos-1]

':'

>>> y = """

... def g(a,b):

...   c = a+b

...   return c*c

... """

>>> y

'\ndef g(a,b):\n  c = a+b\n  return c*c\n'

>>>
