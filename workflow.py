import json
import os
from graphviz import Digraph
from collections import defaultdict

# ---------- 0. Graphviz Path Handling (Removes need for batch file) ----------
# Check if 'dot' is likely missing from PATH and try to add it programmatically
if "Graphviz" not in os.environ["PATH"]:
    possible_paths = [
        r"C:\Program Files\Graphviz\bin",
        r"C:\Program Files (x86)\Graphviz\bin"
    ]
    for p in possible_paths:
        if os.path.exists(p):
            os.environ["PATH"] += ";" + p
            break

# ---------- 1. Load structured input ----------
with open("workflow.json", "r", encoding="utf-8") as f:
    data = json.load(f)

meta = data["meta"]
node_types = data["node_types"]
nodes = data["nodes"]
edges = data["edges"]

# ---------- 2. Create graph ----------
dot = Digraph(
    name="Workflow",
    format="png"
)

# Set global graph attributes (Title, Layout)
dot.attr(
    rankdir=meta.get("layout", "TB"),
    labelloc="t",
    fontsize="18",
    label=meta.get("title", "Workflow Diagram"),
    compound="true" # Allow edges between clusters if needed
)

# ---------- 3. Group nodes by layer ----------
layers = defaultdict(list)
for node in nodes:
    layers[node["layer"]].append(node)

# ---------- 4. Draw nodes layer by layer ----------
for layer in sorted(layers.keys()):
    with dot.subgraph(name=f"cluster_layer_{layer}") as c:
        # Crucial: Set label to empty string to prevent inheriting the main title
        # and ensure rank="same" keeps them aligned horizontally
        c.attr(rank="same", label="", style="invis") 

        for node in layers[layer]:
            node_style = node_types.get(node["type"], {})
            c.node(
                node["id"],
                node["label"],
                style="filled",
                shape=node_style.get("shape", "box"),
                fillcolor=node_style.get("color", "lightgray")
            )

# ---------- 5. Draw edges ----------
node_ids = {n["id"] for n in nodes}

for edge in edges:
    src = edge["from"]
    dst = edge["to"]

    if src in node_ids and dst in node_ids:
        dot.edge(src, dst)

# ---------- 6. Render ----------
try:
    output_path = dot.render("workflow_diagram")
    print(f"Successfully generated: {output_path}")
except Exception as e:
    print(f"Error generating diagram: {e}")

