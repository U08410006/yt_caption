import distance

input_file = open('output.txt', 'r', encoding='utf-8')
output_file = open('cut_point.txt', 'w', encoding='utf-8')
lines = input_file.readlines()
input_file.close()

num = ['0','1','2','3','4','5','6','7','8','9',' ','\n'] # the words can't have nums

line_cnt = 0
left_last = ""
right_last = ""
for line in lines:
    line_cnt += 1
    content = line.split('&') # spilt into two part
    if(len(content) > 3): # there have more than two parts
        print("noise error: ",line_cnt)
        continue
    elif(len(content) == 2 ):  # there just one part
        content[1] = content[0]
    elif(len(content) == 1): # there have no content
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
        output_file.write(str(line_cnt) + '\n')
    
    left_last = left_now
    right_last = right_now

    
    
 