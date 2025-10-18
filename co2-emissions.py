# ======================
# CO2 EMISSIONS PROJECT
# ======================
import pandas as pd
import matplotlib.pyplot as plt

#Loading the dataset
df= pd.read_csv("co2-emissions-per-capita.csv")
print (df)

#Renaming for accessibility
df=df[["Entity", "Year", "Annual Coal emissions (per capita)"]]
df=df.rename(columns={
    "Entity": "country",
    "Year":"year",
    "Annual Coal emissions (per capita)": "co2"
})

#Chosing country data
countries= ["India", "China", "Saudi Arabia", "United States", "High-income countries", "Low-income countries"]
df['country']= df['country'].str.strip()
country_data={}

#Filtering the data
for country in countries:
    country_data[country]= df[df["country"] == country]

#Plotting the trends observed
plt.figure(figsize=(10,6))
for country in countries:
    data= country_data[country]
    plt.plot(data['year'],data['co2'], linewidth= 2.5, marker= 'p', label=country)
    
#Adding plot details
plt.title("CO2 Emissions Per Capita Throughout the Years", fontsize=16, weight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("CO2 Emissions (Per Capita)", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()

# Computing year-on-year percent change
df['YoY_change'] = df.groupby('country')['co2'].pct_change() * 100

# Plot YoY % change
plt.figure(figsize=(10,6))
for country in countries:
    temp = df[df['country'] == country]
    plt.plot(temp['year'], temp['YoY_change'], label=country)

plt.ylabel("Year-on-Year % Change")
plt.title("CO₂ Growth Rate")
plt.legend()
plt.grid(True)
plt.show()

plt.savefig("co2.png", dpi=300)