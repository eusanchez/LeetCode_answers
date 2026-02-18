with open("data.txt", "r", encoding="utf-8") as f:
    for line in f:                # 'line' is each line in the file
        if "ERROR" in line:       # check if the text appears in this line
            print(line.strip())   # print the line (strip removes '
')