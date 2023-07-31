def snap_sack_problem(items: dict, snap_sack_size: int):
  grid = {}
  last_item = ''
  for item, cost_and_weight in items.items():
    grid[item] = []
    for i in range(0, snap_sack_size):
      current_size = i + 1
      grid[item].append({'items': [], 'items_sum': 0})
      if cost_and_weight['weight'] == current_size:
        grid[item][i ]['items'].append(item)
        grid[item][i]['items_sum'] += cost_and_weight['cost']
      elif cost_and_weight['weight']  < current_size:
        grid[item][i]['items'].append(item)
        grid[item][i]['items_sum'] += cost_and_weight['cost']
        if last_item:
          for j in grid[last_item][i-1]['items']:
            grid[item][i-1]['items'].append(j)
          grid[item][i-1]['items_sum'] = grid[last_item][i-1]['items_sum']
      else:
        if last_item:
          for xd in grid[last_item][i - 1 - cost_and_weight['weight']]['items']:
            grid[item][i - 1]['items'].append(xd)
          grid[item][i - 1]['items_sum'] = grid[last_item][i - 1 - cost_and_weight['weight']]['items_sum']
    last_item = item
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
    }
  }
  RESULT = snap_sack_problem(items, 4)
  print(RESULT)
  pass

if __name__ == '__main__':
  main()