class Category:
    def __init__(self, name):
        self.name = name
        self.category = []

    def add_category(self, category):
        self.categories.append(category)

    def remove_category(self, name):
            for category in self.categorys:
                if category.name == name:
                    self.categorys.remove(category)
                    print(f"Категорія {name} успішно видалена")
                    return True
            print(f"Категорія {name} не знайдена в списку ігор")
            return False

    def list_games(self):
        if self.categorys:
            print(f"Відеоігри в категорії {self.name}:")
            for category in self.categorys:
                print(category)
        else:
            print("У цій категорії немає відеоігор")
