digit0 = 9
digit1 = 7
digit2 = 8
digit3 = 0
digit4 = 3
digit5 = 0
digit6 = 6
digit7 = 4
digit8 = 0
digit9 = 6
digit10 = 1
digit11 = 5
digit12 = (
(digit0 + (3 * digit1) + 
digit2 + (3 * digit3) + 
digit4 + (3 * digit5) + 
digit6 + (3 * digit7) + 
digit8 + (3 * digit9) + 
digit10 + (3 * digit11)) % 10)

isbn_number = (digit0 + digit1 + digit2 + "-" + digit3 + "-" + digit4 + digit5 + digit6 + "-" + digit7 + digit8 + digit9 + digit10 + digit11 + "-" + digit12)
print(isbn_number)