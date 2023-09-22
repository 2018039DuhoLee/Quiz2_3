scores = [90, 45, 64, 9, 17, 29]
result = []
for score in scores :
    if score >= 71 :
        result.append("A")
    elif 41<= score < 71 :
       result.append("B")
    elif 11<= score < 41 :
        result.append("C")
    elif score < 10 :
        result.append("D")
print(result)
