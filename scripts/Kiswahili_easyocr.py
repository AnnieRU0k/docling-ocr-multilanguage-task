import easyocr

# 1. Initialize for Swahili only ('sw')
reader = easyocr.Reader(['sw'], gpu=False)

# 2. Extract Text from your screenshot
result = reader.readtext('kiswahili.jpg', detail=0)

# 3. Print Results
for line in result:
    print(line)