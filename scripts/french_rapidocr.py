from rapidocr_onnxruntime import RapidOCR

# 1. Initialize
engine = RapidOCR()

# 2. Extract
result, _ = engine('french.jpg')

# 3. Print Clean Text
if result:
    for line in result:
        print(line[1])