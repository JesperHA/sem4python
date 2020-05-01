import numpy as np 
import matplotlib.pyplot as plt
# plt.ion()

filename = 'befkbhalderstatkode.csv'

bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint,skip_header=1)
# print(type(bef_stats_df)," of size: ", bef_stats_df.size)
# print(bef_stats_df[0], "\n", bef_stats_df[len(bef_stats_df) - 1])

data = bef_stats_df

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}



def number_of_people_per_neighberhood():
    people_per_neighb = {}
    # total_pop = 0

    for i in neighb.keys():
        mask = (data[:, 0] == 2015) & (data[:, 1] == i)
        sum = np.sum(data[mask] [:, 4])
        # print("sum of people in", neighb.get(i), ": ", sum)
        people_per_neighb[neighb.get(i)] = sum
        
        # total_pop = total_pop + sum
    
    # print(total_pop)
    return people_per_neighb




# print(number_of_people_per_neighberhood())

def pop_bar_plot():

    pop_per_neighb = number_of_people_per_neighberhood()
    
    sorted_pop_per_neighb = {k: v for k, v in sorted(pop_per_neighb.items(), key=lambda item: item[1])} #copy pasted from stackoverflow, and not really understood

    plt.figure(figsize=(15, 6))
    plt.bar(sorted_pop_per_neighb.keys(), sorted_pop_per_neighb.values(), width=0.8)
    plt.xlabel("Neighborhood")
    plt.ylabel("Population")
    plt.show()



# pop_bar_plot()


def above_65():
     
    mask = (data[:, 0] == 2015) & (data[:, 2] >= 65)
    sum = np.sum(data[mask] [:, 4])    
    
    return sum


# print(above_65())

def above_65_nordic():
    mask = (data[:, 0] == 2015) & (data[:, 2] >= 65) & (data[:,3] != 5100) 
    sum = np.sum(data[mask] [:, 4])    
    
    return sum


# print(above_65_nordic())

def line_plot_changes():

    østerbro = {}
    vesterbro = {}

    for i in np.arange(1992, 2016):

        mask = ((data[:, 0] == i) & (data[:, 1] == 2))
        sum = np.sum(data[mask] [:, 4])
        østerbro[i] = sum

        mask = ((data[:, 0] == i) & (data[:, 1] == 4))
        sum = np.sum(data[mask] [:, 4])
        vesterbro[i] = sum
    
    østerbro_value = list(østerbro.values())
    vesterbro_value = list(vesterbro.values())
    årstal = list(østerbro.keys())
    
    plt.plot(årstal, østerbro_value)
    plt.plot(årstal, vesterbro_value)

    plt.show()

line_plot_changes()



