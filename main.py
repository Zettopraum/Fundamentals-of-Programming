from category import Category
from game import Game
from game_platform import GamePlatform
from game_review import GameReview

def main():
    platform = GamePlatform()

    while True:
        print("\n****Меню:****")
        print("1. Ігри")
        print("2. Пошук")
        print("3. Категорії")
        print("4. Коментарі")
        print("5. Вийти")

        choice_main = input("Виберіть опцію: ")

        if choice_main == "1":
            while True:
                print("\n      *******Ігри:*******")
                print("      1. Додати гру")
                print("      2. Видалити гру")
                print("      3. Редагувати гру")
                print("      4. Вернутися в меню")
                
                choice_games = input("Виберіть опцію: ")

                if choice_games == "1":
                    name = Game.input_game_name()
                    description = Game.input_game_description()
                    genre = Game.input_game_genre()
                    price = Game.input_game_price()
                    game = Game(name, description, genre, price)
                    platform.add_game(game)
                    print("Гра успішно додана!")

                elif choice_games == "2":
                    name = input("Введіть назву гри для видалення: ")
                    platform.remove_game(name)

                elif choice_games == "3":
                    name = input("Введіть назву гри для редагування: ")
                    game_found = False
                    for game in platform.games:
                        if game.name == name:
                            game_found = True
                            new_name = Game.input_game_name()
                            new_description = Game.input_game_description()
                            new_genre = Game.input_game_genre()
                            new_price = Game.input_game_price()

                            game.edit_game(new_name, new_description, new_genre, new_price)
                            print("Гра успішно відредагована!")
                            break
                    
                    if not game_found:
                        print("Гра не знайдена")

                elif choice_games == "4":
                    break

                else:
                    print("Неправильний вибір, будь ласка, введіть ще раз")

        elif choice_main == "2":
            while True:
                print("\n      *******Пошук:*******")
                print("      1. Пошук за ціною")
                print("      2. Пошук за назвою")
                print("      3. Пошук за жанром")
                print("      4. Вернутися в меню")
                
                choice_search = input("Виберіть опцію: ")

                if choice_search == "1":
                    max_price_input = input("Введіть максимальну ціну: ")
                    if max_price_input.strip():
                        try:
                            max_price = float(max_price_input)
                            platform.search_by_price(max_price)
                        except ValueError:
                            print("Будь ласка, введіть коректну ціну.")
                    else:
                        print("Будь ласка, введіть максимальну ціну для пошуку.")

                elif choice_search == "2":
                    keyword = input("Введіть назву гри для пошуку: ")
                    if keyword.strip():
                        platform.search_by_name(keyword)
                    else:
                        print("Будь ласка, введіть назву гри для пошуку.")

                elif choice_search == "3":
                    genre = input("Введіть жанр гри для пошуку: ")
                    if genre.strip():
                        platform.search_by_genre(genre)
                    else:
                        print("Будь ласка, введіть жанр гри для пошуку.")

                elif choice_search == "4":
                    break

                else:
                    print("Неправильний вибір, будь ласка, введіть ще раз")

        elif choice_main == "3":
            while True:
                print("\n      ************Категорії:************")
                print("      1. Показати список ігор")
                print("      2. Сортувати за назвою")
                print("      3. Сортувати за ціною")
                print("      4. Сортувати за жанром")
                print("      5. Сортувати за оцінкою")
                print("      6. Вернутися в меню")
                
                choice_categories = input("Виберіть опцію: ")

                if choice_categories == "1":
                    platform.list_games()

                elif choice_categories == "2":
                    sorted_games = Game.sort_by_name(platform.games)
                    print("Список ігор, відсортований за назвою:")
                    for game in sorted_games:
                        print(game)

                elif choice_categories == "3":
                    sorted_games = Game.sort_by_price(platform.games)
                    print("Список ігор, відсортований за ціною:")
                    for game in sorted_games:
                        print(game)
                
                elif choice_categories == "4":
                    sorted_games = Game.sort_by_genre(platform.games)
                    print("Список ігор, відсортований за жанром:")
                    for game in sorted_games:
                        print(game)
                
                elif choice_categories == "5":
                    pass

                elif choice_categories == "6":
                    break

                else:
                    print("Неправильний вибір, будь ласка, введіть ще раз")

        elif choice_main == "4":
            while True:
                print("\n      *******Коментарі:*******")
                print("      1. Додати коментар")
                print("      2. Переглянути коментарі")
                print("      3. Вернутися в меню")

                choice_reviews = input("Виберіть опцію: ")

                if choice_reviews == "1":
                    game_name = input("Введіть назву гри для додавання коментаря: ")
                    user_name = input("Введіть ваше ім'я: ")
                    rating = int(input("Введіть оцінку (1-5): "))
                    comment = input("Введіть коментар (максимум 50 символів): ")
                    review = GameReview(user_name, rating, comment)
                    platform.add_review_to_game(game_name, review)

                elif choice_reviews == "2":
                    game_name = input("Введіть назву гри для перегляду коментарів: ")
                    platform.list_reviews_for_game(game_name)

                elif choice_reviews == "3":
                    break

                else:
                    print("Неправильний вибір, будь ласка, введіть ще раз")

        elif choice_main == "5":
            print("До побачення!")
            break
        else:
            print("Неправильний вибір, будь ласка, введіть ще раз")

if __name__ == "__main__":
    main()
