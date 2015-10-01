# bib

## Quick Start

Create a `seed.bib` like the following:

```
@article{
    teh.jordan:hdp,
    doi = {10.1198/016214506000000302},
    oai = {eprints.ucl.ac.uk.OAI2:13457},
    pdf = {http://www.stat.berkeley.edu/~jordan/653.pdf},
    keywords = {bnp}
}

@inproceedings{
    teh:hpylm,
    dblp = {conf/acl/Teh06},
    doi = {10.3115/1220175.1220299},
    pdf = {http://www.stats.ox.ac.uk/~teh/research/compling/acl2006.pdf},
    keywords = {bnp}
}

@book{
    mackay:itila,
    isbn = {9780521642989},
    url = {http://www.inference.phy.cam.ac.uk/itila/},
    pdf = {http://www.inference.phy.cam.ac.uk/itprnn/book.pdf}
}

@inproceedings{
    Duvenaud2013,
    dblp = {conf/icml/DuvenaudLGTG13},
    arxiv = {1302.4922}
}
```

Now run:

```
./bib-update
```

This will automatically pull metadata from the internet, download fulltext PDFs where possible, extract plaintext from PDFs, and generate a `library.bib` that looks like:

```
@article{
    teh.jordan:hdp,
    author = {Teh, Yee Whye and Jordan, Michael I and Beal, Matthew J and Blei, David M},
    doi = {10.1198/016214506000000302},
    oai = {eprints.ucl.ac.uk.OAI2:13457},
    pdf = {http://www.stat.berkeley.edu/~jordan/653.pdf},
    keywords = {bnp},
    title = {Hierarchical Dirichlet Processes},
    volume = {101},
    url = {http://dx.doi.org/10.1198/016214506000000302},
    number = {476},
    journal = {Journal of the American Statistical Association},
    publisher = {Informa UK (American Statistical Association)},
    year = {2006},
    month = {Dec},
    pages = {1566-1581},
    abstract = {We consider problems involving groups of data where each observation within a group is a draw from a mixture model and where it is desirable to share mixture components between groups. We assume that the number of mixture components is unknown a priori and is to be inferred from the data. In this setting it is natural to consider sets of Dirichlet processes, one for each group, where the well-known clustering property of the Dirichlet process provides a nonparametric prior for the number of mixture components within each group. Given our desire to tie the mixture models in the various groups, we consider a hierarchical model, specifically one in which the base measure for the child Dirichlet processes is itself distributed according to a Dirichlet process. Such a base measure being discrete, the child Dirichlet processes necessarily share atoms. Thus, as desired, the mixture models in the different groups necessarily share mixture components. We discuss representations of hierarchical Dirichlet processes in terms of a stick-breaking process, and a generalization of the Chinese restaurant process that we refer to as the "Chinese restaurant franchise." We present Markov chain Monte Carlo algorithms for posterior inference in hierarchical Dirichlet process mixtures and describe applications to problems in information retrieval and text modeling.},
    note = {J AM STAT ASSOC , 101 (476) 1566 - 1581. (2006)},
    subject = {clustering, hierarchical model, Markov chain Monte Carlo, mixture model, nonparametric Bayesian statistics, NONPARAMETRIC PROBLEMS, DENSITY-ESTIMATION, COUNT DATA, MODELS, DISTRIBUTIONS, INFERENCE, INVARIANT, MIXTURES, PRIORS},
    file = {pdf/a5b9c7c4e84231a622902e68c102ae30c5c9571c.pdf},
    txt = {txt/a5b9c7c4e84231a622902e68c102ae30c5c9571c.txt}
}

@inproceedings{
    teh:hpylm,
    author = {Teh, Yee Whye},
    dblp = {http://dblp.uni-trier.de/rec/bibtex/conf/acl/Teh06},
    doi = {10.3115/1220175.1220299},
    pdf = {http://www.stats.ox.ac.uk/~teh/research/compling/acl2006.pdf},
    keywords = {bnp},
    title = {A Hierarchical Bayesian Language Model Based On Pitman-Yor Processes},
    booktitle = {ACL},
    year = {2006},
    ee = {http://aclweb.org/anthology/P06-1124},
    crossref = {DBLP:conf/acl/2006},
    bibsource = {DBLP, http://dblp.uni-trier.de},
    url = {http://dx.doi.org/10.3115/1220175.1220299},
    publisher = {Association for Computational Linguistics},
    pages = {985-992},
    file = {pdf/6bf6c77b895069239ef7a180aee5332ed7b40c79.pdf},
    txt = {txt/6bf6c77b895069239ef7a180aee5332ed7b40c79.txt}
}

@proceedings{
    DBLP:conf/acl/2006,
    editor = {Calzolari, Nicoletta and Cardie, Claire and Isabelle, Pierre},
    title = {ACL 2006, 21st International Conference on Computational Linguistics and 44th Annual Meeting of the Association for Computational Linguistics, Proceedings of the Conference, Sydney, Australia, 17-21 July 2006},
    booktitle = {ACL},
    publisher = {The Association for Computer Linguistics},
    year = {2006},
    ee = {http://aclweb.org/anthology/P/P06/},
    bibsource = {DBLP, http://dblp.uni-trier.de},
    url = {http://aclweb.org/anthology/P/P06/}
}

@book{
    mackay:itila,
    author = {MacKay, David J. C.},
    isbn = {9780521642989},
    url = {http://www.inference.phy.cam.ac.uk/itila/},
    pdf = {http://www.inference.phy.cam.ac.uk/itprnn/book.pdf},
    worldcat = {http://worldcat.org/isbn/9780521642989},
    title = {Information Theory, Inference and Learning Algorithms},
    bibsource = {calibre (0.9.37) [http://calibre-ebook.com]},
    year = {2003},
    month = {Sep},
    abstract = {Information theory and inference, often taught separately, are here united in one entertaining textbook. These topics lie at the heart of many exciting areas of contemporary science and engineering - communication, signal processing, data mining, machine learning, pattern recognition, computational neuroscience, bioinformatics, and cryptography. This textbook introduces theory in tandem with applications. Information theory is taught alongside practical communication systems, such as arithmetic coding for data compression and sparse-graph codes for error-correction. A toolbox of inference techniques, including message-passing algorithms, Monte Carlo methods, and variational approximations, are developed alongside applications of these tools to clustering, convolutional codes, independent component analysis, and neural networks. The final part of the book describes the state of the art in error-correcting codes, including low-density parity-check codes, turbo codes, and digital fountain codes -- the twenty-first century standards for satellite communications, disk drives, and data broadcast. Richly illustrated, filled with worked examples and over 400 exercises, some with detailed solutions, David MacKay's groundbreaking book is ideal for self-learning and for undergraduate or graduate courses. Interludes on crosswords, evolution, and sex provide entertainment along the way. In sum, this is a textbook on information, communication, and coding for a new generation of students, and an unparalleled entry point into these subjects for professionals in areas as diverse as computational biology, financial engineering, and machine learning. \par \emph{Review} \par "...a valuable reference...enjoyable and highly useful." \\ American Scientist \par "...an impressive book, intended as a class text on the subject of the title but having the character and robustness of a focused encyclopedia. The presentation is finely detailed, well documented, and stocked with artistic flourishes." \\ Mathematical Reviews \par "Essential reading for students of electrical engineering and computer science; also a great heads-up for mathematics students concerning the subtlety of many commonsense questions." \\ Choice \par "An utterly original book that shows the connections between such disparate fields as information theory and coding, inference, and statistical physics." \\ Dave Forney, Massachusetts Institute of Technology \par "This is an extraordinary and important book, generous with insight and rich with detail in statistics, information theory, and probabilistic modeling across a wide swathe of standard, creatively original, and delightfully quirky topics. David MacKay is an uncompromisingly lucid thinker, from whom students, faculty and practitioners all can learn." \\ Peter Dayan and Zoubin Ghahramani, Gatsby Computational Neuroscience Unit, University College, London \par "An instant classic, covering everything from Shannon's fundamental theorems to the postmodern theory of LDPC codes. You'll want two copies of this astonishing book, one for the office and one for the fireside at home." \\ Bob McEliece, California Institute of Technology \par "An excellent textbook in the areas of infomation theory, Bayesian inference and learning alorithms. Undergraduate and post-graduate students will find it extremely useful for gaining insight into these topics." \\ REDNOVA \par "Most of the theories are accompanied by motivations, and explanations with the corresponding examples...the book achieves its goal of being a good textbook on information theory." \\ ACM SIGACT News \par \emph{Book Description} \par Information theory and inference, often taught separately, are here united in one entertaining textbook. These topics lie at the heart of many exciting areas of contemporary science and engineering - communication, signal processing, data mining, machine learning, pattern recognition, computational neuroscience, bioinformatics, and cryptography. This textbook introduces theory in tandem with applications. Information theory is taught alongside practical communication systems, such as arithmetic coding for data compression and sparse-graph codes for error-correction. A toolbox of inference techniques, including message-passing algorithms, Monte Carlo methods, and variational approximations, are developed alongside applications of these tools to clustering, convolutional codes, independent component analysis, and neural networks. The final part of the book describes the state of the art in error-correcting codes, including low-density parity-check codes, turbo codes, and digital fountain codes -- the twenty-first century standards for satellite communications, disk drives, and data broadcast. Richly illustrated, filled with worked examples and over 400 exercises, some with detailed solutions, David MacKay's groundbreaking book is ideal for self-learning and for undergraduate or graduate courses. Interludes on crosswords, evolution, and sex provide entertainment along the way. In sum, this is a textbook on information, communication, and coding for a new generation of students, and an unparalleled entry point into these subjects for professionals in areas as diverse as computational biology, financial engineering, and machine learning.},
    publisher = {Cambridge University Press},
    amazon = {http://amazon.com/dp/0521642981},
    gbooks = {http://books.google.com/books?id=AKuMj4PN_EMC},
    subject = {Computers, Computer Science, Computer Vision & Pattern Recognition, Information Theory, Neural Networks, Programming, General, Data Modeling & Design, Science, Physics, Technology & Engineering, Electronics},
    file = {pdf/201b835c3f3a3626ca07be68cc28cf7d286bf8d5.pdf},
    txt = {txt/201b835c3f3a3626ca07be68cc28cf7d286bf8d5.txt}
}

@inproceedings{
    Duvenaud2013,
    author = {Duvenaud, David K. and Lloyd, James Robert and Grosse, Roger B. and Tenenbaum, Joshua B. and Ghahramani, Zoubin},
    dblp = {http://dblp.uni-trier.de/rec/bibtex/conf/icml/DuvenaudLGTG13},
    arxiv = {http://arxiv.org/abs/1302.4922},
    title = {Structure Discovery in Nonparametric Regression through Compositional Kernel Search},
    booktitle = {ICML (3)},
    year = {2013},
    pages = {1166-1174},
    ee = {http://jmlr.org/proceedings/papers/v28/duvenaud13.html},
    crossref = {DBLP:conf/icml/2013},
    bibsource = {DBLP, http://dblp.uni-trier.de},
    oai = {arXiv.org:1302.4922},
    pdf = {http://arxiv.org/pdf/1302.4922},
    url = {http://jmlr.org/proceedings/papers/v28/duvenaud13.html},
    abstract = {Despite its importance, choosing the structural form of the kernel in nonparametric regression remains a black art. We define a space of kernel structures which are built compositionally by adding and multiplying a small number of base kernels. We present a method for searching over this space of structures which mirrors the scientific discovery process. The learned structures can often decompose functions into interpretable components and enable long-range extrapolation on time-series datasets. Our structure search method outperforms many widely used kernels and kernel combination methods on a variety of prediction tasks. \par Comment: 9 pages, 7 figures, To appear in proceedings of the 2013 International Conference on Machine Learning},
    month = {May},
    subject = {Statistics - Machine Learning, Computer Science - Learning, Statistics - Methodology, G.3, I.2.6},
    file = {pdf/57dbb4b91a2ef6a6b39cf252df860e536d373ad9.pdf},
    txt = {txt/57dbb4b91a2ef6a6b39cf252df860e536d373ad9.txt}
}

@proceedings{
    DBLP:conf/icml/2013,
    title = {Proceedings of the 30th International Conference on Machine Learning, ICML 2013, Atlanta, GA, USA, 16-21 June 2013},
    booktitle = {ICML},
    publisher = {JMLR.org},
    series = {JMLR Proceedings},
    volume = {28},
    year = {2013},
    ee = {http://jmlr.org/proceedings/papers/v28/},
    bibsource = {DBLP, http://dblp.uni-trier.de},
    url = {http://jmlr.org/proceedings/papers/v28/}
}
```

as well as a formatted bibliography `library.html` that can be viewed in a web browser:

![](https://raw.githubusercontent.com/davidar/bib/master/screen.png)
