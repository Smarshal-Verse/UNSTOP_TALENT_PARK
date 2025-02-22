
LOG_FILE_PATH = '/home/samanwith/Desktop/job_recommender/recommender/core/log.txt'
EMPLOYERS_DATA_PATH = '/home/samanwith/Desktop/job_recommender/data/companies.csv'
JOBS_DATA_PATH = '/home/samanwith/Desktop/job_recommender/data/jobs.csv'
CV_DATAPATH = '/home/samanwith/Desktop/job_recommender/data/cvdata/ResumeDataSet.csv'
NETWORK_DATA_PATH = '/home/samanwith/Desktop/job_recommender/data/network_data'
NETWORK_BUILDER_SAVE_PATH = '/home/samanwith/Desktop/job_recommender/data/network_data/network_builder.pkl'

VOCAB_PATH = '/home/samanwith/Desktop/job_recommender/data/network_data/vocab.json'
LSA_COMPARER_PATH = '/home/samanwith/Desktop/job_recommender/data/network_data/lsa.pkl'


# Edge weights
#  
POSTED_WEIGHT = 1
APPLIED_WEIGHT = 2

EMPLOYER_TO_EMPLOYER_WEIGHT = 1
JOB_TO_JOB_WEIGHT = 1
CANDIDATE_TO_CANDIDATE_WEIGHT = 1
CANDIDATE_TO_JOB_WEIGHT = 1

PROFILE_MATCH_WEIGHT = 1
EXPERTISE_MATCH_WEIGHT = 1

FAVORITE_WEIGHT = 1
LIKE_WEIGHT  = 0.5
VISIT_WEIGHT = 0.2


NUM_REDUCED_FEATURES = 0.3
# How many neighbors should one node connect to, if it's float, it's the ratio
# of all node considered. 
NEIGHBOR_RATIO = 0.01
PROFILE_MATCHED_NEIHBOR_RATIO = 0.01
SIMILARITY_METHOD = 'cosine'

# Two nodes are considered similar if they have the cosine similarity > this threshold
COSINE_SIMILARITY_THRESHOLD = 0.4
PROFILE_MATCHED_SIMILARITY_THRESDHOLD = 0.4

# damping probability for PageRank
alpha = 0.5