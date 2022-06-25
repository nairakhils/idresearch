# idresearch &#x1F50E;&#128240;
## Documentation

[![codeastro](https://img.shields.io/badge/Made%20at-Code/Astro-blueviolet.svg)](https://semaphorep.github.io/codeastro/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://idresearch.readthedocs.io/en/latest/idresearch.html)

idresearch is a package aimed to help researchers help identify relevant papers and see the development trend in that particular subfield. The package will provide a list of recommended papers and their abstracts. Additionally, it also allows the user to summarize the abstract, find common keywords from the abstract and save the recommended papers in csv format.

- Semantic Scholar API for paper recommendations
- spacy models for Natural Lanugage Processing
- ✨Allows query from websites like arxiv, semantic scholar, biorxiv✨


## Installation


1. Clone the repository to your local machine.
```
git clone https://github.com/nairakhils/idresearch.git
```

**idresearch** requires additional direct dependencies to work.

2. Install the dependencies before installing idsearch (https://spacy.io/models/en#en_core_web_md).

```sh
python -m spacy download en_core_web_md
```

3. After installing the **en_core_web_md** spacy model...

cd to the directory containing _setup.py_

```sh
python setup.py install
```

## Documentation Links

**ReadTheDocs**: https://idresearch.readthedocs.io/en/latest/idresearch.html



## Look into the ['Tutorials'](https://github.com/nairakhils/idresearch/blob/main/tutorials/tutorial.md) folder to get a quick rundown on using idresearch!


>PDF file reader and article result comparison script is under development

