{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "4423e04c",
   "metadata": {},
   "source": [
    "# Data Analysis of Regenerative Farming "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "61fe1128",
   "metadata": {},
   "source": [
    "### Tasks\n",
    "\n",
    "1) Load a dataset using Pandas and perform data cleaning operations such as removing null values, removing duplicates,number format etc.\n",
    "\n",
    "2) Use Pandas to calculate summary statistics for a dataset, such as mean, median, and standard deviation.\n",
    "\n",
    "3) Create a scatter plot using Matplotlib to visualize the relationship between two variables in a dataset.\n",
    "\n",
    "4) Use Pandas to group the data by a categorical variable and calculate summary statistics for each group.\n",
    "\n",
    "5) Create a line chart using Matplotlib to visualize the trend of a variable over time.\n",
    "\n",
    "6) Use Pandas to merge two datasets together based on a common key (try this function - merge(table1, table2, on='Column1', how='inner').\n",
    "\n",
    "7) Create a box plot to visualize the distribution of a variable across different categories.\n",
    "\n",
    "8) Create a histogram using Matplotlib to visualize the distribution of a variable in a dataset."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "371dd07e",
   "metadata": {},
   "source": [
    " ## 0. Introduction\n",
    "    \n",
    "In this analysis, we will be examining the effects of no tillage on crop yields in Kenya. No tillage is a farming practice that involves not digging soil, which helps to maintain soil structure, improves irrigation, and supports soil microorganisms. We will be looking at the impact of this practice on different crops grown in Kenya, and comparing it to traditional farming methods that involve tilling.\n",
    "\n",
    "The main variable of interest is 'percentChange', which measures the change in crop yield compared to traditional farming practices. Positive values indicate an increase in yield, while negative values suggest a decrease. We will be analyzing this variable to see how much of a difference no tillage makes in crop yields.\n",
    "\n",
    "The data comes from various studies and has been aggregated by The Knowledge Network for Biocomplexity (KNB) and agevidence.org.\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "654b9899",
   "metadata": {},
   "source": [
    "### Data sources:\n",
    "- Kenya: [http://www.agevidence.org/#/kenya](http://www.agevidence.org/#/kenya)\n",
    "- USA: [http://www.agevidence.org/#/us-corn-belt](http://www.agevidence.org/#/us-corn-belt)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e07d5a8",
   "metadata": {},
   "source": [
    "## 1. Data cleaning"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91284508",
   "metadata": {},
   "source": [
    "This code creates a subset from a larger dataset that focuses on tillage as the primary study parameter. We will then extract the yield data for different crop types."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "2ee3aca8",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import warnings\n",
    "warnings.simplefilter(action='ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8f325354",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_kenya = pd.read_csv(\"data_kenya.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b9cb63eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['review',\n",
       " 'rv',\n",
       " 'rvYear',\n",
       " 'rvUnits',\n",
       " 'startYear',\n",
       " 'studyLength',\n",
       " 'sampleDepth',\n",
       " 'controlValue',\n",
       " 'trtValue',\n",
       " 'percentChange',\n",
       " 'norm',\n",
       " 'studyduration',\n",
       " 'croptype',\n",
       " 'control',\n",
       " 'treatment',\n",
       " 'numspecies',\n",
       " 'speciestype',\n",
       " 'fertilization',\n",
       " 'intent',\n",
       " 'sampledepth',\n",
       " 'mapregion',\n",
       " 'doi',\n",
       " 'title',\n",
       " 'authors',\n",
       " 'authors_abbrev',\n",
       " 'pubyear',\n",
       " 'journal',\n",
       " 'volume_issue',\n",
       " 'pages']"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_kenya.review.unique()\n",
    "list(data_kenya.columns.values)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "79496df5",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_kenya_till = data_kenya[data_kenya['review'] == 'Tillage']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "24d67719",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_kenya_till_yield = data_kenya_till[data_kenya_till['rv'].str.contains(\"yield\")]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "8e50b8e7",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "data_kenya_till_yield.rv.unique()\n",
    "data_kenya_till_yield[['description', 'property1', 'property2', 'property3']] = data_kenya_till_yield['rv'].str.split(\",\", expand=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "97e2d18e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['maize grain yield', 'Maize yield of maize genotypeCKH08051',\n",
       "       'Maize yield of maize genotypeCKH10077',\n",
       "       'Maize yield of maize genotypeCKH10080',\n",
       "       'Maize yield of maize genotypeCKH10085',\n",
       "       'Maize yield of maize genotypeCKH10717',\n",
       "       'Maize yield of maize genotypeH513', 'maize grain yields',\n",
       "       'maize stover yields', 'bean grain yields', 'bean husk yields',\n",
       "       'bean haulm yields', 'sediment yield', 'maize yield gap closed',\n",
       "       'soybean grain yield', 'cowpea grain yield',\n",
       "       'soybean grain yields', 'maize stover yield'], dtype=object)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_kenya_till_yield.description.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "07994cc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_kenya_till_yield['culture'] = data_kenya_till_yield['description'].str.lower().str.split().apply(lambda x: x[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0fd90e22",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3367    maize\n",
       "3368    maize\n",
       "3369    maize\n",
       "3370    maize\n",
       "3371    maize\n",
       "        ...  \n",
       "5657    maize\n",
       "5658    maize\n",
       "5659    maize\n",
       "5660    maize\n",
       "5661    maize\n",
       "Name: culture, Length: 495, dtype: object"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_kenya_till_yield['culture']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "0c3906ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_kenya_till_yield = data_kenya_till_yield[~data_kenya_till_yield['description'].str.contains('husk|haulm|stover|sediment|gap|horn')]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "1c296276",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3367    maize\n",
       "3368    maize\n",
       "3369    maize\n",
       "3370    maize\n",
       "3371    maize\n",
       "        ...  \n",
       "5609    maize\n",
       "5610    maize\n",
       "5611    maize\n",
       "5612    maize\n",
       "5613    maize\n",
       "Name: culture, Length: 421, dtype: object"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_kenya_till_yield['culture']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "79668e71",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_kenya_till_yield_subset = data_kenya_till_yield[['review','culture','percentChange' ]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb044681",
   "metadata": {},
   "source": [
    "## 2. Summary Statistics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "7e884300",
   "metadata": {},
   "outputs": [],
   "source": [
    "stats = data_kenya_till_yield_subset.agg(['mean', 'median', 'std']).applymap(lambda x: '{:.2f}'.format(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "58a23ef1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "    #T_66f23_ caption {\n",
       "          color: purple;\n",
       "          font-size: 14px;\n",
       "    }</style><table id=\"T_66f23_\" ><caption>Summary Statistics</caption><thead>    <tr>        <th class=\"blank level0\" ></th>        <th class=\"col_heading level0 col0\" >percentChange</th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                        <th id=\"T_66f23_level0_row0\" class=\"row_heading level0 row0\" >mean</th>\n",
       "                        <td id=\"T_66f23_row0_col0\" class=\"data row0 col0\" >6.29</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                        <th id=\"T_66f23_level0_row1\" class=\"row_heading level0 row1\" >median</th>\n",
       "                        <td id=\"T_66f23_row1_col0\" class=\"data row1 col0\" >-4.44</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                        <th id=\"T_66f23_level0_row2\" class=\"row_heading level0 row2\" >std</th>\n",
       "                        <td id=\"T_66f23_row2_col0\" class=\"data row2 col0\" >59.29</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x19828901e20>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from IPython.display import display\n",
    "display(stats.style.set_caption('Summary Statistics').set_table_styles([{'selector': 'caption', 'props': [('color', 'purple'), ('font-size', '14px')]}]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d429f643",
   "metadata": {},
   "source": [
    "The median of the dataset is -4.44, indicating that on average, the percentage change in yield due to no-till methods is negative across all crop types. The mean, however, is 6.29, indicating a positive change in yield overall. The standard deviation of the data is 59.29, which is quite high, suggesting that the data points are spread out over a wide range and that there is significant variability in the effect of no-till methods on crop yields across different crop types."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cf75bbc3",
   "metadata": {},
   "source": [
    "## 3. Visualisation"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4a1bf975",
   "metadata": {},
   "source": [
    "**This part of analysis carries no analytic value and is carried out for practice purposes only.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "5b111662",
   "metadata": {},
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "bb95e546",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "plt.scatter(data_kenya_till_yield['controlValue'], data_kenya_till_yield['percentChange'])\n",
    "# Add labels and title\n",
    "plt.xlabel('Control Value')\n",
    "plt.ylabel('Percent Change')\n",
    "plt.title('Scatter plot')\n",
    "\n",
    "# Show the plot\n",
    "plt.show()\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a5d83fb",
   "metadata": {},
   "source": [
    "##  4. Grouped Summary Statistics\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "378e10ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "grouped_stats = data_kenya_till_yield_subset.groupby('culture')['percentChange'].agg(['mean', 'median', 'std']).applymap(lambda x: '{:.2f}'.format(x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "a849e24b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style  type=\"text/css\" >\n",
       "    #T_019ce_ caption {\n",
       "          color: purple;\n",
       "          font-size: 14px;\n",
       "    }</style><table id=\"T_019ce_\" ><caption>Grouped statistics</caption><thead>    <tr>        <th class=\"blank level0\" ></th>        <th class=\"col_heading level0 col0\" >mean</th>        <th class=\"col_heading level0 col1\" >median</th>        <th class=\"col_heading level0 col2\" >std</th>    </tr>    <tr>        <th class=\"index_name level0\" >culture</th>        <th class=\"blank\" ></th>        <th class=\"blank\" ></th>        <th class=\"blank\" ></th>    </tr></thead><tbody>\n",
       "                <tr>\n",
       "                        <th id=\"T_019ce_level0_row0\" class=\"row_heading level0 row0\" >bean</th>\n",
       "                        <td id=\"T_019ce_row0_col0\" class=\"data row0 col0\" >-22.02</td>\n",
       "                        <td id=\"T_019ce_row0_col1\" class=\"data row0 col1\" >-22.02</td>\n",
       "                        <td id=\"T_019ce_row0_col2\" class=\"data row0 col2\" >7.37</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                        <th id=\"T_019ce_level0_row1\" class=\"row_heading level0 row1\" >cowpea</th>\n",
       "                        <td id=\"T_019ce_row1_col0\" class=\"data row1 col0\" >50.68</td>\n",
       "                        <td id=\"T_019ce_row1_col1\" class=\"data row1 col1\" >44.08</td>\n",
       "                        <td id=\"T_019ce_row1_col2\" class=\"data row1 col2\" >72.11</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                        <th id=\"T_019ce_level0_row2\" class=\"row_heading level0 row2\" >maize</th>\n",
       "                        <td id=\"T_019ce_row2_col0\" class=\"data row2 col0\" >5.25</td>\n",
       "                        <td id=\"T_019ce_row2_col1\" class=\"data row2 col1\" >-4.69</td>\n",
       "                        <td id=\"T_019ce_row2_col2\" class=\"data row2 col2\" >59.30</td>\n",
       "            </tr>\n",
       "            <tr>\n",
       "                        <th id=\"T_019ce_level0_row3\" class=\"row_heading level0 row3\" >soybean</th>\n",
       "                        <td id=\"T_019ce_row3_col0\" class=\"data row3 col0\" >-7.94</td>\n",
       "                        <td id=\"T_019ce_row3_col1\" class=\"data row3 col1\" >-5.08</td>\n",
       "                        <td id=\"T_019ce_row3_col2\" class=\"data row3 col2\" >24.73</td>\n",
       "            </tr>\n",
       "    </tbody></table>"
      ],
      "text/plain": [
       "<pandas.io.formats.style.Styler at 0x19829d8e430>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "display(grouped_stats.style.set_caption('Grouped statistics').set_table_styles([{'selector': 'caption', 'props': [('color', 'purple'), ('font-size', '14px')]}]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20334051",
   "metadata": {},
   "source": [
    "This table shows the grouped statistics of four different crop types - bean, cowpea, maize, and soybean - based on their percent change in yield due to no tillage practices. The mean and median values for each crop type are listed, along with the standard deviation.\n",
    "\n",
    "Looking at the table, we can see that cowpea has the highest mean percent change in yield at 50.68%, indicating that no tillage practices have a significant positive effect on cowpea yield. Bean, on the other hand, has a negative mean percent change at -22.02%, indicating that no tillage practices have a negative impact on bean yield.\n",
    "\n",
    "The median values for each crop type are mostly negative, suggesting that for each crop type, the distribution of percent change in yield due to no tillage is skewed towards lower yields. The standard deviation values also vary across the crop types, with cowpea having the highest standard deviation at 72.11%, indicating a wider range of percent change in yield for cowpea compared to the other crops."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "06ab49f4",
   "metadata": {},
   "source": [
    "## 5. Trend over years"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4fc2e9df",
   "metadata": {},
   "source": [
    "**This part of analysis carries no analytic value and is carried out for practice purposes only.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "576abe6c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Group data by 'rvYear' and calculate the sum of 'percentChange'\n",
    "sums = data_kenya_till_yield.groupby('startYear')['percentChange'].mean()\n",
    "plt.plot(sums.index, sums.values)\n",
    "# Add labels and title\n",
    "plt.xlabel('Review year')\n",
    "plt.ylabel('Percent Change')\n",
    "plt.title('Trend over years')\n",
    "\n",
    "# Show the plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e54ea08f",
   "metadata": {},
   "source": [
    "##  6. Merging Datasets"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a753f275",
   "metadata": {},
   "source": [
    "**This part of analysis carries no analytic value and is carried out for practice purposes only.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "eca08a6d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['soybean', 'corn', 'maize'], dtype=object)"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import re\n",
    "data_us = pd.read_csv(\"data_us.csv\")\n",
    "data_us_till = data_us[data_us['review'] == 'Tillage']\n",
    "data_us_till_yield = data_us_till[data_us_till['rv'].str.contains(\"yield\")]\n",
    "data_us_till_yield.rv.unique()\n",
    "exclude = ['oil','silage','protein','stover', 'nitrogen','emissions', 'residue', 'cob', 'relative', 'cash', 'scaled' ]\n",
    "pattern = '|'.join(exclude)\n",
    "data_us_till_yield = data_us_till_yield[~data_us_till_yield['rv'].str.contains(pattern, flags=re.IGNORECASE)]\n",
    "data_us_till_yield['culture'] = data_us_till_yield['rv'].str.lower().str.split().apply(lambda x: 'corn' if x[0] == 'sweet' else x[0])\n",
    "data_us_till_yield.culture.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ed1e4df6",
   "metadata": {},
   "outputs": [],
   "source": [
    "merged_data = data_us_till_yield.merge(data_kenya_till_yield_subset, on='culture', how='inner')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "ea798e10",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>review_x</th>\n",
       "      <th>rv</th>\n",
       "      <th>rvYear</th>\n",
       "      <th>rvUnits</th>\n",
       "      <th>startYear</th>\n",
       "      <th>studyLength</th>\n",
       "      <th>sampleDepth</th>\n",
       "      <th>controlValue</th>\n",
       "      <th>trtValue</th>\n",
       "      <th>percentChange_x</th>\n",
       "      <th>...</th>\n",
       "      <th>pages</th>\n",
       "      <th>city</th>\n",
       "      <th>state</th>\n",
       "      <th>lat</th>\n",
       "      <th>lon</th>\n",
       "      <th>duration</th>\n",
       "      <th>order</th>\n",
       "      <th>culture</th>\n",
       "      <th>review_y</th>\n",
       "      <th>percentChange_y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>Soybean grain yield</td>\n",
       "      <td>1;2;3;4;5;6;7;8;9</td>\n",
       "      <td>Mg/ha</td>\n",
       "      <td>2007</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.1</td>\n",
       "      <td>-3.13</td>\n",
       "      <td>...</td>\n",
       "      <td>2302-2316</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>soybean</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>-25.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>Soybean grain yield</td>\n",
       "      <td>1;2;3;4;5;6;7;8;9</td>\n",
       "      <td>Mg/ha</td>\n",
       "      <td>2007</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.1</td>\n",
       "      <td>-3.13</td>\n",
       "      <td>...</td>\n",
       "      <td>2302-2316</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>soybean</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>32.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>Soybean grain yield</td>\n",
       "      <td>1;2;3;4;5;6;7;8;9</td>\n",
       "      <td>Mg/ha</td>\n",
       "      <td>2007</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.1</td>\n",
       "      <td>-3.13</td>\n",
       "      <td>...</td>\n",
       "      <td>2302-2316</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>soybean</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>-54.97</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>Soybean grain yield</td>\n",
       "      <td>1;2;3;4;5;6;7;8;9</td>\n",
       "      <td>Mg/ha</td>\n",
       "      <td>2007</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.1</td>\n",
       "      <td>-3.13</td>\n",
       "      <td>...</td>\n",
       "      <td>2302-2316</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>soybean</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>9.93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>Soybean grain yield</td>\n",
       "      <td>1;2;3;4;5;6;7;8;9</td>\n",
       "      <td>Mg/ha</td>\n",
       "      <td>2007</td>\n",
       "      <td>9</td>\n",
       "      <td>NaN</td>\n",
       "      <td>3.2</td>\n",
       "      <td>3.1</td>\n",
       "      <td>-3.13</td>\n",
       "      <td>...</td>\n",
       "      <td>2302-2316</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>soybean</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>-52.43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20698</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>maize grain yield</td>\n",
       "      <td>20</td>\n",
       "      <td>t/ha</td>\n",
       "      <td>1993</td>\n",
       "      <td>20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.8</td>\n",
       "      <td>11.6</td>\n",
       "      <td>-9.38</td>\n",
       "      <td>...</td>\n",
       "      <td>117-195</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>maize</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>-54.55</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20699</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>maize grain yield</td>\n",
       "      <td>20</td>\n",
       "      <td>t/ha</td>\n",
       "      <td>1993</td>\n",
       "      <td>20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.8</td>\n",
       "      <td>11.6</td>\n",
       "      <td>-9.38</td>\n",
       "      <td>...</td>\n",
       "      <td>117-195</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>maize</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>-58.70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20700</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>maize grain yield</td>\n",
       "      <td>20</td>\n",
       "      <td>t/ha</td>\n",
       "      <td>1993</td>\n",
       "      <td>20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.8</td>\n",
       "      <td>11.6</td>\n",
       "      <td>-9.38</td>\n",
       "      <td>...</td>\n",
       "      <td>117-195</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>maize</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>-44.66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20701</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>maize grain yield</td>\n",
       "      <td>20</td>\n",
       "      <td>t/ha</td>\n",
       "      <td>1993</td>\n",
       "      <td>20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.8</td>\n",
       "      <td>11.6</td>\n",
       "      <td>-9.38</td>\n",
       "      <td>...</td>\n",
       "      <td>117-195</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>maize</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>87.27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20702</th>\n",
       "      <td>Tillage</td>\n",
       "      <td>maize grain yield</td>\n",
       "      <td>20</td>\n",
       "      <td>t/ha</td>\n",
       "      <td>1993</td>\n",
       "      <td>20</td>\n",
       "      <td>NaN</td>\n",
       "      <td>12.8</td>\n",
       "      <td>11.6</td>\n",
       "      <td>-9.38</td>\n",
       "      <td>...</td>\n",
       "      <td>117-195</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>maize</td>\n",
       "      <td>Tillage</td>\n",
       "      <td>106.92</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>20703 rows × 32 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      review_x                   rv             rvYear rvUnits  startYear  \\\n",
       "0      Tillage  Soybean grain yield  1;2;3;4;5;6;7;8;9   Mg/ha       2007   \n",
       "1      Tillage  Soybean grain yield  1;2;3;4;5;6;7;8;9   Mg/ha       2007   \n",
       "2      Tillage  Soybean grain yield  1;2;3;4;5;6;7;8;9   Mg/ha       2007   \n",
       "3      Tillage  Soybean grain yield  1;2;3;4;5;6;7;8;9   Mg/ha       2007   \n",
       "4      Tillage  Soybean grain yield  1;2;3;4;5;6;7;8;9   Mg/ha       2007   \n",
       "...        ...                  ...                ...     ...        ...   \n",
       "20698  Tillage    maize grain yield                 20    t/ha       1993   \n",
       "20699  Tillage    maize grain yield                 20    t/ha       1993   \n",
       "20700  Tillage    maize grain yield                 20    t/ha       1993   \n",
       "20701  Tillage    maize grain yield                 20    t/ha       1993   \n",
       "20702  Tillage    maize grain yield                 20    t/ha       1993   \n",
       "\n",
       "       studyLength sampleDepth  controlValue  trtValue  percentChange_x  ...  \\\n",
       "0                9         NaN           3.2       3.1            -3.13  ...   \n",
       "1                9         NaN           3.2       3.1            -3.13  ...   \n",
       "2                9         NaN           3.2       3.1            -3.13  ...   \n",
       "3                9         NaN           3.2       3.1            -3.13  ...   \n",
       "4                9         NaN           3.2       3.1            -3.13  ...   \n",
       "...            ...         ...           ...       ...              ...  ...   \n",
       "20698           20         NaN          12.8      11.6            -9.38  ...   \n",
       "20699           20         NaN          12.8      11.6            -9.38  ...   \n",
       "20700           20         NaN          12.8      11.6            -9.38  ...   \n",
       "20701           20         NaN          12.8      11.6            -9.38  ...   \n",
       "20702           20         NaN          12.8      11.6            -9.38  ...   \n",
       "\n",
       "           pages city state lat lon duration order  culture review_y  \\\n",
       "0      2302-2316  NaN   NaN NaN NaN      NaN   NaN  soybean  Tillage   \n",
       "1      2302-2316  NaN   NaN NaN NaN      NaN   NaN  soybean  Tillage   \n",
       "2      2302-2316  NaN   NaN NaN NaN      NaN   NaN  soybean  Tillage   \n",
       "3      2302-2316  NaN   NaN NaN NaN      NaN   NaN  soybean  Tillage   \n",
       "4      2302-2316  NaN   NaN NaN NaN      NaN   NaN  soybean  Tillage   \n",
       "...          ...  ...   ...  ..  ..      ...   ...      ...      ...   \n",
       "20698    117-195  NaN   NaN NaN NaN      NaN   NaN    maize  Tillage   \n",
       "20699    117-195  NaN   NaN NaN NaN      NaN   NaN    maize  Tillage   \n",
       "20700    117-195  NaN   NaN NaN NaN      NaN   NaN    maize  Tillage   \n",
       "20701    117-195  NaN   NaN NaN NaN      NaN   NaN    maize  Tillage   \n",
       "20702    117-195  NaN   NaN NaN NaN      NaN   NaN    maize  Tillage   \n",
       "\n",
       "       percentChange_y  \n",
       "0               -25.00  \n",
       "1                32.00  \n",
       "2               -54.97  \n",
       "3                 9.93  \n",
       "4               -52.43  \n",
       "...                ...  \n",
       "20698           -54.55  \n",
       "20699           -58.70  \n",
       "20700           -44.66  \n",
       "20701            87.27  \n",
       "20702           106.92  \n",
       "\n",
       "[20703 rows x 32 columns]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "merged_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "550d9a63",
   "metadata": {},
   "source": [
    "## 7. Boxplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "e4ea4f11",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAmcAAAF/CAYAAAAM3256AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjMuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8QVMy6AAAACXBIWXMAAAsTAAALEwEAmpwYAAA7kklEQVR4nO3deXhU5cH+8XuyAkkohkQLQvgBJRBFDBhBFhFaLYiEIIJANG4sglgEK7IooOxbqRK10KitBjGiQXbXiEVAEXhBEMNioAKGJYEgmQQmyzy/P3iZ1yhJAJOZk8n3c1296jPLOfeZiTO3z5lzjs0YYwQAAABL8PF0AAAAAPwfyhkAAICFUM4AAAAshHIGAABgIZQzAAAAC6GcAQAAWAjlDLCQI0eOKCoqSnFxcYqLi1NsbKz69eunbdu2Vcr6mjdvrlOnTpX5mM8//1wvvvjiZS23uLhYw4cPV7du3bR48eIS9yUmJuqWW25RXFycevfurdjYWD300EM6ePDgZeevSDt37tSkSZNKvf9//ud/NGjQINf7MnToUO3bt0+StHnzZvXs2dNdUS/JuHHj9Nprr/2mZRw/flzjxo1TbGysevXqpX79+unTTz8t93k/fz3Ke10B/JqfpwMAKKlGjRpasWKFa7x27VqNHz9eH3/8sUfy7Nq1Sz/99NNlPef48ePasGGDduzYIV9f31/d36NHjxJf2MnJyfrrX/+qZcuW/ea8V+r777/X8ePHL3rfli1bNGbMGL300ktq2bKlJGnlypVKSEjQBx984M6YbnPq1CkNGDBATzzxhGbOnCmbzaY9e/bo4YcfVs2aNdWxY8dLWk5ZryuAi6OcARZ3+vRphYeHu8bvvPOOkpOT5ePjo7CwME2cOFGNGjXSww8/rOuvv15PP/20Nm3apHHjxmnZsmWaN2+eAgMDtWfPHp08eVIdO3bUs88+K39//xLrefnll7VmzRr5+vqqcePGmjhxojIzM5WSkqLi4mKFhIRo9OjRJZ6zdetWzZkzR2fPnpW/v79GjRqlNm3aaPDgwSoqKlKfPn2UmJioiIiIMrexffv2mj9/viQpNzdX06dP1759+1RYWKj27dvr6aeflp+fn1q2bKk//elP2rNnj+bNmyen06lp06a51v/000+rffv2ysjI0PTp03X69GkVFxcrISFBffv21ebNm/X3v/9dDRs21P79+1VUVKTnn39e9evX14IFC5Sbm6vx48dr5syZJfItWLBAjz32mKuYSVKvXr0UGBio4uJiSVJ+fr5Gjx6tAwcOyOFwaNq0aYqJidHBgwc1ZcoU5eXlKSsrSy1atNALL7ygwMBA3XDDDRo6dKg2btyoEydOaPDgwYqPj1dxcbHmzJmjzz77TCEhIWrVqpUyMjKUnJxc5uvzS9u2bdNHH30ku92ujh07auzYsVq7dq2WLFmilJQUSVJmZqbuvfdeffbZZwoICHA9d8mSJWrTpo169+7tuq1FixZasGCBateuLen8zOuXX36p0NDQEuMLjh49WuJ17d27t6ZOnarVq1dLOj/DdmGcmJioHTt26MSJE2revLnmzZunf/zjH/r444/ldDp17bXXavLkybrmmmvK/FsCvIIBYBmHDx82LVq0ML169TK9evUyXbp0Mddff735/PPPjTHGbNq0ydx+++3m5MmTxhhjUlNTzZ133mmcTqc5fvy46dChg/nkk0/Mrbfear7++mtjjDFjx441vXv3Nna73TgcDnPfffeZ5ORkY4wxkZGR5uTJk+a9994z/fv3N3l5ecYYYxYsWGAeeeQR1z8///zzv8p66tQp0759e7Njxw5jjDH79u0zbdu2NYcOHTKHDx820dHRF93GXy6vsLDQzJw50zz66KPGGGPGjRtn3nzzTWOMMUVFReapp54y//znP11533//fWOMMQUFBaZjx45m3bp1xhhjdu3aZXr27GkcDofp0aOH+fbbb40xxpw5c8bceeedZvv27earr74yUVFR5rvvvjPGGPPaa6+Z++67z/VaDh069KKZo6Ojzf79+0t514xruRdei3/961/mgQceMMYYM2vWLLN8+XJX5p49e5oPP/zQtT0X3otdu3aZli1bmnPnzpm3337b3HfffebcuXPG4XCYRx55xNx///3lvj4/N3bsWHP33XebvLw843A4zP3332/eeust43A4TPv27c2+ffuMMca88MILZt68eb96/qOPPmoWL15c6jZfyH/hb/Hn46+++srcddddxpiSr+vPb//leMGCBaZbt26msLDQGGPM+++/b0aNGuUap6SkmMGDB5eZB/AWzJwBFvPL3ZqbNm3SiBEjtHLlSn3xxRfq0aOHa6aiT58+mj59uo4cOaKGDRtq6tSpeuyxx/SXv/xFN998s2sZd999t4KCgiRJcXFxSktL0/333++6f/369erTp49q1aolSXrggQe0cOFCFRQUlJpz586dioiI0I033ihJatasmdq0aaOvv/5a7dq1K3Mb165d6/odXWFhoa6//npNnTpV0vnfuO3atUvvvfeeJOncuXMlnhsTEyNJ2rdvn3x8fNSlSxdJUsuWLbVq1Sp9//33OnTokCZMmOB6zrlz5/Tdd9+padOmql+/vqKioiRJ1113nd5///0ys0qSj4+PnE5nmY9p2LCh67Vo0aKFUlNTJUljxozRxo0blZSUpP/+9786ceKE8vPzXc/705/+JEm6/vrrVVBQoPz8fP3nP/9RXFycAgMDJUn9+/dXcnLyJb0+PxcXF+d6T3v16qX//Oc/io+PV79+/fTuu+9q7Nixev/9913L/jmbzSbj5qv7RUdHu2YA161bp127dumee+6RJDmdTp09e9ateQBPoZwBFtehQwdFRERo165dFy0IxhgVFRVJOv/7nrCwMO3cubPEY37+uy9jjHx8Sh4L5HQ6ZbPZSowvLLM0xcXFJZ7zyyxl+eVvzn6Z5cUXX1TTpk0lSWfOnCmxngtlw9fX91fr37dvn4wxCgkJKVFws7OzFRISoh07dqhGjRqu2y+1gERHR+ubb75RZGRkiduff/553XHHHfL19S2xm/jny33yySdVXFysO++8U126dNHRo0dLrPNCAbuwLcaYX+2i/Pn7Vd7r83O/fN8vLHfAgAHq27ev2rZtq2bNmqlhw4YX3eYdO3aUKPGSlJKSorNnz+rhhx8ucXtZRf6CX77ehYWFJe6/8N5e2M4Lu3kvLP9yf/sIVFUcrQlY3MGDB/Xjjz8qKipKt956q9auXes6wjI1NVV16tRRo0aNtHPnTr355ptKTU1Vbm6u3njjDdcyPvjgAxUUFMjhcOj9999X165dS6zj1ltvVWpqqmtGJzk5WTfffLMCAgLk6+t70cIVHR2tAwcOuIrg/v37tWXLFrVt2/Y3bW+nTp3073//W8YYFRQUaPjw4b864lOSmjRpIpvNpo0bN0qSdu/erQcffFCNGzcuMft49OhR9ezZU99++22Z6y1tOyVp+PDheumll0osY9myZfroo49+Vdh+acOGDRoxYoR69OghSfrmm29cv1MrzW233aaVK1eqoKBARUVFJWb3LvX1kaQ1a9aUeN87d+4sSapXr56i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288hZs68hJ+fn2rWrKk+ffooICBA4eHhOnHihOv+N998U7t371ZRUZHefvttSVJiYqLat2+vgQMHqqCgQK1atdI111zjqU1AJTp37pweeOAB5efna9q0aSouLtbQoUNljFFQUJDmzJkjm82m5557TqtWrVKdOnXk6+urgoICT0dHBWrZsqXGjBmjxMRE+fj4uH6X2r9/fxUWFqp79+66/vrrJUn33nuvpk2bprlz57qe/8033+iBBx6QzWbTjBkzdO211170M6RXr1567LHHVLduXf3+979XTk6OpzYZv9GAAQM0YcIE3X///SouLtarr76qt956SwMHDpTD4dDjjz+uunXrKjQ0VAcPHtTgwYPVokUL/fjjjxo8eLBrOenp6XrwwQd19uxZTZ06VaGhoXrooYeUkJCg4uJiXXvttbrzzjvVvXt3TZ8+XYsWLVK9evWq7d8OBwQAAH5l7dq12r9/v5544glPR0EVl5iYqLCwMA0cONDTUaoMZs4AACXMnz9fW7du1SuvvOLpKEC1xMwZAACAhXBAAAAAgIVQzgAAACyEcgYAAGAhlDMAXm///v0aOnSoEhISdM8992jBggWlnj/pwgW+HQ6H3n33XTcnBQDKGQAvd+bMGT355JOaMGGCkpOTtXTpUu3bt08pKSllPi8rK4tyBsAjKGcAvFpaWpratWun//f//p8kydfXV7Nnz1bDhg01evRo1+M6duxY4nkLFy7U999/r5deekmJiYmukzdnZGQoISFB0vkLhT/++ON68sknlZubq5EjRyohIUEJCQnau3evezYQgNehnAHwaidOnFDDhg1L3BYUFOS6rExphg0bpj/84Q96/PHHS31Mfn6+HnvsMc2fP18LFy7ULbfcouTkZE2dOlXPPfdcRcQHUA1xEloAXq1+/fr67rvvStx2+PBhbdmypcRtV3rKx8aNG0s6f83Ar776Sh988IGk87tTAeBKMHMGwKt17dpVX3zxhQ4dOiTp/AW+Z82aJT8/P2VlZUmSfvzxR/30008lnufj4yOn0ylJCgwMdD32wgWcf/44SWrSpIkeeughJScn64UXXlBsbGylbhcA78XMGQCvFhwcrFmzZunZZ5+VMUZ5eXnq2rWrBg0apG+++Ub9+vVT06ZN1aBBgxLPq1u3rgoLCzV37lwNGDBAo0aN0pYtW9SyZcuLrmfYsGF65plntHTpUtnt9jJ3hwJAWbh8EwAAgIWwWxMAAMBCKGcAAAAWQjkDAACwEMoZAACAhVDOAAAALIRyBgAAYCGUMwAAAAuhnAEAAFjI/wd6gh+4kBuINgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "sns.set_style(\"whitegrid\")\n",
    "sns.set_palette(\"colorblind\")\n",
    "\n",
    "plt.figure(figsize=(10, 6))\n",
    "sns.boxplot(x='culture', y='percentChange', data=data_kenya_till_yield_subset)\n",
    "plt.title(\"Boxplot of Percent Change by Culture\")\n",
    "plt.xlabel(\"Culture\")\n",
    "plt.ylabel(\"Percent Change\")\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91e9e60a",
   "metadata": {},
   "source": [
    "For maize, we can observe a large number of outliers and the changes in yield go up to 700 percent. The median of the data is around zero, and the distribution appears to be symmetrical on both sides, indicating that there is not a significant effect of no-tillage on maize yield except for a few outliers.\n",
    "\n",
    "The boxplot for beans is quite flat, suggesting that there may not be much data available for this crop. The distribution appears to be relatively even on both sides of the median, indicating that there is a negative effect of no-tillage on bean yield.\n",
    "\n",
    "For soybean, the median is around zero, but the lower side of the box is negative, indicating that no-tillage may have a negative effect on soybean yield. \n",
    "\n",
    "In contrast, the boxplot for cowpea shows a significant positive effect of no-tillage, with the median around 50 percent and a relatively normal distribution. The width of the boxplot suggests that the effect is consistent across the data and is positive."
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5bd29c8f",
   "metadata": {},
   "source": [
    "## 8. Histogram"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "4a4afb84",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "plt.hist(data_kenya_till_yield_subset['percentChange'], bins=100, color='blue', edgecolor='black')\n",
    "plt.xlabel('Percent Change')\n",
    "plt.ylabel('Count')\n",
    "plt.title('Histogram of Percent Change')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "259a0ed3",
   "metadata": {},
   "source": [
    "The 'percentChange' variable in a dataset follows a right-skewed normal distribution, it means that there are more extreme data points with higher percent changes than expected. This suggests that there may be some outliers or extreme values in the positive direction that are influencing the distribution."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3f3ba03",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
