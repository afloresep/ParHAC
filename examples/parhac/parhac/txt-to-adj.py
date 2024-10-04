def convert_to_adj(input_file, output_file):
    nodes = set()
    edges = []

    with open(input_file, 'r') as infile:
        for line in infile:
            # Skip comment lines
            if line.startswith('#'):
                continue
            # Split the line into fromNode and toNode
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue
            from_node, to_node = int(parts[0]), int(parts[1])
            nodes.add(from_node)
            nodes.add(to_node)
            edges.append((from_node, to_node))

    # Prepare the output
    n = len(nodes)  # number of unique nodes
    m = len(edges)  # number of edges
    unique_nodes = sorted(nodes)  # sorting to have consistent order

    # Create a mapping from node id to index
    node_index = {node: index for index, node in enumerate(unique_nodes)}

    # Convert edges to index form
    indexed_edges = [f"{node_index[from_node]}\t{node_index[to_node]}" for from_node, to_node in edges]

    # Write to output file
    with open(output_file, 'w') as outfile:
        outfile.write("AdjacencyGraph\n")
        outfile.write(f"{n}\n")
        outfile.write(f"{m}\n")
        outfile.write("\n".join(str(node) for node in unique_nodes) + "\n")
        outfile.write("\n".join(indexed_edges) + "\n")

# Usage
convert_to_adj('soc-LiveJournal1.txt', 'wiki-Vote.adj')
