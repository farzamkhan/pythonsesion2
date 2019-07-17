s = "lorem ipsum is simply dummy text of the printing and typesetting industry. Lorem ipsum \nhas been the industry's standard dummy text ever since the 1500s. when an unknown\nprinter took a gallery of type and scrambled it to make a type specimen book."

text_len = len(s)
print ("text len is:", text_len)
print (s.upper())
print ("printing Location is:", s.find("printing"))
new_s = s.replace("printing", "publishing")
print(new_s)
s2 = "It has survived not only five centuries, but also the leap into electronic typesetting,\nremaining essentially unchanged"
new = s + "\n" + s2
print(new)
