# These codes are the continuation of Creating_dataframe.py codes

##############################################################################
# Veri kümesinin eğitim ve test kümeleri olarak bölünmesi
# Splitting the dataset into training and test sets

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(s1,sonuc3, test_size = 0.33, random_state = 0)
