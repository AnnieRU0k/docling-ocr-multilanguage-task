import easyocr

# 1. Initialize (Simplified Chinese and English)
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)

# 2. Extract from your JPG
result = reader.readtext('chinese.jpg', detail=0)

# 3. Print Results
for line in result:
    print(line)