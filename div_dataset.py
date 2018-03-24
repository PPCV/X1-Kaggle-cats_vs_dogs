#  !/usr/bin/env python
#  -*- coding:utf-8 -*-

#  ==============================================
#  ·
#  · Author: Maoji Wang
#  ·
#  · maoji.wang@cs.nyu.edu
#  ·
#  · Filename: div_dataset.py
#  ·
#  · COPYRIGHT 2018
#  ·
#  · Description:
#    some codes are stolen from:
#  ·      https://zhuanlan.zhihu.com/p/25978105
#  ·
#  ==============================================

import os

org_train_dirname = 'train/'
train_filenames = os.listdir(org_train_dirname)
train_cat_fnamelist = filter(lambda x:x[:3] == 'cat', train_filenames)
train_dog_fnamelist = filter(lambda x:x[:3] == 'dog', train_filenames)

train_cat_dirname = 'train_cat/'
train_dog_dirname = 'train_dog/'
if not os.path.exists(train_cat_dirname): os.mkdir(train_cat_dirname)
if not os.path.exists(train_dog_dirname): os.mkdir(train_dog_dirname)

for filename in train_cat_fnamelist:
    os.symlink('../'+org_train_dirname+filename, train_cat_dirname+filename)

for filename in train_dog_fnamelist:
    os.symlink('../'+org_train_dirname+filename, train_dog_dirname+filename)
