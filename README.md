## **WHAT IS DOCLING?**

Docling is an open-source Python and TypeScript library that simplifies document processing, parsing diverse formats and providing seamless integrations with the gen AI ecosystem.


## **DOCLING OCR: MULTILINGUAL ENGINE RESEARCH AND OPTIMIZATION**

This repository documents the journey through a document processing pipeline, transitioning from a restricted Fedora Linux environment to a high-fidelity Windows-based production workflow. My source is a single scanned document containing 3 different languages i.e Dutch, French and English. The reason was to show how a multilingual document would be inteprated using different engines and OCRs


## **FEDORA DOCLING INSTALLATION AND GRANITE IBM OCR SIZE CONSTRAINTS**

I started the project on Fedora with the goal of using IBM Granite via Docling. I started by installing docling and later installing granite model as an add on.

![Docling Version](./images/1.docling%20version.JPG)


![Tesseract Version](./images/7.%20Tesseract%20version.JPG)


**HARDWARE BARRIERS**: Despite 46GB of disk space, a 1.5GB user quota triggered a OS Error as Disk quota exceeded during VLM downloads.

![Disk Quota Error](./images/size%20issues%20on%20fedora.JPG)

![Space Verification](./images/checking%20space%20again.JPG)

**WORK AROUND**: I bypassed full model specs by downloading only essential resources mentioned in error messages, using community repositories and Gemini AI to verify code viability under these strict constraints.
OUTPUT: Even after bypassing the hardware wall, I observed Model Bias. By injecting a Dutch priority code when loading pdf (nl/nld), English words were misspelled into Dutch phonetics (e.g., "Process" to "Proces") and French accents were dropped. This showed that Code Injection methods often force the AI to erase minority languages on a page to match the prioritized dialect.




## **DOCLING WINDOWS OS INSTALL**

To resolve storage limitations, I migrated to Windows 10, establishing a baseline using Docling’s built-in RapidOCR and there after installing EasyOCR. The code was straight forward and easy to load the pdf However I discovered that despite being able to load pdf through use of "nld" language code in rapid ocr baseline I needed to edit this to “nl” for easyocr. This shows a difference in language tagging between engines for the same language.


![NLD Not Supported](./images/3.%20nld%20not%20supported.JPG)


**OUTPUT**: Despite the stable environment, the Priority Bias persisted. Technical English terms are still being interpreted through a Dutch phonetic lens. This confirmed that the issue was not the OS, but the Linguistic Mesh. The way the OCR engine prioritizes a single language code. This is also evident with multi language codes. The more codes you inject, the lazier the model gets. It starts guessing and because the models are often smaller (to fit memory), they default to the priority or heaviest language in the list.


## **TESSERACT ON WINDOWS OS**

Finally I installed tesseract OCR on window. The difference with the other OCRs was that during the install process there were language components options that you could select for multiple languages.

![Tesseract Languages](./images/2.%20selecting%20language%20with%20tesseract.JPG)


**ENVIRONMENT BARRIERS**: However I need to pivot to RapidOCR (tesseract alternatives) as the primary engine, supported by a system-level Tesseract backend. The pivot away from Tesseract was a matter of environment compatibility. While the system-level Dutch language packs for dutch French and english were ready and chosen upon install, Python 3.13 proved to be too modern for the older version Tesseract bindings. Tesseract’s Python wrappers often rely on legacy C-extensions that have not yet been fully optimized for the internal changes in Python 3.13. This caused the initialization to hang and crash, preventing any document from loading despite the correct configurations being in place.


**RAPIDOCR ONNX SOLUTION**: RapidOCR ONNX is built on a more modern, platform-independent framework. it meshed perfectly with Python 3.13 while using tesseract backend loaded languages. RapidOCR doesn't rely on the same legacy bridges as Tesseract. By using the ONNX runtime, it provided a clean, high-speed execution path that handled the Python 3.13 environment easily.


**THE ADVANTAGE**: This allowed us to keep the advanced features of the newest Python version while getting the best of both worlds. OCR—speed from ONNX and accuracy form the Dutch, English, and French text packages inbuild in the tesseract backend.


**OUTPUT**: This forced pivot proved that RapidOCR ONNX is the more resilient choice for modern development environments. It bypassed the loading errors that crashed Tesseract and delivered the final, clean Markdown files. The final files upheld each language's integrity without bias. Each language had proper spelling and accent retention RapidOCR’s ONNX-based architecture handled the layout better. While the Tesseract feature language pack provided the necessary linguistic grounding without the bias seen in previous attempts.


## **FINAL PROJECT OUTCOME**

• output/: The final high-fidelity .md files produced by the RapidOCR/Tesseract pivot

• scripts/: Reconstructs the logic for each stage of this journey.

A key discovery in this project was the difference between Code Injection (EasyOCR/RapidOCR) and System-Level Integration (Tesseract).

The Bias in Code Injection: In EasyOCR and RapidOCR, we had to specify the language code (nl or nld) within the Python script. This created a priority bias where the engine attempted to map English and French characters to Dutch phonetics.

**Tesseract's Advantage**: Unlike the other engines, Tesseract allowed for the selection of multiple language packs during the installation phase. By installing "nld", "fra", and "eng" simultaneously at the system level, the engine gained a native ability to retain the integrity of all three languages without needing a code to be injected during the markdown process. This effectively eliminated the "Linguistic Erasure" observed in earlier stages. This upheld each language's integrity during markdown.
