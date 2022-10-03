def duplicate_count(text):
    d = list(text).difference(set(text))
    print(d)
    
duplicate_count('abcdeaa')     
