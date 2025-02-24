# My notez
eval() -> parser, który następnie wykonuje operacje wewnątrz stringu
repr() -> tworzymy wygodna do czytania wersje danego obiektu, "dodajemy cudzysłowia" do obiektu
%s jest przestarzały, string.format() jest spoko, ostatnio pojawił się f'string {pi}'
Useful functions: upper(), lower(), index(), slice(), split(), join(), replace()

chr() i ord() to przeciwstawne funkcje
tak samo jak eval() i repr()

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
