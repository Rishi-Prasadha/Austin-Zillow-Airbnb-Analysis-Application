# Austin Zillow/Airbnb Analysis Application

This application starts off by analyzing Zillow data. We begin by training a linear regression model on the Great Recession of 2007-2009 to determine if we are capable of building an application that can help real estate investors decide to either purchase or wait to purchase propwerty in Austin. We then look at what areas of Austin seem to do the best for Airbnb. We look at the average pricing to determine that. Although our Zillow linear regression models were less than satisfactory; using the Airbnb data we were still able to make recommendations on which zip codes are currently best to invest in for prospective real estate investors. 

---

## Technologies

This application is written in Python. The main Python libraries used are 
* [Pandas](https://github.com/pandas-dev/pandas)
* [Numpy](https://github.com/numpy/numpy)
* [hvplot](https://github.com/holoviz/hvplot)

---

## Libraries

This analysis used extensive plotting with the hvplot library. Import statements already present in program, refer to them below:

```python
import numpy as np
import pandas as pd
import hvplot.pandas
import numpy as np
import math
```

---

## Installation Guide

Before running the above libraries, you will need to install them first. 

To install Pandas, go to your terminal and run the following command:

`pip install pandas`

To install Numpy, go to your terminal and run the following command:

`pip install numpy`

To install hvplot, go to your terminal and run the following command:

`pip install hvplot`

---

## Usage

All analysis were done on a Jupyter Notebook, so as long as the above packages have been installed in the dev environment, these notebooks will run smoothly. You can go through the graphs and widgets to see what types of houses and what areas of Austin are most profitable. 

---

## Results 

<img width="1399" alt="Screen Shot 2022-08-04 at 13 16 07" src="https://user-images.githubusercontent.com/107497500/182984555-c1f23ac3-5a59-4ac1-99d0-cc0e725608bd.png">

The black lines in the middle of the bars indicate the price of homes predicted by the regression model. As a result it can be concluded that our models consistenly, across all three months and all zip codes, consistently under predicts the value of homes in said zip code. In terms of numbers we are looking at a 60-70% change between the predicted experimental model and the actual data. As a result we are confident in moving forward and using the derived models for any predictive capability.

---
## Contributors

Brittanie Polasek, Rishi Prasadha, and Quinn Strobe

---

## License

MIT
