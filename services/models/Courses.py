def AddCourse(course_name, course_tags, course_image, course_url, topic_count, video_count, course_bg, course_desc):
    return {
        "course_name" : course_name,
        "course_tags" : course_tags,
        "course_image" : course_image,
        "course_url" : course_url,
        "course_desc" : course_desc,
        "topic_count": topic_count,
        "video_count": video_count,
        "course_bg": course_bg,
    }

def UpdateCourse(course_name, course_tags, course_image, course_url, topic_count, video_count, course_color, course_desc):
    return {
        "course_name" : course_name,
        "course_tags" : course_tags,
        "course_image" : course_image,
        "course_url" : course_url,
        "course_desc" : course_desc,
        "topic_count": topic_count,
        "video_count": video_count,
        "course_bg": course_color      
    }