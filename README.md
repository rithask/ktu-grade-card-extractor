# KTU Grade Card Extractor

Extract info from KTU Semester Grade Card PDFs

# How it works

This app uses [camelot](https://github.com/camelot-dev/camelot) Python library to extract tabular data from PDFs. The KTU Semester Grade Card should contain two tables which consists of the personal informations like name, college, branch etc and result for that semester. The PDF is ony stored temporarily and is deleted after processing it. No data is send to anywhere nor stored anywhere.

The PDF should look like [this](<grade card.pdf>)
