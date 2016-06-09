If you find yourself writing a function like this:
 >>> def get_numbers(x):
 ...     l = []
 ...     if x > 5:
 ...         l.append(5)
 ...     if x < 2:
 ...         for i in range(0, x + 2):
 ...             l.append(i)
 ...     return l
 
You should use the yield keyword instead:
 >>> def get_numbers(x):
 ...     if x > 5:
 ...         yield 5
 ...     if x < 2:
 ...         for i in range(0, x + 2):
 ...             yield i
