from services.urls import CATEGORIES_API_ENDPOINT, COIN_API_ENDPOINT, CMC_COIN_LIST, BASE_URL, COURSE_API_ENDPOINT, NEWS_API_ENDPOINT, NEWS_FEED_ENDPOINT
import requests


def fetchCMCCoins():
    request_url = CMC_COIN_LIST
    headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '5816a2ed-0e54-4cc1-85ef-e4177f99362d'
    }
    response = requests.get(request_url, headers=headers)
    if response.status_code == 200:
        coin_details = response.json()
        coin_details = dict((key,value) for key, value in coin_details.items() if key == 'data')
        coin_details = coin_details['data']
    return coin_details

def fetchCoins():
    request_url = BASE_URL + COIN_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        coin_details = response.json()
        coin_details = dict((key,value) for key, value in coin_details.items() if key == 'results')
        coin_details = coin_details['results']
    return coin_details

def addCoins(coinObject):
    request_url = BASE_URL + COIN_API_ENDPOINT
    requestBody = coinObject.__dict__
    headers = {
    'accept': 'application/json'
    }
    response = requests.post(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        return True
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def coinStatus(coinID, status):
    request_url = BASE_URL + COIN_API_ENDPOINT + "/" + coinID + "/"
    if status == True:
        requestBody = {
            "active" : True
        }
    else:
        requestBody = {
            "active" : False
        }
    headers = {
    'accept': 'application/json'
    }
    print(request_url)
    response = requests.patch(request_url, json=requestBody, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print(response.content)
        print("Update Failed")

def feedStatus(feedID, status):
    request_url = BASE_URL + NEWS_FEED_ENDPOINT + "/" + feedID + "/"
    if status == True:
        requestBody = {
            "active" : True
        }
    else:
        requestBody = {
            "active" : False
        }
    headers = {
    'accept': 'application/json'
    }
    print(request_url)
    response = requests.patch(request_url, json=requestBody, headers=headers)
    if response.status_code == 200:
        return True
    else:
        print(response.content)
        print("Update Failed")

def fetchNews():
    request_url = BASE_URL + NEWS_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        news_list = response.json()
        news_list = dict((key,value) for key, value in news_list.items() if key == 'results')
        news_list = news_list['results']
    return news_list

def fetchSingleNews(id):
    request_url = BASE_URL + NEWS_API_ENDPOINT + "/" + id
    response = requests.get(request_url)
    if response.status_code == 200:
        news_list = response.json()
        news_list = dict((key,value) for key, value in news_list.items())
    return news_list

def addNews(newsObject):
    request_url = BASE_URL + NEWS_API_ENDPOINT + "/"
    requestBody = newsObject
    headers = {
    'accept': 'application/json'
    }
    response = requests.post(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        return True
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def updateNews(id, newsObject):
    request_url = BASE_URL + NEWS_API_ENDPOINT + "/" + id + "/"
    requestBody = newsObject
    headers = {
    'accept': 'application/json'
    }
    response = requests.patch(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        return True
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def fetchCourses():
    request_url = BASE_URL + COURSE_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        course_list = response.json()
        course_list = dict((key,value) for key, value in course_list.items() if key == 'results')
        course_list = course_list['results']
        return course_list
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def fetchCourse(id):
    request_url = BASE_URL + COURSE_API_ENDPOINT + "/" + id + "/"
    response = requests.get(request_url)
    if response.status_code == 200:
        course_list = response.json()
        course_list = dict((key,value) for key, value in course_list.items())
        return course_list
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def addCourse(courseObject):
    request_url = BASE_URL + COURSE_API_ENDPOINT + "/"
    requestBody = courseObject
    headers = {
    'accept': 'application/json'
    }
    response = requests.post(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        return True
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def updateCourse(id, courseObject):
    request_url = BASE_URL + COURSE_API_ENDPOINT + "/" + id + "/"
    requestBody = courseObject
    print(request_url)
    headers = {
    'accept': 'application/json'
    }
    print(courseObject)
    response = requests.patch(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        print("Course Updated")
        return True
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def fetchCategories():
    request_url = BASE_URL + CATEGORIES_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        categories_list = response.json()
        categories_list = dict((key,value) for key, value in categories_list.items() if key == 'results')
        categories_list = categories_list['results']
        return categories_list
    else:
        print("Transaction Failed")
        print(response.content)
        return False