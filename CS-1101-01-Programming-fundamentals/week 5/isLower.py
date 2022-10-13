# def any_lowercase1(s):
#   for c in s:
#     if c.islower():
#       return True
#     else:
#       return False

# # First letter upper case rest all are lower case.
# result1 = any_lowercase1("First")
# # First letter is lower case, rest all are upper case.
# result2 = any_lowercase1("sECOND")
# print(result1, result2)

# def any_lowercase2(s):
#   for c in s:
#     if 'c'.islower():
#       return 'True'
#     else:
#       return 'False'

# result = any_lowercase2("SFADFDSF")
# print(result)

# def any_lowercase3(s):
#   for c in s:
#     flag = c.islower()
#   return flag

# result1 = any_lowercase3("FIRSt")
# result2 = any_lowercase3("seconD")
# print(result1, result2)

# def any_lowercase4(s):
#   flag = False
#   for c in s:
#     flag = flag or c.islower()
#   return flag

# result = any_lowercase4("ssSS")
# print(result)

def any_lowercase5(s):
  for c in s:
    if not c.islower():
      return False
  return True

result = any_lowercase5("rr")
print(result)