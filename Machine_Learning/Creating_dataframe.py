# These codes are the continuation of Encoding.py codes
##############################################################################
# Verilerin birleştirilmesi ve DataFrame oluşturulması
# Combining data and creating DataFrame

# dataframe oluşturulması
# creating DataFrame

sonuc1 = pd.DataFrame(data = ulke, index = range(22), columns = ["fr","tr","us"])
sonuc2 = pd.DataFrame(data = Yas, index = range(22), columns = ["boy","kilo","yas"])

cinsiyet = veriler.iloc[:,-1].values

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns = ["cinsiyet"])

# verilerin birleştirilmesi
# combining data

s1 = pd.concat([sonuc1,sonuc2],axis = 1) 
s2 = pd.concat([s1,sonuc3], axis = 1)
