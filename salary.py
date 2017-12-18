salary= [15000, 20000, 17000, 18900, 30000]
print("After the salary raise, the new salary of each employee are: ")
for i in range(0,len(salary)):
    salary[i] = salary[i] + 23/100 * salary[i]
print(salary[i])