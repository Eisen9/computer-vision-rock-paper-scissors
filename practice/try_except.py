try:
    # open file try.txt
    open('try.txt')
    print("Opens the file try.txt")

except:
    # deals the the situation when there is not file named try.txt
    print("There is no such a file")
