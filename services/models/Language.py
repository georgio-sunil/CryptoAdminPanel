def AddLanguage(locale, name, image):
    return {
    "locale": locale,
    "name": name,
    "image": image,
    "is_active" : False
    }

def updateLanguage(locale, name, image):
    return {
    "locale": locale,
    "name": name,
    "image": image
    }