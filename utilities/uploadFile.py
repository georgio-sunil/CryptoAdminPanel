from utilities.aws_sdk_integration import S3_Resource

BASE_URL = "https://wm-intl-dev-bucket.s3.eu-west-1.amazonaws.com/"

def saveFile(file, file_type):
    s3  = S3_Resource()
    s3_bucket_object_name = file_type + '/' + str(file.name)
    # print(s3_bucket_object_name)
    object = s3.Object('wm-intl-dev-bucket', s3_bucket_object_name)
    result = object.put(Body=file, ContentType=file.content_type, ACL='public-read')
    print(result)
    image_url = BASE_URL + s3_bucket_object_name
    return image_url
    