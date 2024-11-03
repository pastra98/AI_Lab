# About
This is a university project for a course on connectionist machine learning approaches.
I worked on this project together with my colleague and good friend [Riško Hrivnák](https://github.com/Rrisko), with whom I also analyzed [Wikipedia Edit wars](https://github.com/Rrisko/WikiEdits) for another uni project.

We were free to choose any topic & data source, so I proposed to scrape the headlines of one of Austria's biggest online newspapers, [derstandard.at](https://www.derstandard.at/).
The overall goal was to predict the number of comments a given headline would generate by applying an embedding on the text and training simple feed forward neural nets on those embedding vectors.

...We did not succeed in predicting the amount of comments, but analyzing the patterns in newspaper headlines was interesting none the less.

## Repository contents
As the scraping and data processing involved a lot of steps in their own right, the project is split into 3 notebooks:
1. `data_scraping:` Here we explore the page structure of derstandard.at frontpage,
    using beautifulsoup to extract the data we are interested in. The notebook concludes
    with producing a csv file `4yrs_derstandard_frontpage_data.csv` (not included in the repo) that is 57 MB of
    size with over 180 thousand articles. 
2. `data_processing:` Here we perform EDA on our gathered data, and process the text
    using [spacy](https://spacy.io/) to transform it into a vector. The end result of
    this notebook is `ml_data.parquet` (210 MB), which contains all the data ready
    for a machine learning pipeline.
3. `machine_learning:` Here we train various regression networks on our data, evaluate
    them on a test set and also some real data which can be fetched for any given day.

we have concatenated all notebooks into a single pdf (`all_notebooks.pdf`).
We also included /html_nbs directory, where the html of each notebook is stored.

Additionally, we have performed some classification tests as well. This work includes
some separate processing , and is contained in the 4th notebook:

4. `text_processing_classification_models:` Here, the text data is processed
   and used as input to classification models. We try to predict if number
   of comments is large or small (binary classification) based on the title
   and subtitle, and what is the *kicker* or *storylabel* (multi-class classification)
   based on the same inputs. We had to do the text_processing separately
   as this notebook was run on Richard's computer, which would crash when
   working with the large model.

---
References used:
* http://mitloehner.com/lehre/dsai1/
* https://pytorch.org/docs/stable/nn.html
* https://spacy.io/models/de
* https://stackoverflow.blog/2023/11/09/an-intuitive-introduction-to-text-embeddings/
* https://en.wikipedia.org/wiki/Word2vec
* (3b1b on neural networks)[https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi]