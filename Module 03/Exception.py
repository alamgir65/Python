# akta code a error cheak korar jonno ata use kora hoi, if error does then except is executed otherwise no
try:
    result = 45/0
except:
    print("Error Does")
finally:
    print("Finally I am here")

print("Done it")