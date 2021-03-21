##############################################################################
# Kütüphanelerin yüklenmesi

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##############################################################################
# Verilerin okunması

veriler = pd.read_csv("eksikveriler.csv")
print()

##############################################################################
# eksik verilerin ( missing values ) doldurulması

eksik_veriler = pd.read_csv("eksikveriler.csv")
print(eksik_veriler)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values = np.nan, strategy = "mean")
Yas = veriler.iloc[:,1:4].values
#print(Yas)

imputer = imputer.fit(Yas[:,1:4])
Yas[:,1:4] = imputer.transform(Yas[:,1:4])
print(Yas)
