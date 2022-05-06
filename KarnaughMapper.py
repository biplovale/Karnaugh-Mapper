class KarnaughMapper:
    #K_Map for 2 inputs.
    def construct_and_display_k_map(mt, nip):
        for i in range(50):
            print("-", end='')
        print()
        for j in range(len(mt)):
            mt[j] = '0b'+bin(mt[j])[2:].lstrip('0')
        op = ''
        ans = [[0, 0], [0, 0]]
        flag = 0
        temp = []
        for row in range(2):
            for column in range(2):
                p = '0b'+(bin(row)[2:]+bin(column)[2:]).lstrip('0')
                if p in mt:
                    ans[row][column] = 1
        for k in range(50):
            print("-", end='')
        print()

        print("The kmap plotted : ")
        print("  B'B")
        i = 0
        for each in ans:
            if(i == 0):
                print("A'", end='')
            else:
                print("A ", end='')
            print(*each)
            i = i + 1


    #simplification
        if ans == [[1, 1], [1, 1]]:
            flag = 1
            op = '1'

        if flag == 0:
            for row in range(2):
                if ans[row] == [1, 1]:
                    op = 'A ' if row == 1 else "A' "
                    temp.extend([(row, 0), (row, 1)])

        if flag == 0:
            if ans[0][0] == 1 and ans[1][0] == 1:
                op = op + "B' "
                temp.extend([(0, 0), (1, 0)])
            elif ans[0][1] == 1 and ans[1][1] == 1:
                op = op + "B "
                temp.extend([(0, 1), (1, 1)])

        vr = ["A'B' ", "A'B ", "AB' ", "AB "]

        if flag == 0:
            for row in range(2):
                for column in range(2):
                    if ans[row][column]==1 and (row, column) not in temp:
                        op = op + vr[int('0b' + bin(row)[2:] + bin(column)[2:], 2)]
        op = op.rstrip(" ")
        op = op.replace(" ", "+")
        for i in range(50):
            print("*", end='')
        print()
        print("The simplified equation is :", op)
        for i in range(50):
            print("*", end='')
        print()