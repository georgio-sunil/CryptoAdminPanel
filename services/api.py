from services.urls import BANNERS_API_ENDPOINT, CATEGORIES_API_ENDPOINT, COIN_API_ENDPOINT, CMC_COIN_LIST, BASE_URL, COURSE_API_ENDPOINT, LANGUAGES_API_ENDPOINT, NEWS_API_ENDPOINT, NEWS_FEED_ENDPOINT, STATIC_CONTENT_API_ENDPOINT
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
    request_url = BASE_URL + COIN_API_ENDPOINT + "/"
    requestBody = coinObject.__dict__
    headers = {
    'accept': 'application/json'
    }
    response = requests.post(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        if AddCMCCoin():
            return True
    else:
        print("Adding to Coin DB failed.")
        print(response.content)
        return False

def AddCMCCoin():
    fetch_request_url = BASE_URL + CMC_COIN_LIST + "/fetch/"
    refresh_request_url = BASE_URL + CMC_COIN_LIST + "/refresh/"
    headers = {
    'accept': 'application/json'
    }
    fetch_response = requests.get(fetch_request_url, headers=headers)
    refresh_response = requests.get(refresh_request_url, headers=headers)

    if fetch_response.status_code == 201 or refresh_response.status_code == 200:
        return True
    else:
        print("Adding to CMC Failed")
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

def coinRanking(coinID, rank):
    request_url = BASE_URL + COIN_API_ENDPOINT + "/" + coinID + "/"
    requestBody = {
        "coin_rank" : rank
    }
    headers = {
    'accept': 'application/json'
    }
    print(request_url)
    response = requests.patch(request_url, json=requestBody, headers=headers)
    print(response)
    if response.status_code == 200:
        return True
    else:
        print(response.content)
        print("Update Failed")

def feedStatus(feedID, status):
    request_url = BASE_URL + NEWS_FEED_ENDPOINT + "/" + feedID + "/"
    if status == True:
        requestBody = {
            "status" : True
        }
    else:
        requestBody = {
            "status" : False
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

def languageStatus(languageID, status):
    request_url = BASE_URL + LANGUAGES_API_ENDPOINT + "/" + languageID + "/"
    if status == True:
        requestBody = {
            "is_active" : True
        }
    else:
        requestBody = {
            "is_active" : False
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

def addNewsFeed(newsFeedObject):
    request_url = BASE_URL + NEWS_FEED_ENDPOINT
    requestBody = newsFeedObject
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

def fetchFeed():
    request_url = BASE_URL + NEWS_FEED_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        feed_list = response.json()
        feed_list = dict((key,value) for key, value in feed_list.items() if key == 'results')
        feed_list = feed_list['results']
    return feed_list

def fetchNews():
    request_url = BASE_URL + NEWS_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        news_list = response.json()
        news_list = dict((key,value) for key, value in news_list.items() if key == 'results')
        news_list = news_list['results']
    return news_list

def fetchLanguages():
    request_url = BASE_URL + LANGUAGES_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        language_list = response.json()
        language_list = dict((key,value) for key, value in language_list.items() if key == 'results')
        language_list = language_list['results']
    return language_list

def fetchSingleLanguage(id):
    request_url = BASE_URL + LANGUAGES_API_ENDPOINT + "/" + id
    response = requests.get(request_url)
    if response.status_code == 200:
        language_list = response.json()
        language_list = dict((key,value) for key, value in language_list.items())
    return language_list

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

def addLanguage(languageObject):
    request_url = BASE_URL + LANGUAGES_API_ENDPOINT + "/"
    requestBody = languageObject
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

def updateLanguage(id, languageObject):
    request_url = BASE_URL + LANGUAGES_API_ENDPOINT + "/" + id + "/"
    requestBody = languageObject
    headers = {
    'accept': 'application/json'
    }
    response = requests.patch(request_url, json=requestBody, headers=headers)
    if response.status_code == 200 or response.status_code == 201:
        print("Language Updated")
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

def fetchCategory(id):
    request_url = BASE_URL + CATEGORIES_API_ENDPOINT + "/" + id + "/"
    response = requests.get(request_url)
    if response.status_code == 200:
        categories_list = response.json()
        return categories_list
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def addCategory(categoryObject):
    request_url = BASE_URL + CATEGORIES_API_ENDPOINT + "/"
    requestBody = categoryObject
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

def updateCategory(id, categoryObject):
    request_url = BASE_URL + CATEGORIES_API_ENDPOINT + "/" + id + "/"
    requestBody = categoryObject
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

def fetchBanners():
    request_url = BASE_URL + BANNERS_API_ENDPOINT
    response = requests.get(request_url)
    if response.status_code == 200:
        banners_list = response.json()
        banners_list = dict((key,value) for key, value in banners_list.items() if key == 'results')
        banners_list = banners_list['results']
    return banners_list

def fetchBanner(id):
    request_url = BASE_URL + BANNERS_API_ENDPOINT + "/" + id + "/"
    response = requests.get(request_url)
    if response.status_code == 200:
        banners_list = response.json()
        return banners_list
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def updateBanner(id, bannerObject):
    request_url = BASE_URL + BANNERS_API_ENDPOINT + "/" + id + "/"
    requestBody = bannerObject
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

def bannerStatus(bannerID, status):
    request_url = BASE_URL + BANNERS_API_ENDPOINT + "/" + bannerID + "/"
    if status == True:
        requestBody = {
            "is_active" : "True"
        }
    else:
        requestBody = {
            "is_active" : "False"
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

def fetchStaticContent():
    request_url = BASE_URL + STATIC_CONTENT_API_ENDPOINT + "/"
    response = requests.get(request_url)
    if response.status_code == 200:
        static_content_list = response.json()
        static_content_list = dict((key,value) for key, value in static_content_list.items() if key == 'results')
        static_content_list = static_content_list['results']
    return static_content_list

def updateTermsandConditions(tandc_object):
    request_url = BASE_URL + STATIC_CONTENT_API_ENDPOINT + "/6297604d52c3477a549c83bb/"
    requestBody = tandc_object
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

def addBanner(bannerObject):
    request_url = BASE_URL + BANNERS_API_ENDPOINT + "/"
    requestBody = bannerObject
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

def addFAQ(faq_object):
    request_url = BASE_URL + STATIC_CONTENT_API_ENDPOINT + "/"
    requestBody = faq_object
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

def fetchFAQ(faqID):
    request_url = BASE_URL + STATIC_CONTENT_API_ENDPOINT + "/" + faqID + "/"
    response = requests.get(request_url)
    if response.status_code == 200:
        categories_list = response.json()
        return categories_list
    else:
        print("Transaction Failed")
        print(response.content)
        return False

def updateFAQ(id, faqObject):
    request_url = BASE_URL + STATIC_CONTENT_API_ENDPOINT + "/" + id + "/"
    requestBody = faqObject
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