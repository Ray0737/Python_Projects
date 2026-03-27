t_score = 0
for i in range(2):
    a = int(input("Enter score (/50): "))
    t_score += a
print(t_score)
if t_score >= 50:
    print("pass")  
else:
    print("Fail")