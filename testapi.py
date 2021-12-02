import unittest
import requests
import json
class bmi_test(unittest.TestCase):
    def setUp(self):
        self.url = "https://api.jisuapi.com/weight/bmi?"

    def test_succ1(self):
        params = 'appkey=0bf92c507cc4efa1&sex=男&height=175&weight=70'
        r = requests.get(self.url+params)
        data = json.loads(r.text)
        print(data)
        self.assertEqual("正常范围",data["result"]["level"])

    def test_succ2(self):
        params = 'appkey=0bf92c507cc4efa1&sex=male&height=175&weight=70'
        r = requests.get(self.url + params)
        data = json.loads(r.text)
        print(data)
        self.assertEqual("正常范围", data["result"]["level"])

    def test_succ3(self):
        params = 'appkey=0bf92c507cc4efa1&sex=男&height=175&weight=110'
        r = requests.get(self.url + params)
        data = json.loads(r.text)
        print(data)
        self.assertEqual("II度肥胖", data["result"]["level"])

    def test_succ4(self):
        params = 'appkey=0bf92c507cc4efa1&sex=女&height=170&weight=40'
        r = requests.get(self.url + params)
        data = json.loads(r.text)
        print(data)
        self.assertEqual("体重过低", data["result"]["level"])

def suite():
    bmitest = unittest.makeSuite(bmi_test,"test")
    return bmitest

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(suite())