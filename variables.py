from views import pd

csv_files_NUMBER=2

# **********************************************List COUTRIES***************************************
list_country_vente = [
    'Banlieue Nord',
    'Les Berges du Lac',
    'Ariana',
    'Ben arous',
    'Bizerte',
    'Sousse',
    'Mannouba',
    'Nabeul',
    'Sfax',
    'Mahdia',
    'Djerba'
 ]

list_country_loc = [
    'Banlieue Nord',
    'Ariana',
    'Ben arous',
    'Bardo',
    'Mannouba', 
    'Bizerte',
    'Nabeul',   
    'Sfax',
    'Sousse',   
    'Mahdia', 
    'Monastir',
    'Gabes',  
    'Jendouba'
    ]

list_country_ratio = list(
    set(list_country_vente).intersection(list_country_loc))

#Return the dataframe of the csv file    
def dataframes(csv_file):
    return pd.read_csv(csv_file, encoding="Latin 1")

def fill_all_defs(vente_or_loc):
    list_to_fill=list()
    for i in range(csv_files_NUMBER):
        list_to_fill.append(dataframes(f"clear_csv_{vente_or_loc}_{i+1}.csv")) 
    return list_to_fill           

all_df_vente=list()
all_df_vente=fill_all_defs("vente")
all_df_loc=list()
all_df_loc=fill_all_defs("loc")
#***************************AVG Vente**********************************
#Return the avg in a giving country
def avg(str, df):
    return round(df[df["Country"] == str].Moy_prix_by_size.mean(),2)
# *********************RATIO*************************************)
def ratio(str, df_vente, df_loc):
    vente = avg(str, df_vente)
    loc = avg(str, df_loc)
    if(loc != 0):
        return vente/loc
    else:
        return vente

def list_avg(list_country_vente_or_loc,df):
    list_avg = list()
    for i in range(len(list_country_vente_or_loc)):
        list_avg.append(avg(list_country_vente_or_loc[i], df))
    return list_avg

def fill_all_avgs(list_df_vente_or_loc,list_country):
    all_list_avg=list()
    for df in list_df_vente_or_loc:    
        all_list_avg.append(list_avg(list_country, df))
    return all_list_avg   

def fill_all_ratio():
    all_ratio=list()
    sublist=list()
    for i in range(csv_files_NUMBER):
        sublist=list()
        for c in list_country_ratio:
            sublist.append(ratio(c,all_df_vente[i],all_df_loc[i]))
        all_ratio.append(sublist)    
    return all_ratio

#***************************************************************************
all_list_avg_vente=fill_all_avgs(all_df_vente,list_country_vente)
all_list_avg_loc=fill_all_avgs(all_df_loc,list_country_loc)            
all_list_ratio=fill_all_ratio()

def mean_detail(list_to_data):
    d=pd.DataFrame({"a":list_to_data})  
    return d.a.mean()

def avg_detail(folder,list_detail_coutries):
    list_detail=list()
    list_annonce=list()
    for c in list_detail_coutries:
        try:
            path = folder + "/%s.csv" % c
            #path = "Ariana/Chotrana.csv"
            #path=rf'{folder}\{c}.csv'
            df=pd.read_csv(path,encoding="latin 1")
            v=round(df["Moy_prix_by_size"].mean(),2)
            print(v)
            an=df.shape[0] # i will send vente country also for loc, if it doesnt exists : an=0
            list_annonce.append(an)
            list_detail.append(v)
        except:
            an=0 
            list_annonce.append(an)
    return list_detail,list_annonce
#*************************************************************
list_country_vente_Banlieue=["Carthage","Goulette","Kram","Marse","Sidi_bou_said","Gammarth"]
list_country_vente_lac=["Lac1","Lac2"]
list_country_vente_ariana=["Aouina","Chotrana","Cite ghazela","Ennasr","Menzah","Raoued","Sokra"]
list_country_vente_benaous=["Boumhel","El mourouj","Ezzahra","Rades"]
list_country_vente_sousse=["Chatt Meriem","Hergla","Kantaoui","Khezema"]

list_country_loc_Banlieue=["Carthage","Goulette","Kram","Marse"]
list_country_loc_sousse=["Chatt Meriem","Hergla","Kantaoui"]
#****************************************************************
def list_vente(i):#also ANNONCE
    list_all_vente=list()
    list_ban_vente,ann_ban_v=avg_detail(f"Banlieue_vente{i}",list_country_vente_Banlieue)
    list_lac_vente,ann_lac_v=avg_detail(f"Lac_vente{i}",list_country_vente_lac)
    list_ariana_vente,ann_ariana_v=avg_detail(f"Ariana_vente{i}",list_country_vente_ariana)
    list_benaous_vente,ann_benarous_v=avg_detail(f"Ben arous_vente{i}",list_country_vente_benaous)
    list_sousse_vente,ann_sousse_v=avg_detail(f"Sousse_vente{i}",list_country_vente_sousse)  
    list_all_vente=[list_ban_vente,list_lac_vente,list_ariana_vente,list_benaous_vente,list_sousse_vente]
    list_all_an_vente=[ann_ban_v,ann_lac_v,ann_ariana_v,ann_benarous_v,ann_sousse_v]
    return list_all_vente,list_all_an_vente

#**************************************************************
def list_loc(i):
    list_all_loc=list()
    list_ban_loc,ann_ban_l=avg_detail(f"Banlieue_loc{i}",list_country_vente_Banlieue)
    x,ann_lac_v=avg_detail(f"Lac_loc{i}",list_country_vente_lac)
    list_ariana_loc,ann_ariana_l=avg_detail(f"Ariana_loc{i}",list_country_vente_ariana)
    list_benaous_loc,ann_benarous_l=avg_detail(f"Ben arous_loc{i}",list_country_vente_benaous)
    list_sousse_loc,ann_sousse_l=avg_detail(f"Sousse_loc{i}",list_country_vente_sousse)  
    list_all_loc=[list_ban_loc,list_ariana_loc,list_benaous_loc,list_sousse_loc]
    list_all_an_loc=[ann_ban_l,ann_lac_v,ann_ariana_l,ann_benarous_l,ann_sousse_l]
    return list_all_loc,list_all_an_loc

avg_list_vente1,ann_vente1=list_vente(1)
avg_list_vente2,ann_vente2=list_vente(2)

avg_list_loc1,ann_loc1=list_loc(1)
avg_list_loc2,ann_loc2=list_loc(2)

dict_vente1=dict()
dict_vente1={"Banlieue Nord":[list_country_vente_Banlieue,avg_list_vente1[0]],"Les Berges du Lac":[list_country_vente_lac,avg_list_vente1[1]],"Ariana":[list_country_vente_ariana,avg_list_vente1[2]],'Ben arous':[list_country_vente_benaous,avg_list_vente1[3]],"Sousse":[list_country_vente_sousse,avg_list_vente1[4]]}

dict_loc1=dict()
dict_loc1={"Banlieue Nord":[list_country_loc_Banlieue,avg_list_loc1[0]],"Les Berges du Lac":[list(),list()],"Ariana":[list_country_vente_ariana,avg_list_loc1[1]],'Ben arous':[list_country_vente_benaous,avg_list_loc1[2]],"Sousse":[list_country_loc_sousse,avg_list_loc1[3]]}

# ************************************************************************************
dict_vente2=dict()
dict_vente2={"Banlieue Nord":[list_country_vente_Banlieue,avg_list_vente2[0]],"Les Berges du Lac":[list_country_vente_lac,avg_list_vente2[1]],"Ariana":[list_country_vente_ariana,avg_list_vente2[2]],'Ben arous':[list_country_vente_benaous,avg_list_vente2[3]],"Sousse":[list_country_vente_sousse,avg_list_vente2[4]]}

dict_loc2=dict()
dict_loc2={"Banlieue Nord":[list_country_loc_Banlieue,avg_list_loc2[0]],"Les Berges du Lac":[list(),list()],"Ariana":[list_country_vente_ariana,avg_list_loc2[1]],'Ben arous':[list_country_vente_benaous,avg_list_loc2[2]],"Sousse":[list_country_loc_sousse,avg_list_loc2[3]]}

#**************************************Detail *********************************************

dict_detail1={"Banlieue Nord":[list_country_vente_Banlieue,ann_vente1[0],ann_loc1[0],avg_list_vente1[0],avg_list_loc1[0],mean_detail(avg_list_vente1[0]),mean_detail(avg_list_loc1[0])],"Les Berges du Lac":[list_country_vente_lac,ann_vente1[1],ann_loc1[1],avg_list_vente1[1],list(),mean_detail(avg_list_vente1[1]),-1],"Ariana":[list_country_vente_ariana,ann_vente1[2],ann_loc1[2],avg_list_vente1[2],avg_list_loc1[1],mean_detail(avg_list_vente1[2]),mean_detail(avg_list_loc1[1])],'Ben arous':[list_country_vente_benaous,ann_vente1[3],ann_loc1[3],avg_list_vente1[3],avg_list_loc1[2],mean_detail(avg_list_vente1[3]),mean_detail(avg_list_loc1[2])],"Sousse":[list_country_vente_sousse,ann_vente1[4],ann_loc1[4],avg_list_vente1[4],avg_list_loc1[3],mean_detail(avg_list_vente1[4]),mean_detail(avg_list_loc1[3])]}
dict_detail2={"Banlieue Nord":[list_country_vente_Banlieue,ann_vente2[0],ann_loc2[0],avg_list_vente2[0],avg_list_loc2[0],mean_detail(avg_list_vente2[0]),mean_detail(avg_list_loc2[0])],"Les Berges du Lac":[list_country_vente_lac,ann_vente2[1],ann_loc2[1],avg_list_vente2[1],list(),mean_detail(avg_list_vente2[1]),-1],"Ariana":[list_country_vente_ariana,ann_vente2[2],ann_loc2[2],avg_list_vente2[2],avg_list_loc2[1],mean_detail(avg_list_vente2[2]),mean_detail(avg_list_loc2[1])],'Ben arous':[list_country_vente_benaous,ann_vente2[3],ann_loc2[3],avg_list_vente2[3],avg_list_loc2[2],mean_detail(avg_list_vente2[3]),mean_detail(avg_list_loc2[2])],"Sousse":[list_country_vente_sousse,ann_vente2[4],ann_loc2[4],avg_list_vente2[4],avg_list_loc2[3],mean_detail(avg_list_vente2[4]),mean_detail(avg_list_loc2[3])]}

#**************************************Market**********************************************
def shape_market(csv_file):
    return pd.read_csv(csv_file, encoding='ISO-8859-1').shape[0]

def for_market(i):
    j = shape_market(f"jumia_vente{i}.csv")
    tay_v = shape_market(f"tayara_vente{i}.csv")
    tay_l = shape_market(f"tayara_loc{i}.csv")
    tu = shape_market(f"tunisie_loc{i}.csv")
    dict_vente={"Tayara":tay_v,"Jumia":j}
    dict_loc={"Tayara":tay_l,"Tunisie annonce":tu}
    dict_all={"Tayara":tay_l+tay_v,"Tunisie annonce":tu,"Jumia":j}
    return dict_vente,dict_loc,dict_all

dict_market1=for_market(1)#tuple : vente, loc, all
dict_market2=for_market(2)#tuple : vente, loc, all

dict_market_all=[dict_market1,dict_market2]
# **********************************************************************************
#def nb_ann(str,df):#vente or loc
class data(object):
    lable = ""
    y = 0
    url = ""
    color=""
    def __init__(self, label, y,u='/no_deatil',color="#0074D9"):
        self.label = label
        self.y = y
        self.url = u
        self.color=color

class data_detail(object):
    list_countries=list()
    ann_vente = list()
    ann_loc = list()
    prix=list()
    prixl=list()
    mean_vente=0
    mean_loc=0
    def __init__(self,list_countries,ann_vente,ann_loc,prix,prixl,mean_vente,mean_loc):
        self.list_countries=list_countries
        self.ann_vente=ann_vente
        self.ann_loc=ann_loc
        self.prix=prix
        self.prixl=prixl
        self.mean_loc=mean_loc
        self.mean_vente=mean_vente
# ****************************************************************************************************


