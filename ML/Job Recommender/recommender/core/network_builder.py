from typing import Dict, List, Tuple, Any
import logging
import os
import pickle
import string
import sys

import numpy as np
import pandas as pd
import networkx as nx

from sklearn import neighbors
from scipy.spatial import distance
import latent_semantic_analysis
import constants

handler = logging.StreamHandler()
formmater = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formmater)

logger = logging.getLogger()
logger.addHandler(handler)
logger.setLevel(logging.INFO)

class NetworkBuilder:

    def __init__(self, employers_data: pd.DataFrame, 
                jobs_data: pd.DataFrame,
                cv_data: pd.DataFrame) -> None:
        
        if isinstance(employers_data, pd.DataFrame):
            self.employers_data = self.employers_dataframe_to_dict(employers_data)
        elif isinstance(employers_data, str):
            self.employers_data = pd.read_csv(employers_data)
            self.employers_data = self.employers_dataframe_to_dict(self.employers_data)
        else:
            raise ValueError('data should be a dataframe of a path to that dataframe')

        if isinstance(jobs_data, pd.DataFrame):
            self.jobs_data = self.jobs_dataframe_to_dict(jobs_data)
        elif isinstance(jobs_data, str):
            self.jobs_data = pd.read_csv(jobs_data)
            self.jobs_data = self.jobs_dataframe_to_dict(self.jobs_data)
        else:
            raise ValueError('data should be a dataframe of a path to that dataframe')

        if isinstance(cv_data, pd.DataFrame):
            self.cv_data = self.cv_dataframe_to_dict(cv_data)
        elif isinstance(cv_data, str):
            self.cv_data = pd.read_csv(cv_data)
            self.cv_data = self.cv_dataframe_to_dict(self.cv_data)
        else:
            raise ValueError('data should be a dataframe of a path to that dataframe')

        self.G = None
        self.comparer = None

    def employers_dataframe_to_dict(self, companies_df: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
        employers_data = {}
        for i, row in companies_df.iterrows():
            employer_data = {
                'company_name': row['company_name'],
                'average_rating': row['average_rating'],
                'num_review': row['num_review'],
                'city': row['city'],
                'type': row['type'],
                'num_employee': row['num_employee'],
                'country': row['country'],
                'working_day': row['working_day'],
                'OT': row['OT'],
                'overview': row['overview'],
                'expertise': row['expertise'],
                'benefit': row['benefit'],
                'logo_link': row['logo_link']
            }
            employers_data[row['company_id']] = employer_data
        return employers_data

    def jobs_dataframe_to_dict(self, jobs_df: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
        jobs_data = {}
        for i, row in jobs_df.iterrows():
            job_data = {
                'company_id': row['company_id'],
                'job_name': row['job_name'],
                'taglist': row['taglist'],
                'location': row['location'], 
                'three_reasons': row['three_reasons'],
                'description': row['description']
            }
            jobs_data[row['job_id']] = job_data
        return jobs_data

    def cv_dataframe_to_dict(self, cv_df: pd.DataFrame) -> Dict[str, Dict[str, Any]]:
        cv_data = {}
        for i, row in cv_df.iterrows():
            cv_data[i] = {
                'expertise': row['Category'],
                'resume': row['Resume']
            }
        return cv_data

    def create_network_from_data(self) -> nx.MultiDiGraph:
        G = nx.MultiDiGraph(name='Jobs graph', num_employers=0, num_jobs=0, num_candidates=0,
                            candidate_to_job=0, candidate_to_candidate=0, job_to_job=0,
                            employer_to_employer=0, expertise_match=0, num_apply=0, num_favorite=0)

        for employer_id, employer_data in self.employers_data.items():
            G.add_node(employer_id, node_type='employer', **employer_data)
            G.graph['num_employers'] += 1

        for job_id, job_data in self.jobs_data.items():
            G.add_node(job_id, node_type='job', **job_data)
            G.graph['num_jobs'] += 1
            G.add_edge(job_id, job_data['company_id'], weight=constants.POSTED_WEIGHT, edge_type='posted')
            G.add_edge(job_data['company_id'], job_id, weight=constants.POSTED_WEIGHT, edge_type='posted')

        for _, candidate_data in self.cv_data.items():
            candidate_id = 'candidate-%d' % G.graph['num_candidates']
            G.add_node(candidate_id, node_type='candidate', **candidate_data)
            G.graph['num_candidates'] += 1
        return G

    def get_all_document_from_graph(self) -> List[str]:
        all_documents = []
        for _, node_data in self.G.nodes.items():
            if not node_data:
                print(_)
                break
            if node_data['node_type'] == 'employer':
                all_documents.append(' '.join([str(node_data['overview']), str(node_data['benefit'])]))
            elif node_data['node_type'] == 'job':
                all_documents.append(' '.join([str(node_data['three_reasons']), str(node_data['description'])]))
            elif node_data['node_type'] == 'candidate':
                all_documents.append(node_data['resume'])
            else:
                continue
        return all_documents

    def get_lsa(self) -> latent_semantic_analysis.LSA:
        if os.path.isfile(constants.LSA_COMPARER_PATH):
            logger.info(f'Loading LSA comparer from {constants.LSA_COMPARER_PATH}')
            with open(constants.LSA_COMPARER_PATH, 'rb') as f:
                self.lsa = pickle.load(f)
        else:
            all_documents = self.get_all_document_from_graph()
            all_texts = ' '.join(all_documents)
            vocab = latent_semantic_analysis.make_vocab(all_texts, min_word_count=10)
            self.lsa = latent_semantic_analysis.LSA(vocab, all_documents, constants.NUM_REDUCED_FEATURES)
            self.lsa.do_work()
            logger.info(f'Saving LSA comparer to {constants.LSA_COMPARER_PATH}')
            with open(constants.LSA_COMPARER_PATH, 'wb') as f:
                pickle.dump(self.lsa, f, pickle.HIGHEST_PROTOCOL)

    def vectorize_nodes(self) -> None:
        for node_name in self.G:
            node = self.G.nodes[node_name]
            type = node['node_type']
            document = None
            if type == 'employer':
                document = [str(node['overview']), str(node['expertise']), str(node['benefit'])]
            elif type == 'job':
                document = [str(node['three_reasons']), str(node['description'])]
            elif type == 'candidate':
                document = [str(node['expertise']), str(node['resume'])]
            if document is None:
                logger.info(f'Node {node} has no information to vectorize')
                self.G.nodes[node_name]['reduced_tfidf'] = np.array([])
                continue
            document = ' '.join(document)
            vector = self.lsa.vectorize(document)
            self.G.nodes[node_name]['reduced_tfidf'] = vector

    def create_keywords_for_nodes(self) -> None:
        processor = lambda x: x.lower().translate(str.maketrans('', '', string.punctuation)).split()
        for node_name in self.G:
            node = self.G.nodes[node_name]
            type = node['node_type']
            document = None
            if type == 'employer':
                document = [str(node['overview']), str(node['expertise']), str(node['benefit']), str(node['company_name'])]
            elif type == 'job':
                document = [str(node['three_reasons']), str(node['description']), str(node['job_name'])]
            elif type == 'candidate':
                document = [str(node['expertise']), str(node['resume'])]
            document = ' '.join(document)
            keywords = processor(document)
            keywords = ' '.join(keywords).split()
            keywords = set(keywords)
            self.G.nodes[node_name]['keywords'] = keywords

    def get_k_neighbors(self, data: np.ndarray, label: np.ndarray, k: int) -> Tuple[neighbors.KNeighborsClassifier, List[List[int]]]:
        knn = neighbors.KNeighborsClassifier(10, metric='euclidean')
        knn.fit(data, label)
        all_neighbors = []
        for point in data:
            nbs = knn.kneighbors(point.reshape(1, -1), k, return_distance=False)
            all_neighbors.append(nbs)
        return knn, all_neighbors

    def add_relations_edges(self, method='cosine') -> None:
        if method not in ['knn', 'cosine']:
            raise ValueError('Method must be either `knn` or `cosine`')
        employer_node_names = [key for key, item in self.G.nodes.items() if item['node_type'] == 'employer']
        job_node_names = [key for key, item in self.G.nodes.items() if item['node_type'] == 'job']
        candidate_node_names = [key for key, item in self.G.nodes.items() if item['node_type'] == 'candidate']
        employer_vectors = [self.G.nodes[employer]['reduced_tfidf'] for employer in employer_node_names]
        employer_vectors = np.array(employer_vectors).reshape(len(employer_node_names), -1)
        job_vectors = [self.G.nodes[job]['reduced_tfidf'] for job in job_node_names]
        job_vectors = np.array(job_vectors).reshape(len(job_node_names), -1)
        candidate_vectors = [self.G.nodes[candidate]['reduced_tfidf'] for candidate in candidate_node_names]
        candidate_vectors = np.array(candidate_vectors).reshape(len(candidate_node_names), -1)
        if method == 'knn':
            num_employer_neighbors = int(constants.NEIGHBOR_RATIO * len(employer_node_names))
            self.employer_knn, employer_neighbors = self.get_k_neighbors(employer_vectors, np.arange(len(employer_node_names)), num_employer_neighbors)
            num_job_neighbors = int(constants.NEIGHBOR_RATIO * len(job_node_names))
            self.job_knn, job_neighbors = self.get_k_neighbors(job_vectors, np.arange(len(job_node_names)), num_job_neighbors)
            num_candidate_neighbors = int(constants.NEIGHBOR_RATIO * len(candidate_node_names))
            self.candidate_knn, candidate_neighbors = self.get_k_neighbors(candidate_vectors, np.arange(len(candidate_node_names)), num_candidate_neighbors)
            for i, nbs in enumerate(employer_neighbors):
                this_employer = employer_node_names[i]
                for nb_index in nbs[0]:
                    nb_name = employer_node_names[nb_index]
                    if not self.G.has_edge(this_employer, nb_name):
                        self.G.add_edge(this_employer, nb_name, edge_type='employer_to_employer', weight=constants.SIMILAR_WEIGHT)
                        self.G.graph['employer_to_employer'] += 1
            for i, nbs in enumerate(job_neighbors):
                this_job = job_node_names[i]
                for nb_index in nbs[0]:
                    nb_name = job_node_names[nb_index]
                    if not self.G.has_edge(this_job, nb_name):
                        self.G.add_edge(this_job, nb_name, edge_type='job_to_job', weight=constants.SIMILAR_WEIGHT)
                        self.G.graph['job_to_job'] += 1
            for i, nbs in enumerate(candidate_neighbors):
                this_candidate = candidate_node_names[i]
                for nb_index in nbs[0]:
                    nb_name = candidate_node_names[nb_index]
                    if not self.G.has_edge(this_candidate, nb_name):
                        self.G.add_edge(this_candidate, nb_name, edge_type='candidate_to_candidate', weight=constants.SIMILAR_WEIGHT)
                        self.G.graph['candidate_to_candidate'] += 1
            pm_num_neigbors = int(constants.PROFILE_MATCHED_NEIHBOR_RATIO * len(candidate_node_names))
            for i, vector in enumerate(candidate_vectors):
                this_candidate = candidate_node_names[i]
                nbs = self.job_knn.kneighbors(vector.reshape(1, -1), pm_num_neigbors, return_distance=False)
                for nb_index in nbs[0]:
                    nb_name = job_node_names[nb_index]
                    if not self.G.has_edge(this_candidate, nb_name):
                        self.G.add_edge(this_candidate, nb_name, edge_type='candidate_to_job', weight=constants.PROFILE_MATCH_WEIGHT)
                        self.G.graph['candidate_to_job'] += 1
        if method == 'cosine':
            for i, id1 in enumerate(employer_node_names):
                id1_vector = self.G.nodes[id1]['reduced_tfidf']
                for id2 in employer_node_names[i+1:]:
                    id2_vector = self.G.nodes[id2]['reduced_tfidf']
                    sim = 1 - distance.cosine(id1_vector, id2_vector)
                    if sim >= constants.COSINE_SIMILARITY_THRESHOLD:
                        self.G.add_edge(id1, id2, edge_type='employer_to_employer', weight=constants.EMPLOYER_TO_EMPLOYER_WEIGHT, cosine_similarity=sim)
                        self.G.add_edge(id2, id1, edge_type='employer_to_employer', weight=constants.EMPLOYER_TO_EMPLOYER_WEIGHT, cosine_similarity=sim)
                        self.G.graph['employer_to_employer'] += 1
            for i, id1 in enumerate(job_node_names):
                id1_vector = self.G.nodes[id1]['reduced_tfidf']
                for id2 in job_node_names[i+1:]:
                    id2_vector = self.G.nodes[id2]['reduced_tfidf']
                    sim = 1 - distance.cosine(id1_vector, id2_vector)
                    if sim >= constants.COSINE_SIMILARITY_THRESHOLD:
                        self.G.add_edge(id1, id2, edge_type='job_to_job', weight=constants.JOB_TO_JOB_WEIGHT, cosine_similarity=sim)
                        self.G.add_edge(id2, id1, edge_type='job_to_job', weight=constants.JOB_TO_JOB_WEIGHT, cosine_similarity=sim)
                        self.G.graph['job_to_job'] += 1
            for i, id1 in enumerate(candidate_node_names):
                id1_vector = self.G.nodes[id1]['reduced_tfidf']
                for id2 in candidate_node_names[i+1:]:
                    id2_vector = self.G.nodes[id2]['reduced_tfidf']
                    sim = 1 - distance.cosine(id1_vector, id2_vector)
                    if sim >= constants.COSINE_SIMILARITY_THRESHOLD:
                        self.G.add_edge(id1, id2, edge_type='candidate_to_candidate', weight=constants.CANDIDATE_TO_CANDIDATE_WEIGHT, cosine_similarity=sim)
                        self.G.add_edge(id2, id1, edge_type='candidate_to_candidate', weight=constants.CANDIDATE_TO_CANDIDATE_WEIGHT, cosine_similarity=sim)
                        self.G.graph['candidate_to_candidate'] += 1
            for i, id1 in enumerate(candidate_node_names):
                id1_expertise = self.G.nodes[id1]['expertise'] 
                for id2 in candidate_node_names[i+1:]:
                    id2_expertise = self.G.nodes[id2]['expertise']
                    if id1_expertise == id2_expertise:
                        self.G.add_edge(id1, id2, edge_type='expertise_match', weight=constants.EXPERTISE_MATCH_WEIGHT)
                        self.G.add_edge(id2, id1, edge_type='expertise_match', weight=constants.EXPERTISE_MATCH_WEIGHT)
                        self.G.graph['expertise_match'] += 1
                       
    def build(self) -> None:
        logger.info('Start building the master Graph...')
        self.G = self.create_network_from_data()
        logger.info('Master Graph is built.')
        logger.info('Creating LSA comparer')
        self.get_lsa() 
        logger.info('Compute tf-idf vector for every node')
        self.vectorize_nodes()
        logger.info('Creating keywords for nodes...')
        self.create_keywords_for_nodes()
        logger.info('Adding relations edges...')
        self.add_relations_edges(method=constants.SIMILARITY_METHOD)
        logger.info('Network is built.')


if __name__ == '__main__':

    if os.path.isfile(constants.NETWORK_BUILDER_SAVE_PATH):
        logger.info(f'Loading network from {constants.NETWORK_BUILDER_SAVE_PATH}')
        with open(constants.NETWORK_BUILDER_SAVE_PATH, 'rb') as f:
            network = pickle.load(f)

    else:
        network = NetworkBuilder(constants.EMPLOYERS_DATA_PATH,
                            constants.JOBS_DATA_PATH,
                            constants.CV_DATAPATH)

        network.build()

        logger.info(f'saving network builder object to {constants.NETWORK_BUILDER_SAVE_PATH}')

        with open(constants.NETWORK_BUILDER_SAVE_PATH, 'wb') as f:
            pickle.dump(network, f, pickle.HIGHEST_PROTOCOL)
