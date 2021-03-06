
#r+
"""
with open("files1.txt","r+", encoding="utf-8") as file:     #cursordan itibaren günceller, içeriği yazılan harcidinde değiştirmez.
    file.seek(20)
    file.write("deneme")

with open("files1.txt", encoding="utf-8") as file:      #dosyayı okur
    print(file.read())
"""


#append
"""
with open("files1.txt","a", encoding="utf-8") as file:     #dosyanın sonundan itibaren günceller
    file.write("\nAhmet Yılmaz")
    

with open("files1.txt", encoding="utf-8") as file:
    print(file.read())   
"""



# ****************** Sayfa başında güncelleme *************************
"""
with open("files1.txt","r+", encoding="utf-8") as file:     
    content = file.read()
    content = "Efe Turan\n"+content
    file.seek(0)
    print(content)
    file.write(content)
"""


# ****************** Sayfa başında güncelleme *************************
with open("files1.txt","r+", encoding="utf-8") as file:     
    list = file.readlines()
    list.insert(2,"Mehmet Korkmaz\n")
    file.seek(0)
    file.writelines(list)
#    for i in list:      #dosyaya için, VEYA yukaridaki gibi    "file.writelines(list)"     yazarak.   
#        file.write(i)