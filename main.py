import math

def get_float_sizes(items: dict):
  return sorted([cw['weight'] - int(cw['weight']) for cw in items.values() if isinstance(cw['weight'], float)])


def get_calculated_sizes(items: dict, knap_sack_size: int) -> dict:
  float_sizes = get_float_sizes(items)
  return {i: [i + float_size for float_size in float_sizes] for i in range(knap_sack_size + 1)}

      
def knap_sack_problem(items: dict, knap_sack_size: int):
  grid = {}
  sizes = get_calculated_sizes(items, knap_sack_size)
  lattest_gridded_item = None
  for item, attrs in items.items():
    current_item_cost = attrs['cost']
    current_item_weight = attrs['weight']
    grid[item] = {}
    current_gridded_item = grid[item]    
    for size, float_sizes in sizes.items():
      if size != 0:
        current_gridded_item[size] = {
              'items': [],
              'worth': 0
        }
        if size == current_item_weight:
          current_gridded_item[size]['items'] = [item]
          current_gridded_item[size]['worth'] = current_item_cost
        elif size > current_item_weight:
          current_gridded_item[size]['items'].append(item)
          current_gridded_item[size]['worth'] = current_item_cost
          if lattest_gridded_item:
            size_to_sum = abs(size - current_item_weight)
            if lattest_gridded_item.get(size_to_sum):
              current_gridded_item[size]['items'] += lattest_gridded_item[size_to_sum]['items']
              current_gridded_item[size]['worth'] += lattest_gridded_item[size_to_sum]['worth']
        else:
          if lattest_gridded_item:
            current_gridded_item[size]['items'] = lattest_gridded_item[size]['items']
            current_gridded_item[size]['worth'] = lattest_gridded_item[size]['worth']
      for float_size in float_sizes:
        current_gridded_item[float_size] = {
              'items': [],
              'worth': 0
        }
        if float_size == current_item_weight:
          current_gridded_item[float_size]['items'].append(item)
          current_gridded_item[float_size]['worth'] += current_item_cost
        elif float_size > current_item_weight:
          current_gridded_item[float_size]['items'].append(item)
          current_gridded_item[float_size]['worth'] += current_item_cost
          if lattest_gridded_item:
            size_to_sum = abs(float_size - current_item_weight)
            current_gridded_item[float_size]['items'] += lattest_gridded_item[size_to_sum]['items']
            current_gridded_item[float_size]['worth'] += lattest_gridded_item[size_to_sum]['worth']
        else:
          if lattest_gridded_item:
            current_gridded_item[float_size]['items'] += lattest_gridded_item[float_size]['items']
            current_gridded_item[float_size]['worth'] += lattest_gridded_item[float_size]['worth']
        lattest_gridded_float_size = float_size
    lattest_gridded_item = current_gridded_item
  return grid
    
    
def main():
  items = {
    'guitar': {
      'cost': 1500,
      'weight': 1
    },
    'stereo': {
      'cost': 3000,
      'weight': 4
    },
    'laptop': {
      'cost': 2000,
      'weight': 3
    },
    'gold': {
      'cost': 10000,
      'weight': 0.5
      
    }
      
      
  }
  print(knap_sack_problem(items, 4))
  pass




if __name__ == '__main__':
  main()

