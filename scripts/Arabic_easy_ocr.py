import easyocr

reader = easyocr.Reader(['ar', 'en'], gpu=False)

result = reader.readtext('Arabic.jpg', detail=0)

for line in result:
    print(line)
    