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


ozet = verisetim.groupby("sigaraDurum")["odemeMiktari"].mean()

def etiketEkle(x,y):
     for i in range(len(x)):
          plt.text(i,y[i],y[i],ha="center")

print(ozet.index)
print(ozet.values)

#plt.bar(x=ozet.index,height=ozet.values,color="g",width=0.95)
plt.barh(y=ozet.index,width=ozet.values,color="b",height=0.8)
#plt.xlabel("Sigara İçme Durumu")
#plt.ylabel("Ödeme Miktarı")
#etiketEkle(ozet.index,ozet.values.round(2))
plt.show()

 


