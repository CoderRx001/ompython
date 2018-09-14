total = float(input(" What is your bill total? ").strip('$'))
# the above total variable is an input string into a float with a $ being taken away

fifteen = int(total) * 0.15
eightteen = int(total) * 0.18
twenty = int(total) * 0.20
# the above lines turn the total variable into an integer times the tip percentage

print(f" ${fifteen:.2f} is the suggested tip for 15%")
print(f" ${eightteen:.2f} is the suggested tip for 18%")
print(f" ${twenty:.2f} is the suggested tip for 20%")
# the above lines print the tip amount for each different tip
