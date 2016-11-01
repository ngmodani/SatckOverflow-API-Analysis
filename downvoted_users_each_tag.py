import json,os

json_files = [f_json for f_json in os.listdir(".") if f_json.startswith("qst_")]
for js in json_files:
    with open(js,'r') as data_file:
        file_data={}
        file_data = json.load(data_file)
        data_file.close()
    user_dict = {}
    downvoted_user = {}
    for ID in file_data:
        if 'user_id' in file_data[ID]['owner'].keys():
            user_dict[file_data[ID]['owner']['user_id']] = file_data[ID]['owner']
            downvoted_user[file_data[ID]['owner']['user_id']] = (file_data[ID]['down_vote_count'] - file_data[ID]['up_vote_count'])
    count = 0
    worst_5 = []
    for user in sorted(downvoted_user,key=downvoted_user.get,reverse = True):
        if count < 5:
            worst_5.append(user)
            count = count +1
    print("\nWorst 5 users in the field of '"+js[4:-5]+"' are : ")
    for ids in worst_5:
        print(str(user_dict[ids]['user_id'])+"\t"+user_dict[ids]['display_name']+"\t"+
              user_dict[ids]['link']+"\t"+str(user_dict[ids]['reputation']))