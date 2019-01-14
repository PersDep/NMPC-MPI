#!/usr/bin/python

import matplotlib.pyplot as plotter

import os

params = open("mc_walks_stats/stat_10000000_1.txt", "r").readlines()[0]
particles = []
proc_amount = []
time = []
acceleration = []
efficiency = []
i = 1
while i < 200:
    # time.append(float(open("mc_walks_stats/stat_" + str(10000000) + "_" + str(i) + ".txt", "r").readlines()[1].split(' ')[0]))
    time.append(float(open("mc_walks_stats/stat_" + str(1000 * (i ** 3)) + "_" + str(i) + ".txt", "r").readlines()[1].split(' ')[0]))
    particles.append(open("mc_walks_stats/stat_" + str(1000 * (i ** 3)) + "_" + str(i) + ".txt", "r").readlines()[0].split(' ')[4])
    proc_amount.append(i)
    i *= 2
# for filename in os.listdir(os.fsencode('mc_walks_stats')):
#     fileNameParts = str(filename).split('.')[0].split('_')
#     if len(fileNameParts) >= 3 and int(fileNameParts[2]) == 1 and int(fileNameParts[1]) != 1000:
#         particles.append(open(os.fsdecode(os.path.join(os.fsencode('mc_walks_stats'), filename))).readlines()[0].split(' ')[4])
#         time.append(open(os.fsdecode(os.path.join(os.fsencode('mc_walks_stats'), filename))).readlines()[1].split(' ')[0])

for i in time:
    acceleration.append(time[0] / i)
for i, a in enumerate(acceleration):
    efficiency.append(a / proc_amount[i])

# plotter.xlabel('Threads amount')
# # plotter.xlabel('Particles amount')
# plotter.ylabel('Time, sec')
# plotter.xscale('log')
# plotter.grid(True)
# # plotter.plot(particles, time, 'c', linewidth = '2')
# # plotter.plot(particles, time, 'bx', markersize='5')
# plotter.plot(proc_amount, time, 'c', linewidth = '2')
# # plotter.plot(proc_amount, time, 'bx', label="params: " + params, markersize='5')
# plotter.plot(proc_amount, time, 'bx', markersize='5')
# # for i, threads in enumerate(proc_amount):
# #     plotter.text(threads, time[i], particles[i])
# plotter.xticks(proc_amount, proc_amount)
# # plotter.xticks(particles, particles)
#
# # time.remove(time[4])
# # time.remove(time[6])
#
# # time.remove(time[1])
# # time.remove(time[1])
# # time.remove(time[1])
# # time.remove(time[0])
#
# plotter.yticks(time, time)
# plotter.legend()

plotter.xlabel('Threads amount')
# plotter.xlabel('Particles amount')
plotter.ylabel('Acceleration')
plotter.xscale('log')
plotter.grid(True)
# plotter.plot(particles, time, 'c', linewidth = '2')
# plotter.plot(particles, time, 'bx', markersize='5')
plotter.plot(proc_amount, acceleration, 'c', linewidth = '2')
# plotter.plot(proc_amount, acceleration, 'bx', label="params: " + params, markersize='5')
plotter.plot(proc_amount, acceleration, 'bx', markersize='5')
for i, threads in enumerate(proc_amount):
    plotter.text(threads, acceleration[i], particles[i])
plotter.xticks(proc_amount, proc_amount)
# plotter.xticks(particles, particles)
# acceleration.remove(acceleration[3])
# acceleration.remove(acceleration[1])
# acceleration.remove(acceleration[4])
# acceleration.remove(acceleration[4])
# acceleration.remove(acceleration[4])
# acceleration.remove(acceleration[4])
plotter.yticks(acceleration, acceleration)
plotter.legend()

# plotter.xlabel('Threads amount')
# # plotter.xlabel('Particles amount')
# plotter.ylabel('Efficiency')
# plotter.xscale('log')
# plotter.grid(True)
# # plotter.plot(particles, time, 'c', linewidth = '2')
# # plotter.plot(particles, time, 'bx', markersize='5')
# plotter.plot(proc_amount, efficiency, 'c', linewidth = '2')
# plotter.plot(proc_amount, efficiency, 'bx', label="params: " + params, markersize='5')
# # plotter.plot(proc_amount, time, 'bx', markersize='5')
# # for i, threads in enumerate(proc_amount):
# #     plotter.text(threads, time[i], particles[i])
# plotter.xticks(proc_amount, proc_amount)
# efficiency.remove(efficiency[0])
# efficiency.remove(efficiency[1])
# efficiency.remove(efficiency[3])
# plotter.yticks(efficiency, efficiency)
# plotter.legend()

plotter.show()