# import matplotlib
# matplotlib.use('tkAgg')
#
# import matplotlib.pyplot as plt
# import random

# months = range(1, 13)
#
# boston = [28, 32, 39, 48, 59, 68, 75, 73, 66, 54, 45, 34]
# plt.subplot(3, 1, 1)
# plt.ylim(0, 100)
# plt.plot(months, boston, '*b-')
# plt.ylabel('Degrees F')
# plt.xticks((1, 3, 5, 7, 9, 11), ('Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'))
#
# phoenix = [54, 57, 61, 68, 77, 86, 91, 90, 84, 73, 61, 54]
# plt.subplot(3, 1, 2)
# plt.ylim(0, 100)
# plt.plot(months, phoenix, '.g--')
# plt.ylabel('Degrees F')
# plt.xticks((1, 3, 5, 7, 9, 11), ('Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'))
#
# msp = [16, 19, 34, 48, 59, 70, 75, 73, 64, 60, 37, 21]
# plt.subplot(3, 1, 3)
# plt.ylim(0, 100)
# plt.scatter(months, msp, 'or-.')
# plt.ylabel('Degrees F')
# plt.xticks((1, 3, 5, 7, 9, 11), ('Jan', 'Mar', 'May', 'Jul', 'Sep', 'Nov'))
#
#
# plt.suptitle('Boston vs Phoenix vs Minneapolis', fontsize=16)
#
# plt.tight_layout()
# plt.show()


# def get_pop(filename):
#     infile = open(filename, 'r')
#     result = []
#     for line in infile:
#         item = line.split('\t')[2]
#         pop = item.replace(',', '')
#         result.append(int(pop))
#     return result
#
# pops = get_pop('lec25_countryPops.txt')
# firstDigits = []
# for p in pops:
#     firstDigits.append(int(str(p)[0]))
#
# plt.hist(firstDigits, bins = 9,)
# plt.show()


# plt.plot(pops)
# plt.xlim(0, 236)
# # plt.yticks(range(0, 80))
# plt.title('Population Size of Countries in July 2017')
# plt.ylabel('Population')
# plt.xlabel('Country Rank Based on Size')
# plt.semilogy()
# plt.show()


# def prob(side):
#     dice = ['.', ':', ':.', '::', '::.', ':::']
#     Nsims = 1000000
#     count = 0
#     for i in range(Nsims):
#         roll = random.choice(dice)
#         if roll == side:
#             count += 1
#     print(count/Nsims)
#
# prob('.')
# prob(':::')