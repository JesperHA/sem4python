import numpy as np 

a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))

a = np.arange(0, 27).reshape(3, 3, 3)
d = list(range(9, 30, 3))

pi_steps = np.linspace(0, 3 * np.pi, 8)

print (a)

# print('1st row (x-values): \n',a[0,0,:],'\n---------')
# print('1st collumn (y-values, where x==0): \n',a[0,:,0],'\n---------')
# print('1st depth (z-values, where y==0 and x==0): \n',a[:,0,0],'\n---------')
# print('value of first side, second slice, third piece:\n',a[0, 1, 2], '\n-------------')  # equal to a[0][1][2] = 5
# print('values of all x*z where y=2\n',a[:,2], '\n----------')  # equivivalent to a[:,2,:] all z, y=2, all x.
# print('all z and y values where x = 2: \n',a[:,:,2], '\n--------')  # 
# print('skip each second z,y,x: \n',a[::2,::2,::2])  # all z (skip each second) and all y (skip each second) etc.

print("sliced out 12, 13, 14", a[1,1,:])
print("sliced out 3, 12, 21", a[:,1,0])
print("Slice out y values where x is 2 and z is 0", a[0,:,2])