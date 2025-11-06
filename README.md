# 🔢 Numbers ↔ Words Converter

### A simple, clean and reliable efficient python utility or tool to convert **numbers → words** and **words → numbers**.


## 📘 Overview

This repository provides a compact, well-documented Python module that:

- Converts integer and floating-point numbers into English words (supports very large magnitudes).  
- Parses English words describing numbers (including a two-digit fractional part after the word `point`) back into numeric values.

**Repository name:** `numbers-words-converter`  
**Primary module file:** `converters.py`  
**Package / distribution name:** `numbers-words-converter`


## 📦 Installation

```bash
git clone https://github.com/iamx-ariful-islam/numbers-words-converter.git
cd numbers-words-converter
pip install .
# or
python setup.py install
```


## 📂 Folder / File Structure

```bash
numbers-words-converter/
│
├── converters.py
├── README.md
├── setup.py
└── test.py
```


## 🚀 Usage

```python
from converters import NumToWords, WordsToNum

print(NumToWords(1234567.26))
# output: one million two hundred thirty four thousand five hundred sixty seven point two six

print(WordsToNum("one million two hundred thirty four thousand five hundred sixty seven point two six"))
# output: 1234567.26
```


## 💡 Notes & Limitations

- Fractional handling expects exactly two digits after the word point. If fewer than two words follow point, zeros are appended. Example: "point five" → 0.50.
- Input words should be lowercase or will be lowercased internally. Avoid punctuation except digits if mixing numeric tokens.
- Supports very large magnitudes up to "vigintillion" (as defined in the module).
- This is a pure parsing/formatting utility — it does not provide authentication, I/O formatting beyond examples, or localization (English only).
- For production use, validate input strings and consider wrapping calls with try/except for error handling.


## ✅ Quick Summary

| Situation | Markdown Syntax | Example |
|------------|-----------------|----------|
| Normal text | Just type it | `1234.56` |
| Inside code | Backticks | `` `NumToWords(12.34)` `` |
| Inside code block | Triple backticks | ```python ... ``` |
| Start of line | Escape dot | `1\.23` |
---
Would you like me to modify your existing `README.md` file so that all decimal numbers (like `1234567.26`, `3.5` etc.) are properly formatted and displayed cleanly?


## Contributing

Contributions, suggestions, and feedback are always welcome! ❤️
To contribute:

1. Fork the repository
1. Create a new branch (`feature/new-feature`)
1. Commit your changes
1. Push and submit a Pull Request

💬 You can also open an issue if you’d like to discuss a feature or report a bug.


## For more or connect with me

<p align='center'>
  <a href="https://github.com/iamx-ariful-islam"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://twitter.com/mx_ariful_islam"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://bd.linkedin.com/in/iamx-ariful-islam"><img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.facebook.com/jonakisoft.net/"><img src="https://img.shields.io/badge/Facebook-%231877F2.svg?style=for-the-badge&logo=Facebook&logoColor=white" /></a>&nbsp;&nbsp;&nbsp;&nbsp;
</p>


## License

The [MIT](https://choosealicense.com/licenses/mit/) License (MIT)