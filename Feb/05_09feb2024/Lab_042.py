# WAP that calculate and display the letter grade for a given numerical score (e.g, A, B, C, D Or F)
# based on the following grade scale:
# Input score -89
# O/p - B
# A : 90-100
# B : 80-89
# C : 70-79
# D : 60-69
# F : 0-59

# use If, elif, else

# step 1
# figure out the inputs
# intput ? int

scale = int(input("Enter the number you got!\n"))

# Step 2
# figure out Logic
# i have to print A -> if scale <=100 and scale >= 90

if scale >= 90 and scale <= 100:
     print("Grade is A")
elif scale >= 80 and scale <=89:
     print("Grade is B")
elif scale >= 70 and scale <=79:
     print("Grade is C")
elif scale >= 60 and scale <=69:
     print("Grade is D")
elif scale >=0 and scale <=59:
     print("Grade is F")
else:
     print("invalid Input")