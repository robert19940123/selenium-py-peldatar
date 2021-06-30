(lis_t) = []


def pos(mine):
    return [x for x in mine if x > 0] or None


def listmaker():
    while True:
        nice = int(input())
        lis_t.append(nice)
        if nice == 0:
            break


listmaker()
print(pos(reversed(lis_t)))



