import distance

def sec2time(t):
    int_m = int(t/600)
    int_h = int(int_m/60)
    int_m = int_m - int_h * 60
    f = (t - ( int_m * 600 )) % 10
    # float_s = format(((t - ( int_m * 600 )) / 10), '.3f')
    int_s = int((t - ( int_m * 600 )) / 10)
    time_str = str(int_h).zfill(2) + ":" + str(int_m).zfill(2) + " : " + str(int_s).zfill(2) + "," + str(f * 100)
    return time_str

input_file = open('output.txt', 'r', encoding='utf-8')
output_file = open('srt_ver1.txt', 'w', encoding='utf-8')
lines = input_file.readlines()
input_file.close()

num = ['0','1','2','3','4','5','6','7','8','9',' ','\n','`','.','!',',','_'] # the words can't have nums

subtitle_cnt = 1
left_block = [""]
right_block = [""]
line_cnt = 0
line_cnt_last = 0
left_last = ""
right_last = ""
for line in lines:
    line_cnt += 1
    illegal = line.find('#')
    if(illegal == -1):
        regular = line
    elif(illegal == 0):
        regular = ""
    else:
        regular = line[0 : illegal - 1]
    content = regular.split('&') # spilt it into two part
    if(len(content) > 3): # there are more than two parts
        print("noise error: ",line_cnt)
        continue
    elif(len(content) == 2 ):  # there just one part
        content[1] = content[0]
    elif(len(content) == 1): # there is no content
        content[0] = ""
        content.append("")
    left_now = content[0]
    right_now = content[1]

    for i in num:
        left_now = left_now.replace(i,'')
        right_now = right_now.replace(i,'')
    dis_left = distance.levenshtein(left_now,left_last)
    dis_right = distance.levenshtein(right_now,right_last)
    if(dis_left >= 2 and dis_right >= 2):
        left_most = max(set(left_block), key=left_block.count)
        right_most = max(set(right_block), key=right_block.count)
        if(left_most == '' or right_most == ''):
            left_block.clear()
            right_block.clear()
            left_block.append(content[0])
            right_block.append(content[1])
            continue
        # output_file.write("台 : " + left_most + "，國 : " + right_most + "，時間 : " + sec2time(line_cnt_last) + " ~ " + sec2time(line_cnt) + '\n')
        output_file.write(str(subtitle_cnt) + '\n')
        output_file.write(sec2time(line_cnt_last) + " --> " + sec2time(line_cnt) + '\n')
        output_file.write(left_most + '\n' + right_most + '\n\n')
        subtitle_cnt += 1
        line_cnt_last = line_cnt
        left_block.clear()
        right_block.clear()
        left_block.append(content[0])
        right_block.append(content[1])
    else:
        left_block.append(content[0])
        right_block.append(content[1])
    left_last = left_now
    right_last = right_now

    
    
 