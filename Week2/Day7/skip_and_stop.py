for i in range(1, 4):
    for j in range(1, 6):
        if j == 3:
            continue
        print('i:', i, 'j:', j)
        if j == 5:
            break
