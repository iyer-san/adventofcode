import re


def add_values_in_dict(sample_dict, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

def get_bigger_bag_color(str):
    pattern = re.compile('(.*) bag[s]?')
    result = pattern.search(str)
    return result.group(1)

def get_smaller_bag_color(str):
    pattern = re.compile('[0-9]* (.*) bag[s]?')
    result = pattern.search(str)
    return result.group(1)

def get_smaller_bags_list(str):
    smaller_bag_list = []
    if 'no' in str:
        smaller_bag_list.append('no bags')
    else:
        smaller_bags = re.split(',', str)
        for bag in smaller_bags:
            smaller_bag_list.append(get_smaller_bag_color(bag))
    return smaller_bag_list



filename = "adventofcode/7/input.txt"
bag_rules = []
with open(filename) as f:
    content = f.read()
    bag_rules = re.split('\n', content)

bag_dict = {}

for rule in bag_rules:
    rule_parts = re.split("contain", rule)
    bigger_bag_color = get_bigger_bag_color(rule_parts[0])
    # print(bigger_bag_color)
    smaller_bags_colors_list = get_smaller_bags_list(rule_parts[1])
    add_values_in_dict(bag_dict, bigger_bag_color, smaller_bags_colors_list)


indirect_list = []

lst = ["shiny gold"]

def get_recursive_bag_list(lst):
    for key in bag_dict:
        for bag in bag_dict[key]:
            for direct_bag in lst:
                temp_list = []
                if(direct_bag in bag):
                    temp_list.append(key)
                    indirect_list.append(key)
                    if(len(temp_list)>0):
                        get_recursive_bag_list(temp_list)

get_recursive_bag_list(lst)

print("part 1")
print(len(set(indirect_list)))


