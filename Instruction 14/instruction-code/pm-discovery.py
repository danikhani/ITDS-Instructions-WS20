# 1. Import libraries
import os
import csv
from pm4py.objects.log.importer.xes import factory as xes_importer
from pm4py.objects.conversion.dfg import factory as dfg_mining_factory
from pm4py.algo.discovery.dfg import factory as dfg_factory
from pm4py.visualization.dfg import factory as dfg_vis_factory
from pm4py.visualization.petrinet import factory as pn_vis_factory


# 2. preprocessing
with open('dfr1.txt') as file:
    file_reader = csv.reader(file, delimiter='\t')
    dfg = dict()
    for row in file_reader:
        _from,_to=row[0].split(',')
        rel = (_from,_to)
        freq = int(row[1])
        dfg[rel] = freq

# 3. Visualize Directly-follows-graph (DFG)
gviz = dfg_vis_factory.apply(dfg)
dfg_vis_factory.view(gviz)

# 4. Discover and Visualize Workflow-Net
net, im, fm = dfg_mining_factory.apply(dfg)
gviz = pn_vis_factory.apply(net, im, fm)
pn_vis_factory.view(gviz)