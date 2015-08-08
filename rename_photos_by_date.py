from PIL import Image
from PIL.ExifTags import TAGS
import os


#
# Get the creation date and time of the specified image 
#
def get_creation_datetime(img):

    exif_data = img._getexif()

    # TODO - Add error handling
    if exif_data:
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag)
            if decoded == "DateTimeOriginal":
                return value
    else:
        print("No EXIF data found.")

    
#
# Format date and time as a valid image name,
# e.g. "2013:01:01 00:31:03" -> "20130101_003103"
# An optional string may be appended to the datetime sting
#
def format_date(date, str=''):
    if str:
        date += "_" + str

    date = date.replace(":", "").replace(" ", "_")

    return date


#
# Rename the specified image using the specified datetime string
#
def rename_img_by_date(img_path, opt_str):
    img = Image.open(img_path)
    datetime = get_creation_datetime(img)
    img.close()
    extension = os.path.splitext(img_path)[1]
    os.rename(img_path, "test/" + format_date(datetime, opt_str) + extension)


#
# Rename images in the specified directory using the specified string
#
def batch_img_rename_by_date(directory_path, opt_str):
    for f in os.listdir(directory_path):
        if not f.startswith('.'):
            rename_img_by_date(directory_path + "/" + f, opt_str)