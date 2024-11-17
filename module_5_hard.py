import time

class User:
    """
    Класс пользователя, содержащий атрибуты: логин, пароль и возраст.
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def get_info(self):
        return self.nickname, self.password

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nicname == self.nickname

class Video:
    """
    Класс видео с атрибутами: заголовок, продолжительность, секунда остановки, ограничение по возрасту.
    """
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

class UrTube:
    """
    Класс содержащий список объектов User, список объектов Video, текущего пользователя User.
    """
    def __init__(self, users = [], videos = [], current_user = None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self,nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == user.get_info():
                self.current_user = nickname

    def register(self, nickname, password, age):
        flag = True
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                flag = False
                break

            if flag.__eq__(True):
                new_user = User(nickname, password, age)
                self.nickname = new_user.nickname
                self.password = new_user.password
                self.age = new_user.age
                info = [self.nickname, self.password, self.age]
                self.users.append(info)
                self.current_user = self.nickname

    def log_out(self):
        self.current_user = None

    def __add__(self, *args):
        videos_list = [*args]
        for i in videos_list:
            if isinstance(i, Video):
                title = i.title
                if title in self.videos:
                    continue
                else:
                    self.videos.append(i)


    def get_videos(self, search_word):
        videos_list = []
        for i in self.videos:
            if isinstance(i, Video):
                title = i.title
                if search_word.upper() in title.upper():
                    videos_list.append(title)
            else:
                continue
        return videos_list

    def watch_video(self, title):
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            video_exist = 0
            for video in self.videos:
                if title == video:
                    video_exist = 1
                    if self.users[self.current_user].age <= 18:
                        print("Вам нет 18, пожалуйста покиньте страницу")
                    else:
                        for counter in range(0, self.videos[video].duration):
                            self.videos[video].time_now = counter + 1
                            time.sleep(1)
                            print(self.videos[video].time_now, end=' ')
                        print("Конец видео")
            if video_exist == 0:
                print("Видеозапись не обнаружена")


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')