import networkx as nx
import matplotlib.pyplot as plt
import requests
import time

def fetch_paper_data(arxiv_id):
    url = f"https://api.semanticscholar.org/v1/paper/arXiv:{arxiv_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data for arXiv:{arxiv_id}: {response.status_code}")
        return None

def build_citation_network(paper_data, depth=3, max_references=5):
    G = nx.DiGraph()
    papers_to_process = [(paper_data, 0)]
    processed_papers = set()

    while papers_to_process:
        current_paper, current_depth = papers_to_process.pop(0)
        if current_paper['arxivId'] in processed_papers:
            continue

        processed_papers.add(current_paper['arxivId'])
        G.add_node(current_paper['arxivId'], title=current_paper['title'])

        if current_depth < depth:
            references = current_paper.get('references', [])[:max_references]
            for ref in references:
                if ref.get('arxivId'):
                    G.add_edge(current_paper['arxivId'], ref['arxivId'])
                    if ref['arxivId'] not in processed_papers:
                        ref_data = fetch_paper_data(ref['arxivId'])
                        if ref_data:
                            papers_to_process.append((ref_data, current_depth + 1))
                        time.sleep(1)  # To avoid rate limiting

    return G

def plot_network(G):
    fig, ax = plt.subplots(figsize=(20, 15))
    pos = nx.spring_layout(G, k=0.5, iterations=50)
    
    node_sizes = [3000 if node == "2303.14957" else 1000 for node in G.nodes()]
    node_colors = ["red" if node == "2303.14957" else "skyblue" for node in G.nodes()]
    
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, alpha=0.8)
    nx.draw_networkx_edges(G, pos, ax=ax, arrows=True, edge_color="gray", alpha=0.5, arrowsize=10)
    
    labels = {node: G.nodes[node]['title'][:20] + '...' for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, ax=ax, font_size=6, font_weight="bold")
    
    ax.set_title("arXiv Citation Network (3 Layers)", fontsize=16)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

def analyze_network(G):
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    
    degree_centrality = nx.degree_centrality(G)
    top_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\nTop 5 papers by degree centrality:")
    for paper_id, centrality in top_degree:
        print(f"{G.nodes[paper_id]['title'][:50]}... : {centrality:.4f}")
    
    pagerank = nx.pagerank(G)
    top_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)[:5]
    print("\nTop 5 papers by PageRank:")
    for paper_id, rank in top_pagerank:
        print(f"{G.nodes[paper_id]['title'][:50]}... : {rank:.4f}")

if __name__ == "__main__":
    arxiv_id = "2303.14957"
    paper_data = fetch_paper_data(arxiv_id)
    
    if paper_data:
        G = build_citation_network(paper_data, depth=3, max_references=5)
        plot_network(G)
        analyze_network(G)
    else:
        print("Failed to fetch paper data.")
