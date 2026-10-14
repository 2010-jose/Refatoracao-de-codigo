TAX_RATE = 0.2  # Taxa de imposto

def Tax(Price): return Price * TAX_RATE  # Função para cálculo de impostos

def sum_prices(a,b,c,d): return a+b+c+d  # Uma função para resumir preços, que soma todos os preços fornecidos

total = sum_prices(100,200,300,400)
tax = Tax(total)
FinalPrice = total+tax
print ("Final price is", FinalPrice)  # Apresentando o preço final