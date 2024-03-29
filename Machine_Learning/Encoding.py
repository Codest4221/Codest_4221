# These codes are the continuation of Missing_values.py codes

##############################################################################
# Encoding: Katagorik veriler => Numeric veriler
# Encoding process: Converting catagorical data to numerical data

ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

# Label encoding (0,1,2,...)

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])
print(ulke)

# One Hot Encoding: If value exists, it enumerates the data as 1. If not, then it enumerates the data as 0.

ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)
