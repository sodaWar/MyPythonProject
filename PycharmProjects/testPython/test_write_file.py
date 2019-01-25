#-*- coding:utf-8 -*-
t_w = "../../test_file/test_write.txt"
with open(t_w,"w") as tw:
    a = "2332asadwqkkj kjlsadj  lkasjdlaks sda\n"
    b = "11jklew\n"
    c = "1阿达电风扇阿萨德absa12"
    tw.write(a)
    tw.write(b)
    tw.write(c)
with open(t_w,"a") as tw:
    tw.write("Hello")
with open(t_w,"r") as tw:
    print(tw.read())