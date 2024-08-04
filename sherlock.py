def isValid(s: str):

  occurrences = {}
  for char in s:
    if char not in occurrences.keys():
      occurrences[char] = 1
    else:
      occurrences[char] += 1

  violations = 0

  counts = [occurrences[x] for x in occurrences.keys()]
  start = counts[0]
  for i in range(0, len(counts)):
    if abs(start - counts[i]) >= 1:
      violations+=1

  if violations > 1:
    return "NO"
  else:
    return "YES"


print(isValid("abcdefghhgfedecba"))