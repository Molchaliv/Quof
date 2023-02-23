import re


class DecodeError(Exception):
    def __init__(self, string: str): self._string = string
    def __str__(self): return self._string
    def __repr__(self): return self._string


class DumpError(Exception):
    def __init__(self, string: str): self._string = string
    def __str__(self): return self._string
    def __repr__(self): return self._string


class BaseParser(object):
    def __init__(self, file: str, comments: bool = True):
        self._file: str = file
        self._comments: bool = comments

    @property
    def file(self): return self._file

    @property
    def comments(self): return self._comments

    @staticmethod
    def brackets(data: list):
        checker = ""
        for chunk in data:
            if chunk in "()":
                checker += chunk

        while "()" in checker:
            checker = checker.replace("()", "")

        return not checker

    def precompile(self):
        with open(self.file, mode="r", encoding="utf-8") as file:
            predata = []
            unfinished = ""
            for chunk in file.readlines():
                chunk = chunk.strip()

                if not chunk or (chunk[:2] == "//" and self.comments):
                    continue

                if chunk[-1] != ";":
                    unfinished = f"{unfinished}{chunk}"
                else:
                    predata.append(f"{unfinished}{chunk[:-1]}")
                    unfinished = ""

            if unfinished:
                raise DecodeError("Closing bracket not defined!")

        return predata

    def recompile(self):
        redata = []
        for chunk in self.precompile():
            datachunk = [element for element in re.split("( |\\\".*?\\\"|'.*?')", chunk) if element.strip()]

            if len(datachunk) < 3:
                raise DecodeError("Unsupported chunk syntax!")

            if ("(" in datachunk or ")" in datachunk) and not self.brackets(datachunk):
                raise DecodeError("Parentheses were not closed!")

            redatachunk = []
            for data in datachunk:
                if data not in "()":
                    redatachunk.append(data)

            try:
                redata.append([*redatachunk[:2], eval(" ".join(redatachunk[2:]), {"__builtins__": None})])
            except Exception as error:
                raise DecodeError(f"Unsupported syntax: {error}")

        return redata

    def compile(self):
        data = {}
        for chunk in self.recompile():
            if chunk[1] != ":=":
                return DecodeError(f"Unsupported operator '{chunk[1]}'!")

            data[chunk[0]] = chunk[2]

        return data


def loads(file: str, *, comments: bool = True):
    return BaseParser(file, comments).compile()


def dumps(data: dict):
    output = []
    for key, value in data.items():
        if isinstance(value, tuple) or isinstance(value, list):
            datachunk = ",\n".join([f"    \"{chunk}\"" for chunk in value])
            output.append(f"{key} := (\n{datachunk}\n);")
        elif isinstance(value, str):
            output.append(f"{key} := \"{value}\";")
        elif isinstance(value, int) or isinstance(value, float):
            output.append(f"{key} := {value};")
        else:
            raise DumpError(f"Unsupported {type(value)} value type!")

    return "\n".join(output)
