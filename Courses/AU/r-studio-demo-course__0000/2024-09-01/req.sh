#!/bin/bash

sudo apt-get -o Acquire::AllowInsecureRepositories=true -o Acquire::AllowDowngradeToInsecureRepositories=true update && \
sudo apt-get install -y libssl-dev liblzma-dev libbz2-dev libicu-dev && sudo apt-get clean


R -e "install.packages('BiocManager', repos='http://cran.us.r-project.org'); \
           update.packages(ask=F); \
           BiocManager::install(c('gplots','plotly'),ask=F)"