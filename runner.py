import sklearn
import sklearn.ensemble
import sklearn.metrics
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

# File path
FILE_SYSTEM = ""
TRAIN_DATASET_NAME = "/volume/ToTrainDataset.csv"

# Create the df containing data and edit it
df = pd.read_csv(FILE_SYSTEM + TRAIN_DATASET_NAME)

# Create Y set One hot
y = pd.get_dummies(df['STATUS'])

# Drop not needed cols 
x = df.drop(columns=['STATUS', 'OWNER_LOCATION', 'YEAR'])

# Concat one hot encoding for year and location
x = pd.concat([x, pd.get_dummies(df['OWNER_LOCATION']), pd.get_dummies(df['YEAR'])], axis=1)

# Remove IDs
x = x.iloc[:, 1:]
feature_names = x.columns.values
x = np.array(x)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.30, random_state=42)


# Print shapes
print('X_train {} X_test {}'.format(np.shape(X_train), np.shape(X_test)))
print('Y_train {} Y_test {}'.format(np.shape(Y_train), np.shape(Y_test)))

rf = sklearn.ensemble.RandomForestClassifier(n_estimators=250, max_features='sqrt', min_samples_leaf=49, 
                                             oob_score=True)
rf.fit(X_train, Y_train)

pred = rf.predict_proba(X_test)
sklearn.metrics.accuracy_score(Y_test, rf.predict(X_test))