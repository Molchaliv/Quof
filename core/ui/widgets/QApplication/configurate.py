import darkdetect
import json

from ...themes import QDarkStyleSheet, QLightStyleSheet


THEMES = {
    "Dark": QDarkStyleSheet(), "Light": QLightStyleSheet(),
    "System": QDarkStyleSheet() if darkdetect.isDark() else QLightStyleSheet()
}
LANGS = {
    "en": {
        "file": "File", "edit": "Edit", "style": "Style", "help": "Help",

        "new": "New", "open": "Open", "save": "Save", "save_as": "Save As", "print": "Print", "settings": "Settings",
        "exit": "Exit",

        "undo": "Undo", "redo": "Redo", "cut": "Cut", "copy": "Copy", "paste": "Paste", "del": "Delete",
        "select_all": "Select All", "find": "Find", "translate": "Translate", "copy_all": "Copy All",
        "search": "Search", "add_to_dict": "Add to dict",

        "bold": "Bold", "italic": "Italic", "underline": "Underline", "left": "Left", "right": "Right",
        "center": "Center", "both": "Both", "clear_style": "Clear style",

        "about": "About",

        "untitled": "Untitled", "status": "Line: {}, Column: {}, Zoom: {}%",

        "save_msg": "Do you want to save changes to file '{}'?", "save_msg_ok": "Save", "save_msg_no": "Don't Save",
        "save_msg_cansel": "Cansel", "read_err": "Error in read file: {}", "plugin_err": "Error in plugin '{}'!",

        "open_file": "Open File", "text_files": "Text Files (*.txt);;Html File (*.html);;All Files (*.*)",
        "save_file": "Save File",

        "status_bar": "Status bar", "current_line": "Current line", "zoom_enable": "Zoom enable",
        "spelling_enable": "Spelling highlight enable", "lang": "Language", "theme": "Theme", "font": "Font",
        "auto_save": "Auto save", "web_search": "Search", "apply": "Apply", "general": "General",
        "interface": "Interface", "other": "Other",

        "replace": "Replace", "match_case": "Match Case", "back": "Previous", "next": "Next"
    },

    "ru": {
        "file": "Файл", "edit": "Редактирование", "style": "Стиль", "help": "Помощь",

        "new": "Новый", "open": "Открыть", "save": "Сохранить", "save_as": "Сохранить как", "print": "Печать",
        "settings": "Настройки", "exit": "Выйти",

        "undo": "Отменить", "redo": "Исправить", "cut": "Вырезать", "copy": "Копировать", "paste": "Вставить",
        "del": "Удалить", "select_all": "Выбрать всё", "find": "Найти", "translate": "Перевести",
        "copy_all": "Копировать всё", "search": "Найти в интернете", "add_to_dict": "Добавить в словарь",

        "bold": "Жирный", "italic": "Курсив", "underline": "Подчеркнутый", "left": "Слева", "right": "Справа",
        "center": "По центру", "both": "Заполнение", "clear_style": "Очистить стиль",

        "about": "О программе",

        "untitled": "Без имени", "status": "Строка: {}, Колонка: {}, Приближение: {}%",

        "save_msg": "Хотите сохранить изменения в файле '{}'?", "save_msg_ok": "Сохранить",
        "save_msg_no": "Не сохранять", "save_msg_cansel": "Отмена",
        "plugin_err": "Ошибка в работе плагина '{}'!",

        "open_file": "Открыть файл", "text_files": "Текстовые файлы (*.txt);;Html Файл (*.html);;Все файлы (*.*)",
        "save_file": "Сохранить файл",

        "status_bar": "Строка состояния", "current_line": "Текущая строка", "zoom_enable": "Зумирование",
        "spelling_enable": "Подсветка синтаксиса", "lang": "Язык", "theme": "Тема", "font": "Шрифт",
        "auto_save": "Авто сохранение", "web_search": "Поисковая система", "apply": "Применить", "general": "Главное",
        "interface": "Интерфейс", "other": "Прочее",

        "replace": "Заменить", "match_case": "Учитывать регистр", "back": "Предыдущее", "next": "Следующее"
    }
}
SETTINGS = {
    "theme": "system", "lang": "en_EN"
}
