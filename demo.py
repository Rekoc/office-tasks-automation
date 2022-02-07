import pandas

path = "./statics/sampledataworkorders.xlsx"
data_frame = pandas.read_excel(path, sheet_name="WOs")

# Affiche le type des colonnes
#print(data.dtypes)
# Affiche des données diverses relatives aux données
#print(data.info(verbose=True))
# Compte le nombre de cellule non-nulle de chaque ligne/colonne
#print(data.count())
# Affiche les colonnes de votre DataFrame
#print(data.columns)
# Converti les DataFrames en JSON
#print(f"{data.to_json()}\n")
# Converti les DataFrames en dictionnaire
#print(f"{data.to_dict()}\n")
# Créer un fichier de type Excel avec les données "data" importées
# data.to_excel("./demo_excel.xlsx")


"""path = "./statics/exemple-trame.txt"
with open(path, "r") as file_test:
    for line in file_test.readlines():
        line_splited = line.split(";")
        print("----- New line -----")
        for item in line_splited:
            data = item.split(":")
            if len(data) <= 1:
                # Continue la boucle en ignorant le code qui suit
                continue
            # data --> ["regulElapsedDuration", " 0"]
            value_name = data[0]
            value = data[1].replace(' ', '')
            print(f"value_name = {value_name} // value --> {value}")
        print("\n\n")"""

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
value_counts = data_frame["District"].value_counts()
labels = value_counts.index
values = value_counts.values
explode = []
for i in range(0, len(labels)):
    if i % 5 == 0:
        explode.append(0.1)
    else:
        explode.append(0)
wedges, texts, autotexts = ax.pie(
    values,
    explode=explode,
    autopct='%1.1f%%',
    center=(4, 4),
    wedgeprops={"linewidth": 1, "edgecolor": "white"},
    frame=True
)
plt.axis('off')
wedges = value_counts.index
ax.legend(,
          value_counts.index,
          title="District",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.show()





