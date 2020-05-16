import numpy as np

er = ['why','who','how','where','which','what','when','was','were','did','do','does','is','are','many','much']
qst = []
txt = None
ans = None
fnd = []


def chek_qst(qst):
    global er
    for h in er:
        for i in qst:
            if i == h:
                qst.remove(i)
                # qst = np.delete(qst, ([i for i, j in enumerate(qst) if h in j]))
    return qst

def search_word(qst):
    global txt
    for h in qst:
        temp = []
        for n,l in enumerate(txt):
            if [n for i,j in enumerate(l) if h in j] != []:
                temp.append(n)
        # temp = np.array(temp)
        if temp != []:
            fnd.append(temp)

def read():
    global txt
    global qst
    global ans
    txt = np.array((input().lower()).split('.'))
    txt = txt.reshape(len(txt), 1)
    for i in range(5):
        qst.append((input().lower()).replace('?','').split())

    split_quest()
    qst = np.array(qst)
    ans = np.array((input().lower()).split(';'))
    ans = ans.reshape(len(ans), 1)

def split_quest():
    for i in range(len(qst)):
        qst[i] = chek_qst(qst[i])

def find_answer(fnd):
    flag = False
    answer = None
    global ans
    temp_min = []
    for i in fnd:
        if len(i) == 1:
            answer = i[0]
            # print(str(txt[answer][0]))
            for i  in ans:
                for j in i:
                    if j in txt[answer][0]:
                        # print('from first :: ',j,'\n',answer)
                        print(j)
                        flag = True
                if flag:
                    break
            if flag:
                break

    if not flag:
        for i in fnd:
            temp_min.append(len(i))
        temp_min = np.array(temp_min)
        temp_min = temp_min.argmin()
        # print(temp)
        p = []
        for i in fnd[temp_min]:
            count = 0
            for j,h in enumerate(fnd):
                if fnd[temp_min] != h:
                    if i in h:
                        count +=1
            p.append(count)
        p = np.array(p)
        # print('from second :: ',str(txt[fnd[temp_min][p.argmax()]][0]))
        print(str(txt[fnd[temp_min][p.argmax()]][0]))
        # for i in ans:
        #     for j in i:
        #         if j in txt[fnd[temp_min][p.argmax()]][0]:
        #             print(j)
        #             # break
        #     break



read()
for i,qst_num in enumerate(qst):
    fnd = []
    search_word(qst_num)
    # print('\n',fnd)
    find_answer(fnd)
    # fnd = np.array(fnd).reshape(len(fnd))
    # print('questin #{}'.format(i+1),fnd,'\n')
    # print(str(txt[find_answer(fnd)][0]))

# print(ans)
# print('\n',qst)
# print('\n\n',[(i,j[0]) for i,j in enumerate(txt)])
# print('\n\n',[(i,j[0]) for i,j in enumerate(ans)])





'''Zebras are several species of African equids (horse family) united by their distinctive black and white stripes. Their stripes come in different patterns, unique to each individual. They are generally social animals that live in small harems to large herds. Unlike their closest relatives, horses and donkeys, zebras have never been truly domesticated. There are three species of zebras: the plains zebra, the Grévy's zebra and the mountain zebra. The plains zebra and the mountain zebra belong to the subgenus Hippotigris, but Grévy's zebra is the sole species of subgenus Dolichohippus. The latter resembles an ass, to which it is closely related, while the former two are more horse-like. All three belong to the genus Equus, along with other living equids. The unique stripes of zebras make them one of the animals most familiar to people. They occur in a variety of habitats, such as grasslands, savannas, woodlands, thorny scrublands, mountains, and coastal hills. However, various anthropogenic factors have had a severe impact on zebra populations, in particular hunting for skins and habitat destruction. Grévy's zebra and the mountain zebra are endangered. While plains zebras are much more plentiful, one subspecies, the quagga, became extinct in the late 19th century – though there is currently a plan, called the Quagga Project, that aims to breed zebras that are phenotypically similar to the quagga in a process called breeding back.
Which Zebras are endangered?
What is the aim of the Quagga Project?
Which animals are some of their closest relatives?
Which are the three species of zebras?
Which subgenus do the plains zebra and the mountain zebra belong to?
subgenus Hippotigris;the plains zebra, the Grévy's zebra and the mountain zebra;horses and donkeys;aims to breed zebras that are phenotypically similar to the quagga;Grévy's zebra and the mountain zebra
'''