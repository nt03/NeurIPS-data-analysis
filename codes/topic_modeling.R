############### Topic Modeling with STM package #################

# clear environment
rm(list = ls())

# load in packages
library(quanteda)
library(SpeedReader)
library(Rcpp)
library(ggplot2)
library(beepr)

# for running topic models:
# install.packages("stm",dependencies = TRUE)
library(stm)

### insert destination filepath
path <- "filepath"

#read in data
df = read.csv(file = paste0(path, "data_p1.csv"),
              stringsAsFactors = FALSE)

#subset the data to keep relevant columns
df <- df[, c("main_track", "year", "id", "text")]

#set data type
df$text <- as.character(df$text)
df$year <- as.factor(df$year)
df$main_track <- as.factor(df$main_track)


# note that we need to specify a docid field and a text field
corp <- corpus(df,
               docid_field = "id",
               text_field = "text",
               metacorpus = list(source = "scientific paper abstracts corpus"))



# create a dfm object
dtm <- dfm(corp,
           remove_punct = TRUE,
           remove_numbers = TRUE,
           remove = stopwords("english"))


# look at number of features:
dtm


# in order to do some preliminary checks, lets convert our quanteda dfm object
# into an stm object. 
check <-quanteda::convert(dtm,
                          to = "stm")



# trim terms that appear very infrequently, and terms that appear in
# the overwhelming majority of documents:
dtm <- dfm_trim(dtm,
                min_termfreq = 5,
                max_docfreq = 700)


# look at number of features again:
dtm


# convert this to an stm object and pull out some variables for use later:
out <- quanteda::convert(dtm,
                         to = "stm")

docs <- out$documents
vocab <- out$vocab
meta <- out$meta


# lets fit a simple topic model with 8 topics, and the default
# hyperparameters using the STM package. The stm package will fit this topic
# model using a variational approximation 
# STM with no covariate effect

lda_fit <- stm(dtm,
               K = 8,
               seed = 12345,
               verbose = TRUE)
beep(5)


# we can start by looking at the top 8 terms in each of the topics,
# along with thier overall proportion in the corpus:
pdf(file =  paste0(path,"Topic_Summaries.pdf"),
    width = 12,
    height = 7)
plot.STM(lda_fit,
         type="summary",
         n = 8)
dev.off()


# we can also just display the top 20 words in each topic:
pdf(file =  paste0(path, "Topic_Words.pdf"),
    width = 8,
    height = 11)
plot.STM(lda_fit,
         type="labels",
         topics = 1:8)
dev.off()



# finally we can get out estimates of topic correlcations within documents:
cors <- topicCorr(lda_fit)

# and make a network plot:
plot(cors)


############ STM with Covariate effect  ################


#adding the text length variable
df$count <- sapply(strsplit(df$text, " "), length)


# fit a topic model with covariate effects.
stm_fit <- stm(dtm,
               prevalence = as.formula("~year+ count"),
               content = as.formula("~main_track"),
               data = docvars(dtm), 
               K = 8, #number of topics
               seed = 12345,
               verbose = TRUE)


# we can start by looking at the top 8 terms in each of the topics,
# along with thier overall proportion in the corpus:
pdf(file = paste0(path, "Topic_Summaries.pdf"),
    width = 15,
    height = 10)
plot.STM(stm_fit,
         type="summary",
         n = 8)
dev.off()