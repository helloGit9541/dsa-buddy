from datetime import datetime
from accounts.models import *
from accounts.sheets import *

def reset(user):
    problems = Problem.objects.filter(user=user)
    for problem in problems:
        problem.delete()
    topics = Topic.objects.filter(user=user)
    for topic in topics:
        topic.delete()
    print("reset for user : "+user.username+" complete")

def sync_from_start(dsa_user):
    topics_list = get_topics(dsa_user.sheet_link)
    for topic in topics_list:
        new_topic = Topic()
        new_topic.user = dsa_user.user
        new_topic.name = topic
        new_topic.save()
    print("Topics saved")
    problems_list = get_problems(dsa_user.sheet_link)
    for problem in problems_list:
        new_problem = Problem()
        new_problem.user = dsa_user.user
        new_problem.title = problem.get("title")
        new_problem.difficulty = problem.get('difficulty')
        new_problem.link_to_problem = problem.get("link")
        new_problem.notes = problem.get('notes')
        new_problem.row_number = problem.get('row')
        date_list = str(problem.get('date')).split('/')
        month = int(date_list[0])
        day = int(date_list[1])
        year = int(date_list[2])
        new_date = datetime(year=year,month=month,day=day)
        print(new_date)
        new_problem.last_done_on = new_date
        new_problem.save()
        for topic in problem.get('topics'):
            topic_obj = Topic.objects.get(user=dsa_user.user,name=topic)
            new_problem.topics.add(topic_obj)
        new_problem.save()