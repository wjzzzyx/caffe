caffe_root = '../..'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe

from caffe import layers, params

def define_net():
    net = caffe.NetSpec()
    net.data, net.label = layers.Data(source = db, batch_size = batch_size, )
