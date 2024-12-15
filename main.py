from Process import ProcState, Process, ProcessList

P1 = Process("P1", [(ProcState.Executed, 3), (ProcState.Waiting, 4)])
P2 = Process("P1", [(ProcState.Executed, 5), (ProcState.New, 4)])
process_list = ProcessList([P1, P2])
process_list.sort_processes()
print(P1)
