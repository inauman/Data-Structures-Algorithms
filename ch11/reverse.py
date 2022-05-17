def reverse(code):

  # Base Case
  if len(code) == 1:
    return code[0]

  # Subprogram
  return reverse(code[1:len(code)]) + code[0]

print(reverse('abcd'))