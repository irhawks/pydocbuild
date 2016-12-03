# Jupyter介绍


## Jupyter notebook output in markdown

The functions you want are in the `IPython.display` module.
```python
from IPython.display import display, Markdown, Latex
display(Markdown('*some markdown* $\phi$'))
# If you particularly want to display maths, this is more direct:
display(Latex('\phi'))
```

## Writing academic papers in plain text with Markdown and Jupyter notebook

原文见<https://sylvaindeville.net/2015/07/17/writing-academic-papers-in-plain-text-with-markdown-and-jupyter-notebook/>。

My new workflow for writing academic papers involves Jupyter Notebook for data analysis and generating the figures, Markdown for writing the paper, and Pandoc for generating the final output. Works great !

As academics, writing is one of our core activity. Writing academic papers is not quite like writing blog posts or tweets. The text is structured, and include figures, lots of maths (usually), and many citations. Everyone has its own workflow, which usually involves Word or LaTex at some point, as well as some reference management solutions. I have been rethinking about my writing workflow recently, and come up with a new solutions solving a number of requirements I have:


    future proof. I do not want to depend on a file format that might become obsolete.
    lightweight.
    one master file for all kind of outputs (PDF, DOC, but eventually HTML, etc…).
    able to deal with citation management automatically (of course).
    able to update the paper (including plots) as revisions are required, with a minimal amount of efforts (I told you I was lazy).
    open source tools is a bonus.
    strongly binded to my data analysis workflow (more on that later).

After playing around with a couple of tools, I experimented with a nice solution for our latest paper, and will share it here in case anyone else in interested.

This particular paper was particularly suited for my new workflow. What we did was data mine 120+ papers for process parameters and properties of materials to extract trends and look at the relative influence of the various parameters on the properties of the material. The data in that case was a big CSV file, with hundreds of lines. Each data point was labelled by its bib key (e.g. Deville2006), which turned out to be super convenient later.


* The Jupyter notebook generates the figures and saves them in a folder.
* The Markdown file starts with a few YAML metadata, that I use to provide the title, authors, affiliation, and dates.

Summary of the tools you need

* A valid Python and Jupyter notebook installation, if you are doing your data analysis with it.
* Pandoc.
* A valid LaTex installation.
* A bib file for your bibliography.
* CSL file for the bibliography styles you want to use. Get the one you need here.
* A text editor. Many choices available.
* Total cost: 0\$


### IOP的论文展示

在论文展示上，自己觉得IOP做得非常不错，见<http://iopscience.iop.org/article/10.1088/1468-6996/16/4/043501/meta;jsessionid=337BE40986CE17E903B31EEA11358997.c2.iopscience.cld.iop.org>。

里面用网页的形式展示了各种链接与图形。
