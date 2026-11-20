# check if all dependencies are working

import numpy
import pandas
import sklearn
import lightgbms

print('NumPy:', numpy.__version__)
print('Pandas:', pandas.__version__)
print('Scikit-learn:', sklearn.__version__)
print('LightGBM:', lightgbm.__version__)
print('All dependencies working!')
