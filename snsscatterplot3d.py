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

fig= plt.figure(figsize=(10,6))
ax=plt.axes(projection="3d")
ax.scatter(verisetim.yas,verisetim.odemeMiktari,verisetim.vki,color="darkblue")
ax.set_xlabel("Yaş")
ax.set_ylabel("Ödeme Miktari")
ax.set_zlabel("Vücut Kitle İndeksi",rotation=90)

ax.zaxis.labelpad=-0.7

plt.title("3 - Boyutlu Serpilme Diagramı")
 
 
plt.show()

 


