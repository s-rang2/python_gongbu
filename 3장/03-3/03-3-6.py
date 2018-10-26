vowels = 'aeiou'
sentence = 'Life is too short, you need python'
after=''.join([a for a in sentence if a not in vowels])
print(after)
