inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]

w = 0.1
learning_rate = 0.1

def predict(i):
  return w*i

for _ in range(100):
  pred = [predict(i) for i in inputs]
  errors = [t - p for p, t in zip(pred, targets)]
  cost = sum(errors)/len(targets)

  print(f"Targets: ", targets)
  print(f"Predictions: ", pred)
  print(f"Errors: ", errors)
  print(f"Weight: {w: .10f}, Cost: {cost:.6f}")
  w+= learning_rate*cost
