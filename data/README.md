**filename description**:

1. `nips_scraped.csv`: scraped data from NIPS conference website, strucutured
2. `nips_cleaned.csv`: post-EDA after dropping very unbalanced tracks, used for modeling
3. `nips_with_track_cleaned.csv`: dataset with "main_track" column created
4. `nips_yearwise_trackinfo.csv`: yearwise "original_track", "main_track" and "track" information key
5. `maintrack_abs_cleaned.csv`: text data aggregated across the "main_track" column for EDA
6. `/fastbert/labels.csv`: label information for the dataset
6. `/fastbert/train.csv`: train dataset for fastbert
8. `/fastbert/test.csv`: test dataset for fastbert


**Data Dictionary**:
1. `title`: Title of the paper
2. `abstract`: Author supplied abstract
3. `year`: conference year 
4. `pdf_link`: URL to the paper 
5. `track`: the original conference supplied track information in `nips_scraped.csv` (referred to as `original_track` in other CSVs) and cleaned track (under parent main_track) for other data files
6. `original_track`: conference supplied track label eg. "(Application) Bioinformatics and Systems Biology" 
7. `main_track`: parent track for `track` column created by me using 2019 track labels for eg. main_track is "Application" for above example
8. `text`: `abstract` and `title` columns concatenated to create a composite text column
