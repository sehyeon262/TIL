# path = []
# N = 3
#
# def run(lev):
#     if lev == N:
#         print(path)
#         return
#
#     for i in range(1, 4):
#         path.append(i)
#         run(lev + 1)

def KFC(x):
    if x == 3:
        return
    print(x)
    KFC(x + 1)
    print(x)

KFC(0)