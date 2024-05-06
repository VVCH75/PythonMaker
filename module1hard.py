list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(3,21):
    code_= ''
    for j in range(0,19):
        for k in range(1,19):
            if i % (list_[j]+list_[k]) == 0 and list_[j] < list_[k]:
                pare = str(list_[j])+str(list_[k])
                code_= code_ + pare

    print('Код для последовательности ',i,'- ',code_)
