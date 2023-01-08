import requests
from io import BytesIO
from PIL import Image

def url_to_blob(url : str) -> bytes:

    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((100, 100))
    
    blob = BytesIO()
    image.save(blob, "JPEG")
    blob_image = blob.getvalue()

    return blob_image

def blob_to_image(blob : bytes) -> Image:
    
    image = Image.open(BytesIO(blob))

    return image

def str_to_list(string : str, seperator : str = ',') -> list:
    return [item.strip() for item in string.split(seperator) if item.strip() != ""]

def date_to_str(date : str):

    # Handle missing data
    if len(date) < 8:
        return None

    result = ""
    temp = ""
    for char in date:
        if char.isdigit():
            temp += char
            continue
        
        if len(temp) == 1:
            temp = "0"+temp

        result += temp
        temp = ""
    result += temp

    return result
