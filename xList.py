# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:46:08 2015

@author: mcollins
"""

class extendingList(list):
    """list that automatically extends
    (filling in with None)
    when we assign to  index out of bounds"""
    def __setitem__(self, i, val):
        if isinstance(i, slice):
            super().__setitem__(i, val)
            return
        if i < len(self):
            super().__setitem__(i, val)
        else:
            for j in range(len(self), i+1):
                self.append(None)
            self[i] = val