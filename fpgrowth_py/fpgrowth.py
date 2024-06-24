from collections import defaultdict, OrderedDict
from csv import reader
from itertools import chain, combinations
from optparse import OptionParser
from fpgrowth_py.utils import *
from graphviz import Graph as Graphviz
import time
import matplotlib.pyplot as plt

def fpgrowth(itemSetList, minSupRatio, minConf):
    frequency = getFrequencyFromList(itemSetList)
    minSup = len(itemSetList) * minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    if(fpTree == None):
        print('No frequent item set')
    else:
        freqItems = []
        mineTree(headerTable, minSup, set(), freqItems)
        rules = associationRule(freqItems, itemSetList, minConf)
        return freqItems, rules

def fpgrowthFromFile(fname, minSupRatio, minConf):
    itemSetList, frequency = getFromFile(fname)
    #minSup = len(itemSetList) * minSupRatio
    minSup = minSupRatio
    fpTree, headerTable = constructTree(itemSetList, frequency, minSup)
    #createGraphviz(fpTree)
    if(fpTree == None):
        print('No frequent item set')
    else:
        freqItems = []
        mineTree(headerTable, minSup, set(), freqItems)
        rules=None
        #rules = associationRule(freqItems, itemSetList, minConf)
        return freqItems, rules

def createGraphviz(tree):
    dot = Graphviz()
    for k in tree.children:
        dot.edge('NULL', k)
        createGraphvizChildren(k,tree.children[k],dot)
    print(dot.source)
    dot.view()

def createGraphvizChildren(parent, parent_node, dot):
    for count,i in enumerate(parent_node.children):
        if count > 3:
            break
        dot.edge(parent, i)
        if len(parent_node.children[i].children) != 0:
            createGraphvizChildren(i, parent_node.children[i], dot)
    return
if __name__ == "__main__":
    optparser = OptionParser()
    optparser.add_option('-f', '--inputFile',
                         dest='inputFile',
                         help='CSV filename',
                         default=None)
    optparser.add_option('-s', '--minSupport',
                         dest='minSup',
                         help='Min support (float)',
                         default=0.5,
                         type='float')
    optparser.add_option('-c', '--minConfidence',
                         dest='minConf',
                         help='Min confidence (float)',
                         default=0.5,
                         type='float')

    (options, args) = optparser.parse_args()

    #freqItemSet, rules = fpgrowthFromFile(
    #    options.inputFile, options.minSup, options.minConf)
    
    x = []
    y = []
    for i in range(int(options.minSup),int(options.minConf),10):
        start_time = time.time()
        fpgrowthFromFile(options.inputFile, i, options.minConf)
        x.append(i)
        y.append((time.time() - start_time))

    plt.plot(x,y,'k-',marker='o',lw=1.5)
    plt.xlabel('Support threshold')
    plt.ylabel('Runtime (sec)')
    plt.grid(color='black', linestyle='-', linewidth=0.09)
    plt.title('Time against support threshold')
    plt.show()

    #print(freqItemSet)
    #print(rules)
