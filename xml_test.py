from lxml import etree
tree=etree.parse("/home/shubham/Documents/GENIA_term_3.02/GENIAcorpus3.02.xml")
all_recipes=tree.xpath('./recipebook/recipe')
recipe_names=[x.xpath('recipe_name/text()') for x in all_recipes]
ingredients=[x.getparent().xpath('../ingredient_list/ingredients') for x in recipe_names]
ingredient_names=[x.xpath('ingredient_name/text()') for x in ingredients]

for item in ingredient_names:
	print item