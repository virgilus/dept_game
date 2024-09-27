from game.functions import *
df = load_df()
print(df.shape)

type_jeu = input("Nom ou code ?")
if type_jeu.lower() == "nom": play_name(df)
elif type_jeu.lower() == "code": play_code(df)
else: print("bye bye")