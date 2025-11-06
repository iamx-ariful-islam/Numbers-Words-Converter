from converters import NumToWords, WordsToNum


num_value = 1234567.26
print("Number to Words:", NumToWords(num_value))
# Number to Words: one million two hundred thirty four thousand five hundred sixty seven  point two six

word_value = "one million two hundred thirty four thousand five hundred sixty seven point two six"
print("Words to Number:", WordsToNum(word_value))
# Words to Number: 1234567.26



# Find the path
import converters

print(converters.__file__)