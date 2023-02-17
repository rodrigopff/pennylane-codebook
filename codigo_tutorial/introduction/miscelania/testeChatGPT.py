from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
import numpy as np

# Necessario para poder baixar as coisas sem prolemas de verificao de SSl
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Carrega o conjunto de dados MNIST
mnist = fetch_openml('mnist_784')

# Separa os dados de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(mnist.data, mnist.target, test_size=0.2, random_state=42)

# Define os valores para os parâmetros do modelo
param_grid = {'n_neighbors': np.arange(1, 10), 'weights': ['uniform', 'distance']}

# Realiza a busca em grade dos melhores hiperparâmetros
knn = KNeighborsClassifier()
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(X_train, y_train)

# Imprime o melhor conjunto de parâmetros encontrados
print(grid_search.best_params_)

# Treina o modelo com os melhores parâmetros encontrados
knn = KNeighborsClassifier(n_neighbors=grid_search.best_params_['n_neighbors'], weights=grid_search.best_params_['weights'])
knn.fit(X_train, y_train)

# Avalia a acurácia do modelo no conjunto de teste
accuracy = knn.score(X_test, y_test)
print('Acurácia:', accuracy)
