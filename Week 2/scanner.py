file = open('testfile.txt')


line = file.readline()
cnt = 1
while line:
    if line[0].isdigit:
        print("Line {}: {}".format(cnt, line.strip()))
        line = file.readline()
        cnt += 1