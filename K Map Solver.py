import copy

def var2_kmap(mt):
    for i in range(20):
        print("--",end='')
    for i in range(len(mt)):
        mt[i]='0b'+bin(mt[i])[2:].lstrip('0')
    op=''
    ans=[[0,0],[0,0]]
    flag=0
    temp=[]
    for i in range(2):
        for j in range(2):
            p='0b'+(bin(i)[2:]+bin(j)[2:]).lstrip('0')
            if p in mt:
                ans[i][j]=1
    for i in range(20):
        print("--",end='')
    print()
    print("The kmap plotted : ")
    for each in ans:
        print(*each)
    if ans==[[1,1],[1,1]]:
        flag=1
        op='1'

    if flag==0:
        for i in range(2):
            if ans[i]==[1,1]:
                op='A ' if i==1 else "A' "
                temp.extend([(i,0),(i,1)])
    
    if flag==0:
        if ans[0][0]==1 and ans[1][0]==1:
            op=op+"B' "
            temp.extend([(0,0),(1,0)])
        elif ans[0][1]==1 and ans[1][1]==1:
            op=op+"B "
            temp.extend([(0,1),(1,1)])
    vr=["A'B' ","A'B ","AB' ","AB "]

    if flag==0:
        for i in range(2):
            for j in range(2):
                if ans[i][j]==1 and (i,j) not in temp:
                    op=op+vr[int('0b'+bin(i)[2:]+bin(j)[2:],2)]
    op=op.rstrip(" ")
    op=op.replace(" ","+")
    for i in range(20):
        print("==",end='')
    print()
    print("The simplified equation is :",op)
    for i in range(20):
        print("==",end='')
    print()

def var3_kmap(mt):
    for i in range(20):
        print("--",end='')
    print()
    ansg=[[0,0,0,0],[0,0,0,0]]
    op=''
    flag=0
    qrd=[]
    dul=[]
    sngl=[]
    qrd_var_2_2=["B' ","C ","B ","C' "]
    qrd_var_1_4=["A' ","A "]
    dul_vert=["B'C' ","B'C ","BC ","BC' "]
    dul_horz=[["A'B' ","A'C ","A'B ","A'C' "],["AB' ","AC ","AB ","AC' "]]
    sngl_val=[["A'B'C' ","A'B'C ","A'BC ","A'BC' "],["AB'C' ","AB'C ","ABC ","ABC' "]]
    
    for i in range(2):
        for j in range(4):
            p=int('0b'+bin(i)[2:]+bin(j)[2:],2)
            if (i==1) and (j==0 or j==1):
                p=int('0b'+bin(i)[2:]+'0'+bin(j)[2:],2)
            if p in mt:
                ansg[i][j]=1

    for i in range(2):
        (ansg[i][2],ansg[i][3])=(ansg[i][3],ansg[i][2])
    for i in range(20):
        print("--",end='')
    print()
    print("K-Map plotted : ")
    for each in ansg:
        print(*each)

    if ansg==[[1]*4,[1]*4]:
        op=op+'1'
        flag=1
    if flag==0:
        for j in range(-1,3):
            if ansg[0][j]==1 and ansg[-1][j]==1 and ansg[0][j+1]==1 and ansg[-1][j+1]==1:
                qrd.append([(0,j),(-1,j)])
                if j<2:
                    qrd.append([(0,j+1),(-1,j+1)])
                    qrd.append([(0,j),(0,j+1)])
                    qrd.append([(-1,j),(-1,j+1)])
                else:
                    qrd.append([(0,-1),(-1,-1)])
                    qrd.append([(0,j),(0,-1)])
                    qrd.append([(-1,j),(-1,-1)])
                op=op+qrd_var_2_2[j]
    if flag==0:
        for i in range(-1,1):
            if ansg[i]==[1,1,1,1]:
                qrd.append([(i,-1),(i,0)])
                qrd.append([(i,0),(i,1)])
                qrd.append([(i,1),(i,2)])
                qrd.append([(i,2),(i,-1)])
                op=op+qrd_var_1_4[i]
    if flag==0:
        for j in range(-1,3):
            if ansg[0][j]==1 and ansg[1][j]==1:
                temp=0
                if [(0,j),(-1,j)] in qrd:
                    temp=1
                elif [(-1,j),(0,j)] in qrd:
                    temp=1
                if temp==0:
                    dul.append([(0,j),(-1,j)])
                    op=op+dul_vert[j]
                
    if flag==0:
        for i in range(-1,1):
            for j in range(-1,3):
                if ansg[i][j]==1 and ansg[i][j+1]==1:
                    temp=0
                    if j==2:
                        if [(i,j),(i,-1)] in qrd:
                            temp=1
                        elif [(i,-1),(i,j)] in qrd:
                            temp=1
                    else:
                        if [(i,j),(i,j+1)] in qrd:
                            temp=1
                        elif [(i,j+1),(i,j)] in qrd:
                            temp=1
                    if temp==0:
                        if j==2:
                            dul.append([(i,2),(i,-1)])
                        else:
                            dul.append([(i,j),(i,j+1)])
                        op=op+dul_horz[i][j]

    op=op.rstrip(" ")
    opl=op.split(" ")
    for i in range(len(opl)):
        opl[i]=opl[i]+" "
    
    for each in dul:
        d1cnt=0
        d2cnt=0
        (d1,d2)=(each[0],each[1])
        for each1 in dul:
            if d1 in each1:
                d1cnt+=1
            if d2 in each1:
                d2cnt+=1
        if d1cnt>1 and d2cnt>1:
            (d1i,d1j)=d1
            (d2i,d2j)=d2
            if d1i==d2i:
                p=dul_horz[d1i][d1j]
                opl.remove(p)
            else:
                p=dul_vert[d1j]
                opl.remove(p)
            dul.remove([d1,d2])
    op="".join(opl)

    for x in qrd:
        for each in x:
            sngl.append(each)
    for x in dul:
        for each in x:
            sngl.append(each)

    if flag==0:
        for i in range(-1,1):
            for j in range(-1,3):
                if ansg[i][j]==1:
                    if (i,j) not in sngl:
                        op=op+sngl_val[i][j]

    op=op.rstrip(" ")
    op=op.replace(' ',' + ')

    for i in range(20):
        print("==",end='')
    print()
    print("The simplified equation is :",op)
    for i in range(20):
        print("==",end='')
    print()


def var4_kmap(mt):
    for x in range(20):
        print("--",end='')
    print()
    an=[]
    (tmp,flag)=(0,0)
    op=''
    for i in range(4):
        an.append([0]*4)

    for i in range(4):
        for j in range(4):
            if i<2:
                bi='0'+bin(i)[2:]
            else:
                bi=bin(i)[2:]
            if j<2:
                bj='0'+bin(j)[2:]
            else:
                bj=bin(j)[2:]
            p=int('0b'+bi+bj,2)
            if p in mt:
                an[i][j]=1
    for i in range(4):
        (an[i][2],an[i][3])=(an[i][3],an[i][2])
    for i in range(4):
        (an[2][i],an[3][i])=(an[3][i],an[2][i])

    for x in range(20):
        print("--",end='') 
    print()
    print("The K-Map plotted : ")
    for each in an:
        print(*each)

    octa=[]
    qrd=[]
    qrd_ref=[]
    qrd_rep=[]
    dul=[]
    sngl=[]
    octa_val=[["C' ","D ","C ","D' "],["A' ","B ","A ","B' "]]  # 0 for vert and 1 for horz
    qrd_val=[["C'D' ","C'D ","CD ","CD' "],["A'B' ","A'B ","AB ","AB' "]]  # 0 for vert and 1 for horz
    qrd_val_4=[["A'C' ","A'D ","A'C ","A'D' "],["BC' ","BD ","BC ","BD' "],["AC' ","AD ","AC ","AD' "],["B'C' ","B'D ","B'C ","B'D' "]]
    dul_vert=[["A'C'D' ","A'C'D ","A'CD ","A'CD' "],["BC'D' ","BC'D ","BCD ","BCD' "],["AC'D' ","AC'D ","ACD ","ACD' "],["B'C'D' ","B'C'D ","B'CD ","B'CD' "]]
    dul_horz=[["A'B'C' ","A'B'D ","A'B'C ","A'B'D' "],["A'BC' ","A'BD ","A'BC ","A'BD' "],["ABC' ","ABD ","ABC ","ABD' "],["AB'C' ","AB'D ","AB'C ","AB'D' "]]
    sngl_val=[["A'B'C'D' ","A'B'C'D ","A'B'CD ","A'B'CD' "],["A'BC'D' ","A'BC'D ","A'BCD ","A'BCD' "],["ABC'D' ","ABC'D ","ABCD ","ABCD' "],["AB'C'D' ","AB'C'D ","AB'CD ","AB'CD' "]]

    if an==[[1]*4,[1]*4,[1]*4,[1]*4]:
        op='1'
    else:
        for i in range(-1,3):
            if an[i][0]==1 and an[i][1]==1 and an[i][2]==1 and an[i][-1]==1 and an[i+1][0]==1 and an[i+1][1]==1 and an[i+1][2]==1 and an[i+1][-1]==1:
                op=op+octa_val[1][i]
                octa.append([(i,0),(i,1),(i,2),(i,-1)])
                if i<2:
                    octa.append([(i+1,0),(i+1,1),(i+1,2),(i+1,-1)])
                else:
                    octa.append([(-1,0),(-1,1),(-1,2),(-1,-1)])
                if i<2:
                    octa.append([(i,0),(i+1,0),(i,1),(i+1,1)])
                    octa.append([(i,1),(i+1,1),(i,2),(i+1,2)])
                    octa.append([(i,2),(i+1,2),(i,-1),(i+1,-1)])
                    octa.append([(i,-1),(i+1,-1),(i,0),(i+1,0)])
                else:
                    octa.append([(i,0),(-1,0),(i,1),(-1,1)])
                    octa.append([(i,1),(-1,1),(i,2),(-1,2)])
                    octa.append([(i,2),(-1,2),(i,-1),(-1,-1)])
                    octa.append([(i,-1),(-1,-1),(i,0),(-1,0)])

        for i in range(-1,3):
            if an[0][i]==1 and an[1][i]==1 and an[2][i]==1 and an[-1][i]==1 and an[0][i+1]==1 and an[1][i+1]==1 and an[2][i+1]==1 and an[-1][i+1]==1:
                op=op+octa_val[0][i]    
                octa.append([(0,i),(1,i),(2,i),(-1,i)])
                if i<2:
                    octa.append([(0,i+1),(1,i+1),(2,i+1),(-1,i+1)])
                else:
                    octa.append([(0,-1),(1,-1),(2,-1),(-1,-1)])
                if i<2:
                    octa.append([(0,i),(1,i),(0,i+1),(1,i+1)])
                    octa.append([(1,i),(2,i),(1,i+1),(2,i+1)])
                    octa.append([(2,i),(-1,i),(2,i+1),(-1,i+1)])
                    octa.append([(-1,i),(0,i),(-1,i+1),(0,i+1)])
                else:
                    octa.append([(0,i),(1,i),(0,-1),(1,-1)])
                    octa.append([(1,i),(2,i),(1,-1),(2,-1)])
                    octa.append([(2,i),(-1,i),(2,-1),(-1,-1)])
                    octa.append([(-1,i),(0,i),(-1,-1),(0,-1)])

        for i in range(-1,3):
            if an[i][0]==1 and an[i][1]==1 and an[i][2]==1 and an[i][-1]==1:
                qrd_ref.append([(i,0),(i,1),(i,2),(i,-1)])
            if an[0][i]==1 and an[1][i]==1 and an[2][i]==1 and an[-1][i]==1:
                qrd_ref.append([(0,i),(1,i),(2,i),(-1,i)])

        for i in range(-1,3):
            for j in range(-1,3):
                if an[i][j]==1 and an[i][j+1]==1 and an[i+1][j]==1 and an[i+1][j+1]==1:
                    if i==2 and j==2:
                        temp=[(i,j),(-1,j),(i,-1),(-1,-1)]
                    elif i==2 and j<2:
                        temp=[(i,j),(-1,j),(i,j+1),(-1,j+1)]
                    elif j==2 and i<2:
                        temp=[(i,j),(i+1,j),(i,-1),(i+1,-1)]
                    else:
                        temp=[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
                    qrd_ref.append(temp)
        
            
        for i in range(-1,3):
            if an[i][0]==1 and an[i][1]==1 and an[i][2]==1 and an[i][-1]==1:
                if [(i,0),(i,1),(i,2),(i,-1)] not in octa:
                    op=op+qrd_val[1][i]
                    qrd.append([(i,0),(i,1)])
                    qrd.append([(i,1),(i,2)])
                    qrd.append([(i,2),(i,-1)])
                    qrd.append([(i,-1),(i,0)])

        for i in range(-1,3):
            if an[0][i]==1 and an[1][i]==1 and an[2][i]==1 and an[-1][i]==1:
                if [(0,i),(1,i),(2,i),(-1,i)] not in octa:
                    op=op+qrd_val[0][i]
                    qrd.append([(0,i),(1,i)])
                    qrd.append([(1,i),(2,i)])
                    qrd.append([(2,i),(-1,i)])
                    qrd.append([(-1,i),(0,i)])

        for i in range(-1,3):
            for j in range(-1,3):
                if an[i][j]==1 and an[i][j+1]==1 and an[i+1][j]==1 and an[i+1][j+1]==1:
                    if i==2 and j==2:
                        temp=[(i,j),(-1,j),(i,-1),(-1,-1)]
                    elif i==2 and j<2:
                        temp=[(i,j),(-1,j),(i,j+1),(-1,j+1)]
                    elif j==2 and i<2:
                        temp=[(i,j),(i+1,j),(i,-1),(i+1,-1)]
                    else:
                        temp=[(i,j),(i+1,j),(i,j+1),(i+1,j+1)]
                    if temp not in octa:
                        op=op+qrd_val_4[i][j]
                        if i<2 and j<2:
                            qrd.append([(i,j),(i,j+1)])
                            qrd.append([(i+1,j),(i+1,j+1)])
                            qrd.append([(i,j),(i+1,j)])
                            qrd.append([(i,j+1),(i+1,j+1)])
                        if j==2 and i<2:
                            qrd.append([(i,j),(i,-1)])
                            qrd.append([(i+1,j),(i+1,-1)])
                            qrd.append([(i,j),(i+1,j)])
                            qrd.append([(i,-1),(i+1,-1)])
                        if j<2 and i==2:
                            qrd.append([(i,j),(i,j+1)])
                            qrd.append([(-1,j),(-1,j+1)])
                            qrd.append([(i,j),(-1,j)])
                            qrd.append([(i,j+1),(-1,j+1)])
                        if i==2 and j==2:
                            qrd.append([(i,j),(i,-1)])
                            qrd.append([(-1,j),(-1,-1)])
                            qrd.append([(i,j),(-1,j)])
                            qrd.append([(i,-1),(-1,-1)])
                    
        for i in range(-1,3):
            for j in range(-1,3):
                if an[i][j]==1 and an[i][j+1]==1:
                    if j==2:
                        temp=[(i,j),(i,-1)]
                    else:
                        temp=[(i,j),(i,j+1)]
                    if temp not in qrd:
                        op=op+dul_horz[i][j]
                        if j==2:
                            dul.append([(i,j),(i,-1)])
                        else:
                            dul.append([(i,j),(i,j+1)])
                if an[i][j]==1 and an[i+1][j]==1:
                    if i==2:
                        temp=[(i,j),(-1,j)]
                    else:
                        temp=[(i,j),(i+1,j)]
                    if temp not in qrd:
                        op=op+dul_vert[i][j]
                        if i==2:
                            dul.append([(i,j),(-1,j)])
                        else:
                            dul.append([(i,j),(i+1,j)])

        for each in octa:
            sngl.extend(each)
        for each in qrd:
            sngl.extend(each)
        for each in dul:
            sngl.extend(each)
        for i in range(-1,3):
            for j in range(-1,3):
                if an[i][j]==1:
                    if (i,j) not in sngl:
                        op=op+sngl_val[i][j]

        op=op.strip()
        opl=op.split(" ")
        for i in range(len(opl)):
            opl[i]=opl[i]+" "
    
        dulref=copy.deepcopy(dul)

        for each in dul:
            (d1,d2)=(each[0],each[1])
            (cntd1,cntd2)=(0,0)
            for each in dulref:
                if d1 in each:
                    cntd1+=1
                if d2 in each:
                    cntd2+=1
            for each in qrd_ref:
                if d1 in each:
                    cntd1+=1
                if d2 in each:
                    cntd2+=1   
            if cntd1>1 and cntd2>1:
                try:
                    if d1[0]==d2[0]:
                        opl.remove(dul_horz[d1[0]][d1[1]])
                    if d1[1]==d2[1]:
                        opl.remove(dul_vert[d1[0]][d1[1]])
                    dulref.remove([(d1[0],d1[1]),(d2[0],d2[1])])
                except ValueError:
                    continue
    
        for each in qrd_ref:
            (d1,d2,d3,d4)=(each[0],each[1],each[2],each[3])
            (d1cnt,d2cnt,d3cnt,d4cnt)=(0,0,0,0)
            for each1 in dul:
                if d1 in each1:
                    d1cnt+=1
                if d2 in each1:
                    d2cnt+=1
                if d3 in each1:
                    d3cnt+=1
                if d4 in each1:
                    d4cnt+=1
            for each2 in qrd_ref:
                if each!=each2:
                    if d1 in each2:
                        d1cnt+=1
                    if d2 in each2:
                        d2cnt+=1
                    if d3 in each2:
                        d3cnt+=1
                    if d4 in each2:
                        d4cnt+=1
            if d1cnt>0 and d2cnt>0 and d3cnt>0 and d4cnt>0:
                try:
                    if d1[0]!=d2[0] and d1[1]!=d3[1]:
                        opl.remove(qrd_val_4[d1[0]][d1[1]])
                except ValueError:
                    continue

        for each in qrd_ref:
            (d1,d2,d3,d4)=(each[0],each[1],each[2],each[3])
            (d1cnt,d2cnt,d3cnt,d4cnt)=(0,0,0,0)
            for each1 in qrd_ref:
                if each1!=each:
                    if d1 in each1:
                        d1cnt+=1
                    if d2 in each1:
                        d2cnt+=1
                    if d3 in each1:
                        d3cnt+=1
                    if d4 in each1:
                        d4cnt+=1
                if d1cnt>0 and d2cnt>0 and d3cnt>0 and d4cnt>0:
                    try:
                        if d1[0]==d2[0]==d3[0]==d4[0]:
                            opl.remove(qrd_val[1][d1[0]])
                        elif d1[1]==d2[1]==d3[1]==d4[1]:
                            opl.remove(qrd_val[0][d1[1]])
                    except ValueError:
                        continue
                    
        op=''.join(opl)
    for x in range(20):
        print("==",end='')
    print()
    op=op.strip(" ")
    op=op.replace(" "," + ")

    print("Simplified equation is :",op)

    for x in range(20):
        print("==",end='')
    print()


ask='y'
while ask=='y':
    for x in range(20):
        print("--",end='')
    print()
    nfinp=int(input("Enter no of variables (2,3,4) : "))
    mt=list(map(int,input("Enter the Minterms : ").split()))
    if nfinp==2:
        var2_kmap(mt)
    elif nfinp==3:
        var3_kmap(mt)
    elif nfinp==4:
        var4_kmap(mt)
    else:
        print("Error! Please check your Inputs.")
    ask=input("Would you like to plot another K Map? ('y' for yes, 'n' for no): ").lower()
    for i in range(20):
        print("--",end='')
    print()
print("Thanks for trying this Program")
print("\t\t\t---Varun")