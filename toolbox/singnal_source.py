#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 xuekun.zhuang <zhuangxuekun@limei.com>
# Licensed under the Limei tech.co.ltd - http://www.limei.com

import numpy as np
import pandas as pd


def x_sin(x):
    return x * np.sin(x)


def sin_cos(x):
    return pd.DataFrame(dict(a=np.sin(x), b=np.cos(x)), index=x)
