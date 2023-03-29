import boto3, cv2, json
import numpy as np
from django.http import JsonResponse
from PIL import Image
from blur_image.models import Image as My_Image

aws_access_key_id = 'ASIAZAVUAAH6FT3NUEKQ'
aws_secret_access_key = 'N2j2c+dqw5GsEZ8h1P01SKrV5A2zyCnyoWmvRGqR'
aws_session_token = 'FwoGZXIvYXdzEIv//////////wEaDGxjBXS4iUyjeWInUCK9AUajabyaj3PAJC04GPdNVhR7pAPQ5hAqUzZMni4S++pnPlphr6WHRySpwaTAWNVONOlH1mS3XeW0r8p88FCl9u4h3eHnDjKAIPNE4c310PxxpIr6iYvWcvt3aT0oswyay38Zk87D8KNiC70QugMtRvIDD2FNLxPuya1S6J3wFyq6JlABk+o+pt1QbehPICaLUfqnTWXxBo3fzd5OKtxC8nXhhb6ZrAjr8fqUERNMy2bTAjfN/rhvfZcTiNlptSidrY6hBjItyMKB/f4nHpCJ0A4TCzIaTY/EDLcK/xwI+graHnBvKGx9e+2bTQTP9e/brwXV'
bucket = 'pia-sergio-lapaz-aws-bucket'
region = 'us-east-1'

session = boto3.Session(
    aws_access_key_id,
    aws_secret_access_key,
    aws_session_token,
    region
)

s3 = session.resource('s3')
rekognition = session.client('rekognition')

def aws(file, name_file):
    try:
        data = open(file, 'rb')
        key = name_file
        s3.Bucket(bucket).put_object(Key=key, Body=data)
        
        image = {'S3Object':{'Bucket':bucket,'Name':key}}
        attributes = ['ALL']
        
        response = rekognition.detect_faces(Image = image, Attributes = attributes)
        
        filtered_faces = filter(lambda face: face["AgeRange"]["Low"] < 18, response['FaceDetails'])
        filtered_faces = list(map(lambda face: face['BoundingBox'], filtered_faces))
        return JsonResponse(filtered_faces, safe = False)
        
    except:
        print('error')
        
def blur(img, coords=[]):
    img = cv2.imread(img)
    for coord in coords:
        x = int(coord['x'])
        y = int(coord['y'])
        w = int(coord['w'])
        h = int(coord['h'])
        face_roi = img[y:y + h, x:x + w]
        blurred = cv2.medianBlur(face_roi, 99)
        img[y:y + h, x:x + w] = blurred
        
    return Image.fromarray(img)