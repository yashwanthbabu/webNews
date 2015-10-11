import re
import requests
from BeautifulSoup import BeautifulSoup


# make a single request to the homepage
def split_anchor_tag(link):
    """
    This will give us the anchor tag url and text
    """
    a_url = re.findall(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(link))
    a_text = link.text
    return (a_url, a_text)


def split_anchor_tag_without_domain_name(link):
    """
    This will split without domain name anchor tag
    """
    a_url, a_text = None, None
    a_url = re.findall('<a href="?\'?([^"\'>]*)', str(link))
    if link:
        a_text = link.text
    return (a_url, a_text)


def ndtv_page():
    """
    We get the ndtv india-news page and reading the headlines.
    """
    story_list = []
    a_url, outer_header, a_text, story, header_link = None, None, None, None, None
    html_page = requests.get("http://www.ndtv.com/india-news?pfrom=home-topnavigation2015")
    # convert the plaintext HTML markup into a DOM-like structure that we can search
    soup = BeautifulSoup(html_page.text)
    all_stories = soup.findAll("div", "new_storylising_contentwrap")
    for stories in all_stories:
        # find outer header
        outer_header = stories.find("div", "nstory_header")
        story = stories.find("div", "nstory_intro")
        story_dict = {}
        a_url, a_text = split_anchor_tag(outer_header)
        story_dict['a_text'] = a_text
        story_dict['a_url'] = a_url[0]
        story_dict['story_text'] = story.text
        story_list.append(story_dict)
    return story_list


def cnn_page():
    """
    We get the cnn news page and read the headlines.
    """
    story_list = []
    BASE_URL = "http://edition.cnn.com"
    cnn_a_url, cnn_outer_header, cnn_a_text, cnn_story, cnn_header_link = None, None, None, None, None
    html_page = requests.get("http://edition.cnn.com/specials/last-50-stories")
    # convert the plaintext HTML markup into a DOM-like structure that we can search
    soup = BeautifulSoup(html_page.text)
    all_cnn_stories = soup.findAll("div", "cd__content")
    for cnn_storie in all_cnn_stories:
        cnn_header_link = cnn_storie.find("h3", "cd__headline")
        cnn_story = cnn_storie.find("div", "cd__description")
        story_dict = {}
        cnn_a_url, cnn_a_text = split_anchor_tag_without_domain_name(cnn_header_link)
        story_dict['a_text'] = cnn_a_text
        story_dict['a_url'] = BASE_URL + cnn_a_url[0]
        if cnn_story:
            story_dict['story_text'] = cnn_story.text
        else:
            story_dict['story_text'] = cnn_story
        story_list.append(story_dict)
    return story_list


def zee_page():
    story_list = []
    BASE_URL = "http://zeenews.india.com/"
    zee_a_url, zee_outer_header, zee_a_text, zee_story, zee_head_link = None, None, None, None, None
    html_page = requests.get("http://zeenews.india.com/india")
    # convert the plaintext HTML markup into a DOM-like structure that we can search
    soup = BeautifulSoup(html_page.text)
    all_zee_stories = soup.findAll("p", "story-head-pa")
    for zee_storie in all_zee_stories:
        story_dict = {}
        zee_a_url, zee_a_text = split_anchor_tag_without_domain_name(zee_storie)
        story_dict['a_text'] = zee_a_text
        story_dict['a_url'] = BASE_URL + zee_a_url[0]
        story_list.append(story_dict)
    all_zee_stories_next = soup.findAll("div", "col-sm-12 col-md-12 mrgn-tp1")
    for storie in all_zee_stories_next:
        zee_head_link = storie.find("span", "lead-health-ab")
        story_dict = {}
        zee_a_url, zee_a_text = split_anchor_tag_without_domain_name(zee_head_link)
        story_dict['a_text'] = zee_a_text
        story_dict['a_url'] = BASE_URL + zee_a_url[0]
        story_list.append(story_dict)
    return story_list
