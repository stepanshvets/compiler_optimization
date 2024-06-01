import subprocess
import time

res = []

flags = ['-funroll-loops', '-funsafe-math-optimizations', '-fvectorize', '-freciprocal-math', '-fmerge-all-constants', '-funroll-loops -funsafe-math-optimizations', '-funsafe-math-optimizations -freciprocal-math -ffinite-math-only', '-fmerge-all-constants -fstrict-aliasing']
for i, opt in enumerate(flags):
    res.append([])

    subprocess.run(['ls | grep -e ".c$" | xargs clang -O3 ' + opt + ' -o out.o -lm'], shell=True)
    for j in range(10):
        start = time.time()
        subprocess.run(['./out.o 10 ./output.txt 0 0'], shell=True)
        end = time.time()
        res[i].append(round(end * 1000) - round(start * 1000))

for i in res:
    print(*i)
