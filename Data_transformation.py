import os
import json
import pandas as pd
import mysql.connector


path1="pulse/data/aggregated/transaction/country/india/state/"
Agg_trans=os.listdir(path1)
#Agg_trans
#Agg_trans--> to get the list of states in India

#This is to extract the data's to create a dataframe

Agg_trans_list = {'State':[], 'Year':[],'Quarter':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_trans:
    path_i = path1 + i+ "/"
    Agg_yr = os.listdir(path_i)
    for j in Agg_yr:
        path_j = path_i + j + "/"
        Agg_yr_list= os.listdir(path_j)
        for k in Agg_yr_list:
            path_k = path_j + k
            Data = open(path_k,'r')
            Data = json.load(Data)
            for z in Data['data']['transactionData']:
                Name = z['name']
                count = z['paymentInstruments'][0]['count']
                amount = z['paymentInstruments'][0]['amount']
                Agg_trans_list['Transaction_type'].append(Name)
                Agg_trans_list['Transaction_count'].append(count)
                Agg_trans_list['Transaction_amount'].append(amount)
                Agg_trans_list['State'].append(i)
                Agg_trans_list['Year'].append(j)
                Agg_trans_list['Quarter'].append(int(k.strip('.json')))

# Successfully created a dataframe
df_aggregated_transaction=pd.DataFrame(Agg_trans_list)
#print(df_aggregated_transaction)


# TO GET THE DATA-FRAME OF AGGREGATED <--> USER

path2 = "pulse/data/aggregated/user/country/india/state/"
Agg_user = os.listdir(path2)

Agg_user_list = {'State': [], 'Year': [], 'Quarter': [], 'brands': [], 'Count': [],
        'Percentage': []}
for i in Agg_user:
    p_i = path2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            Data = json.load(Data)
            try:
                for l in Data["data"]["usersByDevice"]:
                    brand_name = l["brand"]
                    count_ = l["count"]
                    ALL_percentage = l["percentage"]
                    Agg_user_list["brands"].append(brand_name)
                    Agg_user_list["Count"].append(count_)
                    Agg_user_list["Percentage"].append(ALL_percentage)
                    Agg_user_list["State"].append(i)
                    Agg_user_list["Year"].append(j)
                    Agg_user_list["Quarter"].append(int(k.strip('.json')))
            except:
                pass
df_aggregated_user = pd.DataFrame(Agg_user_list)
#print(df_aggregated_user)




# TO GET THE DATA-FRAME OF MAP <--> TRANSACTION

path3 = "pulse/data/map/transaction/hover/country/india/state/"
map_trans = os.listdir(path3)

map_trans_list = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'count': [],
        'amount': []}
for i in map_trans:
    p_i = path3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k       
            Data = open(p_k, 'r')
            Data = json.load(Data)
            
            for l in Data["data"]["hoverDataList"]:
                District = l["name"]
                count = l["metric"][0]["count"]
                amount = l["metric"][0]["amount"]
                map_trans_list["District"].append(District)
                map_trans_list["count"].append(count)
                map_trans_list["amount"].append(amount)
                map_trans_list['State'].append(i)
                map_trans_list['Year'].append(j)
                map_trans_list['Quarter'].append(int(k.strip('.json')))
df_map_transaction = pd.DataFrame(map_trans_list)
#print(df_map_transaction)

# TO GET THE DATA-FRAME OF MAP <--> USER


path4 = "pulse/data/map/user/hover/country/india/state/"
map_user = os.listdir(path4)

map_user_list = {"State": [], "Year": [], "Quarter": [], "District": [],
        "RegisteredUser": []}
for i in map_user:
    p_i = path4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
           
            Data = open(p_k, 'r')
            Data = json.load(Data)

            for l in Data["data"]["hoverData"].items():
                district = l[0]
                registereduser = l[1]["registeredUsers"]
                map_user_list["District"].append(district)
                map_user_list["RegisteredUser"].append(registereduser)
                map_user_list['State'].append(i)
                map_user_list['Year'].append(j)
                map_user_list['Quarter'].append(int(k.strip('.json')))
df_map_user = pd.DataFrame(map_user_list)
#print(df_map_user)



# TO GET THE DATA-FRAME OF TOP <--> TRANSACTION

path5 = "pulse/data/top/transaction/country/india/state/"
top_trans = os.listdir(path5)

top_trans_list = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_count': [],
        'Transaction_amount': []}
for i in top_trans:
    p_i = path5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            Data = json.load(Data)
            for l in Data['data']['pincodes']:
                Name = l['entityName']
                count = l['metric']['count']
                amount = l['metric']['amount']
                top_trans_list['District'].append(Name)
                top_trans_list['Transaction_count'].append(count)
                top_trans_list['Transaction_amount'].append(amount)
                top_trans_list['State'].append(i)
                top_trans_list['Year'].append(j)
                top_trans_list['Quarter'].append(int(k.strip('.json')))
df_top_transaction = pd.DataFrame(top_trans_list)
# print(df_top_transaction)

# TO GET THE DATA-FRAME OF TOP <--> USER

path6 = "pulse/data/top/user/country/india/state/"
top_user = os.listdir(path6)

top_user_list = {'State': [], 'Year': [], 'Quarter': [], 'District': [],
        'RegisteredUser': []}
for i in top_user:
    p_i = path6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            # print(p_k)
            Data = open(p_k, 'r')
            Data = json.load(Data)
            for l in Data['data']['pincodes']:
                Name = l['name']
                registeredUser = l['registeredUsers']
                top_user_list['District'].append(Name)
                top_user_list['RegisteredUser'].append(registeredUser)
                top_user_list['State'].append(i)
                top_user_list['Year'].append(j)
                top_user_list['Quarter'].append(int(k.strip('.json')))
df_top_user = pd.DataFrame(top_user_list)
# print(df_top_user)

# CHECKING FOR MISSING VALUES,NULL VALUES

#df_aggregated_transaction.info()
#df_aggregated_user.info()
#df_map_transaction.info()
#df_map_user.info()
#df_top_transaction.info()
#df_top_user.info()

df_aggregated_transaction["State"]=df_aggregated_transaction["State"].replace({'andaman-&-nicobar-islands':'Andaman & Nicobar',
                                                                              'andhra-pradesh': 'Andhra Pradesh',
                                                                              'arunachal-p':'Arunanchal Pradesh',
                                                                              'assam': 'Assam',
                                                                              'bihar': 'Bihar',
                                                                              'chandigarh': 'Chandigarh',
                                                                              'chhattisgarh': 'Chhattisgarh',
                                                                              'dadra-&-nagar-haveli-&-dama':'Dadara & Nagar Havelli',
                                                                              'delhi': 'NCT of Delhi',
                                                                              'goa': 'Goa',
                                                                              'gujarat': 'Gujarat',
                                                                              'haryana': 'Haryana',
                                                                              'himachal-pradesh': 'Himachal Pradesh',
                                                                              'jammu-&-kashmir': 'Jammu & Kashmir',
                                                                              'jharkhand': 'Jharkhand',
                                                                              'karnataka': 'Karnataka',
                                                                              'kerala': 'Kerala',
                                                                              'ladakh': 'Ladakh',
                                                                              'lakshadweep':'Lakshadweep',
                                                                              'madhya-pradesh': 'Madhya Pradesh',
                                                                              'maharashtra': 'Maharashtra',
                                                                              'manipur': 'Manipur',
                                                                              'meghalaya': 'Meghalaya',
                                                                              'mizoram':'Mizoram',
                                                                              'nagaland': 'Nagaland',
                                                                              'puducherry': 'Puducherry',
                                                                              'punjab': 'Punjab',
                                                                              'rajasthan': 'Rajasthan',
                                                                              'sikkim': 'Sikkim',
                                                                              'tamil-nadu': 'Tamil Nadu',
                                                                              'telangana': 'Telangana',
                                                                              'tripura': 'Tripura',
                                                                              'uttar-pradesh': 'Uttar Pradesh',
                                                                              'uttarakhand': 'Uttarakhand',
                                                                              'west-bengal': 'WestBengal',
                                                                              'odisha':'Odisha'})
df_aggregated_user["State"] = df_aggregated_user["State"].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar',
                                                                   'andhra-pradesh': 'Andhra Pradesh',
                                                                   'arunachal-p': 'Arunachal Pradesh',
                                                                   'assam': 'Assam',
                                                                   'bihar': 'Bihar',
                                                                   'chandigarh': 'Chandigarh',
                                                                   'chhattisgarh': 'Chhattisgarh',
                                                                   'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
                                                                   'delhi': 'NCT of Delhi',
                                                                   'goa': 'Goa',
                                                                   'gujarat': 'Gujarat',
                                                                   'haryana': 'Haryana',
                                                                   'himachal-pradesh': 'Himachal Pradesh',
                                                                   'jammu-&-kashmir': 'Jammu & Kashmir',
                                                                   'jharkhand': 'Jharkhand',
                                                                   'karnataka': 'Karnataka',
                                                                   'kerala': 'Kerala',
                                                                   'ladakh': 'Ladakh',
                                                                   'lakshadweep': 'Lakshadweep',
                                                                   'madhya-pradesh': 'Madhya Pradesh',
                                                                   'maharashtra': 'Maharashtra',
                                                                   'manipur': 'Manipur',
                                                                   'meghalaya': 'Meghalaya',
                                                                   'mizoram': 'Mizoram',
                                                                   'nagaland': 'Nagaland',
                                                                   'puducherry': 'Puducherry',
                                                                   'punjab': 'Punjab',
                                                                   'rajasthan': 'Rajasthan',
                                                                   'sikkim': 'Sikkim',
                                                                   'tamil-nadu': 'Tamil Nadu',
                                                                   'telangana': 'Telangana',
                                                                   'tripura': 'Tripura',
                                                                   'uttar-pradesh': 'Uttar Pradesh',
                                                                   'uttarakhand': 'Uttarakhand',
                                                                   'west-bengal': 'West Bengal',
                                                                   'odisha': 'Odisha'
                                                               })
df_map_transaction["State"] = df_map_transaction["State"].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar',
                                                                   'andhra-pradesh': 'Andhra Pradesh',
                                                                   'arunachal-p': 'Arunachal Pradesh',
                                                                   'assam': 'Assam',
                                                                   'bihar': 'Bihar',
                                                                   'chandigarh': 'Chandigarh',
                                                                   'chhattisgarh': 'Chhattisgarh',
                                                                   'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
                                                                   'delhi': 'NCT of Delhi',
                                                                   'goa': 'Goa',
                                                                   'gujarat': 'Gujarat',
                                                                   'haryana': 'Haryana',
                                                                   'himachal-pradesh': 'Himachal Pradesh',
                                                                   'jammu-&-kashmir': 'Jammu & Kashmir',
                                                                   'jharkhand': 'Jharkhand',
                                                                   'karnataka': 'Karnataka',
                                                                   'kerala': 'Kerala',
                                                                   'ladakh': 'Ladakh',
                                                                   'lakshadweep': 'Lakshadweep',
                                                                   'madhya-pradesh': 'Madhya Pradesh',
                                                                   'maharashtra': 'Maharashtra',
                                                                   'manipur': 'Manipur',
                                                                   'meghalaya': 'Meghalaya',
                                                                   'mizoram': 'Mizoram',
                                                                   'nagaland': 'Nagaland',
                                                                   'puducherry': 'Puducherry',
                                                                   'punjab': 'Punjab',
                                                                   'rajasthan': 'Rajasthan',
                                                                   'sikkim': 'Sikkim',
                                                                   'tamil-nadu': 'Tamil Nadu',
                                                                   'telangana': 'Telangana',
                                                                   'tripura': 'Tripura',
                                                                   'uttar-pradesh': 'Uttar Pradesh',
                                                                   'uttarakhand': 'Uttarakhand',
                                                                   'west-bengal': 'West Bengal',
                                                                   'odisha': 'Odisha'
                                                               })
df_map_user["State"] = df_map_user["State"].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar',
                                                                   'andhra-pradesh': 'Andhra Pradesh',
                                                                   'arunachal-p': 'Arunachal Pradesh',
                                                                   'assam': 'Assam',
                                                                   'bihar': 'Bihar',
                                                                   'chandigarh': 'Chandigarh',
                                                                   'chhattisgarh': 'Chhattisgarh',
                                                                   'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
                                                                   'delhi': 'NCT of Delhi',
                                                                   'goa': 'Goa',
                                                                   'gujarat': 'Gujarat',
                                                                   'haryana': 'Haryana',
                                                                   'himachal-pradesh': 'Himachal Pradesh',
                                                                   'jammu-&-kashmir': 'Jammu & Kashmir',
                                                                   'jharkhand': 'Jharkhand',
                                                                   'karnataka': 'Karnataka',
                                                                   'kerala': 'Kerala',
                                                                   'ladakh': 'Ladakh',
                                                                   'lakshadweep': 'Lakshadweep',
                                                                   'madhya-pradesh': 'Madhya Pradesh',
                                                                   'maharashtra': 'Maharashtra',
                                                                   'manipur': 'Manipur',
                                                                   'meghalaya': 'Meghalaya',
                                                                   'mizoram': 'Mizoram',
                                                                   'nagaland': 'Nagaland',
                                                                   'puducherry': 'Puducherry',
                                                                   'punjab': 'Punjab',
                                                                   'rajasthan': 'Rajasthan',
                                                                   'sikkim': 'Sikkim',
                                                                   'tamil-nadu': 'Tamil Nadu',
                                                                   'telangana': 'Telangana',
                                                                   'tripura': 'Tripura',
                                                                   'uttar-pradesh': 'Uttar Pradesh',
                                                                   'uttarakhand': 'Uttarakhand',
                                                                   'west-bengal': 'West Bengal',
                                                                   'odisha': 'Odisha'
                                                               })
df_top_transaction["State"] = df_top_transaction["State"].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar',
                                                                   'andhra-pradesh': 'Andhra Pradesh',
                                                                   'arunachal-p': 'Arunachal Pradesh',
                                                                   'assam': 'Assam',
                                                                   'bihar': 'Bihar',
                                                                   'chandigarh': 'Chandigarh',
                                                                   'chhattisgarh': 'Chhattisgarh',
                                                                   'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
                                                                   'delhi': 'NCT of Delhi',
                                                                   'goa': 'Goa',
                                                                   'gujarat': 'Gujarat',
                                                                   'haryana': 'Haryana',
                                                                   'himachal-pradesh': 'Himachal Pradesh',
                                                                   'jammu-&-kashmir': 'Jammu & Kashmir',
                                                                   'jharkhand': 'Jharkhand',
                                                                   'karnataka': 'Karnataka',
                                                                   'kerala': 'Kerala',
                                                                   'ladakh': 'Ladakh',
                                                                   'lakshadweep': 'Lakshadweep',
                                                                   'madhya-pradesh': 'Madhya Pradesh',
                                                                   'maharashtra': 'Maharashtra',
                                                                   'manipur': 'Manipur',
                                                                   'meghalaya': 'Meghalaya',
                                                                   'mizoram': 'Mizoram',
                                                                   'nagaland': 'Nagaland',
                                                                   'puducherry': 'Puducherry',
                                                                   'punjab': 'Punjab',
                                                                   'rajasthan': 'Rajasthan',
                                                                   'sikkim': 'Sikkim',
                                                                   'tamil-nadu': 'Tamil Nadu',
                                                                   'telangana': 'Telangana',
                                                                   'tripura': 'Tripura',
                                                                   'uttar-pradesh': 'Uttar Pradesh',
                                                                   'uttarakhand': 'Uttarakhand',
                                                                   'west-bengal': 'West Bengal',
                                                                   'odisha': 'Odisha'
                                                               })
df_top_user["State"] = df_top_user["State"].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar',
                                                                   'andhra-pradesh': 'Andhra Pradesh',
                                                                   'arunachal-p': 'Arunachal Pradesh',
                                                                   'assam': 'Assam',
                                                                   'bihar': 'Bihar',
                                                                   'chandigarh': 'Chandigarh',
                                                                   'chhattisgarh': 'Chhattisgarh',
                                                                   'dadra-&-nagar-haveli-&-dama': 'Dadra & Nagar Haveli',
                                                                   'delhi': 'NCT of Delhi',
                                                                   'goa': 'Goa',
                                                                   'gujarat': 'Gujarat',
                                                                   'haryana': 'Haryana',
                                                                   'himachal-pradesh': 'Himachal Pradesh',
                                                                   'jammu-&-kashmir': 'Jammu & Kashmir',
                                                                   'jharkhand': 'Jharkhand',
                                                                   'karnataka': 'Karnataka',
                                                                   'kerala': 'Kerala',
                                                                   'ladakh': 'Ladakh',
                                                                   'lakshadweep': 'Lakshadweep',
                                                                   'madhya-pradesh': 'Madhya Pradesh',
                                                                   'maharashtra': 'Maharashtra',
                                                                   'manipur': 'Manipur',
                                                                   'meghalaya': 'Meghalaya',
                                                                   'mizoram': 'Mizoram',
                                                                   'nagaland': 'Nagaland',
                                                                   'puducherry': 'Puducherry',
                                                                   'punjab': 'Punjab',
                                                                   'rajasthan': 'Rajasthan',
                                                                   'sikkim': 'Sikkim',
                                                                   'tamil-nadu': 'Tamil Nadu',
                                                                   'telangana': 'Telangana',
                                                                   'tripura': 'Tripura',
                                                                   'uttar-pradesh': 'Uttar Pradesh',
                                                                   'uttarakhand': 'Uttarakhand',
                                                                   'west-bengal': 'West Bengal',
                                                                   'odisha': 'Odisha'
                                                               })
    
    























#Clear null values in top_transaction Data
df_top_transaction=df_top_transaction.dropna()

df_aggregated_transaction.to_csv("aggregated_transaction.csv",index=False)
df_aggregated_user.to_csv("aggregated_user.csv",index=False)
df_map_transaction.to_csv("map_transaction.csv",index=False)
df_map_user.to_csv("map_user.csv",index=False)
df_top_transaction.to_csv("top_transaction.csv",index=False)
df_top_user.to_csv("top_user.csv",index=False)


"""
cnx = mysql.connector.connect(user='user', password='siddharth',
                              host='localhost',
                              database='database_name')
cursor = cnx.cursor()

create_table_query = '''CREATE TABLE table_name
                        (column1 datatype, column2 datatype, column3 datatype);'''
cursor.execute(create_table_query)

df_aggregated_transaction.to_sql('table_name', con=cnx, if_exists='replace', index=False)

"""