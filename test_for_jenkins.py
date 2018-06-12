import datetime

def test_job():
    with open("../data/test_jenkins.txt", "a") as myfile:
        myfile.write(str(datetime.datetime.time(datetime.datetime.now())) + "\n")

with open("../data/test_jenkins.txt", "a") as myfile:
    myfile.write(str(datetime.datetime.time(datetime.datetime.now())) + "\n")