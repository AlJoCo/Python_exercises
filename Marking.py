mark = int(input("Please enter your mark: "))

if mark > 85:
    print("Pass with distinction")
#if mark > 64 and mark <=85:
    #print("Pass")
elif mark <= 85 and mark > 65:
    print("Pass")
else: print("Fail")