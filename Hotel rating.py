print("Welcome")
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("Getting your XML file.....")

data = []
#print("Getting data")
data = pd.read_excel(r"C:/Users/nilar/Downloads/Book.xlsx")
data = np.array(data)
print("Data reading complete")
#print(data)
#print("Data gathered")

#head = ['Serv. Qual','Satisfaction','Loyalty','Engagement','Percvd Value','Cust.Rel','Serv/Facil/Loc(Tangibles)','Front-line Service Behaviour','General Frontline','Suggestion']
head = []
k = 0.1
print("Preparing.....") 
while ( True):
  #print("k ", k)
  if round(float(k),1) == round(float(k)):
    if round( float(k),1) >= 10:
        head . append(str(round(k, 1)) )
        break  
    head . append(str(round(k, 1)) )
    k = float(k) + 0.1
   # print("k ",round(k,1))
  else:
      head.append('')
      if round( float(k),1) >= 10:
        break
      k = float(k) + 0.1
print("Preprocessing Complete")
  

#print("Head: ",head)
##objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')


print("Choose among the following attributes")
print('1. Serv. Qual\n','2. Satisfaction\n','3. Loyalty\n','4. Engagement\n','5. Percvd Value\n','6. Cust.Rel\n','7. Serv/Facil/Loc(Tangibles)\n','8. Front-line Service Behaviour\n','9. General Frontline\n','10. Suggestion\n', '11. show aggreagate')
ch = int( input( "Enter the serial no. of choice:☺ " ) )
ch = ch + 3
print("Received your choice")
if ch ==14:
    head = ['Serv.Qual','Satsfn','Loaylity','Engmnt.','Prcvd.Val','Cst.Rel','Tangibles','Font-Behav.','Gen.Frntline','Suggst']
    y_pos = np.arange(len(head))
    net =[]
    net = [97,94,25,36,87,33,111,92,43,12]

    #net.pop(0)
    plt.bar(y_pos, net, align='center', alpha=0.8)
    plt.xticks(y_pos, head)
    plt.ylabel('No. of people')
    plt.title('Hotel Rarting')

    plt.show()
    exit()





print("Gathering relevant data")
Data = []
for i in range(150):
    Data. append ( data[i][ch])
    #print("just added: ",data[i][4])

net =[]
#for i in data[150][4:]:
 #   net.append(i)
#print("newdata",net)
y_pos = np.arange(len(head))



#performance = [10,8,6,4,2,1]
##nokw starting analysis
#print(Data)
Data.sort()
#print("Data", Data)
nc = 0.0
cnt = 0
i = 0
print("Processing...")
while(True):
    #print("Chechking for ",nc,"and",Data[i], "with i",i)
   try:
    if nc == Data[i]:
        cnt = cnt + 1
    #   print("match for ",nc,"and",Data[i])
        i = i + 1
    elif  nc < Data[ i]:
        nc = round(nc + 0.1, 1)
        net.append(cnt)
        #print(" cnt = ", cnt , " for ", round(nc -0.1, 1))
        cnt = 0
    if round( nc,1) >= 10.1:
        break
   except:
       net.append(cnt)
       break
#print(net)
print("Processing complete")
print("Opening your graph in new window😀")
        
#print("net: ", len(net), "head:", len(head) )
net.pop(0)
plt.bar(y_pos, net, align='center', alpha=0.8)
plt.xticks(y_pos, head)
plt.ylabel('No. of people')
plt.title('Hotel Rarting')

plt.show()
