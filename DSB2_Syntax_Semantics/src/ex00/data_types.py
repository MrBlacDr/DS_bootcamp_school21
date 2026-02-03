def data_types():
    var1 = 1
    var2 = '1'
    var3 = 3.1415
    var4 = True
    var5 = [1,2,3]
    var6 = {"key": "value"}
    var7 = (1, 2.72)
    var8 = {1,2,3,4}

    all_vars = [var1, var2, var3, var4, var5, var6, var7, var8]

    print('[', end='')
    for i in range(len(all_vars)-1):
        print(type(all_vars[i]).__name__,  end=', ')
    print(type(all_vars[-1]).__name__, ']', sep='')


if __name__ == '__main__':
   data_types()
