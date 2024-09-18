class WordsFinder():
    def __init__(self, *args):
        self.file_names = [*args]

    def get_all_words(self):
        all_words = {}
        for i in self.file_names:
            with open(i, mode='r', encoding='utf8') as file:
                word = ''
                for line in file:
                    for j in range(len(line)):
                        if line[j] != '.' or line[j] != ',' or line[j] != '=' or line[j] != '!' or line[j] != '?' or line[j] != ';'or line[j] != ':':
                            word = word + line[j].lower()
                all_words[i] = word.split()
        return all_words
    def find(self, word):
        tdict = {}
        per = self.get_all_words()
        for key in per:
            for i in range(len(per[key])):
                if word.lower() == per[key][i]:
                    tdict[key] = i + 1
                    break
        return tdict

    def count(self,word):
        tdict = {}
        per = self.get_all_words()
        k = 0
        for key in per:
            for i in range(len(per[key])):
                if word.lower() == per[key][i]:
                    k += 1
                tdict[key] = k
        return tdict
        pass

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))

