import pandas as pd
# Monday
df = pd.read_csv("dite_Mon.csv", encoding='euc_kr')
list2 = []
list21 = [[1,1,110000000000]]
list22 = []
for i in range(len(df)):
    for j in range(i, len(df)):
        if df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate'] >= 220.5 and df.loc[i]['Protein'] + df.loc[j]['Protein'] >= 38.5 and df.loc[i]['Fat'] + df.loc[j]['Fat']>= 36.75:
            carb = df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate']
            protein = df.loc[i]['Protein'] +df.loc[j]['Protein']
            fat = df.loc[i]['Fat'] + df.loc[j]['Fat']
            under = carb + protein + fat
            ratio_carb = carb/under
            ratio_protein = protein/under
            ratio_fat = protein/under
            if 0.55 <= ratio_carb <= 0.65:
                if 0.15 <= ratio_protein <= 0.25:
                    if 0.15 <= ratio_fat <= 0.25:
                        list2.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        if list21[0][2] > int(df.loc[i]['cost'])+ int(df.loc[j]['cost']):
                            del list21[:]
                            del list22[:]
                            list21.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list22.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        elif list21[0][2] == int(df.loc[i]['cost']) + int(df.loc[j]['cost']):
                            list21.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list22.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                else:
                    continue
            else:
                continue
if list2 == []:
    list2.append({'Monday': 'No diet'})
print(list2)
print(list21)
print(list22)
print('=============================')

# Tuesday
df = pd.read_csv("dite_Tues.csv", encoding='euc_kr')
list3 = []
list31 = [[1,1,10000000000]]
list32 = []
for i in range(len(df)):
    for j in range(i, len(df)):
        if df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate'] >= 220.5 and df.loc[i]['Protein'] + df.loc[j]['Protein'] >= 38.5 and df.loc[i]['Fat'] + df.loc[j]['Fat']>= 36.75:
            carb = df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate']
            protein = df.loc[i]['Protein'] +df.loc[j]['Protein']
            fat = df.loc[i]['Fat'] + df.loc[j]['Fat']
            under = carb + protein + fat
            ratio_carb = carb/under
            ratio_protein = protein/under
            ratio_fat = protein/under
            if 0.55 <= ratio_carb <= 0.65:
                if 0.15 <= ratio_protein <= 0.25:
                    if 0.15 <= ratio_fat <= 0.25:
                        list3.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        if list31[0][2] > int(df.loc[i]['cost'])+ int(df.loc[j]['cost']):
                            del list31[:]
                            del list32[:]
                            list31.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list32.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        elif list31[0][2] == int(df.loc[i]['cost']) + int(df.loc[j]['cost']):
                            list31.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list32.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                else:
                    continue
            else:
                continue
if list3 == []:
    list3.append({'Tuesday': 'No diet'})
print(list3)
print(list31)
print(list32)
print('=============================')

# Wednesday

df = pd.read_csv("dite_Wed.csv", encoding='euc_kr')
list4 = []
list41 = [[1,1,110000000000]]
list42 = []
for i in range(len(df)):
    for j in range(i, len(df)):
        if df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate'] >= 220.5 and df.loc[i]['Protein'] + df.loc[j]['Protein'] >= 38.5 and df.loc[i]['Fat'] + df.loc[j]['Fat']>= 36.75:
            carb = df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate']
            protein = df.loc[i]['Protein'] + df.loc[j]['Protein']
            fat = df.loc[i]['Fat'] + df.loc[j]['Fat']
            under = carb + protein + fat
            ratio_carb = carb/under
            ratio_protein = protein/under
            ratio_fat = protein/under
            if 0.55 <= ratio_carb <= 0.65:
                if 0.15 <= ratio_protein <= 0.25:
                    if 0.15 <= ratio_fat <= 0.25:
                        list4.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        if list41[0][2] > int(df.loc[i]['cost'])+ int(df.loc[j]['cost']):
                            del list41[:]
                            del list42[:]
                            list41.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list42.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        elif list41[0][2] == int(df.loc[i]['cost']) + int(df.loc[j]['cost']):
                            list41.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list42.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                else:
                    continue
            else:
                continue

if list4 == []:
    list4.append({'Wednesday':'No diet'})
print(list4)
print(list41)
print(list42)
print('=============================')

# Thursday
df = pd.read_csv("dite_Thurs.csv", encoding='euc_kr')
list5 = []
list51 = [[1,1,110000000000]]
list52 =[]
for i in range(len(df)):
    for j in range(i, len(df)):
        if df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate'] >= 220.5 and df.loc[i]['Protein'] + df.loc[j]['Protein'] >= 38.5 and df.loc[i]['Fat'] + df.loc[j]['Fat']>= 36.75:
            carb = df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate']
            protein = df.loc[i]['Protein'] +df.loc[j]['Protein']
            fat = df.loc[i]['Fat'] + df.loc[j]['Fat']
            under = carb + protein + fat
            ratio_carb = carb/under
            ratio_protein = protein/under
            ratio_fat = protein/under
            if 0.55 <= ratio_carb <= 0.65:
                if 0.15 <= ratio_protein <= 0.25:
                    if 0.15 <= ratio_fat <= 0.25:
                        list5.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        if list51[0][2] > int(df.loc[i]['cost']) + int(df.loc[j]['cost']):
                            del list51[:]
                            del list52[:]
                            list51.append(
                                [df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list52.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        elif list51[0][2] == int(df.loc[i]['cost']) + int(df.loc[j]['cost']):
                            list51.append(
                                [df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list52.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                else:
                    continue
            else:
                continue

if list5 == []:
    list5.append({'Thursday':'No diet'})
print(list5)
print(list51)
print(list52)
print('=============================')

# Friday
df = pd.read_csv("dite_Fri.csv", encoding='euc_kr')
list6 = []
list61 = [[1,1,110000000000]]
list62 = []
for i in range(len(df)):
    for j in range(i, len(df)):
        if df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate'] >= 220.5 and df.loc[i]['Protein'] + df.loc[j]['Protein'] >= 38.5 and df.loc[i]['Fat'] + df.loc[j]['Fat']>= 36.75:
            carb = df.loc[i]['Carbonhydrate'] + df.loc[j]['Carbonhydrate']
            protein = df.loc[i]['Protein'] +df.loc[j]['Protein']
            fat = df.loc[i]['Fat'] + df.loc[j]['Fat']
            under = carb + protein + fat
            ratio_carb = carb/under
            ratio_protein = protein/under
            ratio_fat = protein/under
            if 0.55 <= ratio_carb <= 0.65:
                if 0.15 <= ratio_protein <= 0.25:
                    if 0.15 <= ratio_fat <= 0.25:
                        list6.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        if list61[0][2] > int(df.loc[i]['cost'])+ int(df.loc[j]['cost']):
                            del list61[:]
                            del list62[:]
                            list61.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list62.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                        elif list61[0][2] == int(df.loc[i]['cost']) + int(df.loc[j]['cost']):
                            list61.append([df.loc[i]['cost'], df.loc[j]['cost'], int(df.loc[i]['cost']) + int(df.loc[j]['cost'])])
                            list62.append([df.loc[i]['Menu'], df.loc[j]['Menu']])
                else:
                    continue
            else:
                continue

if list6 == []:
    list6.append({'Friday':'No diet'})
print(list6)
print(list61)
print(list62)
