first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
third = int(input("Enter the third number: "))
small=middle=large=0
if first < third and first < second:
    small = first
    if second < third and second < first:
        small = second
    else:
        small = third
elif first < second and first < third:
    middle = first
    if second > first and second < third:
        middle = second
    else:
        middle = third
elif first > second and first > third:
    large = first
    if second > first and second > third:
        large = second
    else:
        large = third
print("The numbers in accending order are: ", small, middle, large)