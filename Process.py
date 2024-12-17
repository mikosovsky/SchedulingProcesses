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
        self._soft_process_list = self._prepare_soft_process_list()


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
        self._soft_process_list = self._prepare_soft_process_list()

    def append_process(self, process):
        proc_state, duration = process
        if type(proc_state) != ProcState or type(duration) != int:
            raise TypeError("Wrong data types in process_list.")
        elif duration < 1:
            raise ValueError("Wrong value for duration of process.")
        self._process_list.append(process)
        self._soft_process_list = self._prepare_soft_process_list()

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
        return ans

    @property
    def process_ans(self):
        return self._process_ans

    @process_ans.setter
    def process_ans(self, process_ans):
        for proc_state in process_ans:
            if type(proc_state) != ProcState:
                raise TypeError("Wrong data types in process_ans.")
        self._process_ans = process_ans
        self._str_process_ans = self._translate_process_ans_to_str()

    def _prepare_soft_process_list(self):
        soft_process_list = []
        for proc_state in self.process_list:
            for _ in range(proc_state[1]):
                soft_process_list.append(proc_state[0])
        return soft_process_list

    @property
    def soft_process_list(self):
        return self._soft_process_list

class ProcessList(list):
    def __init__(self, iterable):
        for item in iterable:
            if type(item) != Process:
                raise TypeError("Wrong data types in ProcessList.")
        super().__init__(item for item in iterable)

    def __setitem__(self, index, item):
        if type(item) != Process:
            raise("Wrong data type to set in ProcessList.")
        super().__setitem__(index, item)

    def insert(self, index, item):
        if type(item) != Process:
            raise("Wrong data type of item in insert function of ProcessList.")
        super().insert(index, item)

    def append(self, item):
        if type(item) != Process:
            raise("Wrong data type of item in append function of ProcessList")
        super().append(item)

    def extend(self, other):
        if type(other) != ProcessList:
            raise("Wrong data type of list to extend ProcessList.")
        super().extend(other)

    def sort_processes(self):
        if len(self) > 0:
            for i in range(len(self)):
                sorted_processes = [ProcState.New]
                process_list = self[i].soft_process_list
                if i == 0:
                    #TODO: Jeżeli proces jest pierwszy w liście to należy go przepisać 1:1
                    len_process = len(process_list)
                    max_ready_el = process_list.count(ProcState.Executed)
                    max_loop_range = len_process + max_ready_el
                    right_j = 0
                    for j in range(max_loop_range):
                        if process_list[right_j] != ProcState.Executed:
                            sorted_processes.append(process_list[right_j])
                            right_j += 1
                        elif process_list[right_j] == ProcState.Executed and ((sorted_processes[j] != ProcState.Executed and
                        sorted_processes[j] != ProcState.Ready) and right_j != 0):
                            sorted_processes.append(ProcState.Ready)
                        else:
                            sorted_processes.append(process_list[right_j])
                            right_j += 1
                        if right_j == len_process:
                            break
                else:
                    #TODO: Każdy inny proces musi porównać swój aktualny stan ze wszystkimi procesami nad nim, żeby zweryfikować czy może otrzymać status ProcState.Executed
                    len_ans_list = self._get_lengths_of_ans_list()
                    max_len = max(len_ans_list)
                    len_process = sum([el[1] for el in self[i].process_list])
                    max_ready_el = process_list.count(ProcState.Executed)
                    max_loop_range = max_len + len_process + max_ready_el

                    right_j = 0
                    for j in range(max_loop_range):
                        if process_list[right_j] != ProcState.Executed:
                            sorted_processes.append(process_list[right_j])
                            right_j += 1
                        elif process_list[right_j] == ProcState.Executed and \
                                ((sorted_processes[j] != ProcState.Executed and
                                  sorted_processes[j] != ProcState.Ready) and right_j != 0):
                            sorted_processes.append(ProcState.Ready)
                        else:
                            is_executed = False
                            for k in range(i):
                                if len(self[k].process_ans) > j+1 and self[k].process_ans[j+1] == ProcState.Executed:
                                    is_executed = True
                                    break

                            if is_executed:
                                sorted_processes.append(ProcState.Ready)
                            else:
                                sorted_processes.append(process_list[right_j])
                                right_j += 1
                        if right_j == len_process:
                            break

                self[i].process_ans = sorted_processes

    def _get_lengths_of_ans_list(self):
        len_ans_list = []
        for process in self:
            if len(process.process_ans) > 0:
                len_ans_list.append(len(process.process_ans))
        return len_ans_list
