#Max Holdaway Shift Cipher

print("This is a shift cipher it encrypts messages for you.")

print("")

UnCryptedMessage = input("Please give me a message to encrypt: ")

UnCryptedMessage = [UnCryptedMessage]

print("")

a = "a"

b = "b"

c = "c"

d = "d"

e = "e"

f = "f"

g = "g"

h = "h"

i = "i"

j = "j"

k = "j"

l = "l"

m = "m"

n = "n"

o = "o"

p = "p"

q = "q"

r = "r"

s = "s"

t = "t"

u = "u"

v = "v"

w = "w"

x = "x"

y = "y"

z = "z"

def ShiftCrypting(Message, CryptedMessage, SemiCryptedMessage, CharList):
    CharList = (a.ord, b.ord, c.ord, d.ord, e.ord, f.ord, g.ord, h.ord, i.ord, j.ord, k,ord, l.ord, m.ord, n.ord, o.ord, p.ord, q.ord, r.ord, s.ord, t.ord, u.ord, v.ord, w.ord, x.ord, y.ord, z.ord)
    CryptedMessage = Message

print(ShiftCrypting(UnCryptedMessage, "", ""))