import numpy as np
reference = 'hello how are you i am good here'
output = 'hello baby are you i am fine here'

# calculate Brevity penalty
BP = 0
if len(reference) < len(output):
    BP = 1
else:
    BP = np.exp(1-(len(reference)/len(output)))

def Bleu(ref, pred):
    count = []
    clip_count = []

    for i in range(1, len(pred)):
        clp = 0
        cp = 0
        start = set()
        for j in range(len(pred)):
            if j+i >len(pred):
                continue

            goal = pred[j:i+j]

            sum = ''
            for k in goal:
                sum += k+' '

            final = sum[:-1]

            cp += 1
            if final in ref:
                if final in start:
                    continue
                else:
                    clp += 1
                    start.add(final)


        clip_count.append(clp)
        count.append(cp)

    return clip_count, count

clip, count = Bleu(reference, output.split())

N = 4
clip = clip[:4]
count = count[:4]

vec_pn = np.divide(clip, count)

pn = 0
for i in range(N):
    pn += np.log(clip[i]/count[i])

bleu = np.exp(pn * (1/N)) * BP

print(bleu)

