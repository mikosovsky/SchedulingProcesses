from enum import Enum


class ProcState(Enum):
    New = 'n'
    Executed = 'w'
    Waiting = 'o'
    Ready = 'g'


class Process:
    def __init__(self, name, process_list):
        self.name = name
        self.process_list = process_list
        self.process_ans = []
        self.str_process_ans = ""

    def __str__(self):
        if self.str_process_ans == "":
            return self.name + ": " + str([(k.value, l) for k, l in self.process_list])
        else:
            return self.name + ": " + self.str_process_ans

    def __len__(self):
        length = 0
        for state, duration in self._process_list:
            length += duration
        return length

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if type(name) != str:
            raise TypeError("Wrong data type name should be str type.")
        self._name = name

    @property
    def process_list(self):
        return self._process_list

    @process_list.setter
    def process_list(self, process_list):
        for proc_state, duration in process_list:
            if type(proc_state) != ProcState or type(duration) != int:
                raise TypeError("Wrong data types in process_list.")
            elif duration < 1:
                raise ValueError("Wrong value for duration of process.")
        self._process_list = process_list

    def append_process(self, process):
        proc_state, duration = process
        if type(proc_state) != ProcState or type(duration) != int:
            raise TypeError("Wrong data types in process_list.")
        elif duration < 1:
            raise ValueError("Wrong value for duration of process.")
        self._process_list.append(process)

    @property
    def str_process_ans(self):
        return self._str_process_ans

    @str_process_ans.setter
    def str_process_ans(self, str_process_ans):
        if type(str_process_ans) != str:
            raise TypeError("Wrong data type in str_process_ans.")
        self._str_process_ans = str_process_ans

    def _translate_process_ans_to_str(self):
        ans = ""
        for proc_state in self._process_ans:
            ans += proc_state.value
        self.str_process_ans = ans

    @property
    def process_ans(self):
        return self._process_ans

    @process_ans.setter
    def process_ans(self, process_ans):
        for proc_state in process_ans:
            if type(proc_state) != ProcState:
                raise TypeError("Wrong data types in process_ans.")
            self._process_ans = process_ans
            self._translate_process_ans_to_str()


class ProcessList(list):
    def __init__(self, iterable):
        super().__init__(item for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, item)

    def insert(self, index, item):
        super().insert(index, item)

    def append(self, item):
        super().append(item)

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(item for item in other)

    def sort_processes(self):
        if len(self) > 0:
            sorted_processes = []
            for i in range(len(self)):
                if i == 0:
                    #TODO: Jeżeli proces jest pierwszy w liście to należy go przepisać 1:1
                    pass
                else:
                    #TODO: Każdy inny proces musi porównać swój aktualny stan ze wszystkimi procesami nad nim, żeby zweryfikować czy może otrzymać status ProcState.Executed
                    pass
