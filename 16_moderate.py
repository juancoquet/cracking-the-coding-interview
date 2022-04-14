# solving 16.2 word frequencies
def word_freq(book):
    book = book.replace(',', '').replace('.', '').lower()
    words = book.split()
    freqs = {}
    for w in words:
        if w in freqs:
            freqs[w] += 1
        else:
            freqs[w] = 1
    return freqs

