def AddCourse(course_name, course_tags, course_image, course_desc):
    return {
        "course_name" : course_name,
        "course_tags" : course_tags,
        "course_image" : course_image,
        "course_desc" : course_desc,
    }

def UpdateCourse(course_name, course_tags, course_image, course_desc):
    return {
        "course_name" : course_name,
        "course_tags" : course_tags,
        "course_image" : course_image,
        "course_desc" : course_desc,      
    }