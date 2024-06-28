import random
import pandas as pd

# Fonction pour tirer aléatoirement deux jours de la semaine
def generer_jours_nettoyage(semaines):
    jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    planning = {}

    for semaine in range(1, semaines + 1):
        jours_nettoyage = random.sample(jours, 2)
        planning[f'Semaine {semaine}'] = jours_nettoyage

    return planning

# Générer le planning pour 4 semaines
semaines = 4
planning_nettoyage = generer_jours_nettoyage(semaines)

# Convertir le planning en DataFrame pour une meilleure visualisation
df_planning = pd.DataFrame.from_dict(planning_nettoyage, orient='index', columns=['Jour 1', 'Jour 2'])

# Afficher le planning
print(df_planning)
