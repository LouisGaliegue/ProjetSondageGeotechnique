# Ce fichier comporte les fonctions concernants le pretraitement

import sklearn.preprocessing as prepro
import numpy as np
import pandas as pd
import sklearn.model_selection as sk
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

groundType = ['A', 'AL', 'AM', 'AS', 'B', 'C', 'G', 'GY', 'L', 'M', 'MC', 'MS', 'R', 'SL', 'S']
logGranulometrie = np.array([-2.68, -2.3, -2, -1.82, 3.6, 2.7, 0.9, 3., -1.7, 2., 2.18, 1.78, -1.3, -1., -0.3])
argilosite = np.array([8, 7, 8, 6, 0, 0, 0, 0, 3, 0, 0, 0, 0, 2, 1])
# Mise a l'echelle de la classification
logGranulometrie = (logGranulometrie - logGranulometrie.mean())/logGranulometrie.std()
argilosite = (argilosite - argilosite.mean())/argilosite.std()

critere = np.array([logGranulometrie, argilosite])
critere = critere.transpose()

#-----Label-----
def transformerGranuArgi(data):
    """
    Ajoute 2 colonnes qui transforment les sols avec nos criteres
    """
    
    # Création des array pour datafrme : [granulo, argilo]
    label = np.array([[logGranulometrie[groundType.index(data['sol'][i])], argilosite[groundType.index(data['sol'][i])]] for i in range(len(data['sol']))])
    df_label = pd.DataFrame(label, columns = ['Log_Granulo', 'Argilosite'])

    return pd.concat([data, df_label], axis = 1)


def inverse_transforme(couple_data):
    """
    Fonctions inverse_transform adaptée pour notre critère, qui prend un couple en paramètre et lui associe sa roche
    """
    
    for i in range(groundType):
        if couple_data == (logGranulometrie[i], argilosite[i]):
            return groundType[i]
    print("erreur")
