<h1><left>SAVE WORLD: Using Natural Language Processing to identify suicidal posts</left></h1>

___

>"*Suicide doesn’t end the chances of life getting worse, it eliminates the possibility of it ever getting any better.*"


The WHO recommends that countries craft a national suicide prevention strategy that includes creating initiatives that aim at "early identification of groups vulnerable to the risk of suicide".



### Two subreddits with a subtle difference
We needed to choose two subreddits that will yield us suitable data to identify individuals at risk.

On reddit, we found two communities for depression and suicide.These are our two subreddits and their *tag-lines*(which hint at their mission statements):

> **r/depression**: because nobody should be alone in a dark place

> **r/SuicideWatch**: Peer support for anyone struggling with suicidal thoughts.



The project is structured into following three notebooks:

```
SAVE WORLD: Using Natural Language Processing to identify suicidal posts
|__ code
|   |__ 01_Data_Collection.ipynb   
|   |__ 02_Data-Cleaning_Pre-processing_EDA.ipynb   
|   |__ 03_Modelling.ipynb 
|__ data
|   |__ combined_data.csv
|   |__ data_for_model.csv
|   |__ depression.csv
|   |__ suicide_watch.csv
|__ images
|   |__ (various_images_used_for_masking)
|__ HTML_corpus.html
|__ README.md
```


### Visualisations
<img src="./assets/a_wordcloud_readme.png" style="float: center; margin: 50px; width:800px;"> 
<img src="./assets/a_scattertext_readme.png" style="float: center; margin: 50px; width:800px;">
