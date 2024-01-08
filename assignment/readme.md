# Assignment 1 submission - analyzing derstandard.at data
## By Paul Straberger & Risko Hrivnak

Dear Professor Mitlöhner,

We thought it would be interesting to get our own data and decided to go with newspaper articles.
To this end we scraped 4 years worth of `derstandard.at` headlines, which also includes
the number of posts (comments) a given article has generated, which maps neatly to
a machine learning project: predicting the number of posts a given article will generate,
based on the headline, subtitle and time-data.

As the scraping and data processing involved a lot of steps in their own right, we
have decided to split up our project into three notebooks:
1. `data_scraping:` Here we explore the page structure of derstandard.at frontpage,
    using beautifulsoup to extract the data we are interested in. The notebook concludes
    with producing a csv file `4yrs_derstandard_frontpage_data.csv` that is 57 MB of
    size with over 180 thousand articles.
2. `data_processing:` Here we perform EDA on our gathered data, and process the text
    using [spacy](https://spacy.io/) to transform it into a vector. The end result of
    this notebook is `ml_data.parquet` (210 MB), which contains all the data ready
    for a machine learning pipeline.
3. `machine_learning:` Here we train various regression networks on our data, evaluate
    them on a test set and also some real data which can be fetched for any given day.

As you can see, the data we have produced is quite large, which is why we have not
included it in the repository. You may use
[this](https://1drv.ms/f/s!As0d2mVTvxe4hoY_MrtNVk6EieX4OA?e=TuhIek)
download link, which contains everything needed to run the notebook.

However some of the cells took very long to run, and the notebooks require packages
that you may need to install (pyarrow, spacy). For embeddings we also used a large
spacy model (500 MB). For your convenience, we have concatenated all notebooks into
a single pdf (all_notebooks.pdf). We also included /html_nbs directory, where the html
of each notebook is stored. But the code should definitely also execute once
all dependencies are installed along with the data. 

Happy new year,

Paul & Risko

  *Disclaimer: We did not get any permission from derstandard.at to perform this*
  *scraping. As this is only for this university project and the scraped data will not be shared*
  *elsewhere, we hope to not get into any legal trouble because of our scraping - thank you :^)*
