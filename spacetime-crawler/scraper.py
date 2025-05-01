import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen
from urllib.parse import urljoin
import urllib.robotparser

'''
Vaanya Gupta - 92052177
Soumya Sharma - 16463723 
Srilakshmi Godavarti - 82584732
Jae Kim - 59572523
'''
check_duplicate = []  # Has only unique urls and used for checking duplicates
# common_words = {}
# As we are using tokens with length being >=2, the stop words are ammended accordingly
stop_words = ['about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren",
              'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by',
              "can", 'cannot', 'could', "couldn", 'did', "didn", 'do', 'does', "doesn", 'doing', "don",
              'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn", 'has', "hasn", 'have',
              "haven't", 'having', 'he', 'her', 'here', 'hers', 'herself', 'him',
              'himself', 'his', 'how', "how's", 'if', 'in', 'into', 'is',
              "isn", 'it', 'its', 'itself', 'me', 'more', 'most', "mustn", 'my', 'myself',
              'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our',
              'ours', 'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she',
              'should', "shouldn", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs',
              'them', 'themselves', 'then', 'there', 'these', 'they',
              'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn",
              'we', 'were', "weren", 'what', 'when',
              'where', 'which', 'while', 'who', 'whom', 'why', 'with', "won",
              'would', "wouldn", 'you', "ll", "re", "ve", 'your', 'yours', 'yourself',
              'yourselves']
max_len = 0  # Used to find maximum number of words from all crawled pages
max_url = ''  # Used to find url that has maximum number of words
# final_words = []
words_count = {}  # dictionary to find common words


def scraper(url, resp):
    links = extract_next_links(url, resp)
    return [link for link in links if is_valid(link)]


def extract_next_links(url, resp):
    list_tokens = []  # list of tokens on each webpage
    url_file = open("URL.txt", "a+", encoding="utf-8")  # file to read the unique urls
    url_len = open("URL_Length.txt", "a+", encoding="utf-8")  # file to check the length of each url
    url_length = open("URL_Longest.txt", 'a+', encoding="utf-8")  # file to save the url having the longest length.
    url_list = []  # Prevents crawling the same webpage more than once
    parsed = urlparse(url)
    # Robotparser library is used to check if file can be opened
    rp = urllib.robotparser.RobotFileParser()
    domain = parsed.scheme + '://' + parsed.netloc + '/robots.txt'
    rp.set_url(domain)

    try:
        # checking if robot.txt exists for the url
        # if not, it is safe
        # if it exists, allowed and disallowed files needs to be checked
        rp.read()
        read_bool = True
    except:
        read_bool = False
    # Checking status to be 200 because it is a OK success status
    if resp.status == 200:
        passed_bool = False

        if read_bool:
            # If the robot file exists, we check whether we can crawl the url or not by fetching it
            if rp.can_fetch("*", url):
                passed_bool = True
        else:
            passed_bool = True

        if passed_bool:
            # check_duplicate is list that has all the urls that have been crawled
            # So, if the current url is already crawled, it is not crawled again
            if url not in check_duplicate and is_valid(url):
                # print("PARAMETER URL:", url)
                check_duplicate.append(url)

                if resp.raw_response != None:  # check if getting content does not lead to None value
                    content = resp.raw_response.content  # gets content of webpage
                    resp_content = BeautifulSoup(content, "lxml")
                    total_url = 'https://' + parsed.netloc
                    final_words = []  # list of all words in webpage
                    list_tokens = []  # list of final tokens
                    stop_words_count = 0  # used to find ratio of stops words to all words

                    for word in resp_content.get_text().split():  # gather list of words split by spaces
                        tokens = re.split(r'[^a-z0-9]+',
                                          word.lower())  # gather list of words split by everything not alphanumeric
                        final_words += tokens  # final_words contains list of all words in webpage

                    for token in final_words:
                        if len(token) >= 2 and not token.isdigit():  # token requirements
                            if token in stop_words:
                                stop_words_count += 1
                            list_tokens += [token]

                    if (len(list_tokens) != 0):
                        percentage = (stop_words_count / len(
                            list_tokens)) * 100  # get percentage of stop words to all words

                    # low information page: less than or equal to 300 and has more than
                    # or equal to 35% of stop words when compared with the texual content
                    # Low information pages are not being crawled.
                    if len(list_tokens) > 300 and percentage < 35:
                        url_file.write(url + '\n')
                        url_len.write(url + ' : ' + str(len(list_tokens)) + '\n')
                        global max_len

                        if (len(list_tokens) > max_len):  # updates maximum length URL
                            max_len = len(list_tokens)
                            max_url = url
                            url_length.write(max_url + ' ' + str(max_len) + '\n')
                        compute_frequencies(list_tokens)

                        list_of_urls_in_the_page = resp_content.find_all('a')  # 'a' has all the links in the page
                        for urls in list_of_urls_in_the_page:  # all the urls founf on that page
                            parsed_url = urls.get('href')

                            if parsed_url is not None and parsed_url != '#' and parsed_url != '/':

                                if (parsed_url.startswith('/', 0, 1)):
                                    parsed_url = urljoin(total_url, parsed_url)

                                if (not parsed_url.startswith('http', 0, 4)):
                                    parsed_url = 'https://' + parsed_url

                                # Defragmenting the url
                                without_hash = parsed_url.split('#')
                                without_hash = without_hash[0]
                                # If the URL found is valid, it is added to the url_list
                                if (is_valid(without_hash)):
                                    url_list.append(without_hash)
    return (url_list)


# --------------
# VALID DOMAINS :
# --------------
# *.ics.uci.edu/*
# *.cs.uci.edu/*
# *.informatics.uci.edu/*
# *.stat.uci.edu/*
# today.uci.edu/department/information_computer_sciences/*

def is_valid(url):
    try:

        valid_domains = ['ics.uci.edu', 'cs.uci.edu', 'informatics.uci.edu', 'stat.uci.edu',
                         'today.uci.edu']
        parsed = urlparse(url)

        # These are the urls and paths we found to have traps during our test crawls, so we
        # return false to keep our crawler from accessing these pages
        if url == 'http://www.informatics.uci.edu/files/pdf/InformaticsBrochure-March2018':
            return False

        if parsed.netloc == 'www.ics.uci.edu' and 'community/news' in parsed.path:
            return False

        if parsed.netloc == 'wics.ics.uci.edu' and ('events' in parsed.path or 'event' in parsed.path):
            return False

        if 'archive.ics.uci.edu' in parsed.netloc:
            return False

        if parsed.netloc == 'cml.ics.uci.edu' and 'aiml' in parsed.path:
            return False

        if parsed.netloc == 'grape.ics.uci.edu':
            return False

        if "doku.php" in parsed.path:
            return False

            # This is to avoid similar pages
        if "replytocom" in parsed.query:
            return False

        if parsed.scheme not in set(["http", "https"]):
            return False

        domain = parsed.netloc

        if domain.startswith('www.', 0, 4):
            domain = domain[4::]

        if domain.count('.') == 3:
            subdomain = domain.split('.')
            domain = '.'.join(subdomain[1::])

        # This is to avoid similar pages and remove noise
        if "wics.ics.uci.edu" in parsed.netloc:
            for tag in ["img_", "afg", 'share=']:
                if tag in parsed.query:
                    return False

        # This is to avoid calendar traps
        if domain == 'today.uci.edu':
            if '/department/information_computer_sciences' not in parsed.path or 'calendar' in parsed.path:
                return False

        domain_bool = False

        # Changing the domain_bool value for all the valid domains because we want the crawler
        # to crawl these pages.
        for domains in valid_domains:
            if domains == domain:
                domain_bool = True

        # If domain_bool is False we don't want the crawler to crawl that page.
        if domain_bool == False:
            return False

        # Invalid list of formats to avoid crawling pages that are not text or xml format.
        invalid_list = ["css", "js", "bmp", "gif", "jpeg", "ico", "png", "tiff", "mid", "mp2", "mp3",
                        "jpg", "mp4",
                        "wav", "avi", "mov", "mpeg", "ram", "m4v", "mkv", "ogg", "ogv", "pdf", "ps",
                        "eps", "tex", "ppt",
                        "pptx", "doc", "docx", "xls", "xlsx", "names", "data", "dat", "exe", "bz2",
                        "tar", "msi", "bin", "7z", "psd", "dmg", "iso", "epub",
                        "dll", "cnf", "tgz", "sha1", "thmx", "mso", "arff", "rtf", "jar", "csv", "rm",
                        "smil", "wmv", "swf", "wma", "zip", "rar", "gz", "apk"]

        # Checking whether the paths have these extensions and if they have, they are not crawled
        # This is to avoid webpages that are not txt or xml files
        for invalid in invalid_list:
            path = re.split(r'[\.|\/]+', parsed.path.lower())
            if invalid in path:
                return False

        # This is to avoid webpages that are not txt or xml files
        return not re.match(
            r".*\.(css|js|bmp|gif|jpeg|ico"
            + r"|png|tiff?|mid|mp2|mp3|mp4"
            + r"|wav|avi|mov|mpeg|ram|m4v|mkv|ogg|ogv|pdf"
            + r"|ps|eps|tex|ppt|pptx|doc|docx|xls|xlsx|names"
            + r"|data|dat|exe|bz2|tar|msi|bin|7z|psd|dmg|iso"
            + r"|epub|dll|cnf|tgz|sha1"
            + r"|thmx|mso|arff|rtf|jar|csv"
            + r"|rm|smil|wmv|swf|wma|zip|rar|gz)$", parsed.path.lower())

    except TypeError:
        print("TypeError for ", parsed)
        raise


# This function is to compute common words from all the webpages combined
# in order to answer questions for the report
def compute_frequencies(tokens):
    url_common = open("URL_Common.txt", 'a+', encoding="utf-8")
    for token in tokens:
        if token not in stop_words:
            if token not in words_count:
                words_count[token] = 1
            else:
                words_count[token] += 1
    # url_common file is used to find most frequent common words amongst all crawled pages
    url_common.truncate(0)
    url_common.write(str(words_count))
    url_common.write('\n')
