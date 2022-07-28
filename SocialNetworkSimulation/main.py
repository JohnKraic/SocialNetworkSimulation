from tkinter import *
from random import randint
from users import *

extroverts_list = []
introverts_list = []
protectors_list = []
trolls_list = []
yes_men_list = []

all_people_dict = {}


class App:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x600")
        self.root.resizable(False, False)
        self.root.title("Social Network Simulation")

        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=1)

        self.start_button = Button(self.main_frame, text="Начать симуляцию", font="Arial, 18",
                                   command=self.start_simulation)
        self.start_button.pack(pady=20)

        self.extrovert_lbl = Label(self.main_frame, text="Экстравертов: " + str(len(extroverts_list)), font="Arial, 10")
        self.extrovert_lbl.place(x=0, y=10)
        self.introvert_lbl = Label(self.main_frame, text="Интровертов: " + str(len(introverts_list)), font="Arial, 10")
        self.introvert_lbl.place(x=0, y=30)
        self.protectors_lbl = Label(self.main_frame, text="Защитников: " + str(len(protectors_list)), font="Arial, 10")
        self.protectors_lbl.place(x=0, y=50)
        self.trolls_lbl = Label(self.main_frame, text="Троллей: " + str(len(trolls_list)), font="Arial, 10")
        self.trolls_lbl.place(x=400, y=10)
        self.yes_men_lbl = Label(self.main_frame, text="Подпевал: " + str(len(yes_men_list)), font="Arial, 10")
        self.yes_men_lbl.place(x=400, y=30)

        self.simulated = False
        self.run = True
        self.already_written_win = False

        self.good = []
        self.bad = []

        self.canvas = Canvas(self.main_frame, height=50000)
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        self.scroll_bar = Scrollbar(self.main_frame, orient=VERTICAL, command=self.canvas.yview)
        self.scroll_bar.pack(side=RIGHT, fill=Y)

        self.canvas.configure(yscrollcommand=self.scroll_bar.set)
        self.canvas.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.bind("<MouseWheel>", lambda e: self.canvas.yview_scroll(-1 * int((e.delta / 120)), "units"))

        self.message_frame = Frame(self.canvas, height=50000)
        self.canvas.create_window((0, 0), window=self.message_frame, anchor="nw")

        self.root.update()
        self.root.mainloop()

    def start_simulation(self):
        if not self.simulated:  # Проверяем не запускалась ли уже функция
            self.simulated = True  # Ставим, что запускалась
            people_dict = ['Extroverts', 'Introverts']  # Список типов личностей, которые могут начать диалог
            people_type = choice(people_dict)  # Выбираем случайную личность, с которой начнется диалог
            # Перебираем словарь с ключами в виде типов людей и значениями в виде списков объектов
            for name, type_list in all_people_dict.items():
                if name == people_type:  # Находим этот тип личности по ключу
                    obj = choice(type_list)  # Случайно выбираем объект
                    self.write_message(obj)  # Пользуемся функцией вывода сообщения
                    self.root.after(1000)  # Делаем паузу 1 секунду
                    self.root.update()  # Перерисовуем окно
            while self.run:  # Основной цикл
                can_write_message_list = []  # Список пользователей которые могут написать сообщение
                # Перебираем словарь с ключами в виде типов людей и значениями в виде списков объектов как и выше
                for name, type_list in all_people_dict.items():
                    for obj in type_list:
                        self.check_people()  # Вызываем функцию проверки победителя
                        obj.message_checking()  # Вызываем метода класса, отвечающий за обработку сообщений
                        if obj.quit_action:  # Проверяем не выходит ли пользователь
                            self.write_message(obj)  # Выводим сообщение
                            type_list.remove(obj)  # Удаляем пользователя из списка пользователей
                        elif obj.angry_action:  # Проверяем не вышел ли пользователь из себя
                            self.write_message(obj)
                            obj.angry_action = False
                        else:
                            if obj.can_write_the_message:  # Проверяем может ли пользователь писать
                                can_write_message_list.append(obj)  # И добавляем в список, если может
                try:
                    self.write_message(
                        choice(can_write_message_list))  # Случайно выбираем пользователя, который может писать
                except IndexError:  # Иногда бывает что оно багуется и не находит тех, кто может написать, и по этому пришлось добавить исключение
                    available_objects = []  # Список тех кто еще в беседе
                    for name, type_list in all_people_dict.items():
                        if type_list:
                            for obj in type_list:
                                available_objects.append(obj)
                    if len(available_objects) > 1:
                        for chosen_obj in available_objects:
                            if chosen_obj != all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 1]:
                                chosen_obj.message_checking()
                                self.write_message(chosen_obj)  # Обрабатываем случайно выбранного пользователя
                                break  # Выходим из цикла когда мы его нашли
                self.root.after(1000)  # Задержка между сообщениями
                # Ниже обновляем метки на которых количество пользователей
                self.extrovert_lbl['text'] = "Экстравертов: " + str(len(extroverts_list))
                self.yes_men_lbl['text'] = "Подпевал: " + str(len(yes_men_list))
                self.introvert_lbl['text'] = "Интровертов: " + str(len(introverts_list))
                self.protectors_lbl['text'] = "Защитников: " + str(len(protectors_list))
                self.trolls_lbl['text'] = "Троллей: " + str(len(trolls_list))
                self.root.update()
        else:
            self.root.destroy()
            all_people_who_wrote_the_message.clear()
            all_messages.clear()
            generate_users()
            self.__init__()

    def write_message(self, obj):
        if self.run:
            if obj.name in ['Экстраверт', 'Интроверт', 'Защитник']:
                message_lbl = Label(self.message_frame, text=obj.name + "(" + str(obj.score) + ")" + ": " + obj.message,
                                    fg="green", font="Arial, 12")
                message_lbl.pack()
                all_messages.append(message_lbl['text'])
                all_people_who_wrote_the_message.append(obj)
            else:
                message_lbl = Label(self.message_frame, text=obj.name + "(" + str(obj.score) + ")" + ": " + obj.message,
                                    fg="red", font="Arial, 12")
                message_lbl.pack()
                all_messages.append(message_lbl['text'])
                all_people_who_wrote_the_message.append(obj)

    def check_people(self):
        self.good.clear()
        self.bad.clear()
        for name, type_list in all_people_dict.items():
            if type_list:
                for obj in type_list:
                    if obj.name == 'Экстраверт' or obj.name == "Интроверт" or obj.name == "Защитник":
                        self.good.append(obj.name)
                    else:
                        self.bad.append(obj.name)
        if not self.already_written_win:
            if not self.good and self.bad:
                self.run = False
                win_message = "Тролли и Подпевалы победили"
                win_lbl = Label(self.message_frame, text=win_message, font="Arial, 12")
                win_lbl.pack()
                self.already_written_win = True
            elif not self.bad and self.good:
                self.run = False
                win_message = "Экстраверты, Интроверты и Защитники победили"
                win1_lbl = Label(self.message_frame, text=win_message, font="Arial, 12")
                win1_lbl.pack()
                self.already_written_win = True


def generate_users():
    global extroverts_list, introverts_list, protectors_list, trolls_list, yes_men_list, all_people_dict
    extroverts_list = [Extrovert() for i in range(randint(1, 2))]
    introverts_list = [Introvert() for i in range(randint(1, 2))]
    protectors_list = [Protector()]
    trolls_list = [Troll() for i in range(randint(1, 2))]
    yes_men_list = [YesMan() for i in range(randint(1, 2))]

    all_people_dict = {
        'Extroverts': extroverts_list,
        'Introverts': introverts_list,
        'Protectors': protectors_list,
        'Trolls': trolls_list,
        'YesMen': yes_men_list
    }


if __name__ == '__main__':
    generate_users()

    app = App()
