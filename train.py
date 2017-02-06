import argparse
import cPickle, gzip
from numpy import *

parser = argparse.ArgumentParser()

# Defining the arguments to be used
parser.add_argument("--lr", action="store", dest="lr", type=float, help = "Initial learning rate" + chr(225) + " for gradient descent based algorithms", default=1)
parser.add_argument("--momentum", action="store", dest="momentum", type=float, help = "Momentum to be used by momentum based algorithms", default=1)
parser.add_argument("--num_hidden", action="store", dest="num_hidden", type=int, help = "Number of hidden layers")
parser.add_argument("--sizes", action="store", dest="sizes_string", type=str, help = "A comma separated list for the size of each hidden layer")
parser.add_argument("--activation", action="store", dest="activation", type=str, choices=set(("tanh","sigmoid")), help = "The choice of activation function - Valid values are tanh / sigmoid")
parser.add_argument("--loss", action="store", dest="loss", type=str, choices=set(("sq","ce")), help = "Possible choices are squared error[sq] or cross entropy loss[ce]")
parser.add_argument("--opt", action="store", dest="opt", type=str, choices=set(("gd","momentum","nag","adam")) , help = "The optimization algorithm to be used: gd, momentum, nag, adam")
parser.add_argument("--batch_size", action="store", dest="batch_size", type=int, help = "The batch size to be used - Valid values are 1 and multiples of 5", default=1)
parser.add_argument("--anneal", action="store", dest="anneal", type=bool, help = "If true the algorithm should halve the learning rate if at any epoch the validation loss decreases and then restart that epoch", default=1)
parser.add_argument("--save_dir", action="store", dest="save_dir", type=str, help = "The directory in which the pickled model should be saved") 
parser.add_argument("--expt_dir", action="store", dest="expt_dir", type=str, help = "The directory in which the log files will be saved")
parser.add_argument("--mnist", action="store", dest="mnist", type=str, help = "Path to the mnist data in pickeled format")
args = parser.parse_args()
print args

if(args.batch_size != 1 and args.batch_size % 5 != 0):
    print ("Invalid argument")

# Process string_sizes and create sizes
sizes = []
for size_string in args.sizes_string.split(','):
    sizes.append(int(size_string))

# Load the dataset
f = gzip.open(args.mnist, 'rb')
train_set, valid_set, test_set = cPickle.load(f)
f.close()

print(shape(train_set))
print(shape(valid_set))
print(shape(test_set))

INPUT_LAYER_SIZE = 784
OUTPUT_LAYER_SIZE = 10
 
print sizes[0]
W = []

W.append(zeros((INPUT_LAYER_SIZE, sizes[0])))
for i in (1,args.num_hidden-1):
    W.append(zeros((sizes[i-1], sizes[i])))
W.append(zeros((sizes[args.num_hidden-1], OUTPUT_LAYER_SIZE)))

B = []
print args.num_hidden

for i in range(0,args.num_hidden-1):
    print i
    B.append(zeros(sizes[i]))
B.append(zeros(OUTPUT_LAYER_SIZE))

print size(B)
def sigmoid(h,length):
    return

def tanh(h,length):
    return

def forward_propogation():
    return

def backward_propogation():
    return

def loss():
    return

def squared_error_loss():
    return

def cross_entropy_loss():
    return
