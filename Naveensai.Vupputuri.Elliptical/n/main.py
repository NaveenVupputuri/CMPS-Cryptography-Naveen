

import argparse
import sys
import assign3 as sd

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-x1", "--x1", default = "X1 input",type =float, help="X1 value")
    parser.add_argument("-y1", "--y1", default = "Y1 input",type =float,help="Y1 value")
    parser.add_argument("-x2", "--x2", default = "X2 input",type =float,help="X2 value")
    parser.add_argument("-y2", "--y2", default = "Y2 input", type =float,help="Y2 value")
    parser.add_argument("-a", "--a", default = "a value",type =float, help="a value")
    parser.add_argument("-b", "--b", default = "b value",type =float, help="b value")
   

    args = parser.parse_args()
#==============================================================================
#     x1 = float(args.X1)
#     y1 = float(args.Y1)
#     x2 = float(args.X2)
#     y2 = float(args.Y2)
#     a = float(args.a)
#     b = float(args.b)
#==============================================================================
    sd.assignment3(args.x1,args.y1,args.x2,args.y2,args.a,args.b)
   

if __name__ == '__main__':
    main()