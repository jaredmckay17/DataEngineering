
# Introduction - utilizing Juypter Notebook for analysis on batch procesing in Pandas

import pandas as pd


pd.options.display.max_columns = 99
chunk_iter = pd.read_csv('crunchbase-investments.csv', chunksize=5000, encoding='ISO-8859-1')

# Compute each column's missing value counts

mv_list = []
for chunk in chunk_iter:
    mv_list.append(chunk.isnull().sum())
    
combined_mv_vc = pd.concat(mv_list)
unique_combined_mv_vc = combined_mv_vc.groupby(combined_mv_vc.index).sum()
unique_combined_mv_vc.sort_values()

'''
company_country_code          1
company_name                  1
company_permalink             1
company_region                1
investor_region               2
investor_permalink            2
investor_name                 2
funded_quarter                3
funded_at                     3
funded_month                  3
funded_year                   3
funding_round_type            3
company_state_code          492
company_city                533
company_category_code       643
raised_amount_usd          3599
investor_country_code     12001
investor_city             12480
investor_state_code       16809
investor_category_code    50427
dtype: int64
'''

#Total memory footprint for each column

chunk_iter = pd.read_csv('crunchbase-investments.csv', chunksize=5000, encoding='ISO-8859-1')
counter = 0
series_memory_fp = pd.Series()
for chunk in chunk_iter:
    if counter == 0:
        series_memory_fp = chunk.memory_usage(deep=True)
    else:
        series_memory_fp += chunk.memory_usage(deep=True)
    counter += 1

# Drop memory footprint calculation for the index.
series_memory_fp = series_memory_fp.drop('Index')
series_memory_fp

'''
company_permalink         4057788
company_name              3591326
company_category_code     3421104
company_country_code      3172176
company_state_code        3106051
company_region            3411585
company_city              3505926
investor_permalink        4980548
investor_name             3915666
investor_category_code     622424
investor_country_code     2647292
investor_state_code       2476607
investor_region           3396281
investor_city             2885083
funding_round_type        3410707
funded_at                 3542185
funded_month              3383584
funded_quarter            3383584
funded_year                422960
raised_amount_usd          422960
dtype: int64
'''

#Total memory footprint of the data (in megabytes)

series_memory_fp.sum() / (1024 * 1024)
# 56.987607002258301

unique_combined_mv_vc.sort_values()

'''
company_country_code          1
company_name                  1
company_permalink             1
company_region                1
investor_region               2
investor_permalink            2
investor_name                 2
funded_quarter                3
funded_at                     3
funded_month                  3
funded_year                   3
funding_round_type            3
company_state_code          492
company_city                533
company_category_code       643
raised_amount_usd          3599
investor_country_code     12001
investor_city             12480
investor_state_code       16809
investor_category_code    50427
dtype: int64
'''

# Drop columns representing URL's or containing way too many missing values (>90% missing)
drop_cols = ['investor_permalink', 'company_permalink', 'investor_category_code']
keep_cols = chunk.columns.drop(drop_cols)
keep_cols.tolist
Index(['company_name', 'company_category_code', 'company_country_code',
       'company_state_code', 'company_region', 'company_city', 'investor_name',
       'investor_country_code', 'investor_state_code', 'investor_region',
       'investor_city', 'funding_round_type', 'funded_at', 'funded_month',
       'funded_quarter', 'funded_year', 'raised_amount_usd'],
      dtype='object')

# Key: Column name, Value: List of types
col_types = {}
chunk_iter = pd.read_csv('crunchbase-investments.csv', chunksize=5000, encoding='ISO-8859-1', usecols=keep_cols)

for chunk in chunk_iter:
    for col in chunk.columns:
        if col not in col_types:
            col_types[col] = [str(chunk.dtypes[col])]
        else:
            col_types[col].append(str(chunk.dtypes[col]))

uniq_col_types = {}
for k,v in col_types.items():
    uniq_col_types[k] = set(col_types[k])

'''
{'company_category_code': {'object'},
 'company_city': {'object'},
 'company_country_code': {'object'},
 'company_name': {'object'},
 'company_region': {'object'},
 'company_state_code': {'object'},
 'funded_at': {'object'},
 'funded_month': {'object'},
 'funded_quarter': {'object'},
 'funded_year': {'float64', 'int64'},
 'funding_round_type': {'object'},
 'investor_city': {'float64', 'object'},
 'investor_country_code': {'float64', 'object'},
 'investor_name': {'object'},
 'investor_region': {'object'},
 'investor_state_code': {'float64', 'object'},
 'raised_amount_usd': {'float64'}}
'''

# chunk

'''
company_name	company_category_code	company_country_code	company_state_code	company_region	company_city	investor_name	investor_country_code	investor_state_code	investor_region	investor_city	funding_round_type	funded_at	funded_month	funded_quarter	funded_year	raised_amount_usd
50000	NuORDER	fashion	USA	CA	Los Angeles	West Hollywood	Mortimer Singer	NaN	NaN	unknown	NaN	series-a	2012-10-01	2012-10	2012-Q4	2012	3060000.0
50001	ChaCha	advertising	USA	IN	Indianapolis	Carmel	Morton Meyerson	NaN	NaN	unknown	NaN	series-b	2007-10-01	2007-10	2007-Q4	2007	12000000.0
50002	Binfire	software	USA	FL	Bocat Raton	Bocat Raton	Moshe Ariel	NaN	NaN	unknown	NaN	angel	2008-04-18	2008-04	2008-Q2	2008	500000.0
50003	Binfire	software	USA	FL	Bocat Raton	Bocat Raton	Moshe Ariel	NaN	NaN	unknown	NaN	angel	2010-01-01	2010-01	2010-Q1	2010	750000.0
50004	Unified Color	software	USA	CA	SF Bay	South San Frnacisco	Mr. Andrew Oung	NaN	NaN	unknown	NaN	angel	2010-01-01	2010-01	2010-Q1	2010	NaN
50005	HItviews	advertising	USA	NY	New York	New York City	multiple parties	NaN	NaN	unknown	NaN	angel	2007-11-29	2007-11	2007-Q4	2007	485000.0
50006	LockerDome	social	USA	MO	Saint Louis	St. Louis	multiple parties	NaN	NaN	unknown	NaN	angel	2012-04-17	2012-04	2012-Q2	2012	300000.0
50007	ThirdLove	ecommerce	USA	CA	SF Bay	San Francisco	Munjal Shah	NaN	NaN	unknown	NaN	series-a	2012-12-01	2012-12	2012-Q4	2012	5600000.0
50008	Hakia	search	USA	NaN	TBD	NaN	Murat Vargi	NaN	NaN	unknown	NaN	series-a	2006-11-01	2006-11	2006-Q4	2006	16000000.0
50009	bookacoach	sports	USA	IN	Indianapolis	Indianapolis	Myles Grote	NaN	NaN	unknown	NaN	angel	2012-11-01	2012-11	2012-Q4	2012	NaN
50010	LocalCircles	social	USA	CA	SF Bay	Santa Clara	Nadir Godrej	NaN	NaN	unknown	NaN	angel	2012-09-01	2012-09	2012-Q3	2012	NaN
50011	Graphdive	analytics	USA	CA	SF Bay	Menlo Park	Naguib Sawiris	NaN	NaN	unknown	NaN	angel	2012-10-04	2012-10	2012-Q4	2012	1000000.0
50012	Ribbon	ecommerce	USA	CA	SF Bay	San Francisco	Naguib Sawiris	NaN	NaN	unknown	NaN	series-a	2013-02-05	2013-02	2013-Q1	2013	1630000.0
50013	Dokkankom.com	ecommerce	USA	NY	New York	new york	Namek Zu'bi	NaN	NaN	unknown	NaN	angel	2011-10-10	2011-10	2011-Q4	2011	30000.0
50014	Lookery	web	USA	CA	SF Bay	San Francisco	Nana Shin	NaN	NaN	unknown	NaN	angel	2008-02-07	2008-02	2008-Q1	2008	900000.0
50015	TrustDegrees	web	USA	NY	Kenmore	Kenmore	Nancy Barrett	NaN	NaN	unknown	NaN	angel	2011-06-09	2011-06	2011-Q2	2011	8000.0
50016	Altavoz	games_video	USA	DC	Washington DC	Washington	Nancy Jacobsen	NaN	NaN	unknown	NaN	angel	2012-09-11	2012-09	2012-Q3	2012	150000.0
50017	EdSurge	education	USA	CA	SF Bay	Burlingame	Nancy Peretsman	NaN	NaN	unknown	NaN	angel	2012-08-29	2012-08	2012-Q3	2012	400000.0
50018	FullContact	enterprise	USA	CO	Denver	Denver	Nancy Pierce	NaN	NaN	unknown	NaN	series-b	2012-07-09	2012-07	2012-Q3	2012	7000000.0
50019	Rapt Media	enterprise	USA	CO	Denver	Boulder	Nancy Pierce	NaN	NaN	unknown	NaN	series-a	2013-01-23	2013-01	2013-Q1	2013	2288803.0
50020	Humanoid	software	USA	CA	SF Bay	San Francisco	Nat Friedman	NaN	NaN	unknown	NaN	angel	2010-12-01	2010-12	2010-Q4	2010	1100000.0
50021	Runscope	web	USA	CA	SF Bay	San Francisco	Nat Friedman	NaN	NaN	unknown	NaN	angel	2013-05-22	2013-05	2013-Q2	2013	1100000.0
50022	Adzerk	advertising	USA	NC	Raleigh-Durham	Durham	Nat Turner	NaN	NaN	unknown	NaN	angel	2011-07-12	2011-07	2011-Q3	2011	650000.0
50023	Adaptly	advertising	USA	NY	New York	New York	Nat Turner	NaN	NaN	unknown	NaN	series-a	2011-04-18	2011-04	2011-Q2	2011	2000000.0
50024	Lore	education	USA	NY	New York	New York	Nat Turner	NaN	NaN	unknown	NaN	angel	2011-06-27	2011-06	2011-Q2	2011	1000000.0
50025	Tasted Menu	hospitality	USA	MA	Boston	Boston	Nat Turner	NaN	NaN	unknown	NaN	angel	2011-05-01	2011-05	2011-Q2	2011	NaN
50026	Lua Technologies	mobile	USA	NY	New York	New York	Nat Turner	NaN	NaN	unknown	NaN	series-a	2012-08-01	2012-08	2012-Q3	2012	2500000.0
50027	Blue Apron	hospitality	USA	NY	New York	Brooklyn	Nat Turner	NaN	NaN	unknown	NaN	series-a	2013-02-19	2013-02	2013-Q1	2013	3000000.0
50028	ChatID	mobile	USA	NY	New York	New York	Nat Turner	NaN	NaN	unknown	NaN	angel	2012-01-01	2012-01	2012-Q1	2012	NaN
50029	Breakthrough Behavioral	health	USA	CA	SF Bay	Redwood City	Nat Turner	NaN	NaN	unknown	NaN	angel	2012-08-13	2012-08	2012-Q3	2012	900000.0
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
52840	Meddik	health	USA	NY	New York	New York	Zach Weinberg	NaN	NaN	unknown	NaN	angel	2012-05-24	2012-05	2012-Q2	2012	750000.0
52841	Blue Apron	hospitality	USA	NY	New York	Brooklyn	Zach Weinberg	NaN	NaN	unknown	NaN	series-a	2013-02-19	2013-02	2013-Q1	2013	3000000.0
52842	ChatID	mobile	USA	NY	New York	New York	Zach Weinberg	NaN	NaN	unknown	NaN	angel	2012-01-01	2012-01	2012-Q1	2012	NaN
52843	Breakthrough Behavioral	health	USA	CA	SF Bay	Redwood City	Zach Weinberg	NaN	NaN	unknown	NaN	angel	2012-08-13	2012-08	2012-Q3	2012	900000.0
52844	Plaid	software	USA	CA	SF Bay	San Francisco	Zach Weinberg	NaN	NaN	unknown	NaN	series-a	2013-09-19	2013-09	2013-Q3	2013	2800000.0
52845	PokitDok	mobile	USA	CA	SF Bay	Menlo Park	Zach Zeitlin	NaN	NaN	unknown	NaN	angel	2012-07-12	2012-07	2012-Q3	2012	1300000.0
52846	Fitocracy	web	USA	NY	New York	New York	Zachary Aarons	NaN	NaN	unknown	NaN	angel	2011-09-01	2011-09	2011-Q3	2011	250000.0
52847	Square	mobile	USA	CA	SF Bay	San Francisco	Zachary Bogue	NaN	NaN	unknown	NaN	series-a	2009-11-01	2009-11	2009-Q4	2009	10000000.0
52848	MixRank	advertising	USA	CA	SF Bay	San Francisco	Zachary Bogue	NaN	NaN	unknown	NaN	series-a	2011-11-18	2011-11	2011-Q4	2011	1500000.0
52849	Socialcam	mobile	USA	CA	Santa Clara County	Santa Clara County	Zachary Bogue	NaN	NaN	unknown	NaN	angel	2012-04-30	2012-04	2012-Q2	2012	NaN
52850	Nuzzel	news	USA	CA	SF Bay	San Francisco	Zachary Bogue	NaN	NaN	unknown	NaN	venture	2012-11-15	2012-11	2012-Q4	2012	1700000.0
52851	ThirdLove	ecommerce	USA	CA	SF Bay	San Francisco	Zachary Bogue	NaN	NaN	unknown	NaN	series-a	2012-12-01	2012-12	2012-Q4	2012	5600000.0
52852	MXD3D	web	USA	CA	SF Bay	San Francisco	Zaid Ayoub	NaN	NaN	unknown	NaN	angel	2012-01-01	2012-01	2012-Q1	2012	300000.0
52853	MXD3D	web	USA	CA	SF Bay	San Francisco	Zaid Ayoub	NaN	NaN	unknown	NaN	angel	2011-01-01	2011-01	2011-Q1	2011	300000.0
52854	Verious	mobile	USA	CA	SF Bay	San Carlos	Zain Khan	NaN	NaN	unknown	NaN	angel	2011-05-30	2011-05	2011-Q2	2011	800000.0
52855	Identified	analytics	USA	CA	SF Bay	San Francisco	Zao Yang	NaN	NaN	unknown	NaN	series-b	2012-06-05	2012-06	2012-Q2	2012	21000000.0
52856	HaulerDeals	fashion	USA	CA	Los Angeles	Los Angeles	Zaw Thet	NaN	NaN	unknown	NaN	angel	2012-10-31	2012-10	2012-Q4	2012	1250000.0
52857	When You Wish	nonprofit	USA	CA	Los Angeles	Marina Del Rey	Zelda Marzec	NaN	NaN	unknown	NaN	series-a	2011-02-01	2011-02	2011-Q1	2011	1500000.0
52858	Farmeron	analytics	USA	CA	SF Bay	Mountain View	Zeljko Mataija	NaN	NaN	unknown	NaN	angel	2010-10-01	2010-10	2010-Q4	2010	15000.0
52859	Theraclone Sciences	biotech	USA	WA	Seattle	Seattle	Zenyaku Kogyo	NaN	NaN	unknown	NaN	series-b	2013-03-25	2013-03	2013-Q1	2013	8000000.0
52860	SimpleGeo	advertising	USA	CA	SF Bay	San Francisco	Ziv Navoth	NaN	NaN	unknown	NaN	other	2009-11-10	2009-11	2009-Q4	2009	195000.0
52861	Open Me	ecommerce	USA	CA	Los Angeles	Los Angeles	Ziver Birg	NaN	NaN	unknown	NaN	angel	2013-08-01	2013-08	2013-Q3	2013	NaN
52862	Comprehend Systems	enterprise	USA	CA	SF Bay	Palo Alto	Zod Nazem	NaN	NaN	unknown	NaN	series-a	2013-07-11	2013-07	2013-Q3	2013	8400000.0
52863	Payoneer	other	USA	NY	New York	New York	Zohar Gilon	NaN	NaN	unknown	NaN	series-a	2005-01-01	2005-01	2005-Q1	2005	2000000.0
52864	Outbrain	web	USA	NY	New York	New York City	Zohar Gilon	NaN	NaN	unknown	NaN	series-b	2009-02-11	2009-02	2009-Q1	2009	12000000.0
52865	Garantia Data	enterprise	USA	CA	SF Bay	Santa Clara	Zohar Gilon	NaN	NaN	unknown	NaN	series-a	2012-08-08	2012-08	2012-Q3	2012	3800000.0
52866	DudaMobile	mobile	USA	CA	SF Bay	Palo Alto	Zohar Gilon	NaN	NaN	unknown	NaN	series-c+	2013-04-08	2013-04	2013-Q2	2013	10300000.0
52867	SiteBrains	software	USA	CA	SF Bay	San Francisco	zohar israel	NaN	NaN	unknown	NaN	angel	2010-08-01	2010-08	2010-Q3	2010	350000.0
52868	Comprehend Systems	enterprise	USA	CA	SF Bay	Palo Alto	Zorba Lieberman	NaN	NaN	unknown	NaN	series-a	2013-07-11	2013-07	2013-Q3	2013	8400000.0
52869	SmartThings	mobile	USA	DC	unknown	Minneapolis	Zorik Gordon	NaN	NaN	unknown	NaN	series-a	2012-12-04	2012-12	2012-Q4	2012	3000000.0
2870 rows × 17 columns
'''

#Loading Chunks Into SQLite -> easy use for practice, but PostgreSQL and Sybase use in production for GS example. 

import sqlite3
conn = sqlite3.connect('crunchbase.db')
chunk_iter = pd.read_csv('crunchbase-investments.csv', chunksize=5000, encoding='ISO-8859-1')

for chunk in chunk_iter:
    chunk.to_sql("investments", conn, if_exists='append', index=False)
