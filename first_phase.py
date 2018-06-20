import pandas as pd
pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 200)
from collections import Counter

dataframe1 = pd.read_excel("Two Sets - sample data for dedup.xlsx", sheetname="Sample 1")
dataframe2 = pd.read_excel("Two Sets - sample data for dedup.xlsx", sheetname="Sample 2")
dataframe1['Data set 1 - User Name'] = dataframe1['Data set 1 - User Name'].fillna("not_found_1")
dataframe2['Data set 2 - User Name'] = dataframe2['Data set 2 - User Name'].fillna("not_found_2")
dataframe1['Data set 1 - Company Name'] = dataframe1['Data set 1 - Company Name'].fillna("not_found_1")
dataframe2['Data set 2 - Company Name'] = dataframe2['Data set 2 - Company Name'].fillna("not_found_2")
dataframe1['Data set 1  - email'] = dataframe1['Data set 1  - email'].fillna("not_found_1")
dataframe2['Data set 2 - email'] = dataframe2['Data set 2 - email'].fillna("not_found_2")
print("*************** Data Frame 1 ******************")
print(dataframe1.head())
print("*************** Data Frame 2 ******************")
print(dataframe2.head())
print("***********************************************")
def name_matching(str1, str2):
    list1 = str1.lower().strip().split()
    list2 = str2.lower().strip().split()
    list1 = [i.strip() for i in list1]
    list2 = [i.strip() for i in list2]
    combined_list = list1+list2
    counter = Counter(combined_list)
    matched_words = []
    for word in counter:
        if counter[word]>1:
            matched_words.append(word)
    p12 = 0
    p21 = 0
    if matched_words:
        p12 = len(matched_words)/len(list1)*100
        p21 = len(matched_words)/len(list2)*100
    if p12==100 or p21==100:
        return True
    else:
        return False

def email_matching(str1, str2):
    str1 = str1.lower().strip()
    str2 = str2.lower().strip()
    if str1==str2:
        print("Email Matched")
        return True
    else:
        return False

# def phone_matching(str1, str2):

for i in range(len(dataframe1)):
    for j in range(len(dataframe2)):
        print("*****************************************")
        try:
            name_match = name_matching(dataframe1['Data set 1 - User Name'][i],dataframe2['Data set 2 - User Name'][j])
        except Exception as e:
            print("Exception in Name Matching : ",e)
            pass
        try:
            company_match = name_matching(dataframe1['Data set 1 - Company Name'][i],dataframe2['Data set 2 - Company Name'][j])
        except Exception as e:
            print("Exception in Company Name Matching : ",e)
            pass
        try:
            email_match = email_matching(dataframe1['Data set 1  - email'][i],dataframe2['Data set 2 - email'][j])
        except Exception as e:
            print("Exception in Email Matching : ",e)
            pass
        print("Name    1 : {} | Name    2 : {} | Matching : {} ".format(dataframe1['Data set 1 - User Name'][i],dataframe2['Data set 2 - User Name'][j],name_match))
        print("Company 1 : {} | Company 2 : {} | Matching : {}".format(dataframe1['Data set 1 - Company Name'][i],dataframe2['Data set 2 - Company Name'][j],company_match))
        print("Email   1 : {} | Email   2 : {} | Matching : {} ".format(dataframe1['Data set 1  - email'][i],dataframe2['Data set 2 - email'][j],email_match))
        if name_match or company_match or email_match:
            print("************ MATCH FOUND *******************")
            continue