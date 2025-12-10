def count(s):
    result = ''
    for ch in s:
        c = 0
        for i in s:
            if i == ch:
                c += 1

        if ch not in result:
            print(ch, "frequency", c)
            result += ch   


str1 = input("Enter a string: ")
count(str1)
