## Getting Started

### Execution
Run the program with dataset provided and **default** values for *minSupport* = 50 and *minConfidence* = 0.5

```
python fpgrowth.py -f ../dataset/data3.csv
```
Run program with dataset and min support and min confidence  

```
python fpgrowth.py  -f ../dataset/data3.csv -s 60

```
### Example dataset3.csv

<p align=center>
    <img src="./doc/lattice.PNG" width="440" height="331">
</p>

<p align=center>
    <img src="./doc/fp-tree.PNG" width="440" height="331">
</p>


### Compare with apriory 
### Example dataset3.csv

<p align=center>
    <img src="./doc/apriory.PNG" width="440" height="331">
</p>

```
python fpgrowth.py -f ../dataset/data3.csv -s 60
```
