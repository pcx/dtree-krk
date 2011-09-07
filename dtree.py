import sys
import math

class dtnode:
    children = []

    def __init__(self, data, attributes, class_attr):
        self.data = data
        self.attributes = attributes
        self.attr_name = select_split_attr()
        self.class_attr = class_attr
        for value in all_possible_values(self.data, self.attr_name):
            new_data = []
            for datum in data:
                if datum.get(self.attr_name) == value:
                    new_data.append(datum)
            new_attr_list = self.attributes[:].remove(self.attr_name)
            child = dtnode(new_data, new_attr_list, class_attr)
            child.parent_attr = self.attr_name
            child.parent_attr_value = value
            child.parent_attr_num = len(self.data)
            self.children.append(child)

    def all_possible_values(data, attribute):
        """
        Builds a set of all possible values of a given 'attribute'
        from the dataset 'data'
        """
        values_set = set()
        for record in data:
            values_set.add(record[attribute])
        return values_set

    def select_split_attr(self):
        highest_gain = 0
        split_attr = ""
        for attribute in self.attributes:
            attr_gain = gain(attribute)
            if attr_gain > highest_gain:
                highest_gain = attr_gain
                split_attr = attribute
        return split_attr

    def gain(self, attribute):
        #adding the first part of the equation, entropy of self to gain
        gain = self.entropy()
        #getting down to child nodes, one by one
        for value in all_possible_values(self.data, attribute):
            #data gets filtered because of the attribute chosen
            data_of_child = []
            for datum in self.data:
                if datum[attribute] == value:
                    data_of_child.append(datum)
            #calculating entropy of children
            entropy_of_child = 0
            for value in all_possible_values(self.data, self.class_attr):
                count = 0
                for datum in data_of_child:
                    if datum[class_attr] == value:
                        count = count + 1
                p = float(count) / len(data_of_child)
                entropy_of_child = entropy_of_child + (-1 *
                                                        p * log(p,2))
            #subtracting each child's wighted contribution to gain
            gain = gain - (float(len(data_of_child)) *
                           entropy_of_child / len(self.data))
        return gain
                
            
    def entropy(self):
        #return entropy of self
        entropy = 0
        for value in all_possible_values(self.data, class_attr):
            count = 0
            for datum in self.data:
                if datum[class_attr] == value:
                    count = count + 1
            p = count/self.parent_attr_num
            entropy = entropy + (-1 * p * log(p, 2))
        return entropy
