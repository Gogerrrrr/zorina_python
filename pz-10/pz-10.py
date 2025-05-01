#В магазинах имеются следующие товары.
#Магнит - молоко, соль, сахар. Пятерочка - мясо, молоко, сыр. Перекресток - молоко, творог, сыр, сахар.Определить:
#1.полный список всех товаров.
#2.в каких магазинах можно приобрести одновременно молоко и сыр.
#3.в каких магазинах можно приобрести сахар.
magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}
perekrestok = {"молоко", "творог", "сыр", "сахар"}
print("Полный список товаров:", magnit|pyaterochka|perekrestok)

magazini_s_molokom_i_sirom = set()
if "молоко" in magnit and "сыр" in magnit:
    magazini_s_molokom_i_sirom.add("Магнит")
if "молоко" in pyaterochka and "сыр" in pyaterochka:
    magazini_s_molokom_i_sirom.add("Пятёрочка")
if "молоко" in perekrestok and "сыр" in perekrestok:
    magazini_s_molokom_i_sirom.add("Перекрёсток")
    print("Магазины с молоком и сыром:", magazini_s_molokom_i_sirom)

magazini_s_saharom = set()
if "сахар" in magnit:
    magazini_s_saharom.add("Магнит")
if "сахар" in pyaterochka:
    magazini_s_saharom.add("Пятёрочка")
if "сахар" in perekrestok:
    magazini_s_saharom.add("Перекрёсток")
    print("Магазины с сахаром:", magazini_s_saharom)
