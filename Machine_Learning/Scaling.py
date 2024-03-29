# These codes are the continuation of train_test_splitting.py codes

##############################################################################
# Öznitelik ölçekleme ( verileri birbirlerine yakın olacak şekilde ölçekleme )( Her zaman kullanılmak zorunda değil )
# Scaling the dataset

# Standard scaling
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)

# Verileri normalize etmek
# Normal scaling
from sklearn.preprocessing import Normalizer

norm = Normalizer()

X_train_norm = norm.fit_transform(x_train)
X_test_norm = norm.fit_transform(x_test)
