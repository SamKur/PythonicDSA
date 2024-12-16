def count_word_frequency(sentence):
    '''
    Example:
    Input: "hello world hello"
    Output: {'hello': 2, 'world': 1}
    '''
    # Your code goes here
    d = {}
    if str.strip(sentence) == '':
        return d
    for i in sentence.split(' '):
        if i in d.keys():  #or d
            d[i] += 1
        else:
            d[i] = 1
    return d


print(count_word_frequency('hello world hello'))
print(count_word_frequency('')) 