import easyocr

reader = easyocr.Reader(['et'], gpu=False)

result = reader.readtext('estonian.jpg', detail=0)

for line in result:
    print(line)
    