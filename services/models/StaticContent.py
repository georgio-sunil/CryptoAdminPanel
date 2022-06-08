
def UpdateTermsandCondition(termandcond_url):
    return {
        "content_text" : termandcond_url
    }

def FAQ(content_title, content_text):
    return {
        "content_type" : "Questions",
        "content_title" : content_title,
        "content_text" : content_text
    }