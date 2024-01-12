text = open(file='sentences.txt', mode='a')

len_text = 1

while len_text != 0:
    input_line = input('Введіть речення ->>> ')
    len_text = len(input_line)
    text.writelines(input_line + '\n')
    
text.close()