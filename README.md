# Assignemt2 RL
This code includes the relevant files for submission for the RL of assignment2 in the UoT EE569 Deep Learning Course

## Installation:
 ```bash
  git clone https://github.com/OperationRecon/ee569-UoT-assignment2-RL.git
  cd ee569-UoT-assignment2-RL
  pip install -e .
 ```

After installation you can try training your own model using the `main.py` file

sor race against past pre-trained weights by running `eval.py`

## Performance Evaluation
 you can view the training performance of past setup using TensorBoard older runs can be found in their dedicated folder whereas any newer run must be transported there once complete

## Performance Showcase
### Random actions
 ![random actions](./imgs/start.mp4)

### After Training
 ![trained](./imgs/end.mp4)

 attributions:
- [Multi-Car Racing Gym Environment](https://github.com/igilitschenski/multi_car_racing) - Used for the multi-car racing environment.

