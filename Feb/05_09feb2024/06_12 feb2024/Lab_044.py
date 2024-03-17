# Break

# For  - > 1 to  10 ->  range(1,11,1) or range(1,11)
# i = 5 --> i want break from the loop, if i goes to i = 5   - kicked out from the loop

for i in range(1, 11):
    if i == 5:  # 5 is not printed because at i == 5  break applied
        break
    print(i)  # line no 6 to 9 is inside the loop , An vertical line is displayed below if observe this this will give you idea about loop area
    # print("inside of the for loop")   # this is also in loop if you see o/p for this line
print("Outside of the for loop")       # this is not in the loop because see the alignment of print text

# Please pay attention where we write the print() function




