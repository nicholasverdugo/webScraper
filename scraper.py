import requests, json
from bs4 import BeautifulSoup

# GET HTML content from a URL
URL = "https://www.antibodies-online.com/antibody/669606/anti-Protein+tyrosine+Phosphatase,+Receptor+Type,+C+PTPRC+AA+1210-1304+antibody/"
page = requests.get(URL)

# Make soup 
soup = BeautifulSoup(page.content, 'html.parser')

# Extract Isotype
prodDetail = soup.find("dl", id='productDetailsproduct_detail')
data = prodDetail.text
idx_Isotype = data.find('Isotype')
iso = data[idx_Isotype+8:].strip()

# Extract JSON from HTML
json_unformatted = soup.find(type='application/ld+json')
json_text = json_unformatted.text[44:-1]

# Store indices on where to cut the JSON
start = json_text.find('"additionalProperty":')
end = json_text.find('"subjectOf":')

# Slice according to desired data and format for conversion to dictionary
json_full = ('{' + json_text[start:end-1] + '}').replace('\'', '"')

# Convert to list of dictionaries
data = json.loads(json_full)
d = {}

d['Isotype'] = iso

# Create dictionary of categories and values
for cat in data['additionalProperty']:
    d[cat['name']] = cat['value']
    
# Print dictionary
print('Target: ' + d['Target'])
print('Reactivity: ' + d['Reactivity'])
print('Conjugate: ' + d['Conjugate'])
print('Isotype: ' + d['Isotype'])