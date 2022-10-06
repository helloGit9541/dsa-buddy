import gspread

# sheet_link = 'https://docs.google.com/spreadsheets/d/1u4rr3CDg0AJXtrVST_Awrjvff0lYfnxhuEmyKxfVWN4/edit?usp=sharing'

def get_topics(sheet_link,start_row = 2):
    topics_list = []
    service_account = gspread.service_account(filename='/home/tooshort9541/Desktop/Projects/dsa-buddy/accounts/service_account.json')
    sh = service_account.open_by_url(sheet_link)
    problem_records = sh.worksheet('Sheet1').col_values(2)
    current_row = 1
    for record in problem_records:
        if current_row >= start_row:
            topics = record.split()
            for topic in topics:
                topic = str(topic).lower()
                topics_list.append(topic)
        current_row+=1
    topics_list = list(set(topics_list))
    return topics_list

def get_problems(sheet_link,start_row=2):
    problems_list = []
    service_account = gspread.service_account(filename='/home/tooshort9541/Desktop/Projects/dsa-buddy/accounts/service_account.json')
    sh = service_account.open_by_url(sheet_link)
    problem_records = sh.worksheet('Sheet1').get_all_records()
    current_row = 1
    for record in problem_records:
        if current_row >= start_row:
            new_problem = {}
            new_problem['title']=record['question']
            new_problem['topics']=str(record['topics']).split()
            new_problem['difficulty']=record['level']
            new_problem['link']=record['link']
            new_problem['date']=record['date']
            new_problem['notes']=record['notes']
            new_problem['row'] = current_row
            # print(new_problem)
            problems_list.append(new_problem)
        current_row+=1
    # topics_list = list(set(topics_list))
    return problems_list

# print(get_topics(sheet_link))

# print(get_problems(sheet_link))
# for problem in get_problems(sheet_link):
#     print(problem.get('title'))