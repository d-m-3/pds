# pds-cubic
## Proportionally dense subgraphs in cubic graphs - Overview
`pds_cubic` is a framework written in Python for generating and drawing random cubic graphs, showing a proportionally dense subgraph (PDS) of the maximum size, and searching for graphs that do not have a PDS of the maximum size. Bazgan et al. defined *"a proportionally dense subgraph (PDS) as an induced subgraph of a graph with the property that each vertex in the PDS is adjacent to proportionally as many vertices in the subgraph as in the graph" (source: https://arxiv.org/abs/1903.06579)*. A specific search for cubic graphs with no Hamiltonian cycle can be done. Also, cubic graphs with no Hamiltonian cycle can be generated. Finally, it is possible to check that every vertex is part of a PDS of maximum size, and to get all PDSs of a same non-Hamiltonian cubic graph.

## Install
### Command line (bash)
```bash
git clone https://github.com/d-m-3/pds-cubic.git
pip install -r requirements.txt
```

## Usage
- `pds_cubic.py` is the main library that can be imported as a module (see below).
- `pds_cubic_compute.py` is used to create random cubic graphs and check for graphs with no PDS of maximum size. You can also specifically search for cubic graphs that do not have a Hamiltonian cycle. If an exception is found, it is drawn, and saved as a `.png` figure and as an edge list.
- `pds_cubic_draw.py` is used to draw cubic graphs up to 28 vertices.
- `pds_cubic_draw_some_pds.py` is used to draw different (or all) PDSs of the same non-Hamiltonian cubic graph.
- `pds_cubic_every_vertex.py` is used to check if every vertex is part of a PDS of maximum size.
- `create_nham_cubic_graph.py` is used to create one (ore more) cubic graph(s) with no Hamiltonian cycle.
- `pds_cubic_tests.py` contains unit tests. Note that the tests are not exhaustive.
- `gex.py` contains three graph exceptions of 8 vertices, that do not have a PDS of maximum size.

## External usage
You can import the library `pds_cubic` in your own modules:

```python
import pds_cubic as pds
```