#Day 5
#Level 1

lst = []
animals = ["Cat", "Dog", "Monkey", "Elephant", "Penguin", "Snake"]
print(len(lst))
print(len(animals))

print(animals[0])
print(animals[-1])
print(animals[len(animals) // 2])

mixed_data_types = ["Konstantin", 19, 176, False, "Meow 69"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0])
print(it_companies[-1])
print(it_companies[len(it_companies) // 2])

it_companies.append("K1V")
print(it_companies)

it_companies[-1] = "IT company"
it_companies.insert(len(it_companies)//2, "NewCompany")

it_companies[-1] = "IT COMPANY"
print(it_companies)

new_it = "#".join(it_companies)

print("Google" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

del it_companies[0:3]
print(it_companies)
del it_companies[-3:]
print(it_companies)
middle_index = len(it_companies)//2
del it_companies[middle_index]

it_companies.clear()
print(it_companies)

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
it_companies.pop(0)
print(it_companies)

it_companies.pop(len(it_companies) // 2)
print(it_companies)

it_companies.remove("Amazon")
print(it_companies)

it_companies.clear()
print(it_companies)
print(it_companies.clear())

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_and_back_ends = front_end + back_end
print(front_and_back_ends)

full_stack = front_and_back_ends.copy()
more = ("Python", "SQL")
full_stack.extend(more)
print(full_stack)

#Level 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(sorted(ages))
numbers_again = [19, 26]
ages.extend(numbers_again)
print(ages)

mediana = ages[6:8]
print(sum(mediana)/2)

print(sum(ages)//len(ages))

range_ages = 26 - 19
print(range_ages)

average_age = sum(ages)/len(ages)
min_diff = abs(min(ages) - average_age)
max_diff = abs(max(ages) - average_age)

print(min_diff >= max_diff)
print(min_diff <= max_diff)
print(min_diff == max_diff)

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(countries[len(countries)//2])

first_half = countries[:len(countries)//2+1]
second_half = countries[len(countries)//2:]
print(first_half)
print(second_half)

random_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandic_countries = random_countries[3:]