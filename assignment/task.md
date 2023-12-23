# Apply connectionist machine learning to a new dataset:

-   Find another dataset e.g. on the UCI Machine Learning website
    https://archive.ics.uci.edu/ml/index.php
    -   We want a dataset that we have *not* used in the
        course
    -   Datasets on classification with only two or a few output classes
        are most convenient
-   Apply the connectionist machine learning method of your choice
    -   our own pure Python implementation of the basic two-layer
        feed-forward net
    -   or one of our PyTorch code examples
    -   or another architecture of you own choice (easy in PyTorch, just
        change/add layers)
-   Choose an input encoding, if necessary (such as text data, e.g.
    reviews)
-   Modify some parameters e.g. the number of hidden
    units, and observe and document the results.

Use the Jupyter notebook to run your experiments, and add Markdown cells
for documentation. You do not have to describe every
detail of the connectionist approach, only information relevant for your
particular application; imagine that someone else in the course should
be able to pick up where you left. Do not skip on the documentation, the
best software is of little value without proper documentation:

-   What exactly was the problem
-   How did you implement the solution
-   How can someone else use your code (which files need to be present
    etc)

Submit your notebook; this is a single file with suffix
.ipynb which you can download from the JupyterHup server(File/Download)
and then submit; or directly submit the .ipynb file from your computer
if you worked locally. The grading depends on

-   Complexity of challenge
    -   dataset very similar to lecture, with tiny changes to neural net
        = few points
    -   different dataset, needs encoding, additional Keras layers =
        lots of points
-   It works
    -   if it does not and produces only errors = much fewer points
-   Documentation
    -   really helpful for understanding the task and the solution =
        more points
    -   non-existent or useless = fewer points

Maybe choose a bit more of a challenge! Let me know what you plan to do
via Email (mitloehn@wu.ac.at) to get feedback.