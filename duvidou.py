from matplotlib import pyplot as plt
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
import pandas as pd
import numpy as np


def matriz_confusao_media(model, X, y, kf):
    n_classes = len(np.unique(y))
    total_confusion_matrix = np.zeros((n_classes, n_classes), dtype=int)
    
    for train_index, test_index in kf.split(X, y):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        total_confusion_matrix += confusion_matrix(y_test, y_pred)
    
    avg_confusion_matrix = total_confusion_matrix / kf.get_n_splits()
    
    print("Matriz de Confusão Média:")
    print("+---------------------------+")
    print("| não duvidou |   duvidou   |")
    print("+---------------------------+")
    print(f"| {avg_confusion_matrix[0][0]:11.1f} | {avg_confusion_matrix[0][1]:11.1f} |")
    print(f"| {avg_confusion_matrix[1][0]:11.1f} | {avg_confusion_matrix[1][1]:11.1f} |")
    print("+---------------------------+")
    
    return avg_confusion_matrix


if __name__=='__main__':    
    arquivo = pd.read_csv('csv/duvidou.csv')
    y = arquivo['duvidou']
    X = arquivo.drop('duvidou', axis = 1)

    kf = KFold(n_splits=5, shuffle=False) # KFold com 5 divisões
    knn = KNeighborsClassifier(n_neighbors=11) # modelo K-Nearest Neighbors (KNN)
    mat = matriz_confusao_media(knn,X,y,kf)


    accuracy = (mat[0][0]+mat[1][1]) / (mat[0][0]+mat[1][0]+mat[0][1]+mat[1][1])
    precision = (mat[1][1]) / (mat[1][1]+mat[0][1])
    recall = (mat[1][1]) / (mat[1][1]+mat[1][0])
    
    print(f'\nAcurácia: {accuracy:.3f}')
    print(f'Precisão: {precision:.3f}')
    print(f'Recall: {recall:.3f}\n')