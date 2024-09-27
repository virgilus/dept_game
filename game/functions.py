# Imports
import pandas as pd
from random import choice

# Constantes
URL = 'https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254'

# Fonctions
def load_df(URL: str=URL) -> pd.DataFrame:
    return pd.read_csv(URL).set_index('code_departement')

def play_name(df: pd.DataFrame) -> None:
    dpt_a_trouver_lst = list(df.index)
    while dpt_a_trouver_lst:
        code = choice(dpt_a_trouver_lst)
        bonne_reponse = df.loc[code]['nom_departement']
        bonne_region = df.loc[code]['nom_region']
        reponse = input(code + " ?")
        check_answer(bonne_reponse, bonne_region, reponse, code)
        dpt_a_trouver_lst.remove(code)
    print("Vous avez tout trouvé, bravo !")

def play_code(df: pd.DataFrame) -> None:
    dpt_a_trouver_lst = list(df['nom_departement'])
    while dpt_a_trouver_lst:
        nom_dpt = choice(dpt_a_trouver_lst)
        bonne_reponse = str(df.loc[df['nom_departement'] == nom_dpt].index[0])
        bonne_region = df.loc[df['nom_departement'] == nom_dpt]['nom_region'].iloc[0]
        reponse = input(nom_dpt + " ?")
        check_answer(bonne_reponse, bonne_region, reponse, nom_dpt)
        dpt_a_trouver_lst.remove(nom_dpt)
    print("Vous avez tout trouvé, bravo !")
    
def check_answer(bonne_reponse: str, bonne_region: str, reponse: str, guess) -> bool:
    if reponse == 'q':
        print("Bye bye !")
    elif reponse == bonne_reponse:
        print(f"Gagné ! C'était bien le département : {bonne_reponse} ! Dans la région de {bonne_region}")
    else:
        print(f"Perdu ! Indice c'est dans la région : {bonne_region}")
        reponse = input(guess + " ?")
        check_answer(bonne_reponse, bonne_region, reponse) # Fonction récursive !