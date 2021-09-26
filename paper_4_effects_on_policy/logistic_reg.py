import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

compilado = pd.read_csv(
    '/Users/juanmalagon/OneDrive/a_phd/data/clean_data_alteryx/compilado.csv'
    )

compilado.drop(columns=['SEDE_CODIGO'
                        , 'PERIODO_ANIO'
                        , 'PERIODO'
                        , 'COLE_GRADO'
                        , 'INDICE_MATEMATICAS'
                        , 'INDICE_C_NATURALES'
                        , 'INDICE_SOCIALES_CIUDADANAS'
                        , 'INDICE_LECTURA_CRITICA'
                        , 'INDICE_INGLES'
                        , 'INDICE_TOTAL'
                        ]
               , inplace=True
               )

y = compilado[['COLE_CATEGORIA']].copy()

y['COLE_CATEGORIA'].unique()

conditions = [(y['COLE_CATEGORIA']=='A+')
              , (y['COLE_CATEGORIA']=='A')
              , (y['COLE_CATEGORIA']=='B')
              , (y['COLE_CATEGORIA']=='C')
              , (y['COLE_CATEGORIA']=='D')
              ]
choices = [4,3,2,1,0]

y['CATEGORY'] = np.select(conditions, choices)

y = y['CATEGORY']

X = pd.get_dummies(compilado.drop(columns=['COLE_CATEGORIA'])).fillna(0)

checkintegrity = X[X.isna().any(axis=1)]

x_train, x_test, y_train, y_test =\
    train_test_split(X, y, test_size=0.2, random_state=0)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)


model = LogisticRegression(solver='liblinear', C=0.05, multi_class='ovr',
                           random_state=0)
model.fit(x_train, y_train)

x_test = scaler.transform(x_test)

y_pred = model.predict(x_test)

model.score(x_train, y_train)

confusion_matrix(y_test, y_pred)



cm = confusion_matrix(y_test, y_pred)

fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(cm)
ax.grid(False)
ax.set_xlabel('Predicted outputs', fontsize=11, color='black')
ax.set_ylabel('Actual outputs', fontsize=11, color='black')
ax.xaxis.set(ticks=range(5))
ax.yaxis.set(ticks=range(5))
ax.set_ylim(4.5, -0.5)
for i in range(5):
    for j in range(5):
        ax.text(j, i, cm[i, j], ha='center', va='center', color='white')
plt.show()

print(classification_report(y_test, y_pred))









# Check robustness (boostrap)
# Analyze the threshold of the sigmoid functions: from what point it does not matter anymore an increase?
# Check thresholds per school "type" and variables
# Tails are not important: use a threshold some % of the change, so we have a point
# where the high growth happens
# Incorporate "human factor" (employees agreggation) // + "infrastructure"
# Check regularization, which regularization, why regularization?
# Visualization of outputs: the sigmoids 2-D per categories. Make a cool dashboard
# Discuss. Discuss how to read the outputs.
