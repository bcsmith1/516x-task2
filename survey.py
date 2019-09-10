import pandas as pd
url = "https://raw.githubusercontent.com/isu-abe/516x/master/data/surveys1977.csv"
survey = pd.read_csv(url, sep = ",")
survey.head()
survey.describe()
