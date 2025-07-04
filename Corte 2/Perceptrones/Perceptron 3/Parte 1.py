inputs = [1, 2, 3, 4]
targets = [2, 4, 6, 8]

w = 0.1
epochs = 30
learning_rate = 0.1

def predict(i):
  return w*i

for _ in range(epochs):
  pred = [predict(i) for i in inputs]
  errors = [(p - t)**2 for p, t in zip(pred, targets)]
  cost = sum(errors)/len(targets)
  errors_d = [2*(p - t) for p, t in zip(pred, targets)]
  weight_d = [e*i for e, i in zip(errors_d, inputs)]

  w+= learning_rate*sum(weight_d)/len(weight_d)
  print(f"Weight: {w:.2f} Cost: {cost:.2f}")
