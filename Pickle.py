import pickle
s = "Hola mundo".title()
with open("s.pkl", "wb") as f:
    pickle.dump(s, f)
with open("s.pkl", "rb") as f:
    s2 = pickle.load(f).lower()
with open("s2.pkl", "wb") as f:
    pickle.dump(s2,f)
print(s2)