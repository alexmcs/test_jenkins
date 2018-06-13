import datetime

def test_job():
    with open("../data/test_jenkins.txt", "a") as myfile:
        myfile.write(str(datetime.datetime.time(datetime.datetime.now())) + "\n")

with open("c:/Users/Alexey_Yakunin/A_Yakunin/projects/test_jenkins/data/test_jenkins.txt", "a") as myfile:
    myfile.write(str(datetime.datetime.time(datetime.datetime.now())) + "\n")
