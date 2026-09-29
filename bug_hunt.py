count = 1
total = 0

# BUG: Fixed SyntaxError by adding a missing colon (:) at the end of the while condition header.
# BUG: Fixed LogicError by changing the condition from 'count < 5' to 'count <= 5' so the number 5 is included in the sum.
while count <= 5:
    total = total + count
    count = count + 1

# BUG: Fixed TypeError by converting the integer 'total' to a string using str(total) before concatenating with a text string.
print("Sum of 1 to 5 is: " + str(total))
