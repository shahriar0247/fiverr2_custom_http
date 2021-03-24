lol = '\n<html>\n\n<body>\n    <h2> hey </h2>\n    <img alt="All the features needed to add content to your blog"\n        src="Images/FrontPage2sadsadsds017/SectionImages/image%20section%202.png">\n    <p> lol </p>\n    <img alt="All the features needed to add content to your blog"\n        src="Images/FrontPage2017/SectionImages/image%20section%202.png">\n</body>\n\n</html>\n'
lol = lol.replace("\n"," ")
img_loc = lol.find("<img") 
img_src_loc = lol[img_loc:-1].find("src")
first_quote = lol[img_loc:-1][img_src_loc:-1].find("\"")
last_quote = lol[img_loc:-1][img_src_loc:-1][first_quote+1:-1].find("\"")
print(lol[img_loc:-1][img_src_loc:-1][first_quote+1:last_quote+first_quote+1])