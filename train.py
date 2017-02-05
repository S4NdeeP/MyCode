import argparse
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
print args.momentum
print args.lr

if(args.batch_size != 1 and args.batch_size % 5 != 0):
    print ("Invalid argument")
# to process string_sizes

