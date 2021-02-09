import os
import argparse
import functions

my_parser = argparse.ArgumentParser(description='This scrips multiply the pairs or trios that sum 2020')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list, either absolut or from inside this Dir and putting the relative path')

my_parser.add_argument('Part',
                       metavar='part',
                       type=str,
                       help='is it part1 or part2 ?')

# Execute the parse_args() method
args = my_parser.parse_args()

part = args.Part

if __name__ == '__main__':

    try:
        input_path = str(os.getcwd() + str(args.Path))
        ds = functions.read_data(input_path)
    except:
        input_path = str(args.Path)
        ds = functions.read_data(input_path)


    if part == 'part1':

        saveds1 = functions.sum_2_2020(ds)

        with open('saveds1.txt', 'w') as file:
            file.writelines("%s\n" % place for place in saveds1)

    else:

        saveds2 = functions.sum_3_2020(ds)

        with open('saveds2.txt', 'w') as file:
            file.writelines("%s\n" % place for place in saveds2)