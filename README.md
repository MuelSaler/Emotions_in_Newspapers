# Emotions_in_Newspapers
This project was created during the hackathon culture.explore(data) @ Staatsbibliothek Berlin. I used a classifier for emotions developed by Leonard Konle et al. @ University Würzburg to analyse emotions in the German newspaper "Der Tag" between 1911 and 1919. I thank my team mates Alvaro, Fernanda, Jakub, Karin and Tim for their help.

1. Download data set https://lab.sbb.berlin/on-this-day/
2. Run DataPrep (xml to txt, normalization, txt to tsv (columns: id (from file name), text, year (from id), era1 (from year), era2 (from year)))
3. Go to https://github.com/LeKonArD/Gattungen_und_Emotionen_dhd2023 and follow the instructions. Use your tsv-file from 2. as input file.
4. Return to DataPrep and merge results to one tsv. The classifier seems to have problems with single word lines -> delete them. Add metadata colums to differentiate a pre Hugenberg and a post Hugenberg era aswell as a pre war, war and post war era.
5. Run Visualization for better understanding of results and information about significance.
