#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:08:35 2021

@author: cveiga
"""
import time
from spade import agent, quit_spade

class DummyAgent(agent.Agent):
    async def setup(self):
        print("Hello World! I'm agent {}".format(str(self.jid)))

dummy = DummyAgent("naum@naumveiga.com.br", "1234")
future = dummy.start()
future.result()
dummy.web.start(hostname="127.0.0.1", port="10000")
time.sleep(300)
dummy.stop()
quit_spade()