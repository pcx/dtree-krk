import sys

if len(sys.argv) != 2:
    print "error: wrong commandline usage"
    sys.exit(2)

try:
    fin = open(sys.argv[1], "r")
except IOError:
    print "error: could not open file '", sys.argv[1], "'"
    sys.exit(2)
print "status: successfully opened file", sys.argv[1]

records = [line.strip() for line in fin.readlines()]

attributes = ["wkf", "wkr", "wrf", "wrr", "bkf", "bkr", "result"]
class_attr = "result"

print "\nstatus: seven attributes have been set, they are:"
print "\t",attributes
print "status: class attribute set to 'result'"

#saving data as a list of dictionaries
data = []
for record in records:
    data.append(dict(zip(attributes, 
                         [value.strip() for value in record.split(",")])))
records_num = len(data)
print "\nstatus: input data parsed and stored away"
print "status: number of records is:", records_num, ":O"

#building a set of all class labels
class_labels = set()
for datum in data:
    class_labels.add(datum["result"])

#splitting data into training and test data
#1/4th of each class in testing set to maintain proportions
testing_data = []
for class_label  in class_labels:
    count = 0
    i = 0
    for datum in data:
        if datum["result"] == class_label:
            count = count + 1
    for datum in data:
        if i < count/4:
            if datum["result"] == class_label:
                testing_data.append(datum)
                data.remove(datum)
                i = i + 1

print "Testing data seperated, length is", len(testing_data), "records"
print "Training data now is of length", len(data), "records"        

from dtree import dtnode
root_node = dtnode(data, attributes.remove("result"), "result")
