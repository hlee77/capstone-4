### Capstone Project: 

# Product Categorization Model

### Text & Image Based Classification Model

### Contents

- Problem Statement
- Executive Summary
- Phase 1. Data Collection
- Phase 2. Data Cleaning and EDA
- Phase 3. Preprocessing and Modeling
- Conclusion and Recommendations


###  Problem Statement

About 60% of consumers search engines to research the item before making a purchase, reportedly. (link) 
However, many products are positioned in wrong category, and consequently sellers lose chances to sell their products and to reach their potential customers as well as buyers lose chances to purchase better products at better price.
Proper categorization plays an important role in benefiting both sellers and consumers.


### Procedure
1. API Data Collecting 	Collected 25000 text + 15000 image data from eBay.com
2. Data Cleaning 	Data re-categorized based on google category taxonomy
3. Data NLP & Preprocessing	Text data NLP & Vectorization (CountVectorizer/Word2Vec)
4. Text Classification Modeling	Multinomial Bayes, KNN, Logistic Regression
5. Image Classification Modeling	Transfer Learning
6. Text & Image Classification Modeling	Ensemble Classification with Soft Voting attempted
7. Streamlit App	“Be a Best Seller – Product Categorizer” 
https://hlee77-capstone-4-text-img-classifier-xzr8hd.streamlit.app/


### 1. Data Collection
1. Amazon API – strict requirement. Got some data using an open API but limited and blocked

2. Amazon web scraping
- Selenium : able to get single data but blocked
- Beautifulsoup : able to get single data but blocked

3. eBay web scraping
- Before obtaining API key, worked on this using Beautifulsoup.

4. eBay API
- Collected 25,000 product data & 15,000 image data 



### 2. Data Cleaning

#### Data re-categorization
- Re-categorized based on google category taxonomy
- Common categories are selected and some uncommon categories are removed:

28 Main Categories, 3841 Sub-Categories, 25,000 products
==> 16 Categories, 22,000 products


**eBay categories:**
Clothing, Shoes & Accessories
Art
Stamps
Musical Instruments & Gear
Baby
Business & Industrial
Cameras & Photo
Consumer Electronics
Cell Phones & Accessories
Computers/Tablets & Networking
Health & Beauty
Home & Garden
Pottery & Glass
Travel/luggage
Books & Magazines
Music
Business & Industrial
Pet Supplies
Sporting Goods
Sports Mem, Cards & Fan Shop
Toys & Hobbies
Dolls & Bears
Video Games & Consoles
eBay Motors
Jewelry & Watches
Gift Cards & Coupons

**Google categories(25):**
Apparel & Accessories
Arts & Entertainment
Baby & Toddler
Business & Industrial
Cameras & Optics
Electronics
Food, Beverages & Tobacco
Furniture
Hardware
Health & Beauty
Home & Garden
Luggage & Bags
Mature
Media 
Office Supplies
Pet Supplies 
Software
Sporting Goods 
Toys & Games 
Vehicles & Parts
Jewelry & Watches

**Classification model categories(15):**
Apparel_Accessories
Arts_Entertainment
Baby_Toddler
Business_Industrial
Cameras_Optics
Consumer Electronics
Cell Phones
Computers_Tablets
Health_Beauty
Home_Garden
Pet Supplies
Sporting Goods 
Toys_Games 
Vehicles
Jewelry_Watches


### 3. Data Preprocessing
- After cleaning: 21,579 products with 15 categories

- Toys & Games: 13.8% (baseline accuracy)

Toys_Games              0.138746
Arts_Entertainment      0.092358
Home_Garden             0.091988
Sporting Goods          0.087492
Pet Supplies            0.069466
Jewelry_Watches         0.069419
Apparel_Accessories     0.065434
Vehicles                0.065341
Baby_Toddler            0.046249
Business_Industrial     0.046249
Computers_Tablets       0.046249
Health_Beauty           0.046156
Consumer Electronics    0.046110
Cameras_Optics          0.046110
Cell Phones             0.042634


### 4. Modeling Process

#### 1) Text Classification
**Vectorizer:**
- Count Vectorizer
- Tfidf Vectorizer
- Word2Vec

**Classifier**
- K-Neighbors Classifier
- Multinomial NB
- Logistic Regression
- Random Forest

**Results**
	MNB	LGR	SGD	KNN	RF
Train	93	1	94	82	1
Text	85	92	87	73	64
CrossV	85	92	88	69	88
ACC	86	92	87	64	64


#### 2) Image Classification

**Transfer Learning**
- Basic Network
- EfficientNet

- Conv2D
- MaxPooling 2D
- Dense (3)
- Epoch 20

#### 3) Text & Image based Classification
CV & Logistic Regression + Transfer Learning
==> Ensemble Classification with Soft Voting

- Was not able to find a way to put two different inputs (text, image) in Ensemble model.


### 6. APP Deployment

- Streamlit App	“Be a Best Seller – Product Categorizer” 
https://hlee77-capstone-4-text-img-classifier-xzr8hd.streamlit.app/



### Problems
- Text-Image based classification was not implemented due to technical issue: an Ensemble classification model includes multiple models but with the same inputs. 
- Many of eBay product images are uploaded by small business, so they are not professional and unclear. Clearer image data needed for better training.
- Ambiguous product title cannot be correctly classified.
- Ambiguous Categories:  it is hard to distinguish the upper categories due to many lower categories of the same name. (such as pants under Apparel, Baby & Toddler, and Sporing Goods)

###  Recommendations

- Product naming need to represent the product for better classification. (With more description (such as brand, spec), text modeling will be more sophisticated.)
- Clearer product images are recommended for better categorization and for better representation.


### Next Steps

- It is expected to implement more detailed categorization including sub-categories is expected. In order to do so, more data and time is needed to be obtained and trained.
- eBay product description is limited to product tile. The model can be improved a lot if more data such as brand, spec, or more details about products. 
- So if the model is trained with other shopping mall data, such as Amazon, the model can be more powerful and sophisticated categorization model.



#### Citations
eBay API & developer https://developer.ebay.com/
google product category taxonomy list
https://www.google.com/basepages/producttype/taxonomy.en-US.txt
Google Marketing Strategies
https://www.thinkwithgoogle.com/marketing-strategies/search/global-shopper-product-research-statistics/


  
