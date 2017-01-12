k = open("bookinfolist.txt", "rt", encoding = "utf-8")
allthebooks = k.read()
k.close()
cleanedbooks = []
allbooks = allthebooks.split("\n")
allcleanedbooks = allbooks.remove(allbooks[0])
for book in allbooks:
	bookinfo = book.split("',")
	cleanedbookinfo = []
	for info in bookinfo:
		info = str(info)
		dob = info.replace( r"\ufeff", "")
		dab = dob.replace( r"'", "")
		dib = dab.replace( r"[", "")
		deb = dib.replace( r"]", "")
		cleanedbookinfo.append(deb)
	cleanedbooks.append(cleanedbookinfo)
mostgothicbooks = []
for book in cleanedbooks:
	bookpercentage = book[-1]
	nospace = bookpercentage.replace(" ", "")
	percentagefloat = float(nospace)
	if percentagefloat > 100.00000000000001:
		mostgothicbooks.append(book)
mostgothicbooktexts = []
for book in mostgothicbooktexts:
	


		





