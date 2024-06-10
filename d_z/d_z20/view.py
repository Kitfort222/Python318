def add_title(title):
    def wrapper(func):
        def wrap(*args, **kwargs):
            print(f" {title} ".center(50, "="))
            output = func(*args, **kwargs)
            print("=" * 50)
            return output

        return wrap

    return wrapper


class UserUnterface:
    @add_title("Редактирование данных каталога фильмов")
    def wait_user_answer(self):
        # print(" Ввод пользовательских данных ".center(50, "="))
        print("Действия с фильмами:")
        print("1 - добавление фильма"
              "\n2 - каталог фильмов"
              "\n3 - просмотр определенного фильма"
              "\n4 - удаление фильма"
              "\nq - выход из программы")
        user_answer = input("Выберите вариант действия: ")
        # print("=" * 50)
        return user_answer

    @add_title("Добавление фильма")
    def add_user_article(self):
        dict_article = {
            "название фильма": None,
            "режиссер": None,
            "жанр": None,
            "год выпуска": None,
            "длительность": None,
            "студия": None,
            "актеры": None
        }
        # print(" Добавление фильма ".center(50, "="))
        for key in dict_article:
            dict_article[key] = input(f"Введите {key} фильма: ")
        # print("=" * 50)
        return dict_article

    @add_title("Каталог фильмов")
    def show_all_articles(self, articles):
        # print(" Каталог фильмов ".center(50, "="))
        for ind, article in enumerate(articles, 1):
            print(f"{ind}. {article}")
        # print("=" * 50)

    @add_title("Просмотр определенного фильма")
    def get_user_article(self):
        user_article = input("Введите название фильма: ")
        return user_article

    @add_title("Просмотр фильма")
    def show_single_article(self, article):
        for key in article:
            print(f"{key} фильма - {article[key]}")

    @add_title("Сообщение об ошибке")
    def show_incorrect_title_error(self, user_title):
        print(f"Фильм с таким названием {user_title}не существует")

    def remove_single_article(self, article):
        print(f"Фильм {article} - был удален")

    @add_title("Сообщение об ошибке")
    def show_incorrect_answer_error(self, answer):
        print(f"Вариант {answer} не существует")
