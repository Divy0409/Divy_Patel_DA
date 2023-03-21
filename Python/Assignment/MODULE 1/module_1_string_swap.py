def chars_mix_up(a, b):
  new_a = b[:2] + a[2:] # First two characters from xyz and last character form abc
  new_b = a[:2] + b[2:] # First two characters from abc and last character from xyz

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))
