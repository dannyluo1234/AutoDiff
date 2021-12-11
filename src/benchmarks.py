from cs107_creativename import *
import time

### Functions with distinct Variables
f1 = lambda x: 8 * x
f3_single = lambda x1, x2, x3: 8 * x1 + x2 / 5 + sin(x3)
f3_connected = lambda x1, x2, x3: x1 ** (x2 * sin(x3 + x2))
f5_single = lambda x1, x2, x3, x4, x5: 8 * x1 + x2 / 5 + sin(x3) + cos(x4) + exp(x5)
f5_connected = lambda x1, x2, x3, x4, x5: x1 ** (x2 * (x3 - x4) / sin(x5))
f10_single = lambda x1, x2, x3, x4, x5, x6, x7, x8, x9, x10: 8 * x1 + x2 / 5 + sin(x3) + cos(x4) + exp(x5) + logistic(x6) + arcsin(x7) + x8 ** 9 + sinh(x9) + log(x10, 3)
f10_connected = lambda x1, x2, x3, x4, x5, x6, x7, x8, x9, x10: (sin(x1) + cos(x2)) ** (logistic(x3 - x4 * x5) / exp(x6 - x7)) / (x8 ** x9 + sinh(x10))


### Functions with repeated segments
repeat1 = lambda x1, x2, x3: (x1 ** x2) / x3
repeat3 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3)
repeat5 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2)
repeat10 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)
repeat20 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2))
repeat40 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)))
repeat80 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2))) + sin((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2))))
repeat160 = lambda x1, x2, x3: (x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2))) + sin((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)))) / ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2))) + sin((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)) * logistic((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2) / sin ((x1 ** x2) / x3 * sin(x1 ** x2) / logistic(x1 ** x2 - x3) - exp(x1 ** x2) ** (x1 ** x2) * sqrt(x1 ** x2) + (x1 ** x2) ** (4 * x3) / ((x1 ** x2) / log(x1 ** x2, 10)) * (x1 ** x2)))))


benchmarks = [f1, f3_single, f3_connected, f5_single, f5_connected, f10_single,
              f10_connected, repeat1, repeat3, repeat5, repeat10, repeat20,
              repeat40, repeat80, repeat160]
names = ["distinct_1", "distinct_3", "distinct_3_connected", "distinct_5",
"distinct_5_connected", "distinct_10", "distinct_10_connected", "repeat_1",
"repeat_3", "repeat_5", "repeat_10", "repeat_20", "repeat_40", "repeat_80",
"repeat_160"]

values = [[0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5],
[0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5],
[0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5], [0.5, 0.5, 0.5],
[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5],
[0.5, 0.5, 0.5], [0.5, 0.5, 0.5], [0.5, 0.5, 0.5]]

distinct_forward = []
repeat_forward = []
distinct_reverse = []
repeat_reverse = []
f = AutoDiffF(lambda x: x + 1, [8])

for i, b in enumerate(benchmarks):
    start = time.time()
    f = AutoDiffF(b, values[i])
    elapsed = time.time() - start
    if "distinct" in names[i]:
        distinct_forward.append(elapsed)
    else:
        repeat_forward.append(elapsed)

    start = time.time()
    f = AutoDiffR(b, values[i])
    elapsed = time.time() - start
    if "distinct" in names[i]:
        distinct_reverse.append(elapsed)
    else:
        repeat_reverse.append(elapsed)

import matplotlib.pylab as plt
from matplotlib import use
use('tkagg') # allow plot to show if launched from command line
distinct_x = ["1-var", "3-var, isolated", "3-var, connected", "5-var, isolated",
"5-var, connected", "10-var, isolated", "10-var, connected"]
repeat_x = [1, 3, 5, 10, 20, 40, 80, 160]

fig, ax = plt.subplots(1,2)
ax[0].plot(distinct_x, distinct_forward, "+-", label="Forward Mode")
ax[0].plot(distinct_x, distinct_reverse, "+-", label="Reverse Mode")
ax[0].set_xlabel("Function type")
ax[0].set_xticklabels(distinct_x, rotation = 20);
ax[0].set_ylabel("Elapse time (s)")
ax[0].set_title("Execution time for functions with distinct variables")
ax[0].legend()

ax[1].plot(repeat_x, repeat_forward, "+-", label="Forward Mode")
ax[1].plot(repeat_x, repeat_reverse, "+-", label="Reverse Mode")
ax[1].set_xlabel("Number of short repeats")
ax[1].set_ylabel("Elapse time (s)")
ax[1].set_title("Execution time for functions with short repeat segments")
ax[1].legend()
plt.show()
