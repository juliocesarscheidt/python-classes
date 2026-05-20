import pprint
# pip install -q python-Levenshtein==0.27.3
import Levenshtein

def levenshtein_distance(s1, s2):
  len1 = len(s1)
  len2 = len(s2)

  # they may be the same string
  if len1 == len2:
    possibly_same = True
    for i in range(0, len1):
      if s1[i] != s2[i]:
        possibly_same = False
        break
    if possibly_same:
      return 0

  # initialize a matrix with (len1 + 1) rows by (len2 + 1) columns
  matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]

  # fill the very first column
  for i in range(0, len1+1):
    matrix[i][0] = i
  # fill the very first row
  for j in range(0, len2+1):
    matrix[0][j] = j

  print_matrix(matrix)

  # fill the rest of the matrix with the distances, starting at index 1
  # it will compare each letter of the first string with all the letters from the second one
  for i in range(1, len1+1):
    for j in range(1, len2+1):
      # Because your matrix has an extra row and column for the empty string base cases, matrix[i][j] actually corresponds to character i - 1 in your first string and character j - 1 in your second string
      # If they match: The cost is 0
      s1_letter = s1[i - 1]
      s2_letter = s2[j - 1]
      if s1_letter == s2_letter:
        # Set matrix[i][j] equal to the value found diagonally up-and-left at matrix[i - 1][j - 1]
        matrix[i][j] = matrix[i - 1][j - 1]
      # If they mismatch: The cost is 1
      else:
        # Look up three values:
        # - the cell to the left (matrix[i][j - 1])
        # - the cell above (matrix[i - 1][j])
        # - the cell diagonally up-left (matrix[i - 1][j - 1])
        val = min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
        matrix[i][j] = val + 1

  print_matrix(matrix)

  return matrix[len1][len2]

def print_matrix(matrix):
  pprint.pprint(matrix)
  print()

if __name__ == "__main__":
  s1 = "racoon"
  s2 = "cocoon"

  distance = levenshtein_distance(s1, s2)
  print(f"Levenshtein distance between '{s1}' and '{s2}' is: {distance}")

  distance = Levenshtein.distance(s1, s2)
  print(f"Levenshtein distance between '{s1}' and '{s2}' is: {distance}")
