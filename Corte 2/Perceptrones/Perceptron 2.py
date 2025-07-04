inputs = [1, 2, 3, 4]
targets = [4, 6, 8, 10]

w = 0.1
b = 0.3
epochs = 30
learning_rate = 0.1

def predict(i):
  return w*i + b
  #Como la función de la recta

for _ in range(epochs):
  pred = [predict(i) for i in inputs]
  errors = [(p - t)** 2 for p, t in zip(pred, targets)]
  cost = sum(errors)/len(targets)
  errors_d = [2* (p - t) for p, t in zip(pred, targets)]
  weight_d = [e*i for e, i in zip(errors_d, inputs)]
  bias_d = [e*1 for e in errors_d]
  w+= learning_rate*sum(weight_d)/len(weight_d)
  b+= learning_rate*sum(bias_d)/len(bias_d)
  print(f"Weight : {w: .2f}, Bias: {b: .2f}, Cost: {cost: .2f}")
