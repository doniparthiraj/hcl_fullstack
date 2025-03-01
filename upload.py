import networkx as nx
import pandas as pd
from dbhelper import db_helper

# csv_file = "banks.csv"
# df = pd.read_csv(csv_file)


# for _, row in df.iterrows():
#     db_helper.add_bank_details({"bic":row["BIC"], "charges":row["Charge"]})

csv_file = "links.csv"
df = pd.read_csv(csv_file)


for _, row in df.iterrows():
    db_helper.link_bank({
        "from_bic" :row["FromBIC"], 
        "to_bic":row["ToBIC"], 
        "time":row["TimeTakenInMinutes"]})

