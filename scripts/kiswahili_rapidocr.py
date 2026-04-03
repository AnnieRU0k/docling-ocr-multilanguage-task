from rapidocr_onnxruntime import RapidOCR

# 1. Initialize (The engine is natively multilingual)
engine = RapidOCR()

# 2. Extract from your JPG
result, _ = engine('kiswahili.jpg')

# 3. Print Results
if result:
    for line in result:
        print(line[1])