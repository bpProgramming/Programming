#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author  : Bhishan Poudel
# Date    : Apr 09, 2016
# Ref     : http://ggplot.yhathq.com/

# Imports
from ggplot import *

plot1 = ggplot(aes(x='date', y='beef'), data=meat) +\
    geom_line() +\
    stat_smooth(colour='blue', span=0.2)

#print(plot1)

plot2 = ggplot(diamonds, aes(x='carat', y='price', color='cut')) +\
    geom_point() +\
    scale_color_brewer(type='diverging', palette=4) +\
    xlab("Carats") + ylab("Price") + ggtitle("Diamonds")

#print(plot2)

plot3 = ggplot(diamonds, aes(x='price', fill='cut')) +\
    geom_density(alpha=0.25) +\
    facet_wrap("clarity")

print(plot3)
