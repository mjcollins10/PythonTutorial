# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:25:34 2015

@author: mcollins
"""

import threading

class PrimeNumber(threading.Thread):
    """threaded search for prime numbers"""
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self):
        """thread class must redefine threading.Thread.run"""
        counter = 2
        res = True
        while (counter*counter < self.Number) and res: 
            if self.Number % counter == 0: 
               res = False 
            counter += 1 
        PrimeNumber.lock.acquire() 
        print('Determined {0}'.format(self.Number))
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 
        
threads = [] 
for n in range(33,3,-1): 
    N = 3**n + 2
    thread = PrimeNumber(N) 
    threads += [thread] 
    thread.start() 
 
#for x in threads: 
    #don't kill threads when parent exits
    #x.join()
