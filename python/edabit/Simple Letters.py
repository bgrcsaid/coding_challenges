def longest_string(str1, str2):
  str=str1+str2
  return ''.join(sorted(set(str)))