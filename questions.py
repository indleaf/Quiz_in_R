question_bank = [

# =========================
# EASY (1–20)
# =========================

{"question": "What is the main goal of association rule mining?",
 "options": ["Predict numerical values", "Find relationships between items", "Perform classification", "Cluster users"],
 "answer": [2], "is_multiple": False},

{"question": "What is another name for association rule mining?",
 "options": ["Regression analysis", "Market basket analysis", "Time series analysis", "Neural mining"],
 "answer": [2], "is_multiple": False},

{"question": "In the rule {X} → {Y}, what does X represent?",
 "options": ["Consequent", "Transaction", "Antecedent", "Support"],
 "answer": [3], "is_multiple": False},

{"question": "What does support measure in association rules?",
 "options": ["Strength of prediction", "Frequency of an itemset", "Rule direction", "Profitability"],
 "answer": [2], "is_multiple": False},

{"question": "What does confidence measure?",
 "options": ["Frequency of X", "Probability of Y given X", "Total transactions", "Profit margin"],
 "answer": [2], "is_multiple": False},

{"question": "Which algorithm is commonly used to generate frequent itemsets?",
 "options": ["K-means", "Apriori", "ARIMA", "Naive Bayes"],
 "answer": [2], "is_multiple": False},

{"question": "What type of learning is K-means?",
 "options": ["Supervised", "Unsupervised", "Reinforcement", "Deep learning"],
 "answer": [2], "is_multiple": False},

{"question": "What does 'k' represent in K-means?",
 "options": ["Number of features", "Number of clusters", "Number of records", "Number of iterations"],
 "answer": [2], "is_multiple": False},

{"question": "What is the output of a convolution operation in a CNN called?",
 "options": ["Kernel", "Feature map", "Filter", "Stride"],
 "answer": [2], "is_multiple": False},

{"question": "What is the primary purpose of pooling in CNNs?",
 "options": ["Increase dimensions", "Reduce dimensions", "Increase weights", "Normalize data"],
 "answer": [2], "is_multiple": False},

{"question": "Which type of pooling selects the maximum value?",
 "options": ["Average pooling", "Min pooling", "Max pooling", "Global pooling"],
 "answer": [3], "is_multiple": False},

{"question": "What is a time series?",
 "options": ["Random data", "Cross-sectional data", "Data over time", "Image data"],
 "answer": [3], "is_multiple": False},

{"question": "Which component represents long-term increase or decrease in time series?",
 "options": ["Noise", "Trend", "Seasonality", "Irregularity"],
 "answer": [2], "is_multiple": False},

{"question": "Which component represents repeated short-term patterns?",
 "options": ["Trend", "Cycle", "Seasonality", "Noise"],
 "answer": [3], "is_multiple": False},

{"question": "Which model requires stationary data?",
 "options": ["K-means", "CNN", "ARIMA", "Apriori"],
 "answer": [3], "is_multiple": False},

{"question": "What does ADF test check?",
 "options": ["Normality", "Stationarity", "Accuracy", "Clustering quality"],
 "answer": [2], "is_multiple": False},

{"question": "Which method stabilizes variance in time series?",
 "options": ["Differencing", "Log transformation", "Smoothing", "Clustering"],
 "answer": [2], "is_multiple": False},

{"question": "Which moving average is best for visualization?",
 "options": ["Trailing", "Centered", "Weighted", "Exponential"],
 "answer": [2], "is_multiple": False},

{"question": "Which smoothing method gives more weight to recent values?",
 "options": ["Moving average", "Simple exponential smoothing", "Regression", "Seasonal smoothing"],
 "answer": [2], "is_multiple": False},

{"question": "What does early stopping help prevent?",
 "options": ["Underfitting", "Overfitting", "Bias", "Noise"],
 "answer": [2], "is_multiple": False},


# =========================
# MEDIUM (21–40)
# =========================

{"question": "If support(X,Y)=4 and support(X)=6, what is the confidence of X→Y?",
 "options": ["66.7%", "57.1%", "100%", "40%"],
 "answer": [1], "is_multiple": False},

{"question": "What does a lift ratio greater than 1 indicate?",
 "options": ["Negative relationship", "Random association", "Stronger-than-random association", "High support only"],
 "answer": [3], "is_multiple": False},

{"question": "Which step comes first in the K-means algorithm?",
 "options": ["Assign clusters", "Select k", "Update centroids", "Compute distances"],
 "answer": [2], "is_multiple": False},

{"question": "What is the role of centroids in K-means?",
 "options": ["Store labels", "Represent cluster centers", "Normalize data", "Eliminate noise"],
 "answer": [2], "is_multiple": False},

{"question": "Which ARIMA component removes trend?",
 "options": ["AR", "MA", "I", "Q"],
 "answer": [3], "is_multiple": False},

{"question": "Which ARIMA component models past errors?",
 "options": ["AR", "MA", "I", "D"],
 "answer": [2], "is_multiple": False},

{"question": "Which plot helps determine ARIMA parameters?",
 "options": ["Histogram", "Boxplot", "ACF & PACF", "Scatterplot"],
 "answer": [3], "is_multiple": False},

{"question": "Which CNN operation introduces non-linearity?",
 "options": ["Pooling", "Convolution", "ReLU", "Flattening"],
 "answer": [3], "is_multiple": False},

{"question": "Which factor does NOT affect feature map size?",
 "options": ["Filter size", "Stride", "Padding", "Epochs"],
 "answer": [4], "is_multiple": False},

{"question": "Which learning method reuses a pre-trained model?",
 "options": ["Deep training", "Transfer learning", "Batch learning", "Online learning"],
 "answer": [2], "is_multiple": False},

{"question": "Which CNN model popularized deep learning in 2012?",
 "options": ["VGG", "AlexNet", "ResNet", "MobileNet"],
 "answer": [2], "is_multiple": False},

{"question": "Which dataset was AlexNet trained on?",
 "options": ["MNIST", "CIFAR-10", "ImageNet", "COCO"],
 "answer": [3], "is_multiple": False},

{"question": "Which neural network is best for sequential data?",
 "options": ["CNN", "RNN", "KNN", "SVM"],
 "answer": [2], "is_multiple": False},

{"question": "Which data type is best suited for RNN?",
 "options": ["Tabular", "Image", "Sequential", "Categorical"],
 "answer": [3], "is_multiple": False},

{"question": "Which smoothing method is poor at handling seasonality?",
 "options": ["Regression", "Simple moving average", "ARIMA", "Fourier transform"],
 "answer": [2], "is_multiple": False},

{"question": "What happens when window size is too large?",
 "options": ["Under-smoothing", "Over-smoothing", "No smoothing", "Overfitting"],
 "answer": [2], "is_multiple": False},

{"question": "Which smoothing method produces identical future forecasts?",
 "options": ["Centered MA", "Trailing MA", "Regression", "ARIMA"],
 "answer": [2], "is_multiple": False},

{"question": "Which process removes trend only?",
 "options": ["Differencing", "Detrending", "Logging", "Pooling"],
 "answer": [2], "is_multiple": False},

{"question": "Which ARIMA parameter controls differencing order?",
 "options": ["p", "d", "q", "α"],
 "answer": [2], "is_multiple": False},

{"question": "Which technique prevents CNNs from remembering exact pixel positions?",
 "options": ["Padding", "Pooling", "Stride", "Flattening"],
 "answer": [2], "is_multiple": False},


# =========================
# HARD (41–60)
# =========================

{"question": "Which condition defines a stationary time series?",
 "options": ["Constant mean and variance", "Increasing trend only", "Seasonality only", "Random variance"],
 "answer": [1], "is_multiple": False},

{"question": "What is the formula for differencing?",
 "options": ["Yt – Yt-1", "Yt / Yt-1", "Yt × Yt-1", "Yt + Yt-1"],
 "answer": [1], "is_multiple": False},

{"question": "Which ARIMA model is written as ARIMA(p,d,q)?",
 "options": ["Regression model", "Moving average model", "Combined AR, I, MA model", "Clustering model"],
 "answer": [3], "is_multiple": False},

{"question": "Which K-means step repeats until convergence?",
 "options": ["Initialization", "Distance calculation and centroid update", "Selecting k", "Normalizing data"],
 "answer": [2], "is_multiple": False},

{"question": "Which clustering weakness makes K-means sensitive?",
 "options": ["Initialization", "Distance metric", "Outliers", "All of the above"],
 "answer": [4], "is_multiple": False},

{"question": "What does early stopping monitor?",
 "options": ["Training accuracy", "Training loss only", "Validation loss", "Batch size"],
 "answer": [3], "is_multiple": False},

{"question": "Which CNN layer usually comes after convolution?",
 "options": ["Dense", "Pooling", "Flatten", "Dropout"],
 "answer": [2], "is_multiple": False},

{"question": "Which parameter shifts convolution window?",
 "options": ["Kernel", "Stride", "Padding", "Depth"],
 "answer": [2], "is_multiple": False},

{"question": "What does padding help preserve?",
 "options": ["Feature depth", "Original image size", "Training speed", "Kernel size"],
 "answer": [2], "is_multiple": False},

{"question": "Which network stores past information through memory?",
 "options": ["CNN", "RNN", "KNN", "SVM"],
 "answer": [2], "is_multiple": False},

{"question": "What is the depth of a feature map equal to?",
 "options": ["Stride", "Number of filters", "Input width", "Kernel size"],
 "answer": [2], "is_multiple": False},

{"question": "What determines overfitting in early stopping?",
 "options": ["Training loss decreasing only", "Validation loss increasing", "High learning rate", "Low batch size"],
 "answer": [2], "is_multiple": False},

{"question": "Which CNN architecture uses skip connections?",
 "options": ["AlexNet", "VGG-16", "ResNet", "MobileNet"],
 "answer": [3], "is_multiple": False},

{"question": "Which smoothing parameter controls SES responsiveness?",
 "options": ["β", "γ", "α", "δ"],
 "answer": [3], "is_multiple": False},

{"question": "What happens when α is close to 1 in SES?",
 "options": ["More weight to older values", "More weight to recent values", "Equal weights", "No smoothing"],
 "answer": [2], "is_multiple": False},

{"question": "Which type of moving average suppresses seasonality best?",
 "options": ["Short window", "Long window", "Weighted", "SES"],
 "answer": [2], "is_multiple": False},

{"question": "Which method combines regression and MA forecasting?",
 "options": ["ARIMA hybrid", "Detrending + MA", "Clustering regression", "CNN regression"],
 "answer": [2], "is_multiple": False},

{"question": "Which clustering validation method is commonly used with K-means?",
 "options": ["Elbow method", "ROC curve", "Lift ratio", "ADF test"],
 "answer": [1], "is_multiple": False},

{"question": "Which feature map dimension corresponds to number of filters?",
 "options": ["Height", "Width", "Depth", "Stride"],
 "answer": [3], "is_multiple": False},

{"question": "Which dataset characteristic is required for RNN?",
 "options": ["Image structure", "Temporal dependency", "Independence", "Static patterns"],
 "answer": [2], "is_multiple": False}

]
