with open('./read/text.txt', "r") as t :
  textfile = t.readline()
  while textfile :
    print(textfile)
    textfile = t.readline()