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

data = []
for record in records:
    data.append(dict(zip(attributes, 
                         [value.strip() for value in record.split(",")])))
records_num = len(data)
print "\nstatus: input data parsed and stored away"
print "status: number of records is:", records_num, ":O"

def all_possible_values(data, attribute):
    """
    Builds a set of all possible values of a given 'attribute'
    from the dataset 'data'
    """
    values_set = set()
    for record in data:
        values_set.add(record[attribute])
    return values_set

def attribute_values_dict(data, attributes):
    """
    Given a list of attributes, this builds a dictionary of
    keys and sets of all their possible values
    """
    attr_values_ratios = dict()
    for attribute in attributes:
#        attribute_values[attribute] = all_possible_values(data, attribute)
        ratios_dict = dict()
        for attr_value in list(all_possible_values(data, attribute)):
            count = 0
            for record in data:
                if record[attribute] == attr_value:
                    count = count + 1
        #               print "count is ", count
                ratios_dict[attr_value] = float(count)/records_num
        attr_values_ratios[attribute] = ratios_dict

    return attr_values_ratios

#diction = attribute_values_dict(data, attributes)
#for key in diction.keys():
#    print "For attribute", key, ":"
#    for value in diction[key].keys():
#        print value, diction[key][value]
#print all_possible_values(data, "wrf")    
def calc_attr_ratios(attribute, values_set):
    ratios_dict = dict()
    for value in values_set:
        count = 0
        for record in data:
            if record[attribute] == value:
                count = count + 1
 #               print "count is ", count
        ratios_dict[value] = float(count)/records_num
    
    return ratios_dict
print attribute_values_dict(dict, attributes)
*/
#calc_attr_ratios(class_attr, values_set)

#print records_num
#print "\nset of values for class label is:", values_set, len(values_set)



#def entropy(data, target):
    
 
