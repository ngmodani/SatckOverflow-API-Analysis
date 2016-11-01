# SatckOverflow-API-Analysis

*This* *repository* *is* *aimed* *to* *draw* *some results* *from* API::StackOverflow *so* *that* *one* *can* *directly get some insights from* 'StackOverflow'

Please run *data_download.py* before running any other file

ex. : python data_download.py pandas,pythonE

data_download script fetches <b>questions</b> related to the mentioned tag (like pandas,python in above example).
It also pulls the data of the associated <b>user</b> and <b>accepted_answers</b> data.

The StackOverflow API help can be found at http://api.stackexchange.com/2.2/

API documentation can be found at http://api.stackexchange.com/docs/

By default the code is designed to fetch 100 results per call.

All the codes are implemented in Python3.x

<b>Average Response of given pre-defined tags</b>

ex. : python avg_response_time.py windows,ios,php

This script calculates average days elapsed between posting a question and getting an acceptable answer.


<b>Average Statistics of accepted answers for each predefined tag</b>

ex. : python acc_answers_stats.py

For each predefined tag, this script calculates average length of the accepted answers and what percentage of those answers have a code embedded in them.(used BeautifulSoup for parsing answer body)


<b>Average Statistics of each predefined tag</b>

ex. : python tag_stats.py

For each predefined tag, this script calculates average no. of views per question and also avg. no. of answers given per question.


<b>Most Downvoted User for each predefined tag</b>

ex. : python downvoted_users_each_tag.py

This script gives the 5 most downvoted users for each predefined tag.


<b>Top Users & Questions for a user entered tag</b>

ex. : python top_Users_Questions.py

This script gives an output of 5 most reputed users for the required tag along with questions raised by such well reputed users.


<b>Top Locations for all predefined tags</b>

ex. : python top_locations.py

The locations from where users asks the max. no. of questions about a specific tag can be determined with the use of this script..
