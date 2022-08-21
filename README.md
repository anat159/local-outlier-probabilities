## Local Outlier Probabilities
Implementing the article 'LoOP: Local Outlier Probabilities'.
The article is attached under the name 'LoOP.pdf'
# Intrudction
LoOP is unsupervised outlier detection method which compute a scoring includes normalization to each point in the dataset mapped into the range [0,1].
In this method  the score of abnormality of one sample is compared with the scores of its neighbors.
![LoOP](https://user-images.githubusercontent.com/71435004/178737862-abe70e5c-5bf5-40aa-b5d2-9a04b5dfb778.jpeg)

# Discussion
* The number of neighbors should be carefully chosen since big K may contain outliers influencing the mean accordingly. Therefore, calculating the variance might be considered.
 The disadvantage of small k is that a point may be an outlier considering other points but not to a cloud of points.
 
 * A cloud of outliers in some direction is problematic since if a point is an outlier considering her set, the chance that her neighbor will be an outlier concerning her set is smaller.
 
* The author uses ROC-AUC for an unbalanced dataset, other metrics, such as PR-AUC will demonstrate the contribution of the algorithm better.

# Instructions
To run this code:

1.Make a new virtual environment with the packages attached at "requirments.txt" 

2.Run "LoOP.ipynb"
