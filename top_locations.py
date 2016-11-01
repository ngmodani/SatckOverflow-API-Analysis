import json,os
import json,os

json_files = [f_json for f_json in os.listdir(".") if f_json.startswith("usr_")]
for js in json_files:
    with open(js,'r') as data_file:
        file_data={}
        file_data = json.load(data_file)
        data_file.close()
    count = 0 
    loc_dict={}
    for ID in file_data:
        if 'location' in file_data[ID]:
            if file_data[ID]['location'] in loc_dict:
                loc_dict[file_data[ID]['location']] = loc_dict[file_data[ID]['location']] + 1
            else:
                loc_dict[file_data[ID]['location']] = 1
    print("\nTop 3 locations posting questions about '"+js[4:-5]+"' : ")
    count = 0
    for place in sorted(loc_dict,key=loc_dict.get,reverse =True):
        if count<3:
            print(str(loc_dict[place])+"\t"+place)
            count = count + 1