# pds
## Proportionally Dense Subgraphs in k-regular Graphs - Overview
`pds` is a framework written in Python for generating and drawing random k-regular graphs, computing and showing proportionally dense subgraphs (PDSs) of the maximum size.

Bazgan et al. defined *"a proportionally dense subgraph (PDS) as an induced subgraph of a graph with the property that each vertex in the PDS is adjacent to proportionally as many vertices in the subgraph as in the graph" (source: https://arxiv.org/abs/1903.06579)*.

The project also contains several *use cases* that show specific usages of the framework. Some use cases were used to check ideas and conjectures about PDSs in k-regular graphs empirically. These use cases are described in the section *Usage* (see below).

## Install
### On Debian-based Linux
In a `bash` terminal, type:
```bash
sudo apt update
sudo apt install python3-pip
git clone https://github.com/d-m-3/pds.git
pip install -r requirements.txt
```
### On macOS
1. Check that Python 3 is installed. In a terminal, type:
```bash
python3 --version
```
2. Download `pip`. In a terminal, type:
```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
3. Install `pip`. In a terminal, type:
```bash
python3 get-pip.py
```
4. Install the modules `networkx` and `matplotlib` with pip. In a terminal, type:
```bash
pip install networkx
pip install matplotlib
```
5. Get the files of the project. Two options:\
a) With `git clone`. In a terminal, type:
`git clone https://github.com/d-m-3/pds.git`\
b) Or click on *Code - Download ZIP*
on the project's GitHub page: https://github.com/d-m-3/pds

## Usage
- `pds.py` is the main library that can be imported as a module (see *External Usage* below).
- `pds_tests.py` contains the unit tests for all the functions in `pds.py`, except for the functions that draw and/or save graphs.
- `usecase_search_exceptions.py`. It creates random cubic graphs and tests if they do not have a PDS of the maximum size. If such a graph is found, the program's execution is stopped, the graph is drawn, and it is saved as a .png figure and as an edge list that can be imported later. The number of vertices in a graph and the number of created and tested graphs can be defined. If the boolean "only_nh" is set to "True", only cubic graphs that do not have a Hamiltonian cycle are considered (please notice that it takes much longer).
- `usecase_draw_1_pds.py`. It creates and draws a random cubic graph on a given number of vertices. It finds a PDS of the maximum size, and its vertices are colored in red. Alternatively, it can create and draw a random k-regular bipartite graph instead of a cubic graph. In that case, a specific layout for bipartite graphs can be used.
- `usecase_draw_all_pds.py`. It creates a random cubic graph on a given number of vertices. It finds and draws all its PDSs of the maximum size, and vertices belonging to a PDS are colored in red. Alternatively, it can create a random k-regular bipartite graph instead of a cubic graph. In that case, a specific layout for bipartite graphs can be used.
- `usecase_every_v_in_pds.py`. It creates random cubic graphs and tests if, for every graph, every vertex is part of at least one PDS of the maximum size. If the program finds a graph in which there are vertices that are not part of any PDS, the graph is drawn, the vertices that are not part of any PDS are displayed, and the program's execution is stopped. The number of vertices in a graph and the number of created and tested graphs can be defined. If the boolean "only_nh" is set to "True", only cubic graphs that do not have a Hamiltonian cycle are considered (please notice that it takes much longer).
- `usecase_every_v_ds2.py`. It creates random cubic graphs and tests if, for every graph, there exists a PDS of the maximum size and d_s(v) = 2 for every vertex v. If there is no such PDS for a graph, the graph and all the PDSs of the maximum size are drawn, and the program's execution is stopped. The number of vertices in a graph and the number of created and tested graphs can be defined. If the boolean "only_nh" is set to "True", only cubic graphs that do not have a Hamiltonian cycle are considered (please notice that it takes much longer).
- `usecase_every_v_ds2_ds3.py`. It creates random cubic graphs and tests if, for every graph, there exists a PDS of the maximum size and d_s(v) = 2 for every vertex v, except for at most `ds3_nb` vertices, where d_s(v) = 3. If there is no such PDS for a graph, the graph and all the PDSs of the maximum size are drawn, and the program's execution is stopped. The number of vertices in a graph and the number of created and tested graphs can be defined. If the boolean "only_nh" is set to "True", only cubic graphs that do not have a Hamiltonian cycle are considered (please notice that it takes much longer).
- `usecase_create_nham_graph.py`. It creates a non-Hamiltonian cubic graph on a given number of vertices, saves it in the given folder, with the number of vertices at the end of the filename. It also saves the figure in .png in the same directory.
- `usecase_k_regular_bipartite.py`. It creates and draws a k-regular bipartite graph on a given number of vertices. It finds a PDS of the maximum size, and its vertices are colored in red. Alternatively, it tries to find a k-regular bipartite graph that has no PDS of the maximum size.
- `gex.py`. It contains specific graphs used for unit tests and exceptions of cubic graphs on eight vertices, i.e., cubic graphs that do not have a PDS of the maximum size.

## External Usage
You can import the library `pds` in your own modules:

```python
import pds
```