# Given the variable countries defined as:

#             Name    Capital  Populations (millions)
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the list
def country_capital(country) :
    i = 0 
    while True :
        if countries[i][0] == country :
            return countries[i][1]
        else :
            i = i+1

def test() :
    assert country_capital('China')=='Beijing'
    assert country_capital('India')=='Delhi'
    assert country_capital('Romania')=='Bucharest'
    assert country_capital('United States')=='Washington'
    print "Tests finished."

test()
print country_capital('India')