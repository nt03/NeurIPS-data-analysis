# NeurIPS-data-analysis
Collection, cleaning and classification analysis of NeurIPS conference data.

## AI conference papers

This repo contains materials for identifying AI-relevant research publications
using conference metadata. Our motivation is to better understand the boundaries
of AI as defined by conference organizers and participating researchers.

### Data collection

#### 1. Conferences

Our first step is identifying conferences where we can find papers of interest.
At this stage, it's better to be inclusive if uncertain about a conference. We
can filter some conferences out later and will prioritize further data
collection appropriately. Some possible starting points: existing lists of AI or
ML conferences; Springer conference proceedings series; and references to
conferences in Google Scholar results (e.g., "Prepared for the 11th meeting of
...").

The output from this search is a table (as a CSV in this repo) in which each
each row describes a conference.

| name    | year | description | url                 | notes                    |
| --      | --   | --          | --                  | --                       |
| NeurIPS | 2019 | todo        | https://neurips.cc/ | Previously known as todo |
| --      | --   | --          | --                  | --                       |


TODO [JD]: add conferences from CSET conference tracker

#### 2. Selection

Next, we review the results and decide which conferences to target for data
collection. A leading consideration is the difficulty of gathering identifying
data on conference papers. It may be possible to acquire the data we need from
conference organizers, or it might be necessary to scrape it.

#### 3. Papers

For each paper from the selected conferences, we want metadata that allows us to
identify a corresponding record in Web of Science or Dimensions.  We also want
any conference-specific metadata available, and in particular the series or
track under which the paper appeared. If the paper itself is easily available
and we're writing a scraper, we'll try to collect the full text in some form
too.
 
#### 4. Tracks

We review the names of tracks across conferences and attempt to reconcile
differences. This could result in an ontology in which general conferences
contribute high-level areas like "computer vision" and specialized conferences
further define these higher-level areas. Our goal is to derive canonical labels
for tracks and in turn the papers they included. This structure may be
interesting in itself, and not just a vehicle for labeling papers. This task
depends on (1) and (2), but not necessary (3). We can probably gather track
names more easily than papers. Some specialized conferences may not have tracks,
and that's okay.

#### 5. Linkage

Given conference-paper metadata, we can attempt to identify matching papers in
Web of Science or Dimensions. The point of doing this is to place the labeled
papers in the citation graph these datasets define.

### Analysis

* Using the output of (4), we can describe the conference topic space. (TODO:
  think about embeddings.)

* With (4) and (3) or (5), i.e., using a dataset of paper metadata and
  associated track labels, we can develop models to identify papers in Web of
  Science and Dimensions similar to those from conferences.

* We'll use the conference papers as a gold corpus for evaluation of other
  subject classifiers (e.g., the arXiv-trained classifier).

* After linkage with Web of Science or Dimensions records, we can use conference
  papers as starting points for walking the citation graph to identify related
  papers. This could leverage Ilya's communities of practice work and similarity
  measures. 

In addition to supporting these analytic goals, completing the work described
here should result in a standalone paper.
