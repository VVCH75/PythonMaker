from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
class UrTube():
    Videos = {}
    users = {}
    current_user = None
    def add(self, *args):
        for i in args:
            self.Videos[i.title] = (i.duration, i.time_now, i.adult_mode)
    def get_videos(self, args):
        Find = []
        for i in self.Videos:
            if str(args).lower() in str(i).lower():
                Find.append(i)
        return Find

    def log_in(self, nickname, password):
        if self.users[nickname][0] == hash(password):
            self.current_user = nickname
        else:
            print(f'Пользователь {nickname} уже существует')

    def register(self, nickname, password, age):
        Us = User(nickname, password, age)
        if Us.nickname in self.users:
            UrTube.log_in(self, Us.nickname, Us.password)
        else:
            UrTube.users[Us.nickname] = (Us.password, Us.age)
            UrTube.current_user = Us.nickname
    def log_out():
        UrTube.current_user = None


def watch_video(title):
    if UrTube.current_user == None:
        print('Войдите в аккаунт, чтобы смотреть видео')
    else:
        if UrTube.users[UrTube.current_user][1] < 18 and UrTube.Videos[title][2] == True:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
            UrTube.log_out()
        else:
            for i in UrTube.Videos:
                if title in i:
                    duration = UrTube.Videos[title][0]
                else:
                    duration = 0
            if duration > 0:
                for i in range(duration):
                    print(i + 1, end=' ')
                    sleep(1)
                return print('Конец фильма')
            else:
                print('нет такого фильма')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
watch_video('Для чего девушкам парень программист?')
#
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# Попытка воспроизведения несуществующего видео
watch_video('Лучший язык программирования 2024 года!')


