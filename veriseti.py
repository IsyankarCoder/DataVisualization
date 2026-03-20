import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

verisetim = pd.read_csv("insurance.csv")
pd.set_option("display.max_columns",20)

verisetim =verisetim.rename(columns={"age":"yas", "sex":"cinsiyet","bmi":"vki","children":"cocukSayisi","smoker":"sigaraDurum","region":"bolge","charges":"odemeMiktari"})
verisetim["cinsiyet"]=verisetim["cinsiyet"].replace(["male","female"],["erkek","kadin"])
verisetim["sigaraDurum"]=verisetim["sigaraDurum"].replace(["no","yes"],["evet","hayir"])
verisetim["bolge"]=verisetim["bolge"].replace(["southeast","northwest","southwest","northeast"],
                                              ["guneydogu","kuzeybati","guneybati","kuzeydogu"])

print(verisetim.dtypes)
verisetim["cinsiyet"]=verisetim["cinsiyet"].astype('category')
verisetim["sigaraDurum"]= verisetim["sigaraDurum"].astype('category')
verisetim["bolge"]=verisetim["bolge"].astype('category')
verisetim.dtypes



print(verisetim.dtypes)
print(verisetim.describe(include="all"))


x=range(1,21)
y1=verisetim.iloc[0:20,2]
y2=verisetim.iloc[20:40,2]

plt.xticks(x)
plt.plot(x,y1,x,y2)
plt.show()



