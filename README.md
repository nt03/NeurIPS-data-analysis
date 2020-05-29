## AI conference papers Analysis Project

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

**Update**:    

The all_conferences.xlsx and conference_list.md detail the AL/ML conferences that were considered. The `/codes/codes/other scraping codes/` subdirectory contains the scraping codes for some of these other conferences. 


#### 2. Selection

Next, we review the results and decide which conferences to target for data
collection. A leading consideration is the difficulty of gathering identifying
data on conference papers. It may be possible to acquire the data we need from
conference organizers, or it might be necessary to scrape it.

**Update**:    

The project scope was limited to NeurIPS (2016-2019) for analysing use of track labels as corpus classification criteria. 

#### 3. Papers

For each paper from the selected conferences, we want metadata that allows us to
identify a corresponding record in Web of Science or Dimensions.  We also want
any conference-specific metadata available, and in particular the series or
track under which the paper appeared. If the paper itself is easily available
and we're writing a scraper, we'll try to collect the full text in some form
too.

**Update**:   

The metadata for NeurIPS was successively collected is in documented and analysed in the `/code`, `/data` and `/plots` subdirectories. 
 
 
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

**Update**:     

Using NeurIPS 2019 track labels an attempt was made to create parent 9 `main_track` labels for previous conference years (2016-2019). 


#### 5. Linkage

Given conference-paper metadata, we can attempt to identify matching papers in
Web of Science or Dimensions. The point of doing this is to place the labeled
papers in the citation graph these datasets define.

**Update**: 

Not attempted


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

**Update**:      

After wrangling the data to accomodate the parent labels supervised and unsupervised techniques were used to assess using these labels as a classification criteria. We trained the models on a section of corpus and validated it against a reserved test dataset. The model accuracy (across multiple models) (AUC) averaged ~ 55% at best. The unsupervised Topic Modeling technique was used to identify any latent topics occuring in the corpus to devise any future classes in a more organic manner. The outcomes in the form of top occuring terms across topics still need to be validated using domain knowledge of AL/ML topics. 

**Conclusion:**     

The supervised techniques to classify the conference paper corpus using track labels did not yield good results. This could be potentially attributed to:
- Lack of coherence in track assignment,
- Less than optimal training data per track

Topic Modeling could be a better way to classify the papers to accomodate evolving nature of tracks and paper content. However, constantly changing topics (over the years) may not be most helpful in building a homogenous classification criteria across the conference papers ecosystem. 
