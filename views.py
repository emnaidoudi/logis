from app import app,render_template,pd
from variables import data,dict_detail1,dict_detail2,dict_market_all,dict_loc1,dict_loc2,dict_vente2,dict_vente1,list_country_vente,list_country_loc,list_country_ratio,all_list_avg_vente,all_list_avg_loc,all_list_ratio ,data,data_detail
                    
countries_to_detail=["Banlieue Nord","Les Berges du Lac","Ariana","Ben arous","Sousse"]
@app.route("/next/<int:id>")
def next(id):
    i = 0
    list_obj_vente = list()
    list_obj_loc = list()
    data_points_ratio = list()
    data_points_mark_all = list()
    data_points_mark_vente = list()
    data_points_mark_loc = list()
    for a, b in zip(list_country_vente, all_list_avg_vente[id]):
        if(a in countries_to_detail):
            i += 1
            list_obj_vente.append(data(a, b, f'/detail/{i}/{a}/{id}',"#34dbcb"))
        else:
            list_obj_vente.append(data(a, b))

    for a, b in zip(list_country_loc, all_list_avg_loc[id]):
        if(a in countries_to_detail):  
            i += 1
            list_obj_loc.append(data(a, b, f'/detail/{i}/{a}/{id}',"#34dbcb"))
        else:
            list_obj_loc.append(data(a, b))


    for a, b in zip(list_country_ratio, all_list_ratio[id]):
        i += 1
        data_points_ratio.append(data(a, b))
   
    pie=dict_market_all[id] #dict_marketi
    for a,b in pie[0].items():#dict_vente
        data_points_mark_vente.append(data(a,b))
    for a,b in pie[1].items():#dict_loc
        data_points_mark_loc.append(data(a,b))    
    for a,b in pie[2].items():#dict_all
        data_points_mark_all.append(data(a,b))
    return render_template("next1.html",
                           data_points=list_obj_vente,
                           data_points_loc=list_obj_loc,
                           data_points_ratio=data_points_ratio,
                           data_points_mark_vente=data_points_mark_vente,
                           data_points_mark_all=data_points_mark_all,
                           data_points_mark_loc=data_points_mark_loc,
                           current_id=id,
                           countries_to_detail=countries_to_detail,
                           )

# ****************************************************************************************************

def for_detail(dict_vente,dict_loc,country,dict_ann):
    list_obj_vente = list()
    list_obj_loc = list()
    for a,b in dict_vente.items():
        if(a==country):
            for i,j in zip(b[0],b[1]):
                list_obj_vente.append(data(i, j))
    for a, b in dict_loc.items():
        if(a==country):
            for i,j in zip(b[0],b[1]):
                list_obj_loc.append(data(i, j))  
    for a, b in dict_ann.items():
        if(a==country):
            obj_ann=data_detail(b[0],b[1],b[2],b[3],b[4],b[5],b[6])
    return list_obj_vente,list_obj_loc,obj_ann            
    
@app.route('/detail/<int:id>/<string:country>/<int:next_page>')
def detail(id,country,next_page):
    print(f"Country {country}")
    if next_page == 0:
        list_obj_vente, list_obj_loc, obj_ann = for_detail(dict_vente1, dict_loc1, country, dict_detail1)
    else:
        list_obj_vente, list_obj_loc, obj_ann = for_detail(dict_vente2, dict_loc2, country, dict_detail2)  
    print(obj_ann.prix)
    #return (list_obj_vente[0].label) #, list_obj_loc, obj_ann))
    return render_template('detail.html',
        data_points=list_obj_vente,
        data_points_loc=list_obj_loc,
        data_ann=obj_ann,
 )

# ****************************************************************************************************


@app.route('/')
def dash():
    return next(0)

@app.route('/no_deatil')
def no_deatil():
    return render_template("nodetail.html")

@app.route('/click')
def click():
    return render_template("inline_CANVAS.html")

@app.route('/compare')
def compare():
    list_obj_vente=list()
    list_obj_vente1=list()
    list_obj_loc=list()
    list_obj_loc1=list()
    for a, b in zip(list_country_vente, all_list_avg_vente[0]):
        list_obj_vente.append(data(a, b))
    for a, b in zip(list_country_vente, all_list_avg_vente[1]):
        list_obj_vente1.append(data(a, b))
    for a, b in zip(list_country_loc, all_list_avg_loc[0]):
        list_obj_loc.append(data(a, b))   
    for a, b in zip(list_country_loc, all_list_avg_loc[1]):
        list_obj_loc1.append(data(a, b))          
    return render_template('compare.html',
        data_points=list_obj_vente,
        data_points1=list_obj_vente1,
        data_points_loc=list_obj_loc,
        data_points_loc1=list_obj_loc1
 )
