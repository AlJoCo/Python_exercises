def isbn_calc(isbn-early-number):
    digit12 = 10 – (( digit0 + (3 x digit1) + digit2 + (3 x digit3) + digit4 + (3 x digit5) + digit6 + (3 x digit7) + digit8 + (3 x digit9) + digit10 + (3 x digit11) ) % 10)
    isbn-number = digit0 + digit1 + digit2 + "-" + digit3 + "-" + digit4 + digit5 + digit6 + "-" + digit7 + digit8 + digit9 + digit10 + digit11 + "-" + digit12
    return isbn-number

isbn-early-number = [digit0, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9, digit10, digit11]
(digit0, digit1, digit2, digit3, digit4, digit5, digit6, digit7, digit8, digit9, digit10, digit11) = int input("Please enter the first 12 digits of the ISBN number: ")
print(isbn-number)