### **WHAT IS DOCLING?**
Docling is an open-source Python and TypeScript library that simplifies document processing, parsing diverse formats and providing seamless integrations with the gen AI ecosystem.

### **DOCLING OCR: MULTILINGUAL ENGINE RESEARCH AND OPTIMIZATION**
This repository documents the journey through a document processing pipeline, transitioning from a restricted Fedora Linux environment to a high-fidelity Windows-based production workflow. My source is a single scanned document containing 3 different languages i.e Dutch, French and English. The reason was to show how a multilingual document would be interpreted using different engines and OCRs.

---

### **FEDORA DOCLING INSTALLATION AND GRANITE IBM OCR SIZE CONSTRAINTS**
I started the project on Fedora with the goal of using IBM Granite via Docling. I started by installing docling and later installing granite model as an add on.

![Docling Fedora Setup](./images/1.%20docling%20version.JPG)

**HARDWARE BARRIERS:** Despite 46GB of disk space, a 1.5GB user quota triggered a OS Error as Disk quota exceeded during VLM downloads.

**WORK AROUND:** I bypassed full model specs by downloading only essential resources mentioned in error messages, using community repositories and Gemini AI to verify code viability under these strict constraints.

---

### **DOCLING WINDOWS OS INSTALL**
To resolve storage limitations, I migrated to Windows 10, establishing a baseline using Docling’s built-in RapidOCR and there after installing EasyOCR. 

![Language Tagging Conflict](./images/3.%20nld%20not%20supported.JPG)

**OUTPUT:** Despite the stable environment, the Priority Bias persisted. Technical English terms are still being interpreted through a Dutch phonetic lens. This confirmed that the issue was not the OS, but the Linguistic Mesh.

---

### **TESSERACT ON WINDOWS OS**
Finally I installed tesseract OCR on window. The difference with the other OCRs was that during the install process there were language components options that you could select for multiple languages.

![Tesseract Multi-Language Selection](./images/2.%20selecting%20language%20with%20tesseract.JPG)

**ENVIRONMENT BARRIERS:** I need to pivot to RapidOCR as the primary engine, supported by a system-level Tesseract backend. Python 3.13 proved to be too modern for the older version Tesseract bindings, causing the initialization to hang and crash.

**RAPIDOCR ONNX SOLUTION:** RapidOCR ONNX is built on a more modern, platform-independent framework. It meshed perfectly with Python 3.13 while using tesseract backend loaded languages.

![RapidOCR ONNX Runtime](./images/4.%20rapiocr%20version.JPG)

---

### **FINAL PROJECT OUTCOME**
The final files upheld each language's integrity without bias. Each language had proper spelling and accent retention.

![Final Successful Output](./images/5.%20its%20working.JPG)

* **output/**: The final high-fidelity .md files produced by the RapidOCR/Tesseract pivot.
* **scripts/**: Reconstructs the logic for each stage of this journey.
