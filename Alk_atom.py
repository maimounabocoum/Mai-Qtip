# Here is the Class alk_atom created by Maimouna Bocoum - 01-08-2023
class alk_atom:
    def __init__(self,myList:list):
        # test the type of the list and trck error
        #try:
            self.MakeAtomFromList(myList)

        # except:
        #     print("error in construction format inpout. exemple of acceptable inpout: [ [0,[3,4]] , [1,[3,4]] ]")
        # pass

    def AddLeveltoList(self,Level:list):
          # Level exemple of list structure: [0,[1,2]], for l=0 ; F=1 and F=2
        self.LevelList.append(Level)
        self.MakeAtomFromList()
        
    def MakeAtomFromList(self,myList):
            N = len(myList)
            self.LevelList = myList
            self.F = []
            self.L = []
            self.J = []
            self.M = []

            for loop in range(0,N):
                Line = myList[loop]  # get l orbital number. l=0 for 6S1/2 , l=1 for 6P1/2 and 6P3/2
                F = Line[2]          # get list of hyperfine F values
                for f in range(0,len(F)):
                     for m in range(0,F[f]*2+1):
                        self.L.append(Line[0])
                        self.J.append(Line[1])
                        self.F.append(F[f])
                        self.M.append( - F[f] + m )
                        
            self.N = len(self.M)

            # count how many levels are not in the ground state
            self.N_notground = 0
            for loop in range(0,self.N):
                if [self.L[loop] , self.J[loop] , self.F[loop]]!=[0,0.5,min(self.F)]:
                    self.N_notground = self.N_notground + 1

    def BuildMvector(self):
        self.M = []
        for i in range(0,len(self.F)):
             for m in range(0,self.F[i]*2+1):
                self.M.append( - self.F[i] + m )

    def printAtom(self):
        print(self.N)
        print(self.LevelList)
        print(self.L)
        print(self.J)
        print(self.F)
        print(self.M)

    #@classmethod
    def FetchKetIndex(self,Level:list):
         # get List of all elements
         # list is in the form [[],[],[],[]]
        KetList = []
        for loop in range(0,self.N,1):
            KetList.append([self.L[loop],self.J[loop],self.F[loop],self.M[loop]])
        return [ i for (i,e) in enumerate(KetList) if e == Level ]
    
    def GetHPSDipolarElement(self,L1,J1,F1,M1,L2,J2,F2,M2,q):
        # transistion from (L1,J1,F1,M1) --> (L2,J2,F2,M2)
        Iatom = 7/2
        a = (-1)**(2*F2-1+M1+J1+1+Iatom)
        b = np.sqrt((2*F1 + 1) *(2.0 *F2 + 1) * (2 *J1 + 1))*Wigner6j(J2,J1,1,F1,F2,Iatom)*Wigner3j(F1,1,F2,M1,q,-M2)

        if abs(J1-J2) == 0:
            c = 3.182192647373821
        elif abs(J1-J2) == 1:
            c = 4.478602220001236
        else:
            raise Exception("Ckech J1 and J2 values!") 

        return a*b*c
    
    def GetHPSTransitionStrength(self,J,F1,F2):# F1->F2 transition S_FF' factor in Steck
            if J==0.5: # value for D1 line
                if F2==4:
                    if F1==4: # LEVEL FROM WHERE DECAY
                        S=5/12 
                    elif F1==3: # LEVEL FROM WHERE DECAY
                        S=7/12 
                elif F2==3:
                    if F1==4: # LEVEL FROM WHERE DECAY
                        S=3/4
                    elif F1==3: # LEVEL FROM WHERE DECAY
                        S=1/4 
            elif J==1.5: # value for D1 line
                if F2==4:
                    if F1==2: # LEVEL FROM WHERE DECAY
                        S=0 
                    elif F1==3: # LEVEL FROM WHERE DECAY
                        S=7/72 
                    elif F1==4: # LEVEL FROM WHERE DECAY
                        S=7/24
                    if F1==5: # LEVEL FROM WHERE DECAY
                        S=11/18 
                elif F2==3:
                    if F1==2: # LEVEL FROM WHERE DECAY
                        S=5/14 
                    elif F1==3: # LEVEL FROM WHERE DECAY
                        S=3/8 
                    elif F1==4: # LEVEL FROM WHERE DECAY
                        S=15/56
                    elif F1==5: # LEVEL FROM WHERE DECAY
                        S=0  
                    else:# error cast
                        raise Exception("Sorry, wrong number!") 
            
            else:# error cast
                raise Exception("Sorry, wrong number!") 
            return S


