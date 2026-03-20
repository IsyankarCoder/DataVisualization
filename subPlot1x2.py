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


#plot 1: İlk 20 müşterinin vki'si
x=np.arange(1,21)
y1=verisetim.iloc[0:20,2]

plt.subplot (1,2,1) 
#plt.subplot(2,1,1)
plt.plot(x,y1)
plt.xticks(x)

plt.title("İlk 20 müşteri")

#plot 2: Ikinci 20 müşterinin vki'si
y2= verisetim.iloc[20:40,2]

#plt.subplot(2,1,2)
plt.subplot (1,2,2) 
plt.plot(x,y2)
plt.xticks(x)

plt.title("İlk 20 Müşteri")
plt.suptitle("VKİ karşılaştırması")

plt.tight_layout(pad=1)

plt.show()


 


