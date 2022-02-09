#A minimized Generative Adversarial Network Training Model for Generating Audio Encoded MP4 Video Files
import os,sys,time,datetime,getopt,argparse
import numpy as np
from matplotlib import pyplot as plt
import argparse
import tensorflow as tf
import tensorflow.contrib.slim as slim
import tensorflow.contrib.slim.python.slim.nets as nets
import tensorflow.contrib.slim.python.slim.arguments as arguments
from tensorflow.contrib.slim.python.slim.data import dataset

def conv2d(data, num_filters, filter_size, stride, scope='conv2d', bn=False, act=tf.nn.relu):
    with tf.name_scope(scope):
        if bn:
            with tf.name_scope('bn'):
                slim.conv2d(data, num_filters, 3, stride, padding='SAME', scope='conv2d/bn', bn=True, act=None)
        else:
            with tf.name_scope('conv2d'):
                slim.conv2d(data, num_filters, filter_size, stride, padding='SAME', scope='conv2d', act=None)

def conv2d_bn(data, num_filters, filter_size, stride, scope='conv2d_bn', bn=True, act=tf.nn.relu):
    with tf.name_scope(scope):
        if bn:
            with tf.name_scope('bn'):
                slim.conv2d(data, num_filters, 3, stride, padding='SAME', scope='conv2d_bn/bn', bn=True, act=None)
        else:
            with tf.name_scope('conv2d_bn'):
                slim.conv2d(data, num_filters, filter_size, stride, padding='SAME', scope='conv2d_bn', bn=True, act=None)

def fc(data, num_output, scope='fc', act=tf.nn.relu):
    with tf.name_scope(scope):
        slim.fully_connected(data, num_output, act, scope='fc')

def conv2d_block(data, in_channels, out_channels, stride, block, scope='conv2d_block', bn=False, act=tf.nn.relu):
    with tf.name_scope(scope):
        if bn:
            with tf.name_scope('bn'):
                conv2d_bn(data, in_channels, out_channels, stride, scope='conv2d_block/bn', bn=True, act=None)
        else:
            conv2d(data, in_channels, out_channels, stride, scope='conv2d_block', bn=False, act=None)

def fc_block(data, in_channels, out_channels, stride, block, scope='fc_block', act=tf.nn.relu):
    with tf.name_scope(scope):
        slim.fully_connected(data, out_channels, act, scope='fc_block')

def max_pool(data, pool_size):
    with tf.name_scope('max_pool'):
        stride = (1, 1)
        tf.nn.max_pool(data, ksize=pool_size, strides=stride, padding='SAME', name='max_pool')

def resnet_blocks(block, blocks, output_channels, pool_size, train=True):
    return [block for block in blocks if train]

def build_resnet(network, input_dim, num_classes):
    # create blocks
    net = slim.fully_connected(inputs=network, num_outputs=output_channels, activation_fn=None, weights_initializer=tf.random_normal_initializer(stddev=0.02), weights_regularizer=None)
    # select model
    lr = tf.placeholder(tf.float32, name='learning_rate')
    if train:
        optimizer = tf.train.AdamOptimizer(learning_rate=lr)
    else:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=lr)
    grads = optimizer.compute_gradients(net.loss)
    # clip gradients
    grads = [tf.clip_by_value(g, -10., 10.) for g in grads]
    # make sure all gradients are no larger than 5.0
    update = tf.group(*[g for g in grads if g[0] < 5.])
    # apply gradients and update parameters
    net.apply_gradients(grads)
    net.assign_from(net.loss, is_training=train)
    # get logits
    logits = net.get_logits()
    # compute softmax
    predictions = tf.nn.softmax(logits)
    # compute the loss
    losses = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=tf.placeholder(tf.float32, name='y_true'), logits=logits))
    # compute accuracy
    correct_prediction = tf.equal(tf.argmax(logits, 1), tf.argmax(y_true, 1))
    correct_prediction = tf.cast(correct_prediction, tf.float32)
    accuracy = tf.reduce_mean(correct_prediction)
    # start training
    if train:
        train_step = optimizer.minimize(losses, tf.placeholder(tf.float32, name='global_step'))
        # display logs
        with tf.name_scope('display'):
            tf.summary.histogram('x', x_data)
            tf.summary.histogram('y_true', y_true)
            tf.summary.histogram('y_pred', predictions)
            tf.summary.histogram('accuracy', accuracy)
            tf.summary.scalar('loss', losses)
            tf.summary.scalar('learning_rate', lr)
            tf.summary.scalar('global_step', train_step)
    else:
        train_step = tf.constant(0, dtype=tf.int64)
        display_step = tf.constant(0, dtype=tf.int64)
        # print the loss
