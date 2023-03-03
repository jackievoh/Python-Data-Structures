# Step 1
import pandas as pd
import numpy as np
import seaborn as sns

# Step 2
iris = sns.load_dataset('iris')

# Step 3
iris = iris.drop('species', axis=1)

# Step 4
iris['sepal_sum'] = iris['sepal_length'] + iris['sepal_width']
iris['petal_sum'] = iris['petal_length'] + iris['petal_width']

# Step 5
iris_stats = pd.DataFrame({
    'mean': iris.mean(),
    'std': iris.std(),
    'min': iris.min(),
    'max': iris.max()
})

iris_stats = iris_stats[['mean', 'std', 'min', 'max']]

print(iris_stats)