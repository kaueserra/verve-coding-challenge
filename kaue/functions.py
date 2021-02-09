def read_data(path):

    #create a function to read the data

    #open the file
    file_r = open(path, "r")

    #create empty list
    list_data = []
    for line in file_r:
        #splitting by line and putting into integer form
        list_data.extend([int(x) for x in line.split()])

    file_r.close()

    return list_data

def sum_2_2020(dataset):

    #empty list
    ans = []

    x = dataset

    set_x =set()
    #iterate for each element of the array
    for i in range(len(x) - 1):

        # if there is the number (2020 - the ith elemente) append the multiplication of the pair
        if (2020 - x[i]) in set_x:

            ans.append(x[i] * (2020 - x[i]))

            print(" The numbers are {}, {}".format(x[i], (2020 - x[i])))

            print(" And their multiplier is {}".format(x[i]*(2020 - x[i])))

            print("--" * 20)

        set_x.add(x[i])

    # if there is no pair print it
    return ans if len(ans) > 0 else print('no 2 numbers sum 2020')


def sum_3_2020(dataset):

    #following the same logic as before
    ans = []

    x = dataset

    for i in range(len(x) - 1):
        # but now let's iterate 1 extra time and use hashing with the second iteration to not repeat
        # As if I don't do that the trio can reappear with a different order but same index
        set_x = set()
        for j in range(i + 1, len(x)):
            if (2020 - (x[i] + x[j])) in set_x:
                ans.append(x[i] * x[j] * (2020 - (x[i] + x[j])))
                print(" The numbers are {}, {}, {}".format(x[i],x[j],(2020-x[i]-x[j])))
                print(" And their multiplier is {}".format(x[i] * (2020 - x[i] -x[j])*x[j]))
                print("--"*20)

                #adding to the hashing
            set_x.add(x[j])

    return ans if len(ans) > 0 else print('no 3 numbers sum 2020')

