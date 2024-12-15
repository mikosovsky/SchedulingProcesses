from enum import Enum


class ProcState(Enum):
    New = 'n'
    Executed = 'w'
    Waiting = 'o'
    Ready = 'g'


class Process:
    __name: str
    __process_list: list[(ProcState, int)]
    __process_ans: str

    def append_proc(self, new_proc):
        state, duration = new_proc
        if type(state) == ProcState and type(duration) == int:
            self.__process_list.append(new_proc)

    def append_ans(self, process_ans):
        self.__process_ans = process_ans

    def get_process_list(self):
        return self.__process_list

    def __str__(self):
        if self.__process_ans == "":
            return self.name + ": " + str([(k.value, l) for k, l in self.__process_list])
        else:
            return self.name + ": " + self.__process_ans

    def __len__(self):
        length = 0
        for state, duration in self.__process_list:
            length += duration
        return length

    def __init__(self, name, process_list):
        self.name = name
        self.__process_list = process_list
        self.__process_ans = ""


class ProcessList(list):
    def __init__(self, iterable):
        super().__init__(str(item) for item in iterable)

    def __setitem__(self, index, item):
        super().__setitem__(index, str(item))

    def insert(self, index, item):
        super().insert(index, str(item))

    def append(self, item):
        super().append(str(item))

    def extend(self, other):
        if isinstance(other, type(self)):
            super().extend(other)
        else:
            super().extend(str(item) for item in other)

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


