import numpy as np 
import matplotlib.pyplot as plt

filename = './befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint,skip_header=1)
# print(type(bef_stats_df)," of size: ", bef_stats_df.size)
# print(bef_stats_df[0], "\n", bef_stats_df[len(bef_stats_df) - 1])

data = bef_stats_df

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}



def number_of_people_per_neighberhood():
    people_per_neighb = {}

    for i in neighb.keys():
        mask = (data[:, 0] == 2015) & (data[:, 1] == i)
        sum = np.sum(data[mask] [:, 4])
        # print("sum of people in", neighb.get(i), ": ", sum)
        people_per_neighb[neighb.get(i)] = sum
    
    return people_per_neighb



# print(number_of_people_per_neighberhood())

mask = (data[:,0] == 2015) & (data[:,2] == 18) & (data[:,3] == 5100)
print(data[mask])
# plt.axis([0,10,300,600])
plt.bar(data[:,1], data[:,4])
print(np.sum(data[mask][:,4]))
plt.show()




