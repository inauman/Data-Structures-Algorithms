def countx(mystr):

  # Base Case
  if len(mystr) == 0:
    return 0

  # Subprogram
  if mystr[0] == 'x':
    return 1 + countx(mystr[1:len(mystr)])
  else:
    return countx(mystr[1:len(mystr)])

print(countx('axbxcxd'))