import requests
import json,os
import time
import datetime
import argparse

# function to convert normal date_time to epoch time 
def date_to_epoch(normal_time):
    pattern = '%m-%d-%Y'
    epoch_time = int(time.mktime(time.strptime(normal_time, pattern)))
    return epoch_time

# function to convert epoch time to normal date_time
def epoch_to_date(epoch_time):
    normal_time = datetime.datetime.fromtimestamp(epoch_time) # 1973-11-29 22:33:09
    return normal_time

# function to calculate no. of days in between two dates
def time_diff_in_days(dt1,dt2):
    dt1 = epoch_to_date(epoch_fromdate) # 1973-11-29 22:33:09
    dt2 = epoch_to_date(epoch_todate) # 1977-06-07 23:44:50
    timediff = dt2-dt1
    return timediff.days

# function to write json data in file
def write_data_in_file(file_name,data_dict):
    json_files = [f_json for f_json in os.listdir(".") if f_json == file_name]
    if json_files:
        with open(json_files[0],'r') as data_file:
            file_data={}
            file_data = json.load(data_file)
            data_file.close()
        for ID in data_dict:
            file_data[ID] = data_dict[ID]
        with open(file_name,'w') as f:  
            json.dump(file_data,f)
            f.close()
            return True
    else:          
        with open(file_name,'w') as f:
            json.dump(data_dict,f)
            f.close() 
            return True
    return False


parser = argparse.ArgumentParser()

parser.add_argument("search_tag",type= str,help = "Enter the tags separated by comma") 

args = parser.parse_args()
query = args.search_tag
query = query.lower()
tag = query.split(",")
tags = (";").join(tag)
# My Auth Key for STACKOVERFLOW API
key = "ZXgv0x2p)nEbVgWLoOFRdA(("
# prepare params for questions API
payload_questions={}
payload_questions["key"] = key
payload_questions["site"] = "stackoverflow"
payload_questions["order"] = "desc"
payload_questions["sort"] = "activity"
payload_questions["pagesize"] = "100"
# filter fetches some extra details like "badges_count,vote_count" etc.
payload_questions["filter"] = "!b0OfN.wWPfp*gn"
url_questions= "http://api.stackexchange.com/2.2/questions"
# pattern = '%m-%d-%Y'
payload_questions["tagged"] = tags

#if args.from_date:
#	fromdate = args.from_date
#	payload_questions["fromdate"] = date_to_epoch(fromdate)
#if args.to_date:
#	todate = args.to_date
#	payload_questions["todate"] = date_to_epoch(todate)



# API call to get questions for "specific" tags
questions_response = requests.get(url_questions,params=payload_questions)                    

if questions_response.ok:
    questions_json = questions_response.json()
    ques_dict = {}
    user_ids = []
    accepted_answer_ids = []
    for data in questions_json["items"]:
        # creating global questions file
        ques_dict[data["question_id"]] = data
        # storing all user_ids of this tag
        if 'user_id'in data['owner'].keys():
            user_ids.append(str(data['owner']['user_id']))
        # storing accepted answers of this tag
        if 'accepted_answer_id' in data.keys():
            accepted_answer_ids.append(str(data['accepted_answer_id']))

    # writing all questions to unified questions.json 
    questions_file_name = "questions.json"
    write_data_in_file(questions_file_name,ques_dict)
    # writing questions to tag specific files
    for tag_name in tag:
        quest_tag_file_name = "qst_"+tag_name+".json"
        write_data_in_file(quest_tag_file_name,ques_dict)

    # prepare params for users API
    url_users = 'http://api.stackexchange.com/2.2/users/'
    payload_users = {}
    payload_users["pagesize"] = "100"
    payload_users['order']='desc'
    payload_users['sort']='reputation'
    payload_users['site']='stackoverflow'
    payload_users['filter']='!9YdnSBV_a'
    payload_users["key"] = key
    s = ";".join(user_ids)
    url_users = url_users+s
    # API call to get users for above pulled questions
    users_response = requests.get(url_users,params=payload_users)

    if users_response.ok:
        users_json = users_response.json()
        users_dict = {}
        for data in users_json["items"]:
            users_dict[data["user_id"]] = data

        # writing all users to unified users.json 
        users_file_name = "users.json"
        write_data_in_file(users_file_name,users_dict)

        # writing questions to tag specific files
        for tag_name in tag:
            user_tag_file_name = "usr_"+tag_name+".json"
            write_data_in_file(user_tag_file_name,users_dict)

    # prepare params for answers API
    url_answers = 'http://api.stackexchange.com/2.2/answers/'
    payload_answers = {}
    payload_answers["pagesize"] = "100"
    payload_answers['order']='desc'
    payload_answers['sort']='activity'
    payload_answers['site']='stackoverflow'
    payload_answers['filter']='!-*f(6sCNvvau'
    payload_answers["key"] = key
    s = ";".join(accepted_answer_ids)
    url_answers = url_answers+s
     # API call to get accepted ans. for above pulled questions
    answers_response = requests.get(url_answers,params=payload_answers)

    if answers_response.ok:
        answers_json = answers_response.json()
        ans_dict = {}
        for data in answers_json["items"]:
            ans_dict[data["answer_id"]] = data

        # writing all users to unified answers.json 
        answers_file_name = "answers.json"
        write_data_in_file(answers_file_name,ans_dict)
        # writing questions to tag specific files
        for tag_name in tag:
            answers_tag_file_name = "ans_"+tag_name+".json"
            write_data_in_file(answers_tag_file_name,ans_dict)