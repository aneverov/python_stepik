
genome = input()
c = genome.upper().count('c'.upper())
g = genome.upper().count('g'.upper())
cnt = len(genome)
percent = ((c + g)/cnt) * 100
print(percent)
