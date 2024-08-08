# cd /Desktop/30DaysOfPython/python_for_datasience
# virtualenv pyds
# source pyds/bin/activate

# pip install numpy
# pip install pandas
# pip install xlrd # read and format Excel data
# pip install pynsee # for Insee data
# pip install great_tables # to have pretty table
# pip install requests # to send API request
# pip install matplotlib # for plots

"""
Manipulation - part 1
"""

# 4.1

## download data
import requests

url = "https://www.insee.fr/fr/statistiques/fichier/6800675/v_commune_2023.csv"
response = requests.get(url)

# Assurez-vous que la requête a réussi
if response.status_code == 200:
    with open("cog_2023.csv", "wb") as file:
        file.write(response.content)
else:
    print("Download failed. HTTP status :", response.status_code)

## The file was written in the dir of Python-datascientist-notebook
"Python-datascientist-notebook/cog_2023.csv"
# data has 12 columns and contians some missing data


# 4.2 read online CSV
url = "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"

## 4.2.1 import CSV
import pandas as pd

emissions = pd.read_csv(url)

## 4.2.2
emissions.head(10) # first 10
emissions.tail(15) # last 15
emissions.sample(10) # 10 random lines

## 4.2.3
emissions.sample(frac=0.05, replace=False)

## 4.2.4
emissions.sample(10).sample(100, replace=True)

## 4.2.5
emissions.sample(6).sample(100, replace=True, weights=[0.5] + [0.1] * 5)


# 7
df = pd.read_csv(
    "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"
)
df.head(3)
df[df["Commune"].str.contains("MAUR")]
df.iloc[35600,:]

aa = df.agg(
    {
        "Agriculture": ["sum", "mean"],
        "Résidentiel": ["mean", "std", "var"],
        "Commune": "nunique",
    }
)
type(aa)

emissions_totales = pd.DataFrame(
    df.sum(numeric_only=True), columns=["emissions"]
).reset_index(names="secteur")

emissions_totales["emissions (%)"] = (
    100 * emissions_totales["emissions"] / emissions_totales["emissions"].sum()
)
emissions_totales.sort_values("emissions", ascending=False).round()


# 9

import pandas as pd

url = "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"

emissions = pd.read_csv(url)
emissions.head(2)

## 9.1
variables = [
    "INSEE commune", "Commune", "Autres transports", "Autres transports international"
]
emissions_copy = emissions.loc[:, variables]

## 9.2
emissions_copy = emissions_copy.rename(
    {
        "INSEE commune": "code_insee",
        "Autres transports": "transports",
        "Autres transports international": "transports_international"
    },
    axis="columns"
)

## 9.3
emissions_copy = emissions_copy.fillna(0)

## 9.4
emissions_copy["dep"] = emissions_copy["code_insee"].str[:2]
emissions_copy["transports_total"] = emissions_copy["transports"] + emissions_copy["transports_international"]

## 9.5
emissions_copy = emissions_copy.sort_values("transports_total", ascending=False)
# emissions_copy["dep"].count()
# emissions_copy["dep"].nunique()

## 9.6
dep13_31 = emissions_copy[
    emissions_copy["dep"].isin(["13", "31"])
].sort_values("transports_total", ascending=False)

## 9.7
emi_dep = emissions_copy.groupby("dep").agg({"transports_total": "sum"})
emi_dep = emi_dep.reset_index(names="dep")
emi_dep["pct"] = emi_dep["transports_total"] / emi_dep["transports_total"].sum() * 100
emi_dep.sort_values("pct", ascending=False)

emissions_totales = pd.DataFrame(
    df.sum(numeric_only=True), columns=["emissions"]
).reset_index(names="secteur")


"""
Manipulation - part 2
https://pythonds.linogaliana.fr/content/manipulation/02_pandas_suite.html
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pynsee
import pynsee.download

np.random.seed(123)


meta = pynsee.get_file_list()
meta.loc[meta["label"].str.contains(r"Filosofi.*2016")] # targeted files


url = "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"
emissions = pd.read_csv(url)
emissions.head(2)

secteurs = emissions.select_dtypes(include="number").columns # get all numeric columns

emissions["dep"] = emissions["INSEE commune"].str[:2] # creat department abbr


filosofi = pynsee.download_file("FILOSOFI_COM_2016") # get file of income 2016

filosofi.dtypes # all columns are "object"

## convert to float for all columns starts from the index 2 (col 3)
## use dictionary comprenhension to generate keys of column name and value are float
## then do the astype to convert
filosofi = filosofi.astype({c: "float" for c in filosofi.columns[2:]})

filosofi.isnull().mean().sort_values(ascending=False) # pct of NA
filosofi.isnull().sum().sort_values(ascending=False) # nb of NA

filosofi["dep"] = filosofi["CODGEO"].str[:2]

filosofi.groupby("dep").__class__
# <class 'pandas.core.groupby.generic.DataFrameGroupBy'>

### ref commune
url_cog_2023 = "https://www.insee.fr/fr/statistiques/fichier/6800675/v_commune_2023.csv"
cog_2023 = pd.read_csv(url_cog_2023)
communes = cog_2023.loc[cog_2023["TYPECOM"] == "COM"]
communes.loc[:, ["COM", "DEP", "REG"]].nunique()
# COM    34945
# DEP      101
# REG       18
# dtype: int64
communes.groupby("DEP").agg({"COM": "nunique"})
#      COM
# DEP     
# 01   392
# 02   798
# 03   317
# 04   198
# 05   162
# ..   ...
# 971   32
# 972   34
# 973   22
# 974   24
# 976   17
#
# [101 rows x 1 columns]

# convert Series to DF, reset index and order by nb commune
(
    communes.groupby("DEP")
    .agg({"COM": "nunique"})
    .reset_index()
    .sort_values("COM")
)

type(filosofi["NBPERSMENFISC16"].sum()) # <class 'numpy.float64'>
type(filosofi.agg({"NBPERSMENFISC16": "sum"})) # <class 'pandas.core.series.Series'>

filosofi.groupby("dep")["LIBGEO"].count() # count nb of communes per department
filosofi[filosofi["dep"] == "01"]

filosofi.groupby("dep")["NBPERSMENFISC16"].sum() # sum of NBPERSMENFISC16 per department
## 1st groupby, 2nd select the column, 3rd operation
## output is a Series

filosofi.groupby("dep").agg({"NBPERSMENFISC16": "sum"})
## output is a DF

# Exercice of section 3.4

## Q1

url = "https://koumoul.com/s/data-fair/api/v1/datasets/igt-pouvoir-de-rechauffement-global/convert"

import pandas as pd

emissions = pd.read_csv(url)

emissions["dep"] = emissions["INSEE commune"].str[:2]
emissions.columns
# Index(['INSEE commune', 'Commune', 'Agriculture', 'Autres transports',
#        'Autres transports international', 'CO2 biomasse hors-total', 'Déchets',
#        'Energie', 'Industrie hors-énergie', 'Résidentiel', 'Routier',
#        'Tertiaire', 'dep'],
#       dtype='object')

emis_dep = (
    emissions.groupby("dep")
    .agg({'Résidentiel': "sum"})
    .reset_index()
    .sort_values("Résidentiel", ascending=False)
)
emis_dep['Résidentiel (% valeur max)'] = (
    emis_dep['Résidentiel'] / emis_dep['Résidentiel'].max()
)

## Q2 

emis_dep_total = emissions.groupby("dep").sum(numeric_only=True)
emis_dep_total["total"] = emis_dep_total.sum(axis="columns")

secteurs = emissions.select_dtypes(include="number").columns

emis_dep_total["pct" + secteurs] = (
    emis_dep_total.loc[:, secteurs]
    .div(emis_dep_total["total"], axis = "index") * 100
)

# Exercice of 4.2
## Q1
df_wide = emissions.copy()

## Q2
id_cols = df_wide.select_dtypes(include="object").columns
df_long = df_wide.melt(id_vars=id_cols, var_name="secteurs", value_name="emission")

## Q3
(
    df_long.groupby("secteurs").agg({"emission": "sum"})
    .reset_index()
).plot(kind="hist")

## Q4
df_long["dep"] = df_long["INSEE commune"].str[:2]
(
    df_long.sort_values(["dep", "emission"], ascending=False)
    .groupby("dep")
    .head(1)
)

## or use indexing
# Group by 'dep' and get the index of the row with the maximum emission for each group
idx = df_long.groupby('dep')['emission'].idxmax()
# Use the index to filter the original DataFrame
df_long.loc[idx, ['dep', 'secteurs', 'emission']]


# 5 Join databases

emissions.head(2)
filosofi.head(2)

emissions = emissions.reset_index(names=["id_left"])
filosofi = filosofi.reset_index(names=["id_right"])

left_merged = emissions.merge(
    filosofi, 
    left_on = ["INSEE commune", "dep"],
    right_on = ["CODGEO", "dep"],
    how = "left"
)
left_merged.head(3)

left_merged.shape[0] == emissions.shape[0]
left_merged.loc[left_merged["id_right"].isna()].tail(3)
filosofi.loc[
    filosofi["LIBGEO"].str.lower().str.contains("courcouronnes")]

right_merged = emissions.merge(
    filosofi, 
    left_on = ["INSEE commune", "dep"],
    right_on = ["CODGEO", "dep"],
    how = "right"
)
right_merged.head(3)
right_merged.shape[0] == filosofi.shape[0]
right_merged["id_left"].isna().sum()
right_merged.loc[right_merged["id_left"].isna()].tail(2)

emissions.loc[emissions["Commune"].str.contains("MARSEILLE")]

emissions.loc[emissions["INSEE commune"].str.startswith("75")]

inner_merged = emissions.merge(
    filosofi, 
    left_on = ["INSEE commune", "dep"],
    right_on = ["CODGEO", "dep"],
    how = "inner"
)
inner_merged.head(3)

inner_merged.shape[0] == (left_merged.shape[0] - left_merged["id_right"].isna().sum())
inner_merged.shape[0] == (right_merged.shape[0] - right_merged["id_left"].isna().sum())

full_merged = emissions.merge(
    filosofi, 
    left_on = ["INSEE commune", "dep"],
    right_on = ["CODGEO", "dep"],
    how = "outer"
)

(full_merged["id_left"].isna().sum() + full_merged["id_right"].isna().sum()) == (
    left_merged["id_right"].isna().sum() + right_merged["id_left"].isna().sum()
)


emissions.loc[emissions["INSEE commune"].str.contains("216")]

filosofi.loc[
    filosofi["CODGEO"].str.contains("216")
    & filosofi["LIBGEO"].str.contains("Tours")
]

# exercice 5.4.1
## Q1

filosofi.shape
emissions.shape

## Q2
doublons = filosofi.groupby("LIBGEO").count()["CODGEO"]
doublons = doublons.loc[doublons > 1]
doublons = doublons.reset_index()

## Q3
filosofi[filosofi["LIBGEO"].isin(doublons["LIBGEO"])]

## Q4
filosofi[filosofi["LIBGEO"].isin(doublons["LIBGEO"])].sort_values("LIBGEO")

## Q5
dup_commune = filosofi[filosofi["LIBGEO"].isin(doublons["LIBGEO"])]
dup_commune["NBPERSMENFISC16"].describe()

nodup_commune = filosofi[~filosofi["LIBGEO"].isin(doublons["LIBGEO"])] # `~` is the bitwise NOT operator
# nodup_commune = filosofi[filosofi["LIBGEO"].isin(doublons["LIBGEO"]) == False]
nodup_commune["NBPERSMENFISC16"].describe()

## Q6
big_city = filosofi[filosofi["NBPERSMENFISC16"] > 1e5].copy()
taux = big_city["LIBGEO"].isin(doublons["LIBGEO"]).mean() * 100 #4/48=0.83
print(f"The percentage is {taux:.2f}%")

## Q7
filosofi[filosofi["LIBGEO"] == "Montreuil"]
filosofi[filosofi["LIBGEO"].str.contains("Saint-Denis")]

# exercice 5.4.2
## Q1
emissions["emissions"] = emissions.sum(numeric_only=True, axis="columns")

## Q2
tab_merge = emissions.merge(
    filosofi,
    left_on="INSEE commune", right_on="CODGEO", how="left"
)

## Q3
tab_merge["empreinte"] = tab_merge["emissions"] / tab_merge["NBPERSMENFISC16"]

## Q4
tab_merge["empreinte"].describe()
tab_merge["empreinte"].plot(kind="hist")
np.log(tab_merge["empreinte"]).plot(kind="hist")
