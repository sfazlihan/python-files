with open("files1.txt",encoding="utf-8") as file:   # with, dosya.close() yapmaya gerek bırakmaz.
    content1=file.read()
    print(content1)
    file.seek(0)    # cursoru başa alır.
    print(file.tell())  # cursorun bulunduğu byte konumunu gösterir.
    content2=file.read(25)  # cursorun bulunduğu konumdan itibaren 25byte okur.
    print(content2)