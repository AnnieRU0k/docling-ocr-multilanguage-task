from rapidocr_onnxruntime import RapidOCR

# 1. Initialize for Chinese/English mixed
engine = RapidOCR()

# 2. Extract from your JPG
result, _ = engine('chinese.jpg')

# 3. Print Results (Terminal handles UTF-8 automatically)
if result:
    for line in result:
        print(line[1])