# Particle Size Distribution Curve

This is a really small personal project done for **Department of Civil Engineering, Delhi Technological University (formerly Delhi College of Engineering)** for a course in **Soil Mechanics (Course Code - CE206)**.

It is a simple program using ```Python```, ```Pandas``` and ```Matplotlib```that helps a user to plot a particle size distribution curve for a soil sample.

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
