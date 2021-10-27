# pds
## Proportionally dense subgraphs in cubic graphs - Overview
`pds` is a framework written in Python for generating and drawing random cubic graphs, showing a proportionally dense subgraph (PDS) of the maximum size, and searching for graphs that do not have a PDS of the maximum size. Bazgan et al. defined *"a proportionally dense subgraph (PDS) as an induced subgraph of a graph with the property that each vertex in the PDS is adjacent to proportionally as many vertices in the subgraph as in the graph" (source: https://arxiv.org/abs/1903.06579)*. For cubic graphs, the maximum size of a PDS is floor((2*|V| + 1)/3). A specific search for cubic graphs with no Hamiltonian cycle can be done. Also, cubic graphs with no Hamiltonian cycle can be generated. Finally, it is possible to check that every vertex is part of a PDS of the maximum size and to get all the PDSs of the same non-Hamiltonian cubic graph.

## Install
### Command line (bash)
```bash
git clone https://github.com/d-m-3/pds.git
pip install -r requirements.txt
```

## Usage
- `pds.py` is the main library that can be imported as a module (see below).
- `pds_tests.py` contains the unit tests for all the functions in `pds.py`, except for the functions that draw and/or save graphs.
- `usecase_search_exceptions.py` is used to create random cubic graphs and check for graphs with no PDS of the maximum size. You can also specifically search for cubic graphs that do not have a Hamiltonian cycle. If an exception is found, it is drawn, and saved as a `.png` figure and as an edge list.
- `usecase_draw_1_pds.py` is used to draw cubic graphs up to 28 vertices.
- `usecase_draw_all_pds.py` is used to draw different (or all) PDSs of the same non-Hamiltonian cubic graph.
- `usecase_every_v_in_pds.py` is used to check if every vertex is part of a PDS of the maximum size.
- `usecase_every_v_ds2.py` is used to check if, for every graph, there exists a PDS of the maximum size and d_s(v) = 2 for every vertex v.
- `usecase_every_v_ds2_ds3.py` is used to check if, for every graph, there exists a PDS of the maximum size and d_s(v) = 2 for every vertex v, except for at most `ds3_nb`, where d_s(v) = 3.
- `usecase_create_nham_graph.py` is used to create one (ore more) cubic graph(s) with no Hamiltonian cycle.
- `gex.py` contains specific graphs, notably, exceptions of 8 vertices, that do not have a PDS of the maximum size, and graphs used for unit tests.

## External usage
You can import the library `pds` in your own modules:

```python
import pds
```