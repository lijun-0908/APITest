from locust import HttpUser,TaskSet,task
import random
class getBMI(TaskSet):

    def on_start(self):
        self.url = '/weight/bmi?'

    @task(7)
    def getBMIFat(self):
        self.client.get(self.url,params={'sex':'女',
            'height':'170','weight':'90','appkey':'0bf92c507cc4efa1'})
        print('胖子')

    @task(2)
    def getBMINor(self):
        self.client.get(self.url,params={'sex':'男',
            'height':'175','weight':'75','appkey':'0bf92c507cc4efa1'})
        print('正常')

    @task(1)
    def getBMIThin(self):
        sex = ['男', '女', 'male', 'female']
        heights = ['165', '163', '162', '167', '163', '170', '177', '165', '160', '163', '160', '166', '163', '158']
        i = random.randint(0,len(heights) - 1)
        sg = heights[i]
        i = random.randint(0,len(sex) - 1)
        xb = sex[i]
        print(sg)

        self.client.get(self.url,params={'sex':xb,'height':sg,'weight':'75','appkey':'0bf92c507cc4efa1'})

class WebsiteUser(HttpUser):
    # task_set = getBMI
    tasks = [getBMI]
    min_wait = 1000
    max_wait = 3000