
# Online Python - IDE, Editor, Compiler, Interpreter
print("Podaj mi tekst do szyfrowania")
#s = input()
s="Przykładowy tekst"
print(s)
s_sec=''.join([chr(ord(x)+1) for x in  s])
#s_shifted = []
#print(s_sec)
print(s_sec)
s_rev=''.join([chr(ord(x)-1) for x in  s_sec])
print(s_rev)

