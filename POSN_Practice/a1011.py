message = input("Enter msg: ").upper()
message = list(message)
message.sort()
counts = {}

if len(message) == 5:
    for char in message:
        counts[char] = counts.get(char,0) + 1

ans = ""
for key, item in counts.items():
    ans += f"{item}{key}"

print(ans)
        

            


            
