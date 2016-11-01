import json,os
import time
from datetime import datetime 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("search_tag",type= str,help = "Enter the tags separated by comma") 
args = parser.parse_args()
search = args.search_tag
query = search.split(",")

def date_to_epoch(normal_time):
    pattern = '%m-%d-%Y'
    epoch_time = int(time.mktime(time.strptime(normal_time, pattern)))
    return epoch_time

# function to convert epoch time to normal date_time
def epoch_to_date(epoch_time):
    normal_time = datetime.fromtimestamp(epoch_time)
    return normal_time

for tag in query:	

	#file_name = "questions.json"
	#tag= 'ios'

	with open("questions.json",'r') as data_file:
	    file_data={}
	    file_data = json.load(data_file)
	    data_file.close()

	tag_dict={}
	accept_ans_ids =[]
	for ID in file_data:
	    if tag in file_data[ID]['tags']:
	        if 'accepted_answer_id' in file_data[ID]:
	            record =[]
	            ques_create_date = file_data[ID]['creation_date']
	            quest_id = file_data[ID]['question_id']
	            accepted_answer_id = file_data[ID]['accepted_answer_id']
	            record.append(quest_id)
	            record.append(accepted_answer_id)
	            accept_ans_ids.append(str(accepted_answer_id))
	            record.append(epoch_to_date(ques_create_date))
	            tag_dict[quest_id] = record
	  

	with open("answers.json",'r') as ans_file:
	    ans_file_data = {}
	    ans_file_data = json.load(ans_file)
	    ans_file.close()

	ans_dict ={}	
	for ids in accept_ans_ids:
	    if ids in ans_file_data:	    	
	        record=[]
	        record.append(ans_file_data[ids]['question_id'])
	        record.append(ans_file_data[ids]['answer_id'])
	        record.append(epoch_to_date(ans_file_data[ids]['creation_date']))
	        ans_dict[ans_file_data[ids]['question_id']]=record	        


	d3 = { k : tag_dict[k] + ans_dict[k] for k in tag_dict if k in ans_dict }
	#print(ans_dict)
	#print()
	days_diff = 0
	for qus in d3:
	    diff_time = d3[qus][5] - d3[qus][2]
	    days_diff = days_diff + diff_time.days
	if len(d3) > 0:
		print("Avg. Days to find an accepted Ans. for tag '"+tag+"' is : ")
		print(days_diff/len(d3))
	else:
		print("No Accepted answers available yet")

