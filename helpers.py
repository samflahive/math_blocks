def list_match(a, b):
   # bool whether a and b are equivalent lists
   # this function works as long as all items in a can use the == operator
   # with all items in b

   
   # same length
   if len(a) != len(b):
      return False
   # each item in a is also in b
   for sub_a in a:
      if not sub_a in b:
         return False
   # the above two prove a == b
   return True
