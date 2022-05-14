eng = 'abcdefghijklmnopqrstuvwxyz'
phrase_in = input()
phrase = phrase_in.split()
phrase_res = []
len_eng = 26
result = ''
step = 0

def ave_caesar(result):
    for z in range(len(phrase)):
        temp_result = ''
        for y in range(len(phrase[z])):

            if phrase[z][y].isalpha():
                phrase_res.append(phrase[z][y])
            elif y == 0 and not phrase[z][y].isalpha():
                result = result + phrase[z][y]
            else:
                temp_result = phrase[z][y]

        step = len(phrase_res)
        temp = ''.join(phrase_res)

        for i in range(len(temp)):
            if ord('A') <= ord(temp[i]) <= ord('Z'):
                result = result + eng[step - (len_eng - eng.find(temp[i].lower()))].upper()
            else:
                result = result + eng[step - (len_eng - eng.find(temp[i].lower()))]

        result = result + temp_result
        phrase_res.clear()
        step = 0

        print(result, end=' ')
        result = ''


ave_caesar(result)


