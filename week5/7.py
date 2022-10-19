#Create a short dictionary: e.g Finnish to English.
#Add some wordpairs to a list.

english=['sponge','Santa','Claus','computer','airplane',
		'huutokauppa','dragon','railway','world','sandwich','raccoon']
finnish=['pesusieni','joulupukki','tietokone','lentokone','auction',
		'lohikaarme','rautatie','maailma','voileipa','pesukarhu']
d=dict(zip(english,finnish))
print(d)

d['tissue']='nenaliina'
print(d)
print(d['sponge'])

