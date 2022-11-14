


#########################    SET

class Set:
    def __init__(self,a,b):
        self.a=a
        self.b=b


    def pop(self,list,nPop):
        print(list)
        try:
            list.pop(nPop)
        except:
            print("That index is not exist")
        print(list)

    def add(self,list,nAdd):

        list.append(nAdd)
        return a.sett(list)




    def union(self,list,list2):
        list3=[]
        list3=list+list2
        return a.sett(list3)


    def difference(self,list,list2):
        list3=[]
        list4=[]
        print(list2)
        for i in range(len(list)):
            count=0
            for j in range(len(list2)):
                if list[i]==list2[j]:
                   count+=1
                if count == 1:
                    break
            if count ==0:
                list3.append(list[i])
        for i in range(len(list2)):
            count1=0
            for j in range(len(list)):
                if list2[i]==list[j]:
                   count1+=1
                if count1 == 1:
                    break
            if count1 == 0:
                list4.append(list2[i])
        print("a.difference(b) = ",list3)
        print("b.difference(a) = ",list4)




    def intersection(self,list,list2):
        list3=[]
        for i in range(len(list)):
            count=0
            for j in range(len(list2)):
                if list[i]==list2[j]:
                    count+=1
                if count==1:
                    list3.append(list[i])
        a.sett(list3)




    def sett(self,list):
        #12 12 13 14
        for i in range(len(list)):
            count = 0
            for j in range(len(list)):
                if list[i]==list[j]:
                    count+=1
                    if count==2:
                        list.pop(j)
                        return a.sett(list)
        list=sorted(list)
        print(list)



    def main(self):
        n=int(input("Enter n: "))
        list=[]
        for i in range(n):
            i=int(input("Enter element: "))
            list.append(i)
        print(list)
        a.sett(list)

        while True:
            print("1.pop\n2.add\n3.union\n4.difference\n5.intersection")
            try:
                n = int(input("Enter n: "))
            except ValueError:
                print("Please try again")
            else:
                if n == 1:
                    while True:
                        try:
                            nPop=int(input("Enter index element: "))
                        except ValueError:
                            print("Please try again")
                        else:
                            a.pop(list,nPop)
                            break
                elif n == 2:
                    while True:
                        try:
                            nAdd=int(input("add new element: "))
                        except ValueError:
                            print("Please try again")
                        else:
                            a.add(list,nAdd)

                elif n == 3:
                    nSizeNewMass=int(input("Enter size new set: "))
                    list2=[]
                    for i in range(nSizeNewMass):
                        nElement=int(input("Enter elements: "))
                        list2.append(nElement)
                    a.sett(list2)
                    a.union(list,list2)
                elif n == 4:
                    nSizeNewMass = int(input("Enter size new set: "))
                    list2 = []
                    for i in range(nSizeNewMass):
                        nElement = int(input("Enter elements: "))
                        list2.append(nElement)
                    a.difference(list,list2)
                elif n==5:
                    nSizeNewMass = int(input("Enter size new set: "))
                    list2 = []
                    for i in range(nSizeNewMass):
                        nElement = int(input("Enter elements: "))
                        list2.append(nElement)
                    a.intersection(list,list2)
                else:
                    print("Please try again")
a=Set(2,3)
a.main()


# a={2,2,2,3,1,4,0}
# b={3,4,5,1,1,2,2}
# print(a)
# print(b)
#
#
#
# print(a.intersection(b))

#a.pop()
#a.add()
#a.clear()
#a.union()
#a.copy()
#difference
#intersection

















