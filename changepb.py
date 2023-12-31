

import keras.models
from keras_retinanet import models
from keras.models import load_model
import tensorflow as tf
import os
import os.path as osp
from keras import backend as K

input_path = 'C:\\keras-retinanet\\retinamodels\\'
weight_file = 'training.h5'
weight_file_path = osp.join(input_path,weight_file)
#weight_file_path = osp.join('C:\\keras-retinanet\\retinamodels\\inference.h5')
output_graph_name = weight_file[:-3]+'.pb'

def h5_to_pb(h5_model,output_dir,model_name,out_prefix = 'output_'):
    if osp.exists(output_dir) == False:
        os.mkdir(output_dir)
        out_nodes = []
        for i in range (len(h5_model.outputs)):
            out_nodes.append(out_prefix+str(i+1))
            tf.identity(h5_model.outputs[i],out_prefix+str(i+1))
        sess = K.get_session()

        from tensorflow.python.framework import  graph_util,graph_io
        init_graph = sess.graph.as_graph_def()
        main_graph = graph_util.convert_variables_to_constants(sess,init_graph,out_nodes)
        graph_io.write_graph(main_graph,output_dir,name = model_name,as_text = Flase)

output_dir = osp.join(os.getcwd(),"pb_model")
h5_model = models.load_model(weight_file_path)
h5_to_pb(h5_model,output_dir = 'C:\\keras-retinanet\\pb_model',model_name= output_graph_name)
print('model saved')



