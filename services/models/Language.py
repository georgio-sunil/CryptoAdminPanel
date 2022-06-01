def AddLanguage(locale, name, image, file):
    return {
    "locale": locale,
    "name": name,
    "image": image,
    "string_file_url" : file,
    "is_active" : False
    }

def updateLanguage(locale, name, image, file):
    return {
    "locale": locale,
    "name": name,
    "image": image,
    "string_file_url" : file,
    }