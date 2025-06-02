# indexing = accessing elements of a sequence using [] (indexing operator)
#           [start: end: step]

credit_number = "1234-5678-9012-3456"

print(credit_number[0]) # print the first digit
print(credit_number[0:4]) # print the first 4 digits
print(credit_number[5:]) # print the last 12 digits
print(credit_number[-1]) # print the last digit
print(credit_number[::2]) # print every line by 2 step

# Print the last 4 digits of the credit card number
last_digits = credit_number[-4:]
print(f"Your credit card number is: XXXX-XXXX-XXXX-{last_digits}")