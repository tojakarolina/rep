shopping_list = {"piekarnia":["chleb", "bułki", "pączki"],
"warzywniak":["marchew","seler", "rukola"]}

shops = list(shopping_list.keys())
products = list(shopping_list.values())
warzywniak_products = products[0]
piekarnia_products = products[1]
for a in range(len(warzywniak_products)):
        warzywniak_products[a] = warzywniak_products[a].capitalize()
        piekarnia_products[a] = piekarnia_products[a].capitalize()
products[0] = warzywniak_products
products[1] = piekarnia_products
        
print("Lista zakupów")
for i in range(len(shops)):
        print( f"Idę do {shops[i].capitalize()}, kupuję tu następujące rzeczy: {products[i]}.")

product = []
for x in range(len(products)):
        product += products[x]
print(f"W sumie kupuję {len(product)} produktów.")
