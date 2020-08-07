import os
import json
import requests
import time

# Delay to launch test (Waiting for containers)
print("WWaiting " + os.environ['TESTDELAYSECONDS'] + " seconds...")
time.sleep(float(os.environ['TESTDELAYSECONDS']))

# Global parameters
headers = {"Content-Type": "application/json"}
url = 'http://0.0.0.0:' + os.environ['PORT'] + '/api/v1/'
data = {"name":"Matias", "last_name":"Medrano", 
        "age":26, "picture_url":"htttp://example.com/matias"}


class TestAPI(object):
    def test_create_user(self):
        response = requests.post(url+'people',
                                headers=headers,
                                data=json.dumps(data))
        #jsonReponse = response.json()
        assert response.status_code == 201

    def test_get_users(self):
        response = requests.get(url+'people',
                                headers=headers)
        jsonReponse = response.json()
        assert response.status_code == 200
        assert "Matias" in jsonReponse[0]['name']
        assert "Medrano" in jsonReponse[0]['last_name']
        assert "26" in jsonReponse[0]['age']
        assert "htttp://example.com/matias" in jsonReponse[0]['picture_url']

    def test_get_users_by_id(self):
        response = requests.get(url+'people/1',
                                headers=headers)
        jsonReponse = response.json()
        assert response.status_code == 200
        assert "Matias" in jsonReponse['name']
        assert "Medrano" in jsonReponse['last_name']
        assert "26" in jsonReponse['age']
        assert "htttp://example.com/matias" in jsonReponse['picture_url']

    def test_update_users_by_id(self):
        response = requests.put(url+'people/1',
                                headers=headers,
                                data=json.dumps({"name":"Ignacio", 
                                                 "last_name":"Gamonal",
                                                 "age":26, 
                                                 "picture_url":"htttp://example.com/diego"}))
        assert response.status_code == 200

    def test_delete_users_by_id(self):
        response = requests.delete(url+'people/1')
        assert response.status_code == 200
