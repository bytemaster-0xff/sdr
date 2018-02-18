import sys

if len(sys.argv) != 3 :
    print ("usage: ")
    print ("rsqrwav.py [COUNT_SYNC] [COUNT_DATA]")
else :
    out_str = ''
    
    for x in range(0, int(sys.argv[1])) :
        out_str += "1,1,1,0,"

    for x in range(0, int(sys.argv[2])):
        if(x > 0) : 
            out_str += ","
            
        out_str += "1,0"

    print(out_str)
