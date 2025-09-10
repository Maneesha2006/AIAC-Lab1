def grade(s):
    return "FDCBAA"[(s>=60)+(s>=70)+(s>=80)+(s>=90)]
try:
    print(grade(float(input("Enter the score: "))))
except:
    print("Invalid input.")
