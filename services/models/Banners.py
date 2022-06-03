def AddBanners(banner_image, banner_title, banner_text, button_text, button_link, banner_color):
    return {
        "Image": banner_image,
        "Banner_title": banner_title,
        "Banner_text": banner_text,
        "Button_text": button_text,
        "Button_link": button_link,
        "Color_code": banner_color,
        "is_active": "False"
    }

def UpdateBanner(banner_image, banner_title, banner_text, button_text, button_link, banner_color):
    return {
        "Image": banner_image,
        "Banner_title": banner_title,
        "Banner_text": banner_text,
        "Button_text": button_text,
        "Button_link": button_link,
        "Color_code": banner_color,
    }