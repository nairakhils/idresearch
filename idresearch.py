import requests
import json
import pandas as pd
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest
from matplotlib import pyplot as plt
from itertools import *

NER = spacy.load("en_core_web_md")
nlp = spacy.load("en_core_web_md")


#----------------------------------------#

def get_doc(doc_url):
    """Get-response

    Obtaining responses from semanticscholar api.

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.

    Returns:
        doc_fox (dict): dictionary. Contains metadata of the main article query
        doc_paperId (str): string. Contains semanticscholar paperId 
        reco_fox (dict): dictionary. Contains metadata of the recommended papers using SemanticScholar AI   

    """

    response = requests.get(f"https://api.semanticscholar.org/graph/v1/paper/URL:{doc_url}?fields=abstract")
    doc_fox = response.json()
    doc_paperId = doc_fox['paperId']
    response = requests.get(f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/{doc_paperId}?fields=url,abstract,year,citationCount,authors,venue")
    reco_fox = response.json()
    return doc_fox, doc_paperId, reco_fox


def reco_abstract(i, url):
    """Recommended Paper's Abstract

    Obtains article abstract for the queried recommended paper

    Args:
        i (int): integer. Denotes the index number as seen in the output from get_reco_df or export_reco_csv functions
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
    
    Returns:
        reco_abs (str): string. Abstract of the queried recommended paper.
    """
    doc_fox, doc_paperId, reco_fox = get_doc(url)
    reco_abs = reco_fox['recommendedPapers'][i]['abstract']
    return reco_abs

def main_abstract(url):
    """Main Paper's Abstract

    Obtains article abstract for the queried main paper

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
    
    Returns:
        main_abs (str): string. Abstract of the main queried paper.
    """
    doc_fox, doc_paperId, reco_fox = get_doc(url)
    main_abs = doc_fox['abstract']
    return main_abs


def get_ner(raw_abs):
    """Get Name Entity Recognition

    Obtains Name Entity type: ORG and PRODUCT from the abstract. 

    Args:
        raw_abs (str): string. Raw text of any article abstract.

    Returns:
        org_ent (list): list. Gives string type output within a list with ORG type entities.
        prod_ent (list): list. Gives string type output within a list with PRODUCT type entities.
    """
    text1 = NER(raw_abs)
    entities = {key: list(set(map(lambda x: str(x), g))) for key, g in groupby(sorted(text1.ents, key=lambda x: x.label_), lambda x: x.label_)}
    org_ent = []
    prod_ent = []

    try:
        org_ent = entities['ORG']
    except KeyError:
        pass

    try:
        prod_ent = entities['PRODUCT']
    except KeyError:
        pass

    return org_ent, prod_ent  


def get_reco_df(url):
    """Get Recommended Articles dataframe

    Obtains a dataframe of all the recommended articles (url, abstract, year, publisher, citation_count)

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
    
    Returns:
        new_df (dataframe): dataframe. Dataframe contatinig information on all recommended articles.
    """
    doc_fox, doc_paperId, reco_fox = get_doc(url)
    dict1 = [dict(paperId=a1['paperId'], url=a1['url'], abstract=a1['abstract'], year=a1['year'], publisher=a1['venue'], citation_count=a1['citationCount']) for a1 in reco_fox['recommendedPapers']]
    df1 = pd.DataFrame(dict1)
    new_df = df1.sort_values(by = 'citation_count', ascending=False, ignore_index=False)
    return new_df

def export_reco_csv(url):
    """Export Recommended Articles dataframe

    Exports a csv of all the recommended articles (url, abstract, year, publisher, citation_count)

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
    
    Exports:
        new_df (csv): csv. Exports a csv containing information on all recommended articles. Filename: recolist.csv
    """
    new_df = get_reco_df(url)
    new_df.to_csv('recolist.csv')
    

def summarize_doc(raw_abs, n):
    """Summarize the abstract document

    Summarizes the abstract by assigning weights to each sentence (based on common words and length of sentences).

    Args:
        raw_abs (str): string. Raw text of any article abstract.
        n (int): integer. Number of lines for the summary.
    
    Returns:
        summary (str): string. Summary of the abstract in 'n' number of lines, based on the arguement.
    """
    doc1 = nlp(raw_abs)
    keywords = []
    stopwords = list(STOP_WORDS)
    pos_tag =['PROPN', 'ADJ', 'NOUN', 'VERB', 'NUM', 'SYM', 'X']
    for token in doc1:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keywords.append(token.text)

    freq_word = Counter(keywords)
    max_freq = Counter(keywords).most_common(1)[0][1]
    for word in freq_word.keys():
        freq_word[word] = (freq_word[word]/max_freq)

    sent1 = {}
    for se in doc1.sents:
        for word in se:
            if word.text in freq_word.keys():
                if se in sent1.keys():
                    sent1[se] = sent1[se] + freq_word[word.text]
                else:
                    sent1[se] = freq_word[word.text]

    summary = nlargest(n, sent1, sent1.get)
    
    return summary


def doc_stats(raw_abs):
    """Abstract Statistics

    Finds most frequently used keywords in the abstract.

    Args:
        raw_abs (str): string. Raw text of any article abstract.

    Returns:
        freq_ans (dict): dictionary. Shows the word and number of occurences in the abstract.
    """
    doc1 = nlp(raw_abs)
    keywords = []
    stopwords = list(STOP_WORDS)
    pos_tag =['PROPN', 'ADJ', 'NOUN', 'VERB', 'NUM', 'SYM', 'X']
    for token in doc1:
        if(token.text in stopwords or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            keywords.append(token.text)

    freq_word = Counter(keywords)
    freq_ans = freq_word.most_common(5)

    return freq_ans


def reco_authors(url, num):
    """Get list of authors

    Provides the list of authors and the number of times an author's paper has been recommended in decending order.

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
        num (int): integer. Number of author names in the output.
    
    Returns:
        occurence_common (dict): dictionary. Returns a dictionary with the Author name and number of times the author's article has been recommended.
    """
    doc_fox, doc_paperId, reco_fox = get_doc(url)
    authors1 = []
    authorids1 = []

    for i in range(len(reco_fox['recommendedPapers'])):
        x1 = reco_fox['recommendedPapers'][i]['authors']
        for j in range(len(x1)):
            authors1.append(x1[j]['name'])
            authorids1.append(x1[j]['authorId'])

    occurence_count = Counter(authors1)
    occurence_common = dict(occurence_count.most_common(num))

    return occurence_common


def plot_CitationCount_url(url):
    """Plot Number of Papers vs Citation Count

    Plots a Number of Papers vs Citation Count histogram.

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
    
    Returns:
        plot: Returns a matplotlib plot.
    """
    new_df = get_reco_df(url)
    new_df['citation_count'].plot(kind='hist',bins=25)
    plt.xlabel('No of citations')
    plt.ylabel('Number of papers')
    plt.title("Number of citations for recommended papers")
    plt.show()


def plot_CitationCount_df(new_df):
    """Plot Number of Papers vs Citation Count

    Plots a Number of Papers vs Citation Count Year histogram.

    Args:
        new_df (dataframe): Pandas dataframe exported using get_reco_df function.
    
    Returns:
        plot: Returns a matplotlib plot.
    """
    new_df['citation_count'].plot(kind='hist',bins=25)
    plt.xlabel('No of citations')
    plt.ylabel('Number of papers')
    plt.title("Number of citations for reccomended papers")
    plt.show()


def plot_YearTrend_url(url):
    """Plot Number of Papers vs Publication Year

    Plots a Number of Papers vs Publication Year histogram.

    Args:
        url (str): string. URL from semanticsscholar, arxiv, aclweb, acm, biorxiv are supported.
    
    Returns:
        plot: Returns a matplotlib plot.
    """
    new_df = get_reco_df(url)
    new_df['year'].plot(kind='hist',bins=25)
    plt.ylabel('Number of papers')
    plt.xlabel('year')
    plt.title("Trend of development of field")
    plt.show()


def plot_YearTrend_df(new_df):
    """Plot Number of Papers vs Publication Year

    Plots a Number of Papers vs Publication Year histogram.

    Args:
        new_df (dataframe): Pandas dataframe exported using get_reco_df function.
    
    Returns:
        plot: Returns a matplotlib plot.
    """
    new_df['year'].plot(kind='hist',bins=25)
    plt.ylabel('Number of papers')
    plt.xlabel('year')
    plt.title("Trend of development of field")
    plt.show()

