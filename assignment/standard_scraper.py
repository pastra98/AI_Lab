#%%
from bs4 import BeautifulSoup
from collections import defaultdict
import requests


#%%
def get_standard_soup(link):
    response = requests.get(link, cookies={'DSGVO_ZUSAGE_V1': 'true'})
    return BeautifulSoup(response.content, 'html.parser')

#%%

# Load the HTML file content
html_file_path = './standard_downloads/chronologie.htm'
with open(html_file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

soup = get_standard_soup('https://www.derstandard.at/frontpage/2023/12/19')

# Function to generate a dictionary of articles with title as key and the bs4 element as value
def generate_articles_dict(soup):
    articles_dict = {}
    articles = soup.select('div.chronological>section article')
    for article in articles:
        title_tag = article.find('a')
        if title_tag and title_tag.has_attr('title'):
            title = title_tag['title']
            articles_dict[title] = article
    return articles_dict

# Function to generate a dictionary of tags with each tag containing a list of article titles
def generate_tags_dict(articles_dict):
    tags_dict = defaultdict(list)
    for title, article in articles_dict.items():
        # Finding all tags in the article
        for tag in article.find_all(True):
            tags_dict[tag.name].append(title)
    return tags_dict

#%%
# Generate the articles dictionary
articles_dict = generate_articles_dict(soup)

# Generate the tags dictionary
tags_dict = generate_tags_dict(articles_dict)

# Displaying a sample of the tags dictionary
list(tags_dict.items())[:5]  # Display first 5 items for brevity


# %%
for key in tags_dict:
    print(f"{key}: {len(tags_dict[key])}\n")

# %%
len(articles_dict)

# %%
articles_dict['Es bleibt eine Segnung für Paare zweiter Klasse']
# %%
# Function to analyze attributes of specified tags and their attributes
def analyze_tag_attributes(articles_dict):
    analysis_result = {
        'article': {
            'class': defaultdict(list),
            'data-type': defaultdict(list)
        },
        'span': {
            'data-label-category': defaultdict(list),
            'data-label-name': defaultdict(list)
        }
    }

    for title, article in articles_dict.items():
        # Analyzing <article> tag attributes
        if 'article' in analysis_result and article.name == 'article':
            for attr in ['class', 'data-type']:
                if article.has_attr(attr):
                    analysis_result['article'][attr][' '.join(article[attr])].append(title)
                # else:
                #     print(f'Article {title} does not have attribute {attr}')

        # Analyzing <span> tag attributes within the article
        spans = article.find_all('span')
        for span in spans:
            for attr in ['data-label-category', 'data-label-name']:
                if span.has_attr(attr):
                    analysis_result['span'][attr][span[attr]].append(title)
                else:
                    print(f'Span within article {title} does not have attribute {attr}')
                    print(f"article has {len(spans)} spans")
                    print()

    return analysis_result

# Perform the analysis
tags_attributes_analysis = analyze_tag_attributes(articles_dict)

# Displaying a sample of the analysis result
{tag: {attr: list(values.keys())[:3] for attr, values in attrs.items()} for tag, attrs in tags_attributes_analysis.items()}  # Display first 3 items for brevity


# %%
# Function to search for <div class="storylabels"> in articles and print content
def search_and_print_storylabels(articles_dict):
    for title, article in articles_dict.items():
        storylabel_div = article.find('div', class_='storylabels')
        print(f"Article: {title}")
        if storylabel_div:
            print("This article has storylabels:")
            print(storylabel_div.get_text(strip=True))
        else:
            print("This article does not have labels")
        print("\n")  # Newline for separation between articles

# Call the function
search_and_print_storylabels(articles_dict)

# %%
# Function to extract specific data from each article
def extract_article_data(articles_dict):
    extracted_data = []
    
    for title, article in articles_dict.items():
        data = {
            'title': None,
            'link': article.find('a')['href'],
            'time': None,
            'teaser-kicker': None,
            'n_posts': None,
            'teaser-title': None,
            'teaser-subtitle': None,
            'storylabels': None
        }

        # for live articles, there is a second time tag with the duration of the live post
        # however, we only care about the time of publication here
        time = [tag for tag in article.find_all('time') if 'datetime' in tag.attrs][0]
        data['time'] = time['datetime'].rstrip('\r\n')

        # if there are no comments, the string is empty so set it to 0
        n_posts = article.find('div', 'teaser-postingcount').get_text(strip=True)
        try: data['n_posts'] = int(n_posts.rstrip('Posting').replace('.', ''))
        except ValueError: data['n_posts'] = 0
        

        # Extracting other specified tags
        for tag, class_name in [('p', 'teaser-kicker'), 
                                ('h1', 'teaser-title'), 
                                ('p', 'teaser-subtitle'), 
                                ('div', 'storylabels')]:
            found_tag = article.find(tag, class_=class_name)
            if found_tag:
                data[class_name] = found_tag.get_text(strip=True)

        extracted_data.append(data)
    return extracted_data

# Extract data from articles
extracted_articles_data = extract_article_data(articles_dict)

#%%
# Display a sample of the extracted data
extracted_articles_data[:3]  # Displaying first 3 articles for brevity


# %%
# list all unique teaser-kickers
set([article['teaser-kicker'] for article in extracted_articles_data])

# %%
first_article = extracted_articles_data[0]['link']

link = 'https://www.derstandard.at/story/3000000200432/dortmund-und-leipzig-zum-jahresabschluss-mit-nur-einem-punkt'
# link = 'https://www.derstandard.at/frontpage/2023/12/19'

response = requests.get(link, cookies={'DSGVO_ZUSAGE_V1': 'true'})
soup = BeautifulSoup(response.content, 'html.parser')

article_body = soup.select('div.article-body')
ps = [paragraph.get_text(strip=True) for paragraph in article_body[0].find_all('p')]
# %%
article = '\n'.join(ps)
print(article)

# %%
with open('./standard_downloads/entire_article.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')
soup.select('div.article-body')



# %%
def generate_css_path(element, path=""):
    # If this element has a tag name, add it to the path
    if element.name:
        path += f" > {element.name}"
        
        # If this element has an id, add it to the path
        if 'id' in element.attrs:
            path += f"#{element['id']}"
        
        # If this element has a class, add it to the path
        if 'class' in element.attrs:
            path += "." + ".".join(element['class'])
        
        print(path)
    
    # Recursively generate paths for all children of this element
    for child in element.children:
        if child.name:
            generate_css_path(child, path)

# Generate CSS paths for all elements in the soup object
generate_css_path(soup)

# %%