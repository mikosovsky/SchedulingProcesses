from Process import ProcState, Process, ProcessList

P1 = Process("P1", [(ProcState.Executed, 3), (ProcState.Waiting, 4)])
P2 = Process("P2", [(ProcState.Executed, 5), (ProcState.New, 4)])
process_list = ProcessList([P1])
# process_list[1].process_ans = [ProcState.Executed, ProcState.Executed, ProcState.Executed]
process_list.sort_processes()
print(P1)
print(P2)
for p in process_list:
    print(p)
