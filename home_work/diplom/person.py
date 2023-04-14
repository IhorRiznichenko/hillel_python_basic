import datetime


class Person:
    def __init__(self, name, day_of_birthday, sex, day_of_death=None, surname=None, middle_name=None):
        self.name = name
        self.surname = surname
        self.middle_name = middle_name
        self.day_of_birthday = self.create_date(day_of_birthday)
        self.day_of_death = self.create_date(day_of_death) if day_of_death else None
        self.sex = self.validate_sex(sex)
        self.age = self.age_calculation()

    @staticmethod
    def validate_sex(sex):
        if not sex:
            raise ValueError("Строка с половым признаком не может быть пустой")
        if sex.lower() not in ["м", "ж"]:
            raise ValueError("Неверный пол: ")
        return sex

    @staticmethod
    def create_date(date):
        if not date:
            raise ValueError("Дата не может быть пустой")
        date_formats = ["%d%m%Y", "%d-%m-%Y", "%d/%m/%Y", "%d %m %Y", "%d.%m.%Y", "%d %b %Y"]
        date_len = len(date)
        if date_len not in [8, 10, 11]:
            raise ValueError(f"Неверный формат даты: {date}")
        if not all(c.isdigit() or c in "-/, . " for c in date):
            raise ValueError(f"Недопустимые символы в дате: {date}")
        for date_format in date_formats:
            try:
                return datetime.datetime.strptime(date, date_format).date()
            except ValueError:
                pass
        raise ValueError(f"Недопустимое значение даты: {date}")

    @staticmethod
    def create_date_1(date):
        if not date:
            return None
        date_formats = ["%d%m%Y", "%d-%m-%Y", "%d/%m/%Y", "%d %m %Y", "%d.%m.%Y", "%d %b %Y"]
        date_len = len(date)
        if date_len not in [8, 10, 11]:
            raise ValueError(f"Неверный формат даты: {date}")
        if not all(c.isdigit() or c in "-/, . " for c in date):
            raise ValueError(f"Недопустимые символы в дате: {date}")
        for date_format in date_formats:
            try:
                return datetime.datetime.strptime(date, date_format).date()
            except ValueError:
                pass
        raise ValueError(f"Недопустимое значение даты: {date}")

    def age_calculation(self):
        today = datetime.date.today()
        if self.day_of_death:
            if (self.day_of_death.month, self.day_of_death.day) < (self.day_of_birthday.month, self.day_of_birthday.day):
                delta = self.day_of_death.year - self.day_of_birthday.year - 1
            else:
                delta = self.day_of_death.year - self.day_of_birthday.year
        else:
            if (today.month, today.day) < (self.day_of_birthday.month, self.day_of_birthday.day):
                delta = today.year - self.day_of_birthday.year - 1
            else:
                delta = today.year - self.day_of_birthday.year
        if delta < 0:
            delta += 1
        return delta

    def create_list(self):
        return [self.name, self.middle_name, self.surname, self.day_of_birthday, self.day_of_death, self.sex, self.age]

    @staticmethod
    def print_list(list_xlsx):
        gender = "мужчина" if "м" in list_xlsx[5] else "женщина"
        birth_date = list_xlsx[3].replace("00:00:00", "")
        death_date = list_xlsx[4].replace("00:00:00", "") if list_xlsx[4] else ""
        birth_suffix = "ся" if gender == "мужчина" else "ась"
        death_suffix = "" if gender == "мужчина" else "ла"
        output = f"{list_xlsx[0]} {list_xlsx[1]} {list_xlsx[2]} {list_xlsx[6]} г., {gender}. Родил{birth_suffix}: {birth_date}"
        if death_date:
            output += f" Умер{death_suffix}: {death_date}"
        return output
