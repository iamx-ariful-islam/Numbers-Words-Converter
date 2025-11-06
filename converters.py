# convert numbers to words and words to numbers
# author  : Md. Ariful Islam
# version : 1.0.0
# github  : https://github.com/iamx-ariful-islam


# default values
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
        'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
powers = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion',
          'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion', 'duodecillion', 'tredecillion',
          'quattuordecillion', 'quindecillion', 'sexdecillion', 'septendecillion', 'octodecillion',
          'novemdecillion', 'vigintillion']

data = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7,
    'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
    'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20,
    'thirty': 30, 'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
    'hundred': 100, 'thousand': 1000, 'million': 1000000, 'billion': 1000000000,
    'trillion': 1000000000000, 'quadrillion': 1000000000000000, 'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000, 'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000, 'nonillion': 1000000000000000000000000000000,
    'decillion': 1000000000000000000000000000000000, 'undecillion': 1000000000000000000000000000000000000,
    'duodecillion': 1000000000000000000000000000000000000000,
    'tredecillion': 1000000000000000000000000000000000000000000,
    'quattuordecillion': 1000000000000000000000000000000000000000000000,
    'quindecillion': 1000000000000000000000000000000000000000000000000,
    'sexdecillion': 1000000000000000000000000000000000000000000000000000,
    'septendecillion': 1000000000000000000000000000000000000000000000000000000,
    'octodecillion': 1000000000000000000000000000000000000000000000000000000000,
    'novemdecillion': 1000000000000000000000000000000000000000000000000000000000000,
    'vigintillion': 1000000000000000000000000000000000000000000000000000000000000000
}


# convert numbers to words
def find_words(x):
    if x < 0:
        return 'minus ' + find_words(abs(x))
    if x < 20:
        return ones[x]
    if x < 100:
        return tens[x // 10] + ('' if x % 10 == 0 else ' ' + ones[x % 10])
    if x < 1000:
        return ones[x // 100] + ' hundred' + ('' if x % 100 == 0 else ' ' + find_words(x % 100))
    words = []
    for i in range(len(powers)):
        if x == 0:
            break
        triplet = x % 1000
        if triplet != 0:
            words.append(find_words(triplet) + ' ' + powers[i])
        x //= 1000
    return ' '.join(reversed(words))


def NumToWords(x, prefix='', suffix=''):
    d = []
    if type(x) == int:
        pass
    elif type(x) == float:
        x, y = str(round(x, 2)).split('.')
        d = [int(i) for i in y]
    else:
        return

    in_words = find_words(int(x))
    if sum(d) > 0:
        if len(d) == 1:
            d.append(0)
        in_words += ' point ' + ones[d[0]] + ' ' + ones[d[1]]
    else:
        try:
            d[0] == 0
            in_words += ' point zero'
        except:
            pass
    return (prefix + ' ' + in_words + ' ' + suffix).strip()


# convert words to numbers
def find_nums(words):
    total = 0
    value = 0
    for word in words:
        if word.isdigit():
            value += int(word)
        elif word in data:
            if word == "hundred":
                value *= data[word]
            elif word in ['thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion',
                          'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion', 'undecillion',
                          'duodecillion', 'tredecillion', 'quattuordecillion', 'quindecillion',
                          'sexdecillion', 'septendecillion', 'octodecillion', 'novemdecillion', 'vigintillion']:
                total += value * data[word]
                value = 0
            else:
                value += data[word]
    return total + value


def WordsToNum(word):
    words = word.lower().split()
    wL = len(words)
    pindex = wL

    try:
        pindex = words.index('point')
    except:
        pass

    total = find_nums(words[:pindex])

    if wL > pindex:
        x = words[pindex + 1:]
        x.extend(['zero', 'zero']) if len(x) < 1 else x.append('zero')
        total += (data[x[0]] * 10 + data[x[1]]) / 100
    return total


# root
if __name__ == '__main__':
    print("Example Demo:")
    num_value = 1234567.26
    print("Number to Words:", NumToWords(num_value))
    word_value = "one million two hundred thirty four thousand five hundred sixty seven point two six"
    print("Words to Number:", WordsToNum(word_value))