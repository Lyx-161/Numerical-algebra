import numpy as np
import matplotlib.pyplot as plt

def polyfit(x,y,degree):
    X=np.vander(x,degree+1)
    coeffs = np.linalg.solve(X.T@X,X.T@y)
    #print(coeffs)
    return coeffs

def predict_value(coeffs,x):
    degree = len(coeffs) - 1
    temp=0
    for j in coeffs:
        temp+=j*(x**degree)
        degree-=1
    return temp

data = {
2010 :{"total_population":13.4091 , "birth_population":1588 },
2011 :{"total_population":13.4916 , "birth_population":1599 },
2012 :{"total_population":13.5922 , "birth_population":1630 },
2013 :{"total_population":13.6726 , "birth_population":1635 },
2014 :{"total_population":13.7646 , "birth_population":1683 },
2015 :{"total_population":13.8326 , "birth_population":1655 },
2016 :{"total_population":13.9232 , "birth_population":1786 },
2017 :{"total_population":14.0011 , "birth_population":1723 },
2018 :{"total_population":14.0541 , "birth_population":1523 },
2019 :{"total_population":14.1008 , "birth_population":1465 },
2020 :{"total_population":14.1212 , "birth_population":1202 },
2021 :{"total_population":14.1260 , "birth_population":1062 },
2022 :{"total_population":14.1175 , "birth_population":956  },
2023 :{"total_population":14.1000 , "birth_population":902  },
}

years = np.array(list(data.keys()))
total_population = np.array([data[year]["total_population"] for year in years])
birth_population = np.array([data[year]["birth_population"] for year in years])

years-=2000

target_year=[24,30,40]

print("Total Population")
coeffs_total_3=polyfit(years,total_population,3)
coeffs_total_5=polyfit(years,total_population,5)

print("3 degrees")
for pre_year in target_year:
    pre_total=predict_value(coeffs_total_3,pre_year)
    print(pre_year+2000,' :',pre_total,'亿')

print("5 degrees")
for pre_year in target_year:
    pre_total=predict_value(coeffs_total_5,pre_year)
    print(pre_year+2000,' :',pre_total,'亿')

print("Birth Population")
coeffs_birth_3=polyfit(years,birth_population,3)
coeffs_birth_5=polyfit(years,birth_population,5)

print("3 degrees")
for pre_year in target_year:
    pre_total=predict_value(coeffs_birth_3,pre_year)
    print(pre_year+2000,' :',pre_total,'万')

print("5 degrees")
for pre_year in target_year:
    pre_total=predict_value(coeffs_birth_5,pre_year)
    print(pre_year+2000,' :',pre_total,'万')

plt.figure(figsize=(12, 6))

# 总人口拟合
plt.subplot(1, 2, 1)
plt.scatter(years+2000, total_population, color="blue", label="Actual Data")
years_fit = np.linspace(0, 40, 500)
total_population_3_fit = [predict_value(coeffs_total_3, year) for year in years_fit]
total_population_5_fit = [predict_value(coeffs_total_5, year) for year in years_fit]
plt.plot(years_fit+2000, total_population_3_fit, label="3rd degree fit", color="green")
plt.plot(years_fit+2000, total_population_5_fit, label="5th degree fit", color="red")
plt.title("Total Population")
plt.xlabel("Year")
plt.ylabel("Population (亿)")
plt.legend()

#出生人口拟合
plt.subplot(1, 2, 2)
plt.scatter(years+2000, birth_population, color="blue", label="Actual Data")
years_fit = np.linspace(-5, 50, 500)
birth_population_3_fit = [predict_value(coeffs_birth_3, year) for year in years_fit]
birth_population_5_fit = [predict_value(coeffs_birth_5, year) for year in years_fit]
plt.plot(years_fit+2000, birth_population_3_fit, label="3rd degree fit", color="green")
plt.plot(years_fit+2000, birth_population_5_fit, label="5th degree fit", color="red")
plt.title("Birth Population")
plt.xlabel("Year")
plt.ylabel("Population (万)")
plt.legend()

plt.show()