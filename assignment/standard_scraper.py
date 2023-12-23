#%%
from bs4 import BeautifulSoup
import requests

# fetch the html content of a derstandard.at page
def get_standard_soup(link):
    response = requests.get(link, cookies={'DSGVO_ZUSAGE_V1': 'true'})
    return BeautifulSoup(response.content, 'html.parser')

# generate a dictionary of articles with title as key and the bs4 element as value
def generate_articles_dict(soup):
    articles_dict = {}
    articles = soup.select('div.chronological>section article')
    for article in articles:
        title_tag = article.find('a')
        if title_tag and title_tag.has_attr('title'):
            title = title_tag['title']
            articles_dict[title] = article
    return articles_dict

#%%
# Generate the articles dictionary for an arbitrary frontpage
soup = get_standard_soup('https://www.derstandard.at/frontpage/2023/12/19')
articles_dict = generate_articles_dict(soup)
print(f'We have fetched {len(articles_dict)} articles')
print('Example for an article that we have fetched:')
print(articles_dict['Hat die Gen Z Angst davor, im Restaurant eine Bestellung aufzugeben?'])

# %%
# Function to analyze attributes of specified tags and their attributes
def analyze_tag_attributes(articles_dict):
    no_data_type = set()
    no_story_label = set()

    for title, article in articles_dict.items():
        # Check if every article (tag) has a data-type attribute
        if not article.has_attr('data-type'):
            no_data_type.add(title)
        # search for <div class="storylabels"> in articles
        if not article.find('div', class_='storylabels'):
            no_story_label.add(title)

    return no_data_type, no_story_label

no_data_type, no_story_label = analyze_tag_attributes(articles_dict)
print(f'Number of articles without data-type attribute: {len(no_data_type)}')
print(f'Number of articles without storylabels: {len(no_story_label)}')
# get articles that have a story label
has_label = set(articles_dict.keys()).difference(no_story_label)
print(f'Number of articles with story attribute: {len(has_label)}')

# a lot of articles do not have a story label, maybe an interesting goal for machine learning

# %%
# example of an article without story label
print(f'No storylabel:\n{articles_dict[list(no_story_label)[0]]}\n')
print(80*'-')

# articles with story label 
print(f'With storylabel:\n{articles_dict[list(has_label)[0]]}')

# we will analyze the labels later in more detail
# %%
# Function to extract specific data from each article
def extract_article_data(articles_dict):
    HOST = 'https://www.derstandard.at'
    article_data = []
    
    for title, article in articles_dict.items():
        data = {
            'title': title,
            'link': None,
            'time': None,
            'teaser-kicker': None,
            'n_posts': None,
            'teaser-title': None,
            'teaser-subtitle': None,
            'storylabels': None
        }

        # most links are relative, so we need to add the host
        link = article.find('a')['href']
        if not link.startswith(HOST):
            link = HOST + link
        data['link'] = link
        
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

        article_data.append(data)

    return article_data

article_data = extract_article_data(articles_dict)
# last 5 articles, of which some have a story label
article_data[-5:]
