def palindrome(word):
    word = word.replace(' ', '').lower()
    backward_word = word[:: -1]
    if word == backward_word:
        return True
    else:
        return False


def run():
    word = input('Write a word: ')
    is_palindrome = palindrome(word)
    if is_palindrome == True:
        print('It is a palindrome')
    else: 
        print('It is not a palindrome')


if __name__ == '__main__':
    run()