from Process import ProcState, Process, ProcessList

P1 = Process("P1", [(ProcState.Executed, 3), (ProcState.Waiting, 5), (ProcState.Executed, 4)])
P2 = Process("P2", [(ProcState.New, 2), (ProcState.Executed, 5), (ProcState.Waiting, 2), (ProcState.Executed, 5)])
P3 = Process("P3", [(ProcState.New, 3), (ProcState.Executed, 1), (ProcState.Waiting, 1), (ProcState.Executed, 3)])
ans_P1 = "nwwwooooogwwww"
ans_P2 = "nnngwwwwwoogggwwwww"
ans_P3 = "nnnngggggwoggggggggwww"
ans = [ans_P1, ans_P2, ans_P3]
process_list = ProcessList([P1, P2, P3])

for p in process_list:
    print(p)

process_list.sort_processes()

for p in range(len(process_list)):
    print(process_list[p])
    if process_list[p].str_process_ans == ans[p]:
        print("Odpowiedź jest prawidłowa")


