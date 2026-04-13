from rapidocr_onnxruntime import RapidOCR

engine = RapidOCR()

result, elapsed = engine('russian.jpg')

if result:
    for line in result:
        print(line[1])
else:
    print("No text detected.")