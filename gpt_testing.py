import scipy.stats as stats

gpt_3_pelis = (6,8,4,9,8,8,6,6,5,6)
gpt_4_pelis = (8,4,6,9,7,9,7,6,10,9)

gpt_3_libros = (6,2,7,7,6,6,2,8,8,7)
gpt_4_libros = (8,3,7,10,9,8,5,8,9,8)

gpt_3_personas = (8,9,8,3,7,8,8,8,5,6)
gpt_4_personas = (6,9,9,6,7,9,8,10,9,8)

gpt_3_noticias = (7,6,5,9,8,8,5,9,9,9)
gpt_4_noticias = (10,8,8,6,7,7,8,8,6,10)

gpt_3_total = (6,8,4,9,8,8,6,6,5,6,6,2,7,7,6,6,2,8,8,7,8,9,8,3,7,8,8,8,5,6,7,6,5,9,8,8,5,9,9,9)
gpt_4_total = (8,4,6,9,7,9,7,6,10,9,8,3,7,10,9,8,5,8,9,8,6,9,9,6,7,9,8,10,9,8,10,8,8,6,7,7,8,8,6,10)

gpt3_ls = [gpt_3_pelis,gpt_3_libros,gpt_3_personas,gpt_3_noticias,gpt_3_total]
gpt4_ls = [gpt_4_pelis,gpt_4_libros,gpt_4_personas,gpt_4_noticias,gpt_4_total]

clases_ls =['Peliculas', 'Libros', 'Personas', 'Noticias', 'GPT-3.5 vs GPT-4.0 Global']

for gpt_3, gpt_4, clase in zip(gpt3_ls,gpt4_ls,clases_ls):

    resultados = stats.ttest_rel(a=gpt_3, b=gpt_4)

    significativa = "es significativa" if resultados.pvalue < 0.05 else "no es significativa"

    print(f"\n {clase}\n El pvalor de la prueba da {resultados.pvalue} por lo que la diferencia {significativa}\n")
