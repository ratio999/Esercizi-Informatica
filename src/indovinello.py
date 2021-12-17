print("Indovinello per Dementi")
print("Benvenuta/o all'indovinello per VERI dementi")
print("Rispondi alla seguente domanda:")
print("Asciuga bagnandosi. Cos'è? (quit se non ti piace questo gioco)")
test=True
while test:
 guess=input()
 if guess=="asciugamano":
  print("e la risposta esatta è...")
  print("*suspence*")
  guess=guess+"!"
  for x in guess:
   print(x) 
  test=False
 elif guess=="quit":
  test=False
 else:
  print("Non ci siamo...")
else:
 print("Grazie per aver giocato")
