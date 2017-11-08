#!/usr/bin/env python
import requests
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#Wasn't able to get this to work... but tried going based of discussion boards and hints
#create dataframe
df = []
csv = open("ELECTION_ID", "w") #open from ELECTION_ID csv files

for id in ELECTION_ID:
    lastyear_url = base.format(id)
    lastyear_text = requests.get(lastyear_url).text
    Election_Data = "president_general_" + d[id] + ".csv"
#read csv files
    header = pd.read_csv(Election_Data, nrows = 1).dropna(axis = 1)
#submit to dataframe
    d = header.iloc[0].to_dict()
    df = pd.read_csv(Election_Data, index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican per hints
    df.dropna(inplace = True, axis = 1)    # drop empty columns per hints
    df["Election_Data"] = source[0]
#name dataframes by row header2
    df.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])
    all = pd.concat(df) #concat dataframes
    all["Republican Share"] = all["Republican"]/all["Total Votes Cast"] #for Republican proportion

#create graphs
#Accomack County
df["Accomack"].plot(kind = line)
plt.title("Accomack County Share of Republican Vote (1924-2016)")
plt.xlabel("Year") #x-axis
plt.ylabel("Republican Share") #y-axis
plt.savefig('accomack.pdf')
#Albermarle County
df["Albermarle"].plot(kind = line)
plt.title("Albermarle County Share of Republican Vote (1924-2016)")
plt.xlabel("Year")
plt.ylabel("Republican Share")
plt.savefig('albermarle.pdf')
#Alexandria County
df["Alexandria"].plot(kind = line)
plt.title("Alexandria City Share of Republican Vote (1924-2016)")
plt.xlabel("Year")
plt.ylabel("Republican Share")
plt.savefig('alexandria.pdf')

df["Alleghany County"].plot(kind = line)
plt.title("Alleghany County Share of Republican Vote (1924-2016)")
plt.xlabel("Year")
plt.ylabel("Republican Share")
plt.savefig('alleghany.pdf')
