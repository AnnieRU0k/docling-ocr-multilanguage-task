import easyocr

# 1. Initialize for French ('fr')
reader = easyocr.Reader(['fr'], gpu=False)

# 2. Extract Text
result = reader.readtext('french.jpg', detail=0)

# 3. Print Results
for line in result:
    print(line)