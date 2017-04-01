import pandas as pd
import sys

file_name = sys.argv[1]

df = pd.read_csv(file_name)


def fix_coordinates(coordinates_string):
    if type(coordinates_string) != str:
        res = coordinates_string
    else:
        splitted = split_coordinates(coordinates_string)
        pre = join_coordinates(splitted)
        res = "MULTIPOLYGON((( " + pre + ")))"
    return(res)

def split_coordinates(coordinates):
    coord_parsed = coordinates.split(",")
    splitted = [coord.split(" ") for coord in coord_parsed]
    return([item for sublist in splitted for item in sublist])

def join_coordinates(coordinates_list):
    l = []
    for i in range(0,len(coordinates_list)-1, 2):
        if i > len(coordinates_list):
            break
        coords = coordinates_list[i] + " " + coordinates_list[i+1]
        l.append(coords[:-1])
    return(",".join(l))

df["poligono_fix"] = map(lambda x: fix_coordinates(x), df.poligono)
file_out = sys.argv[2]
df.to_csv(file_out, index = False)