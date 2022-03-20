import random
rc_chain = {
    'buggy': ['buggy', 'programs', 'programs', 'programs', 'programs'],
    'programs': ['buggy', 'buggy', 'buggy', 'buggy','programs']
}

rc = [random.choice(list(rc_chain.keys()))]

for i in range(3):
    rc.append(random.choice(rc_chain[rc[i]]))


for i in range(4):
    if (i % 2 != 0):
        print(rc[i], end =". ")
    else:
        print(rc[i], end =" ")

