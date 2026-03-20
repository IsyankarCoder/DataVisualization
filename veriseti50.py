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


x=np.arange(1,51)
y=verisetim.iloc[0:50,0]

plt.title("Oy farfara farfara ateş düştü şalvara...") 
plt.xlabel("Müşteri ID si")
plt.ylabel("Yaş")
#plt.grid(color="red",linestyle="--",linewidth=0.5)


plt.grid(axis="both") # grafikte x ve y eksenine ızgara ekler

plt.plot(x,y)

plt.show()
 


