workscore = int(input("work score (../10): "))
midtermscore = int(input("midterm score (../40): "))
finalscore = int(input("final score (../50): "))

if workscore < 5 or midtermscore < 20 or finalscore < 25:
    print("Fail")
else:
    print("Pass")