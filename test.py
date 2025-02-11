# 讀取文件
with open('input.txt', 'r') as file:
    content = file.read()
    print("文件內容：", content)
 
# 寫入文件
with open('output.txt', 'w') as file:
    file.write("這是寫入的新內容。")
    print("內容已寫入output.txt")s123456