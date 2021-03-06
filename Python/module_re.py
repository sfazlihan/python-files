import re

#-----------------re module--------------------

str="Python Kursu: Python Programlama Rehberiniz | 44 saat"

# #re.findall()   #string içinde arar ve listede tutar.
# result=re.findall("Python",str)


# #re.split()     #stringleri ayırır.
# result=re.split(" ",str)


# #re.sub()   #ilk parametredekini ikinci parametre ile değiştirir. 3.parametre içinde olur.
# result=re.sub(" ","/",str)


#re.search()    #str içinde arar. <re.Match object; span=(0, 6), match='Python'> sonucunu verir. Yani 0-6 arasındaymış.
result=re.search("Python",str)
# result=result.span()        #(0, 6) sonucunu direk verir.
# result=result.start()       #.span ifadesinin başını verir
# result=result.end()         #.span ifadesinin sonunu verir
# result=result.group()       #.search() moduluile ne aradığımızı gösterir
# result=result.string        #"arattığımız stringin içinde ne var?"




#-----------------------regular expression---------------------------
"""
    [] köşeki parantez içine yazılan her karakterler aranır.

        [abc] =>  a       : 1 sonuç
                ab      : 2 sonuç
                abc     : 3 sonuç
                Python  : sonuç yok


        [a-e]   =>   [abcde]
        [1-5]   =>   [12345]
        [0-39]  =>   [01239]

        [^abc]  => abc dışındaki bütün karakterler
        [^0-9]  => rakam olmayan bütün karakterler
    
"""
result=re.findall('[abc]',str)
result=re.findall('[sat]',str)
result=re.findall('[a-e]',str)
result=re.findall('[a-z]',str)
result=re.findall('[A-Z]',str)
result=re.findall('[0-5]',str)
result=re.findall('[^a-e]',str)
result=re.findall('[^0-9]',str)


"""
    . - Her hangi bir karakteri belirtir.
        .. => a      : sonuç yok
              ab     : 1 sonuç
              abc    : 1 sonuç
              abcd   : 2 sonuç
"""
result=re.findall("..",str)
result=re.findall("...",str)
result=re.findall("Py..on",str)


"""
    ^ - "belirtilen string karakteriyle başlıyormu?"
        ^a => a    : 1 sonuç
              abc  : 1 sonuç
              bca  : sonuç yok
"""
result=re.findall("^a",str)
result=re.findall("^P",str)


"""
        $ - "Belirtilen karakterle bitiyormu?"
            a$ => a      : 1 sonuç        
            a$ => lamba  : 1 sonuç        
            a$ => Python : sonuç yok        
"""
result=re.findall("t$",str)
result=re.findall("y$",str)


"""
        * - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
        ma*n => mn      : 1 sonuç
                man     : 1 sonuç
                maaan   : 1 sonuç
                main    : 1 sonuç   (sonuç yok çünkü a nın arkasına n gelmiyor.)
"""
result=re.findall("sa*t",str)


"""
        + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.
                ma+n => mn      : sonuç yok
                        man     : 1 sonuç
                        maaan   : 1 sonuç
                        main    : sonuç yok       (sonuç yok çünkü a nın arkasına n gelmiyor.)
"""
result=re.findall("sa*t",str)


"""
        ? - Bir karakterin sıfır ya da bir kez olmasını kontrol eder.
                ma+n => mn      : sonuç yok
                        man     : 1 sonuç
                        maaan   : 1 sonuç
                        main    : sonuç yok (a nın arkasına n gelmiyor.)
"""
result=re.findall("sa?t",str)



"""
        {} - karakter sayısını kontrol eder.
                al{2} =>   a karakterinin arkasına, l karakteri 2 kez tekrar etmeli.
                al{2,3}  =>   a karakterinin arkasına, l karakteri en az 2, en çok 3 kez tekrar etmeli.
                [0-9]{2,4} => en az 2, en çok 4 basamaklı sayılar.
"""
result=re.findall("a{2}",str)
result=re.findall("a{2,3}",str)
result=re.findall("[0-9]{2,3}",str)



"""
        | - alternatif seçeneklerden birinin gerçekleşmesini sağlar.
                a|b => a yada b
                        cde => sonuç yok
                        ace => 1 sonuç
                        abuea => 3 sonuç
"""
result=re.findall("p|P",str)


"""
() - gruplamak için kullanılır.
        (a,b,c)xz => a,b,c karakterlerinin arkasına xz karakterleri gelmelidir.
"""
result=re.findall("(P,y,t)hon",str)




"""
        \ - özel karakterleri aramanızı sağlar.
                \$a => $ karakterinin arkasına a karakterini arar. Yani $ regular exp. engine tarafından yorumlanmaz.



        \A - Belirtilen karakter, stringin başındamı?
        \Athe => the, stringin başındamı



        \Z - Belirtilen karakter, stringin sonundamı?
        the\Z => the, stringin sonundamı


        \b - Belirtilen karakter, kelimenin başında veya sonundamı?
        \bthe => the, kelimenin başındamı
        the\b => the, kelimenin sonundamı


        \B - Belirtilen karakter, kelimenin başında veya sonundamı?
        \Bthe => the, kelimenin başında değil mi
        the\B => the, kelimenin sonunda değil mi


        \d - [0-9] ile aynı anlama gelir yani rakamları arar.
        \d => 12abc97


        \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
        \D => 464asfa46_46


        \s - Boşluk karakterini arar.
        \S - Boşluk karakteri dışındakiler.
        \w - Alfabetik karakterler, rakamlar ve alt çizgi karakterleri.
        \W - \w'nin tam tersi.
"""
print(result)