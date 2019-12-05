import pandas as pd
import numpy as np

def extract(best):
    f = open(best+".html","r",encoding="utf-8")

    lines = f.readlines()
    actors  = []

    for x in lines :
        if x.find("ref_=nmls_pst") != -1 and x.find('<img alt="') != -1 :
            x = x[:95]
            # print(x)
            # print(">>>>>>>>>>>>" ,x.find("ref_=nmls_pst"))
            inquotes = False
            captured =False
            name=""
            i = x.find('<img alt="')
            while  True  :
                if inquotes :
                    if x[i] == '"':
                        captured = True
                        break
                    name+= x[i]
                else :
                    if x[i] == '"':
                        inquotes = True
                i+=1
            actors.append(name.replace(" ","").lower())
    df = pd.DataFrame({best : actors})
    df.to_csv(best+".csv",index=False)
extract("famousactors")
extract("bestwriters")
extract("bestproducers")
extract("bestdirectors")
