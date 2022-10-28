import configparser
import os
from typing import Any
from setting import logger


class Config:
    """
    Класс по настройке, установке и изменению настроек программы SADSGP
    """

    def __init__(self, path: str = 'settings.ini') -> None:
        self.path_file = path
        self.config = configparser.ConfigParser()

        self.exists_config()
        self.read_config()

    @logger.logger.catch
    def create_config(self) -> None:
        """
        Создание файла настроек
        """
        self.config.add_section("BASE_PATH")
        self.config.set("BASE_PATH", "font", "Courier")
        self.config.set("BASE_PATH", "font_size", "12")
        self.config.set("BASE_PATH", "font_style", "Normal")
        self.config.set("BASE_PATH", "btn_color", "green")

        self.config.add_section("OTHER")
        self.config.set("OTHER", "font", "Courier")
        self.config.set("OTHER", "font_size", "12")
        self.config.set("OTHER", "font_style", "Normal")
        self.config.set("OTHER", "btn_color", "green")

        self.config.add_section("FONT_and_COLOR")
        self.config.set("FONT_and_COLOR", "font", "Courier")
        self.config.set("FONT_and_COLOR", "font_size", "14")
        self.config.set("FONT_and_COLOR", "font_style", "Normal")
        self.config.set("FONT_and_COLOR", "btn_color", "grey")

        with open(self.path_file, "w") as config_file:
            self.config.write(config_file)

    @logger.logger.catch
    def exists_config(self) -> None:
        """
        Проверяет путь до файла конфигурации. Если файла нету, то создает его
        """
        if not os.path.exists(self.path_file):
            self.create_config()

    @logger.logger.catch
    def read_config(self) -> None:
        """
        Считывает настройки из файла и устанавливает их в курсор
        """
        self.config.read(self.path_file)

    @logger.logger.catch
    def update_config(self, section: str, key: str, value: Any) -> None:
        """
        Изменяет значение ключей курсора

        :param section: str
        :param key: str
        :param value: Any
        :return: None
        """
        self.config.set(section=section, option=key, value=value)

    @logger.logger.catch
    def remove_config(self, section: str, key: str) -> None:
        """
        Удаляет ключ из курсора по заданной секции

        :param section: str
        :param key: str
        :return: None
        """
        self.config.remove_option(section=section, option=key)

    @logger.logger.catch
    def remove_section(self, section: str) -> None:
        """
        Удаляет заданную секцию из курсора настроек

        :param section: str
        :return: None
        """
        self.config.remove_section(section=section)

    @logger.logger.catch
    def return_section_configfile(self) -> list:
        """
        Возвращает список с названиями секций конфигурационного файла

        :return: list с названиями секций конфигурационного файла
        """
        return self.config.sections()


if __name__ == '__main__':
    check = Config()
    pass
