shopping_list = {"piekarnia": ["chleb", "bułki", "pączki"],
"warzywniak": ["marchew", "seler", "rukola"]}

shops = list(shopping_list.keys())
products = list(shopping_list.values())

warzywniak_products = products[0]
piekarnia_products = products[1]

print('Lista zakupów')

for a in range(len(warzywniak_products)):
        warzywniak_products[a] = warzywniak_products[a].capitalize()
        piekarnia_products[a] = piekarnia_products[a].capitalize()
products[0] = warzywniak_products
products[1] = piekarnia_products

for i in range(len(shops)):
        print(f"Idę do {shops[i].capitalize()}, kupuję tu następujące rzeczy: {products[i]}.")

