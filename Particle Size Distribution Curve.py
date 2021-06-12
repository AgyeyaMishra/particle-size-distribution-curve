"""
Author: Agyeya Mishra
Institute: Delhi Technological University (formerly, Delhi College of Engineering)
Language: Python
Version: 3.x
"""

from pandas import DataFrame
data = {
        "opening": [4.75, 2.00, 0.850, 0.425, 0.250, 0.150, 0.075, 0],
        "mass_retained": [0, 17.6, 56.3, 108.2, 91.9, 94.1, 57.6, 25.0]
       }
df = DataFrame(data)

 
def calculate_percent_finer(df):
     total_mass = df.mass_retained.sum()
     arr = []
     for count, sieve in enumerate(df.opening.values):
         cumulative_mass = sum([df.mass_retained.values[i] for i in range(count + 1)])
         percent_finer = ((total_mass - cumulative_mass) / total_mass) * 100
         arr.append(percent_finer)
     return df.assign(p_finer = arr)


print(df)     
print("\n")

import matplotlib.pyplot as plt

df2 = calculate_percent_finer(df)

print (df2) 
plt.style.use("bmh")
plt.semilogx(df2.opening, df2.p_finer)
plt.gca().invert_xaxis()
plt.xlabel("Grain Size (mm) -- log scale")
plt.ylabel("Percent Passing")
plt.title("Particle Size Distribution Curve")
plt.show()

