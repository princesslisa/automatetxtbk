x = "tears"
y = "test"
count = 0
for i in range(len(x)):
    if x[i] == y[i]:
        count += 1
    else:
        continue
print("The number of matches from your entered strings is " + str(count))
