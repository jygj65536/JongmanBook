C = int(input())


def makepair(listToPair):
    global ans
    global relation
    if len(listToPair) == 2:
        if relation[listToPair[0]][listToPair[1]]:
            ans += 1
        return

    else:
        for i in range(len(listToPair)):
            if(relation[listToPair[0]][listToPair[i]]):
                newlist = listToPair[1:i]
                if i != len(listToPair) - 1:
                    newlist = newlist + listToPair[i+1:]
                makepair(newlist)


for testcase in range(C):
    ans = 0;
    relation = [[0] * 10 for i in range(10)]

    [n, m] = list(map(int, input().split()))

    friendshipList = list(map(int, input().split()))

    for group in (friendshipList[pos:pos + 2] for pos in range(0, len(friendshipList), 2)):
        relation[group[0]][group[1]] = 1
        relation[group[1]][group[0]] = 1

    makepair([i for i in range(n)])

    print(ans)
