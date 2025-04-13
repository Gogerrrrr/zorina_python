#В магазинах имеются следующие товары.
#Магнит - молоко, соль, сахар. Пятерочка - мясо, молоко, сыр. Перекресток - молоко, творог, сыр, сахар.Определить:
#1.полный список всех товаров.
#2.в каких магазинах можно приобрести одновременно молоко и сыр.
#3.в каких магазинах можно приобрести сахар.
magazini = {"Магнит": {"молоко", "соль", "сахар"}, "Пятёрочка": {"Мясо", "молоко", "сыр"},"Перекрёсток": {"молоко", "творог", "сыр", "сахар"}}
all_products = set()
for products in magazini.values():
    all_products.update(products)
print("полный список товаров", all_products)
milk_and_cheese = [magazini for magazini, all_products in magazini.items() if "молоко" in all_products and "сыр" in all_products]
print("Магаизны, в которых есть молоко и сыр", milk_and_cheese)
sugar = [magazini for magazini, all_products in magazini.items() if "сахар" in all_products]
print("Магазины, в котором есть сахар:", sugar)