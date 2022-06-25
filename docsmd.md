

# idresearch Functions[](#idresearch "Permalink to this heading")

Function for idresearch.

<span id="module-idresearch" class="target"></span>

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">doc\_stats</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">raw\_abs</span></span>*<span class="sig-paren">)</span>[](#idresearch.doc_stats "Permalink to this definition")  
    Abstract Statistics
    
    Finds most frequently used keywords in the abstract.
    
      - Parameters  
        **raw\_abs** (*str*) – string. Raw text of any article abstract.
    
      - Returns  
        dictionary. Shows the word and number of occurences in the
        abstract.
    
      - Return type  
        freq\_ans (dict)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">export\_reco\_csv</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">url</span></span>*<span class="sig-paren">)</span>[](#idresearch.export_reco_csv "Permalink to this definition")  
    Export Recommended Articles dataframe
    
    Exports a csv of all the recommended articles (url, abstract, year,
    publisher, citation\_count)
    
      - Parameters  
        **url** (*str*) – string. URL from semanticsscholar, arxiv,
        aclweb, acm, biorxiv are supported.
    
    <!-- end list -->
    
      - Exports:  
        new\_df (csv): csv. Exports a csv containing information on all
        recommended articles. Filename: recolist.csv

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">get\_doc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">doc\_url</span></span>*<span class="sig-paren">)</span>[](#idresearch.get_doc "Permalink to this definition")  
    Get-response
    
    Obtaining responses from semanticscholar api.
    
      - Parameters  
        **url** (*str*) – string. URL from semanticsscholar, arxiv,
        aclweb, acm, biorxiv are supported.
    
      - Returns  
        dictionary. Contains metadata of the main article query
        doc\_paperId (str): string. Contains semanticscholar paperId
        reco\_fox (dict): dictionary. Contains metadata of the
        recommended papers using SemanticScholar AI
    
      - Return type  
        doc\_fox (dict)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">get\_ner</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">raw\_abs</span></span>*<span class="sig-paren">)</span>[](#idresearch.get_ner "Permalink to this definition")  
    Get Name Entity Recognition
    
    Obtains Name Entity type: ORG and PRODUCT from the abstract.
    
      - Parameters  
        **raw\_abs** (*str*) – string. Raw text of any article abstract.
    
      - Returns  
        list. Gives string type output within a list with ORG type
        entities. prod\_ent (list): list. Gives string type output
        within a list with PRODUCT type entities.
    
      - Return type  
        org\_ent (list)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">get\_reco\_df</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">url</span></span>*<span class="sig-paren">)</span>[](#idresearch.get_reco_df "Permalink to this definition")  
    Get Recommended Articles dataframe
    
    Obtains a dataframe of all the recommended articles (url, abstract,
    year, publisher, citation\_count)
    
      - Parameters  
        **url** (*str*) – string. URL from semanticsscholar, arxiv,
        aclweb, acm, biorxiv are supported.
    
      - Returns  
        dataframe. Dataframe contatinig information on all recommended
        articles.
    
      - Return type  
        new\_df (dataframe)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">main\_abstract</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">url</span></span>*<span class="sig-paren">)</span>[](#idresearch.main_abstract "Permalink to this definition")  
    Main Paper’s Abstract
    
    Obtains article abstract for the queried main paper
    
      - Parameters  
        **url** (*str*) – string. URL from semanticsscholar, arxiv,
        aclweb, acm, biorxiv are supported.
    
      - Returns  
        string. Abstract of the main queried paper.
    
      - Return type  
        main\_abs (str)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">plot\_CitationCount\_df</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">new\_df</span></span>*<span class="sig-paren">)</span>[](#idresearch.plot_CitationCount_df "Permalink to this definition")  
    Plot Number of Papers vs Citation Count
    
    Plots a Number of Papers vs Citation Count Year histogram.
    
      - Parameters  
        **new\_df** (*dataframe*) – Pandas dataframe exported using
        get\_reco\_df function.
    
      - Returns  
        Returns a matplotlib plot.
    
      - Return type  
        plot

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">plot\_CitationCount\_url</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">url</span></span>*<span class="sig-paren">)</span>[](#idresearch.plot_CitationCount_url "Permalink to this definition")  
    Plot Number of Papers vs Citation Count
    
    Plots a Number of Papers vs Citation Count histogram.
    
      - Parameters  
        **url** (*str*) – string. URL from semanticsscholar, arxiv,
        aclweb, acm, biorxiv are supported.
    
      - Returns  
        Returns a matplotlib plot.
    
      - Return type  
        plot

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">plot\_YearTrend\_df</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">new\_df</span></span>*<span class="sig-paren">)</span>[](#idresearch.plot_YearTrend_df "Permalink to this definition")  
    Plot Number of Papers vs Publication Year
    
    Plots a Number of Papers vs Publication Year histogram.
    
      - Parameters  
        **new\_df** (*dataframe*) – Pandas dataframe exported using
        get\_reco\_df function.
    
      - Returns  
        Returns a matplotlib plot.
    
      - Return type  
        plot

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">plot\_YearTrend\_url</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">url</span></span>*<span class="sig-paren">)</span>[](#idresearch.plot_YearTrend_url "Permalink to this definition")  
    Plot Number of Papers vs Publication Year
    
    Plots a Number of Papers vs Publication Year histogram.
    
      - Parameters  
        **url** (*str*) – string. URL from semanticsscholar, arxiv,
        aclweb, acm, biorxiv are supported.
    
      - Returns  
        Returns a matplotlib plot.
    
      - Return type  
        plot

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">reco\_abstract</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">i</span></span>*,
    *<span class="n"><span class="pre">url</span></span>*<span class="sig-paren">)</span>[](#idresearch.reco_abstract "Permalink to this definition")  
    Recommended Paper’s Abstract
    
    Obtains article abstract for the queried recommended paper
    
      - Parameters
        
          - **i** (*int*) – integer. Denotes the index number as seen in
            the output from get\_reco\_df or export\_reco\_csv functions
        
          - **url** (*str*) – string. URL from semanticsscholar, arxiv,
            aclweb, acm, biorxiv are supported.
    
      - Returns  
        string. Abstract of the queried recommended paper.
    
      - Return type  
        reco\_abs (str)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">reco\_authors</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">url</span></span>*,
    *<span class="n"><span class="pre">num</span></span>*<span class="sig-paren">)</span>[](#idresearch.reco_authors "Permalink to this definition")  
    Get list of authors
    
    Provides the list of authors and the number of times an author’s
    paper has been recommended in decending order.
    
      - Parameters
        
          - **url** (*str*) – string. URL from semanticsscholar, arxiv,
            aclweb, acm, biorxiv are supported.
        
          - **num** (*int*) – integer. Number of author names in the
            output.
    
      - Returns  
        dictionary. Returns a dictionary with the Author name and number
        of times the author’s article has been recommended.
    
      - Return type  
        occurence\_common (dict)

<!-- end list -->

  - <span class="sig-prename descclassname"><span class="pre">idresearch.</span></span><span class="sig-name descname"><span class="pre">summarize\_doc</span></span><span class="sig-paren">(</span>*<span class="n"><span class="pre">raw\_abs</span></span>*,
    *<span class="n"><span class="pre">n</span></span>*<span class="sig-paren">)</span>[](#idresearch.summarize_doc "Permalink to this definition")  
    Summarize the abstract document
    
    Summarizes the abstract by assigning weights to each sentence (based
    on common words and length of sentences).
    
      - Parameters
        
          - **raw\_abs** (*str*) – string. Raw text of any article
            abstract.
        
          - **n** (*int*) – integer. Number of lines for the summary.
    
      - Returns  
        string. Summary of the abstract in ‘n’ number of lines, based on
        the arguement.
    
      - Return type  
        summary (str)

</div>

</div>

</div>

<div class="rst-footer-buttons" role="navigation" aria-label="Footer">


