import distance

def sec2time(t):
    int_m = int(t/600)
    float_s = format(((t - ( int_m * 600 )) / 10), '.1f')
    time_str = str(int_m) + " : " + str(float_s)
    return time_str

input_file = open('output.txt', 'r', encoding='utf-8')
output_file = open('final.txt', 'w', encoding='utf-8')
lines = input_file.readlines()
input_file.close()

num = ['0','1','2','3','4','5','6','7','8','9',' ','\n'] # the words can't have nums

left_block = [""]
right_block = [""]
line_cnt = 0
line_cnt_last = 0
left_last = ""
right_last = ""
for line in lines:
    line_cnt += 1
    content = line.split('&') # spilt it into two part
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
        output_file.write("台 : " + left_most + "，國 : " + right_most + "，時間 : " + sec2time(line_cnt_last) + " ~ " + sec2time(line_cnt) + '\n')
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

    
    
 