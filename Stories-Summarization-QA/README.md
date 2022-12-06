# Stories - Summarization and Question-Answering

## Scraping
The scrapy projects to download aesop fables and short stories from reedsy are in scrapers  
1. Run "scrapy crawl BedtimeStories -o bedtimestories.jsonl" to retrieve reedsy short stories  
2. Run "scrapy crawl aesop -o aesopfables.jsonl" to retrieve aesop fables.  
  
## Scripts
1. Run AesopCreateCSV.py to clean and export aesop fables to a csv file  
2. Run CleanDataAndCreateCSV.py to clean and export reedsy short stories to a csv file  
3. The generated csv files are stored in data/aesop and data/bedtimestories respectively

## Data Annotations
1. aesopfables.csv is divided into aesopfables-train.csv and aesopfables-test.csv  
2. bedtimestories.csv is divided into bedtimestories_train.csv and bedtimestories_test.csv  
3. The above train and test files are annotated using Haystack Annotation Tool.  
4. The annotations in SQuAD format are stored in data/qa-squad.  
5. The annotations in csv format are stored in data/qa-csv.  

## Data Summarisations
1. Around 50 aesop fables are summarised and stored in aesopfables-summaries.csv for model evaluation purposes 

## Models - Summarization
1. notebooks/summarization_abstractive_bart.ipynb  
2. notebooks/summarization_abstractive_long_t5_tglobal_xl.ipynb  
3. notebooks/summarization_abstractive_pegasus.ipynb  
4. notebooks/summarization_extractive_bert.ipynb  
5. notebooks/Q_A_Summarization_pretrainedmodels.ipynb  

## Models - Question and Answering
1. notebooks/Q_A_Summarization_pretrainedmodels.ipynb  
2. notebooks/Omniscient_Reader_Finetuning_BERT.ipynb  

### ----------------------------------------- ###
### Archive ###
Summarization was done on the first chapter of Harry Potter and the Philosopher's stone using extractive summarization methods provided as part of the 'sumy' package.
1. lex_rank  
2. luhn  
3. lsa  
4. text_rank  