def get_float_sizes(items: dict):
    return sorted([cw['weight'] - int(cw['weight']) for cw in items.values() if isinstance(cw['weight'], float)])

def get_calculated_sizes(items: dict, knap_sack_size: int) -> dict:
    float_sizes = get_float_sizes(items)
    return {i: [i + float_size for float_size in float_sizes] for i in range(knap_sack_size + 1)}

      

def knap_sack_problem(items: dict, knap_sack_size: int):
  grid = {}
  sizes = get_calculated_sizes(items, knap_sack_size)
  for item, attrs in items.items():
    current_item_cost = attrs['cost']
    current_item_weight = attrs['weight']
    grid[item] = {}
    current_gridded_item = grid[item]    
    for size, float_sizes in sizes.items():
      int_size = int(size)
      if (int_size != 0):
        
        if (current_item_weight == int_size):
          current_gridded_item[size] = {
              'items': [item],
              'worth': current_item_cost
            }
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