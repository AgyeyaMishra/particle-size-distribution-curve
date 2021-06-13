# Particle Size Distribution Curve

This is a really small personal project done for **Department of Civil Engineering, Delhi Technological University (formerly, Delhi College of Engineering)** for a course in **Soil Mechanics (Course Code - CE206)**.

It is a simple program using ```Python```, ```Pandas``` and ```Matplotlib```which helps a user to plot a particle size distribution curve for a soil sample.

---

# Documentation

### What is a Particle Size Distribution Curve?

A particle size distribution curve or grain size distribution curve represents the size range of soil grains in a given soil mass as percentages of the total dry weight. Engineers or lab technicians perform a sieve analysis for coarse-grain soils such as gravels and sands and hydrometer analysis for fine-grained soils like silts and clays to determine the soil sample’s grain size distribution. The results of mechanical analysis (sieve and hydrometer analyses) are generally presented by these semi-logarithmic plots known as particle-size distribution curves. The particle diameters are plotted in log scale, and the corresponding percent finer in arithmetic scale. 

### Sieve Analysis Results

Let’s assume we finished a sieve analysis that has the following results:

|Sieve Opening (mm) |Mass Retained (g) |
|-------------------| ---------------- |
|4.75|0|
|2.00|17.6|
|0.850|56.3|
|0.425|108.2|
|0.250|91.9|
|0.150|94.2|
|0.075|57.6|
|Pam|25.0|

From the sieve analysis, we can determine the percent finer for each sieve, the percentage of the soil passing through the sieve, and plot the grain size distribution curve.

### Calculating Percent Finer

First, we need to define a dictionary with two lists: one for the sieve opening and another for the mass retained. Then we create a pandas DataFrame from the data.

```python
from pandas import DataFrame
data = {
        "opening": [4.75, 2.00, 0.850, 0.425, 0.250, 0.150, 0.075, 0],
        "mass_retained": [0, 17.6, 56.3, 108.2, 91.9, 94.1, 57.6, 25.0]
       }
df = DataFrame(data)
```

This will result into the DataFrame ```df``` as:

![DataFrame df](https://user-images.githubusercontent.com/53916781/121565707-594c0400-ca3a-11eb-9058-48e8faa2e0cd.png)

After this, we create a function called ```calculate_percent_finer``` that will calculate the percent finer for each sieve and create a new column in our DataFrame called ```percent_finer```.

```python
def calculate_percent_finer(df):
     total_mass = df.mass_retained.sum()
     arr = []
     for count, sieve in enumerate(df.opening.values):
         cumulative_mass = sum([df.mass_retained.values[i] for i in range(count + 1)])
         percent_finer = ((total_mass - cumulative_mass) / total_mass) * 100
         arr.append(percent_finer)
     return df.assign(p_finer = arr)
```     

When this function returns and we print the new DataFrame, it will look like below:

![New DatFrame](https://user-images.githubusercontent.com/53916781/121566080-c5c70300-ca3a-11eb-8cd5-bd815c9081fc.png)

The ```calculate_percent_finer``` function takes in the DataFrame as a single argument and returns a new DataFrame with a ```percent_finer``` column. After this, we proceed to plot the particle size distribution curve.

```python
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
```

To plot the particle size distribution curve, we import ```matplotlib.pyplot``` as ```plt``` and use the ```semilogx()``` method to graph a semilog graph. The x-axis is plotted in ascending order by default. So we can use the ```invert_xaxis``` method to reverse the x-axis. Lastly, we add x-axis, y-axis and title labels to the plot and show the graph.

![Particle Size Distribution Curve Plot](https://user-images.githubusercontent.com/53916781/121566831-85b45000-ca3b-11eb-8413-7f580fedc64e.png)
===
