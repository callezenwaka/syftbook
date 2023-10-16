# Contributing a new Jupyter Notebook

Differential privacy is a technique used to protect the privacy of individuals in a dataset. It is a mathematical framework that provides strong privacy guarantees while still allowing useful analysis of the data. OpenMined is an open-source stack that provides secure and private data science in Python. It decouples private data from model training using techniques such as federated learning, differential privacy, and encrypted computation. OpenMined's PyDP library provides an easy-to-use interface for working with differential privacy in Python.

To learn more about differential privacy, you can visit the [OpenMined Blog](https://blog.openmined.org/privacy-series-basics-definition/) or the [PyDP documentation](https://openmined.github.io/PyDP/introduction.html). To get started with OpenMined and PyDP, you can visit the [OpenMined website](https://www.openmined.org/) or the [PyDP GitHub repository](https://github.com/OpenMined/PyDP).

I hope this helps!
## Topics

Source: Conversation with Bing, 10/15/2023
- Local vs Global Differential Privacy - OpenMined Blog. https://blog.openmined.org/basics-local-differential-privacy-vs-global-differential-privacy/.
- Introduction To Differential Privacy — PyDP 1.1.1 documentation. https://openmined.github.io/PyDP/introduction.html.
- Privacy Series Basics: Definition - OpenMined Blog. https://blog.openmined.org/privacy-series-basics-definition/.
-  How to convert a text document into .md(markdown) file. https://stackoverflow.com/questions/71792638/how-to-convert-a-text-document-into-mdmarkdown-file.
- Online TEXT to MARKDOWN Converter - Vertopal. https://www.vertopal.com/en/convert/text-to-markdown.
- How to Convert a Word Document to Markdown Format. https://www.epiphanydigest.com/2020/06/12/how-to-convert-a-word-document-to-markdown-format/.
- Online Markdown Editor - Dillinger, the Last Markdown Editor ever.. https://dillinger.io/.
- TXT to MD | CloudConvert. https://cloudconvert.com/txt-to-md.
- undefined. https://www.npmjs.com/package/markdown-to-txt.

## Building the site

### Create a conda environment

The first time you check out this repository, run:

```bash
conda env update -f environment.yml
```

This will create or update the dev environment (`pythia-book-dev`).

### Install `pre-commit` hooks

This repository includes `pre-commit` hooks (defined in `.pre-commit-config.yaml`). To activate/install these pre-commit hooks, run:

```bash
conda activate pythia-book-dev
pre-commit install
```

This is also a one-time step.

### Building the book locally

To build the book locally, run the following:

```bash
conda activate pythia-book-dev
jupyter-book build .
```

Finally, you can view the book by opening the file `_build/html/index.html` with your favorite web browser. On most platforms you can simply run:

```bash
open _build/html/index.html
```

### Keeping your dev environment up to date

It's good practice to update the packages in your `pythia-book-dev` conda environment frequently to their latest versions, especially if it's been a while since you used it. If the `jupyter-book build .` command above generates error messages, that is a good indication that your conda environment may be out of date.

To update all packages in the currently activated environment to their latest versions, do this:

```bash
conda update --all
```

