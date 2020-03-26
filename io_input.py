def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)  # Returns True or False


input_text = input('Input text: ')

# Making all cases able to be compared
input_text = input_text.casefold()

# Removing punctuation
punctuation_signs = [',', '.', '!', '?', '/', '\\', ':', ' ']
for x in punctuation_signs:
    input_text = input_text.replace(x, '')


if is_palindrome(input_text):
    print('Yes, it\'s palindrome!')
else:
    print('No, it isn\'t palindrome...')
k
