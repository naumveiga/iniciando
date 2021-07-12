#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 11:19:44 2021

@author: cveiga
"""

import time
import asyncio
from spade.agent import Agent
from spade.behaviour import CyclicBehaviour

class DummyAgent(Agent):
    class MyBehav(CyclicBehaviour):
        async def on_start(self):
            print("Starting behaviour . . .")
            self.counter = 0

        async def run(self):
            print("Counter: {}".format(self.counter))
            self.counter += 1
            await asyncio.sleep(1)

    async def setup(self):
        print("Agent starting . . .")
        b = self.MyBehav()
        self.add_behaviour(b)

if __name__ == "__main__":
    dummy = DummyAgent("naum@naumveiga.com.br", "1234")
    future = dummy.start()
    future.result()
    dummy2 = DummyAgent("nadois@naumveiga.com.br", "1234")
    future2 = dummy2.start()
    future2.result()
    dummy.web.start(hostname="naumveiga.com.br",port=10000)

    print("Wait until user interrupts with ctrl+C")
    try:
        while True:
            time.sleep(3)
            print("Passou aqui!")
    except KeyboardInterrupt:
        print("Stopping...")
    dummy.stop()
    dummy2.stop()