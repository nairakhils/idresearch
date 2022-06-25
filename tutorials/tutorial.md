# idresearch &#x1F50E;&#128240;
## Tutorials

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://idresearch.readthedocs.io/en/latest/idresearch.html)

## Installation

**idresearch** requires additional direct dependencies to work.

Install the dependencies before installing idsearch (https://spacy.io/models/en#en_core_web_md).

```sh
python -m spacy download en_core_web_md
```

After installing the **en_core_web_md** spacy model...

cd to the directory containing _setup.py_

```sh
python setup.py install
```

### To find abstract of an arxiv paper

```
>> import idresearch as idr

>> url = "https://arxiv.org/abs/2103.12877"
>> main_abs = idr.main_abstract(url)
>> print(main_abs)
```

### To find most common keywords in an abstract

```
>> import idresearch as idr
>> url = "https://arxiv.org/abs/2103.12877"
>> main_abs = idr.main_abstract(url)
>> print(idr.doc_stats(main_abs))
```
**Output**
```
>>> [('orbital', 6), ('eccentricity', 4), ('orbits', 4), ('orbit', 3), ('inclination', 3)]
```


### To get recommended papers using Semantic Scholar API, and save the details as a csv file

```
>> import idresearch as idr
>> url = "https://arxiv.org/abs/2103.12877"
>> reco_papers = idr.get_reco_df(url)  ##this will create a pandas dataframe

>> idr.export_reco_csv(url)   ##To save the dataframe as a csv directly to your current directory
```


### To plot Number of Papers published vs Year of publication (for recommended papers)

```
>> import idresearch as idr
>> url = "https://arxiv.org/abs/2103.12877"
>> idr.plot_YearTrend_url(url)
```

### To perform the Name Entity Recognition of abstract text
#### (Currently in early testing phase) 
*Returns a list for ORG_type entity and PRODUCT_type entity each* (https://spacy.io/usage/linguistic-features#named-entities)

```
>> import idresearch as idr
>> url = "https://arxiv.org/abs/2103.12877"
>> reco_abs = idr.reco_abstract(0, url)  ##abstract of first entry amongst recommended papers

>> print(idr.get_ner(reco_abs))
```
**Output**
```
>>> (['the Orbits For The Impatient'], []) 
```
