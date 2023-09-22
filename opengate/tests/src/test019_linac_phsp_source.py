#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import opengate as gate
import test019_linac_phsp_helpers as test019

if __name__ == "__main__":
    # create sim
    sim = gate.Simulation()
    test019.create_simu_test019_phsp_source(sim)

    # start simulation
    sim.run()

    # print results
    stats = sim.output.get_actor("Stats")
    print(stats)

    # analyse
    is_ok = test019.analyse_test019_phsp_source(sim)

    utility.test_ok(is_ok)
