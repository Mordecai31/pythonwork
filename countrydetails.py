from countryinfo import CountryInfo
print('Welcome, You can get information about any country here!')
enter = input("Enter a country name:")
country = CountryInfo(enter)
print("The Capital of the country is :" ,  country.capital())
print("The Currency of the country is :" , country.currencies())
print("The language of the country is :" , country.languages())
print("The Borders of the country is :" , country.borders())
print("The Area of the country is :" , country.area())
print("The Time zone  of the country is :" , country.timezones())
print("The Population of the country is :" , country.population())
print("The region  of the country is :" , country.region())
print("The calling code  of the country is :" , country.calling_codes())
print("The other names of the country is :" , country.alt_spellings())


