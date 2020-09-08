import re


class TextFormatter:
    lines = None

    def __init__(self, path, file, tab_value):
        self.path = path
        self.file = file
        self.tab_value = tab_value
        self.get_all_file_lines()

    def get_all_file_lines(self):
        with open('{}/{}'.format(self.path, self.file), 'r') as rf:
            self.lines = rf.readlines()

    def tab_to_space(self):
        with open('{}/{}'.format(self.path, self.file), 'w') as wf:
            edited_rows = []
            for index, line in enumerate(self.lines):
                y = re.search(rf"^( ){{{self.tab_value}}}", line)
                if y:
                    edited_rows.append(index)
                x = re.sub(rf"^( ){{{self.tab_value}}}", " ", line)
                if x:
                    line = x
                wf.write(line)
            self.print_edited_rows(edited_rows)

    def space_to_tab(self):
        with open('{}/{}'.format(self.path, self.file), 'w') as wf:
            edited_rows = []
            for index, line in enumerate(self.lines):
                spaces = self.get_empty_space_from_tab_value(self.tab_value)
                y = re.search(r"^ (?=\S)", line)
                if y:
                    edited_rows.append(index)
                x = re.sub(r"^ (?=\S)", spaces, line)
                line = x
                wf.write(line)
            self.print_edited_rows(edited_rows)

    def analyze_file(self):
        spaces = []
        tabs = []
        with open('{}/{}'.format(self.path, self.file), 'r'):
            for index, line in enumerate(self.lines):
                s = re.search(r"^ (?=\S)", line)
                t = re.search(rf"^( ){{{self.tab_value}}}", line)
                if s:
                    spaces.append(index + 1)
                if t:
                    tabs.append(index + 1)
        return [spaces, tabs]

    @staticmethod
    def print_analyze_file(spaces: [], tabs: []):
        t_l = len(tabs)
        s_l = len(spaces)
        if s_l != 0:
            print(f"The program founded {s_l} spaces in rows: ", end=" ")
            for i, s in enumerate(spaces):
                if i == s_l:
                    print(f"{s}")
                else:
                    print(f"{s}", end=", ")
            print("")
        if t_l != 0:
            print(f"The program founded {t_l} tabs in rows: ", end=" ")
            for i, t in enumerate(tabs):
                if i == t_l:
                    print(f"{t}")
                else:
                    print(f"{t}", end=", ")
            print("")
        x = "-"
        arr_x = []
        for i in range(40 + t_l + s_l):
            arr_x.append(x)
        print(''.join(arr_x))

    @staticmethod
    def print_edited_rows(edited_rows: []):
        edited_rows_len = len(edited_rows)
        print(f"The program edited {edited_rows_len} rows")

    @staticmethod
    def get_empty_space_from_tab_value(tab_value):
        if not tab_value:
            return
        l1 = []
        s = " "
        i = 0
        while i < tab_value:
            l1.append(s)
            i += 1
        return ''.join(l1)
