from typing import List
import re

import numpy as np
import pandas as pd
import networkx as nx
from scipy.spatial import distance

from latent_semantic_analysis import *
import constants
from typing import List, Dict, Any, Optional

class JobRecommender:
    def __init__(self, G: nx.MultiDiGraph, lsa: LSA):
        self.G = G
        self.lsa = lsa
        self.all_node_types = ['candidate', 'employer', 'job']
        self.target_node = None

    def _add_candidate_node(self, data: Dict[str, Any]) -> None:
        """Add a candidate node to the graph."""
        node_name = f"candidate-{self.G.graph['num_candidates']}"
        processed_resume = self.lsa.preprocess_text(data['resume'])
        vectorized_resume = self.lsa.vectorize(processed_resume)

        self.G.add_node(node_name, node_type='candidate', 
                        reduced_tfidf=vectorized_resume, **data)
        self.G.graph['num_candidates'] += 1
        self.target_node = node_name

        for n in self.G:
            if self.G.nodes[n]['node_type'] == 'job':
                continue
            elif self.G.nodes[n]['node_type'] == 'candidate':
                this_node_expertise = self.G.nodes[n]['expertise']
                if this_node_expertise == data['expertise']:
                    self.G.add_edge(node_name, n, edge_type='expertise_match',
                                    weight=constants.EXPERTISE_MATCH_WEIGHT)
                    self.G.add_edge(n, node_name, edge_type='expertise_match',
                                    weight=constants.EXPERTISE_MATCH_WEIGHT)
        # Additional logic for connecting candidate to other nodes based on resume similarity

    def _add_employer_node(self, data: Dict[str, Any]) -> None:
        """Add an employer node to the graph."""
        raise NotImplementedError()  # Implement similar to _add_candidate_node

    def _add_job_node(self, data: Dict[str, Any]) -> None:
        """Add a job node to the graph."""
        raise NotImplementedError()  # Implement similar to _add_candidate_node

    def add_node_to_graph(self, node_type: str, node_data: Dict[str, Any]) -> None:
        """Add a node to the graph."""
        if node_type not in self.all_node_types:
            raise ValueError(f'Node type must be one of {self.all_node_types}, received {node_type} instead.')

        if node_type == 'candidate':
            self._add_candidate_node(node_data)
        elif node_type == 'employer':
            self._add_employer_node(node_data)
        elif node_type == 'job':
            self._add_job_node(node_data)

    def rank_nodes(self, personalized: bool = False, target_node: Optional[str] = None,
                   return_node_type: Optional[str] = 'job', alpha: float = 0.5) -> Dict[str, float]:
        """Rank nodes using PageRank algorithm."""
        if personalized:
            ranks = nx.pagerank(self.G, alpha, personalization={target_node: 1})
        else:
            ranks = nx.pagerank(self.G, alpha)

        filtered_ranks = {key: value for key, value in ranks.items() if key.startswith(return_node_type)}
        sorted_ranks = dict(sorted(filtered_ranks.items(), key=lambda x: x[1], reverse=True))
        return sorted_ranks

    def search(self, keywords: str) -> List[str]:
        """Search for nodes (jobs or employers) based on keywords."""
        results = []
        processed_keywords = set(keywords.lower().translate(str.maketrans('', '', string.punctuation)).split())

        for n in self.G:
            if self.G.nodes[n]['node_type'] == 'candidate':
                continue
            elif self.G.nodes[n]['node_type'] in ['job', 'employer']:
                node_keywords = set(self.G.nodes[n]['keywords'])
                if processed_keywords.issubset(node_keywords):
                    results.append(n)

        return results

    def _rank_node_with_context(self, target_node: str, context_nodes: List[str],
                                alpha: float, return_node_type: Optional[str] = 'job') -> Dict[str, float]:
        """Rank nodes based on personalized PageRank with context."""
        personalized = {target_node: 1}
        personalized.update({node: 1 for node in context_nodes})
        ranks = nx.pagerank(self.G, alpha, personalization=personalized)

        filtered_ranks = {key: value for key, value in ranks.items() if key.startswith(return_node_type)}
        sorted_ranks = dict(sorted(filtered_ranks.items(), key=lambda x: x[1], reverse=True))
        return sorted_ranks
