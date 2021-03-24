lol = '\n<html>\n\n<body>\n    <h2> hey </h2>\n    <img alt="All the features needed to add content to your blog"\n        src="2sadsadasdsd02.png">\n    <p> lol </p>\n    <img alt="All the features needed to add content to your blog"\n        src="Images/FrontPage2017/SectionImages/image%20section%202.png">\n</body>\n\n</html>\n'
imgs = lol.split("<img")

for one_img in imgs:

    img_src_loc = one_img.find("src")
    first_quote = one_img[img_src_loc:-1].find("\"")
    last_quote = one_img[img_src_loc:-1][first_quote+1:-1].find("\"")
    print(one_img[img_src_loc:-1][first_quote+1:last_quote+first_quote+1])