import urllib, sys, os

curr_dir = ''
# input_file = curr_dir + "/temp_input.txt"
# output_file1 = curr_dir + "/temp_output1.txt"
# output_file2 = curr_dir + "/temp_output2.txt"
# output_file3 = curr_dir + "/temp_output3.txt"

def over_lapped_string_length(s1, s2):
    t = []
    if len(s1) > len(s2):
        s1 = s1[len(s1) - len(s2):]

    t = compute_back_track_table(s2)
    if t is not None:
        m = 0
        i = 0
        while m + i < len(s1):
            if s2[i] is s1[m + i]:
                i += 1
            else:
                m += i - t[i]
                if i > 0:
                    i = t[i]
        return i
    else:
        return False


def compute_back_track_table(s):
    t = []
    cnd = 0
    t.insert(0, -1)
    t.insert(1, 0)
    pos = 2
    while pos < len(s):
        if s[pos - 1] is s[cnd]:
            t.insert(pos, cnd+1)
            pos += 1
            cnd += 1
        elif cnd > 0:
            cnd = t[cnd]
        else:
            t.insert(pos,0)
            # t[pos] = 0
            pos += 1
    return t


def parse_text(here):
    print "Parse text"
    fi = open(here + "/temp_input.txt", "r")
    fo = open(here + "/temp_output1.txt", "w+")
    # print fi.read().replace('\n', '+')
    lines = fi.readlines()

    for line in lines:
        fo.write(urllib.unquote_plus(line.replace('\n', '###')))
    fi.close()
    fo.close()


    ###########################Step 2#################################
    fi = open(here + "/temp_output1.txt", "r")
    fo = open(here + "/temp_output2.txt", "w+")
    lines = fi.readlines()
    for line in lines:
        # print line
        templine = line
        # if templine.isspace():
        #     print "Ankit" + templine
        # else:
        while "###" in templine:
            str = templine.split("###", 1)
            if len(str) > 1:
                    n = over_lapped_string_length(str[0], str[1])
                    if n > 2 or str[1] is '':
                        # print str[1][n:]
                        templine = str[0] + str[1][n:]
                        # print str[0] + str[1][n:]
                    else:
                        templine = ''
        fo.write(templine)
    fi.close()
    fo.close()

    ###########################Step 3#################################
    fi = open(here + "/temp_output2.txt", "r")
    fo = open(here + "/temp_output3.txt", "w+")
    lines = fi.readlines()
    oldline = ''
    for line in lines:
        if oldline is line:
            fo.write('')
        else:
            fo.write(line)
        oldline = line
    fi.close()
    fo.close()
    print "Ankit"
    return


def rest_api(here):
    fi = open(here + "/temp_rest_input.txt", "r")
    fo = open(here + "/temp_input.txt", "w+")
    lines = fi.readlines()
    for line in lines:
        fo.write(line.replace('\r', ''))
    fi.close()
    fo.close()


def genome(here):
    # curr_dir = here
    if len(sys.argv) is not 1:
        input_file = sys.argv[1]
        print input_file
        if sys.argv[1] == 'run':
            print sys.argv[1]
            rest_api(here)
        else:
            fi = open(input_file, "r")
            fo = open(here + "/temp_input.txt", "w+")
            lines = fi.readlines()
            for line in lines:
                fo.write(line)
            fi.close()
            fo.close()
    elif sys.stdin.isatty():
        print "STDIN"
        print here
        fo = open(here + "/temp_input.txt", "w+")
        for line in sys.stdin:
            fo.write(line)
        fo.close()
    else:
        rest_api(here)
    parse_text(here)

if __name__ == "__main__":
    genome(os.getcwd())

