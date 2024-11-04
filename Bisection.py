from tabulate import tabulate
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return x**2 - 3

def calculation(l, u, limit):
    if l >= u or func(l) * func(u) >= 0:
        print("No roots exist within the given interval")
        return

    count = 1
    result_list = []
    while count <= limit:
        mid = (l + u) / 2
        fl = func(l)
        fu= func(u)
        fm = func(mid)
        result_list.append([l, u, mid, fl, fu, fm])
        if func(mid) == 0:
            return mid
        elif func(l) * func(mid) < 0:
            u = mid
        else:
            l = mid
        count += 1

    header = ["a", "b", "mid", "f(a)", "f(b)", "f(mid)"]
    print(tabulate(result_list, headers=header, tablefmt="pretty"))

    # Plotting the function
    x_values = np.linspace(l - 1, u + 1, 100)
    y_values = func(x_values)

    plt.plot(x_values, y_values, label='f(x) = x^2 - 3')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
    plt.axvline(result_list[-1][2], color='red', linestyle='--', label='Root')
    #
    # plt.scatter(result_list[-1][2], func(result_list[-1][2]), color='red')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Bisection Method')
    plt.legend()
    plt.grid(True)
    plt.show()

lower_bound = float(input("Enter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))
num_iterations = int(input("Enter the number of iterations: "))
calculation(lower_bound, upper_bound, num_iterations)


# import  numpy as np
# import matplotlib.pyplot as plt
# from tabulate import tabulate
#
#
# def f(x):
#     return  x*x-3
#
# def bisection(u,l,iteration):
#     resrlt_list =[]
#
#
#     if u<l or f(u)*f(l)>0:
#         return
#     for i in range (iteration):
#         iter=i
#         r=(u+l)/2
#         fl=f(l)
#         fu=f(u)
#         fr=f(r)
#         resrlt_list.append([iter,l,u,fl,fu,fr])
#
#         if r==0 :
#             return r
#         elif fl*fr<0:
#             a=r
#         else:
#             b=r
#
#     print(tabulate( resrlt_list,headers=['iter','l','u','fl','fu','fr'],tablefmt="pretty"))
#     plt.scatter(resrlt_list[-1][2], f(resrlt_list[-1][2]), color='red')
#     x_v=np.linspace(l-1,u+1,100)
#     plt.axvline(resrlt_list[-1][2])
#     # plt.axhline(resrlt_list[-1][2])
#     y_v=f(x_v)
#     plt.plot(x_v,y_v)
#     plt.xlabel('x')
#     plt.ylabel('y')
#     plt.show()
#
#
# bisection(4,1,10)