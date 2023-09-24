from tkinter import *
import numpy as np
import random
import math

from code_hamming import error_correction 

# creation de la matrice
matrice = []
for i in range(24):
  ligne = []
  for j in range(32):
    ligne.append(-5)
  matrice.append(ligne)

# enlever les coins non utlisees
def ajouter_vide():
  for i in range(8,16):
    for j in range(9,17):
      matrice[i][j] = -3
  for i in range(8,16):
    for j in range(24,32):
      matrice[i][j] = -3


def ajouter_orientation_timming():
  matrice[8][0] = -1
  matrice[9][0] = -2
  matrice[10][0] = -1
  matrice[11][0] = -2
  matrice[12][0] = -1
  matrice[13][0] = -2
  matrice[14][0] = -1
  matrice[15][0] = -2

  matrice[8][24] = -1
  matrice[9][24] = -2
  matrice[10][24] = -1
  matrice[11][24] = -2
  matrice[12][24] = -1
  matrice[13][24] = -2
  matrice[14][24] = -1
  matrice[15][24] = -2

  matrice[8][0] = -1
  matrice[8][1] = -2
  matrice[8][2] = -1
  matrice[8][3] = -2
  matrice[8][4] = -1
  matrice[8][5] = -2
  matrice[8][6] = -1
  matrice[8][7] = -2
  matrice[8][8] = -1
  matrice[8][25] = -2
  matrice[8][26] = -1
  matrice[8][27] = -2
  matrice[8][28] = -1
  matrice[8][29] = -2
  matrice[8][30] = -1
  matrice[8][31] = -2

  matrice[15][0] = -2
  matrice[15][1] = -1
  matrice[15][2] = -2
  matrice[15][3] = -1
  matrice[15][4] = -2
  matrice[15][5] = -1
  matrice[15][6] = -2
  matrice[15][7] = -1
  matrice[15][8] = -2
  matrice[15][25]= -1
  matrice[15][26] = -2
  matrice[15][27] = -1
  matrice[15][28] = -2
  matrice[15][29] = -1
  matrice[15][30] = -2
  matrice[15][31] = -1

def separateurs():
  for i in range(9,15):
    for j in range(1,9):
      matrice[i][j] = 4



def tracerMatrice(ctx):
  for i in range(24):
    for j in range(32):
      if matrice[i][j] == 1 :
        couleur = "#%06x" % random.randint(0, 0xFFFFFF)
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill=couleur)
      elif matrice[i][j] == 0 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#FFFFFF")
      elif matrice[i][j] == -5 :
         ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#949494")
      if matrice[i][j] == -1 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#FFFFFF")
      elif matrice[i][j] == -2 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#000000")
      elif matrice[i][j] == 3 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#00FF00")
      elif matrice[i][j] == 4 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#FF0000")
      
      elif matrice[i][j] == -3 :
        ctx.create_rectangle(i*10, j*10, (i+1)*10, (j+1)*10, fill="#949494")


def add_message():
  phrase = input("Saisir la phrase :")
  phrase_array = list(phrase)
  byte_list=  []
  for i in phrase_array:
    print(i)
    byte_list.append('{0:06b}'.format(ord(i)))

  # byte_array = bytearray(phrase, "utf8")

  # for byte in byte_array :
  #   binary_rep = bin(byte)
  #   byte_list.append(binary_rep)
  
  return ''.join(byte_list)

def remplir_matrice(mes):
  index = 0
  for i in range(24):
    for j in range(32):
      if (matrice[i][j] == -5) and index < len(list(mes)):
        # print(mes[index])
        matrice[i][j] = int(mes[index])
        index += 1


def main():
  message = add_message()
  message_corriger = error_correction(message)
  print(message)
  if len(message_corriger) > 570 :
    print("taille tres grande !!!!")
  else :
    root = Tk()
    ctx = Canvas(width=400, height= 400, bg="#949494")

    # add_content(x)
    ajouter_vide()
    ajouter_orientation_timming()
    separateurs()
    remplir_matrice(message)

    tracerMatrice(ctx)

    ctx.pack(fill=BOTH, expand= 1)
    root.mainloop()



if __name__ == "__main__" :
  main()