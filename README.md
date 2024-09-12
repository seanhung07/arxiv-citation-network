# arXiv Citation Network

This project creates and visualizes a citation network for academic papers from the arXiv repository, leveraging the Semantic Scholar API. The network shows relationships between papers based on their citations, where each node represents a paper, and edges represent the citation links. The goal of this project is to explore citation connections and identify influential papers within a specified depth of references.

## Features

- **Paper Data Fetching**: Retrieves metadata and citation information for an arXiv paper using the Semantic Scholar API.
- **Citation Network Building**: Constructs a directed graph of citation relationships between papers up to a customizable depth, with the ability to limit the number of references processed for each paper.
- **Graph Visualization**: Displays the citation network using a graph, where the original paper is highlighted, and edges represent citation links between papers.
- **Network Analysis**: Analyzes the network to calculate key metrics, including:
  - **Degree Centrality**: Identifies the most-cited papers within the network.
  - **PageRank**: Determines the most influential papers based on their position in the network.

## How It Works

1. **Initial Paper**: The user provides an arXiv ID of a paper as the starting point for building the citation network.
2. **Data Fetching**: The script uses the Semantic Scholar API to fetch metadata for the given paper, including its references (i.e., other papers it cites).
3. **Citation Network**: A directed graph is created where nodes represent papers, and edges represent citation relationships. The depth of the graph can be customized to specify how many layers of references are fetched.
4. **Graph Visualization**: The network is visualized using a graph, with the original paper highlighted. Nodes represent papers, and edges represent citation links.
5. **Network Analysis**: The script calculates metrics like degree centrality and PageRank to identify the most cited and influential papers in the network.

## Customization

The following parameters can be adjusted to customize the citation network:

- **Depth**: Controls how many layers of references are included in the citation network. A greater depth means more layers of papers are included in the graph, potentially revealing deeper citation relationships.
- **Max References**: Limits the number of references processed for each paper to prevent excessive API calls and focus on the most relevant citations.

## Network Analysis Metrics

- **Degree Centrality**: Measures the number of direct citations a paper has. Higher values indicate papers that are more frequently cited within the network.
- **PageRank**: Measures the importance of a paper based on its position in the network. It considers not only direct citations but also the citations of those papers, giving a broader view of influence.

## Requirements

To run this project, you'll need:

- **Python 3.x**: The project is written in Python.
- **NetworkX**: A library for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.
- **Matplotlib**: A plotting library for visualizing the citation network as a graph.
- **Requests**: Used for sending HTTP requests to the Semantic Scholar API.
<img width="1710" alt="Screenshot 2024-09-12 at 5 17 35 PM" src="https://github.com/user-attachments/assets/d19e83e5-98a7-42ad-9b1a-1bb8f1b0a08c">


