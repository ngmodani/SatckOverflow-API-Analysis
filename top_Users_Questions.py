import json,os
import time
import datetime
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("search_tag",type= str,help = "Enter the tags separated by comma") 
args = parser.parse_args()
search = args.search_tag
tags = search.split(",")

for tag in tags:	

	file_name = "qst_"+tag+".json"
	json_files = [f_json for f_json in os.listdir(".") if f_json == file_name]
	if json_files:
	    with open(json_files[0],'r') as data_file:
	        file_data={}
	        file_data = json.load(data_file)
	        data_file.close()
	    user_dict = {}
	    best_user = {}
	    for ID in file_data:
	        user_dict[file_data[ID]['owner']['user_id']] = file_data[ID]['owner']
	        best_user[file_data[ID]['owner']['user_id']] = file_data[ID]['owner']['reputation']
	    count = 0
	    top_5 = []
	    for user in sorted(best_user,key=best_user.get,reverse = True):
	        if count < 5:
	            top_5.append(user)
	            count = count +1
	    print("\nTop 5 users in the field of '"+tag+"' are : ")
	    for ids in top_5:
	        print(str(user_dict[ids]['user_id'])+"\t"+user_dict[ids]['display_name']+"\t"+
	              user_dict[ids]['link']+"\t"+str(user_dict[ids]['reputation']))
	    print("\nTop 5 questions in the field of '"+tag+"' are : ")
	    for ids in top_5:
	        for ID in file_data:
	            if file_data[ID]['owner']['user_id'] == ids:
	                print(file_data[ID]['owner']['display_name']+"\t"+file_data[ID]['title'])