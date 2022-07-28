from random import choice

all_messages = []
all_people_who_wrote_the_message = []


class Extrovert:
    def __init__(self):
        self.name = "Экстраверт"

        self.support_message = "поддерживает"
        self.happy_message = "веселое сообщение"
        self.sad_message = "грустное сообщение"
        self.calm_message = "отвечает спокойно"
        self.aggressive_message = "агрессирует"
        self.insult_message = "оскорбляет"
        self.quit_message = "покидает беседу"
        self.message = choice([self.happy_message, self.sad_message])
        self.can_write_the_message = True

        self.action = "*злиться*"
        self.angry_action = False
        self.quit_action = False

        self.score = 0
        self.angry_score = 35
        self.leave_score = 80

    def action_checking(self):
        if self.score >= self.angry_score:
            self.angry_action = True
            self.message = self.action
            self.can_write_the_message = True
        else:
            self.angry_action = False
        if self.score >= self.leave_score:
            self.message = self.quit_message
            self.can_write_the_message = False
            self.quit_action = True

    def message_checking(self):
        self.action_checking()  # Проверяем все ли у пользователя в порядке
        if not self.quit_action:  # Если все ок, обрабатываем сообщение
            # Ниже получаем: имя пользователя, который написал сообщение, само сообщение,
            # Ссылку на его объект, и ссылку на объект, который написал прошлое сообщение
            name, last_message = all_messages[len(all_messages) - 1].split(': ')
            last_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 1]
            previous_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 2]

            if 'Тролль' in name and last_message == '*агрессирует и оскорбляет*':
                if self.score >= 15:
                    self.score -= 15
                    self.can_write_the_message = True
                    self.message = choice([self.aggressive_message, self.insult_message])
                else:
                    self.score = 0
            elif 'Подпевала' in name and last_message == '*агрессирует*':
                if self.score >= 5:
                    self.score -= 5
                else:
                    self.score = 0

            if last_obj == self:  # Если пользователь только что писал сообщение, то он не может писать еще раз
                self.can_write_the_message = False
            else:
                if previous_obj != self:  # Если это сообщение не адресовалось этому пользователю, то он будет сразу отвечать
                    if 'Тролль' in name and last_message == '*агрессирует и оскорбляет*':
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.insult_message])
                    elif 'Интроверт' in name or 'Защитник' in name:
                        if last_message != self.support_message:
                            self.can_write_the_message = True
                            self.message = choice([self.support_message, self.happy_message, self.sad_message])
                        else:
                            self.can_write_the_message = True
                            self.message = choice([self.happy_message, self.sad_message])
                    elif 'Тролль' in name or 'Подпевала' in name:
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.calm_message, self.insult_message])
                    else:
                        self.can_write_the_message = False
                else:  # Если ему, то пересчитываем переменную score
                    if last_message == 'ехидное сообщение':
                        self.score += 5
                    elif last_message == 'агрессирует' or last_message == 'оскорбляет':
                        self.score += 10
                    elif last_message == 'поддакивает':
                        self.score += 15
                    elif 'Экстраверт' not in name and last_message == 'поддерживает':
                        if self.score >= 4:
                            self.score -= 4
                        else:
                            self.score = 0


class Introvert:
    def __init__(self):
        self.name = "Интроверт"

        self.support_message = "поддерживает"
        self.happy_message = "веселое сообщение"
        self.sad_message = "грустное сообщение"
        self.calm_message = "отвечает спокойно"
        self.aggressive_message = "агрессирует"
        self.insult_message = "оскорбляет"
        self.quit_message = "покидает беседу"
        self.can_write_the_message = True
        self.message = choice([self.happy_message, self.sad_message])

        self.action = "*плачет*"
        self.angry_action = False
        self.quit_action = False

        self.score = 0
        self.angry_score = 15
        self.leave_score = 40

    def action_checking(self):
        if self.score >= self.angry_score:
            self.angry_action = True
            self.message = self.action
            self.can_write_the_message = True
        else:
            self.angry_action = False
        if self.score >= self.leave_score:
            self.message = self.quit_message
            self.can_write_the_message = False
            self.quit_action = True

    def message_checking(self):
        self.action_checking()
        if not self.quit_action:
            name, last_message = all_messages[len(all_messages) - 1].split(': ')
            last_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 1]
            previous_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 2]

            if 'Тролль' in name and last_message == '*агрессирует и оскорбляет*':
                if self.score >= 2:
                    self.score -= 2
                    self.can_write_the_message = True
                    self.message = choice([self.aggressive_message, self.insult_message])
                else:
                    self.score = 0
            elif 'Подпевала' in name and last_message == '*агрессирует*':
                if self.score >= 1:
                    self.score -= 1
                else:
                    self.score = 0

            if last_obj == self:
                self.can_write_the_message = False
            else:
                if previous_obj != self:
                    if 'Тролль' in name and last_message == '*агрессирует и оскорбляет*':
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.insult_message])
                    elif 'Интроверт' in name or 'Защитник' in name or 'Экстраверт' in name:
                        if last_message != self.support_message:
                            self.can_write_the_message = True
                            self.message = choice([self.support_message, self.happy_message, self.sad_message])
                        else:
                            self.message = choice([self.happy_message, self.sad_message])
                    elif "Тролль" in name or "Подпевала" in name:
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.calm_message, self.insult_message])
                    else:
                        self.can_write_the_message = False
                else:
                    if last_message == 'ехидное сообщение':
                        self.score += 7
                    elif last_message == 'агрессирует' or last_message == 'оскорбляет':
                        self.score += 12
                    elif last_message == 'поддакивает':
                        self.score += 17
                    elif last_message == 'поддерживает':
                        if self.score >= 3:
                            self.score -= 3
                        else:
                            self.score = 0


class Protector:
    def __init__(self):
        self.name = 'Защитник'

        self.message = ""
        self.support_message = "поддерживает"
        self.calm_message = "отвечает спокойно"
        self.aggressive_message = "агрессирует"
        self.insult_message = "оскорбляет"
        self.quit_message = "покидает беседу"
        self.can_write_the_message = False

        self.score = 0
        self.angry_score = 70
        self.leave_score = 100

        self.action = '*агрессирует*'
        self.angry_action = False
        self.quit_action = False

    def action_checking(self):
        if self.score >= self.angry_score:
            self.angry_action = True
            self.message = self.action
            self.can_write_the_message = True
        else:
            self.angry_action = False
        if self.score >= self.leave_score:
            self.message = self.quit_message
            self.can_write_the_message = False
            self.quit_action = True

    def message_checking(self):
        self.action_checking()
        if not self.quit_action:
            name, last_message = all_messages[len(all_messages) - 1].split(': ')
            last_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 1]
            previous_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 2]

            if 'Тролль' in name and last_message == '*агрессирует и оскорбляет*':
                if self.score >= 10:
                    self.score -= 10
                    self.can_write_the_message = True
                    self.message = choice([self.aggressive_message, self.insult_message])
                else:
                    self.score = 0
            elif 'Подпевала' in name and last_message == '*агрессирует*':
                if self.score >= 3:
                    self.score -= 3
                else:
                    self.score = 0

            if last_obj == self:
                self.can_write_the_message = False
            else:
                if previous_obj != self:
                    if 'Тролль' in name and last_message == '*агрессирует и оскорбляет*':
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.insult_message, self.calm_message])
                    elif 'Тролль' in name or 'Подпевала' in name:
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.calm_message, self.insult_message])
                    elif 'Экстраверт' in name or 'Интроверт' in name:
                        if last_message != self.support_message:
                            self.can_write_the_message = True
                            self.message = self.support_message
                        else:
                            self.can_write_the_message = False
                    else:
                        self.can_write_the_message = False
                else:
                    if last_message == 'ехидное сообщение':
                        self.score += 10
                    elif last_message == 'агрессирует' or last_message == 'оскорбляет':
                        self.score += 10
                    elif last_message == 'поддакивает':
                        self.score += 15
                    elif last_message == 'поддерживает':
                        if self.score >= 2:
                            self.score -= 2
                        else:
                            self.score = 0


class Troll:
    def __init__(self):
        self.name = 'Тролль'

        self.message = ""
        self.aggressive_message = "агрессирует"
        self.insult_message = "оскорбляет"
        self.snide_message = "ехидное сообщение"
        self.can_write_the_message = False
        self.quit_message = "покидает беседу"

        self.score = 0
        self.angry_score = 55
        self.leave_score = 110

        self.action = "*агрессирует и оскорбляет*"
        self.angry_action = False
        self.already_was_angry = False
        self.quit_action = False

    def action_checking(self):
        if self.score >= self.angry_score and not self.already_was_angry:
            self.angry_action = True
            self.message = self.action
            self.can_write_the_message = True
            self.already_was_angry = True
        else:
            self.angry_action = False
            self.already_was_angry = False
        if self.score >= self.leave_score:
            self.message = self.quit_message
            self.can_write_the_message = False
            self.quit_action = True

    def message_checking(self):
        self.action_checking()
        if not self.quit_action:
            name, last_message = all_messages[len(all_messages) - 1].split(': ')
            last_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 1]
            previous_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 2]

            if 'Экстраверт' in name and last_message == '*злится*':
                if self.score >= 10:
                    self.score -= 10
                else:
                    self.score = 0
            elif 'Интроверт' in name and last_message == '*плачет*':
                if self.score >= 15:
                    self.score -= 15
                else:
                    self.score = 0
            elif 'Защитник' in name and last_message == '*агрессирует*':
                if self.score >= 20:
                    self.score -= 20
                else:
                    self.score = 0

            if last_obj == self:
                self.can_write_the_message = False
            else:
                if previous_obj != self:
                    if 'Тролль' not in name and 'Подпевала' not in name:
                        self.can_write_the_message = True
                        self.message = choice([self.aggressive_message, self.insult_message, self.snide_message])
                    else:
                        self.can_write_the_message = False
                    if name == 'Подпевала':
                        self.can_write_the_message = False
                else:
                    if last_message == 'агрессирует' or last_message == 'оскорбляет':
                        self.score += 5
                    elif last_message == 'отвечает спокойно':
                        self.score += 10
                    elif last_message == 'поддакивает':
                        if self.score >= 1:
                            self.score -= 1
                        else:
                            self.score = 0


class YesMan:
    def __init__(self):
        self.name = 'Подпевала'

        self.message = ""
        self.yes_message = "поддакивает"
        self.snide_message = "ехидное сообщение"
        self.can_write_the_message = False
        self.quit_message = "покидает беседу"

        self.score = 0
        self.angry_score = 25
        self.leave_score = 50

        self.action = "*агрессирует*"
        self.angry_action = False
        self.quit_action = False

    def action_checking(self):
        if self.score >= self.angry_score:
            self.angry_action = True
            self.message = self.action
            self.can_write_the_message = True
        else:
            self.angry_action = False
        if self.score >= self.leave_score:
            self.message = self.quit_message
            self.can_write_the_message = False
            self.quit_action = True

    def message_checking(self):
        self.action_checking()
        if not self.quit_action:
            name, last_message = all_messages[len(all_messages) - 1].split(': ')
            last_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 1]
            previous_obj = all_people_who_wrote_the_message[len(all_people_who_wrote_the_message) - 2]

            if 'Экстраверт' in name and last_message == '*злится*':
                if self.score >= 15:
                    self.score -= 15
                else:
                    self.score = 0
            elif 'Интроверт' in name and last_message == '*плачет*':
                if self.score >= 20:
                    self.score -= 20
                else:
                    self.score = 0
            elif 'Защитник' in name and last_message == '*агрессирует*':
                if self.score >= 25:
                    self.score -= 25
                else:
                    self.score = 0

            if last_obj == self:
                self.can_write_the_message = False
            else:
                if previous_obj != self:
                    if 'Тролль' in name:
                        if last_message != self.yes_message:
                            self.can_write_the_message = True
                            self.message = self.yes_message
                        else:
                            self.can_write_the_message = False
                    elif 'Интроверт' in name or 'Экстраверт' in name or 'Защитник' in name:
                        self.can_write_the_message = True
                        self.message = self.snide_message
                    else:
                        self.can_write_the_message = False
                else:
                    if 'Тролль' not in name and last_message == 'агрессирует' or last_message == 'оскорбляет':
                        self.score += 10
                    elif last_message == 'отвечает спокойно':
                        self.score += 15
