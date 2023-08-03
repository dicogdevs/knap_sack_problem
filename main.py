def get_float_sizes(items: dict):
    return sorted([cw['weight'] - int(cw['weight']) for cw in items.values() if isinstance(cw['weight'], float)])

def get_calculated_sizes(items: dict, knap_sack_size: int) -> dict:
    float_sizes = get_float_sizes(items)
    return {i: [i + float_size for float_size in float_sizes] for i in range(knap_sack_size + 1)}

      

def snap_sack_problem(items: dict, knap_sack_size: int):
  grid = {}
  sizes = get_calculated_sizes(items, knap_sack_size)
  for item, attrs in items.items():
    grid[item] = {}
    current_item = grid[item]
    current_item_cost = attrs['cost']
    current_item_weight = attrs['weight']
    for size, float_sizes in sizes.items():
      pass
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
  print(get_calculated_sizes(items, 4))
  pass

if __name__ == '__main__':
  main()