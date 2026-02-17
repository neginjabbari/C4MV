import os
import torch
from sklearn.neighbors import kneighbors_graph

if torch.cuda.is_available():
    torch.backends.cudnn.enabled = True
    torch.backends.cudnn.benchmark = True
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'
    print("num GPUs", torch.cuda.device_count())
    dtype = torch.cuda.FloatTensor
    ltype = torch.cuda.LongTensor
else:
    dtype = torch.FloatTensor
    ltype = torch.LongTensor
    print("CPU")

eps = torch.tensor(10 ** -10)

data = torch.load('Coil100.npy', weights_only=False)
V = len(data)-1
X0 = data[:-1]
X = []
for x in X0:
    X.append(torch.tensor(x).type(dtype))


lam1 = 1
lam2 = 1000
lam3 = 0.001
alpha = 0.5

XXT = []
for v in range(V):
    d, n = X[v].shape                    

    A0 = kneighbors_graph(X[v].T.cpu(), 30, mode='connectivity', include_self=True, metric='euclidean').toarray()
    A0 = torch.tensor(A0).type(dtype)
    A0 = torch.maximum(A0, A0.T)

    if v==0:
        C = A0
    else:
        C = torch.minimum(C, A0)
    
    XXT.append(X[v] @ X[v].T)
           
    if v==0:
        dis = torch.cdist(X[v].T, X[v].T, p=2).type(dtype)
    else:
        dis = torch.minimum(dis, torch.cdist(X[v].T, X[v].T, p=2).type(dtype))

dis = dis/torch.sum(dis, dim=1)

A0 = []
D = torch.sum(C, dim = 1)    
nC = torch.zeros(n, n).type(dtype)
nC[C == 0] = dis[C == 0]                               

W = []
H = []
r = 50
for v in range(V):
    d, n = X[v].shape
    W.append(torch.rand(d, r).type(dtype))
    H.append(torch.rand(r, n).type(dtype))

Hs = torch.rand(r, n).type(dtype)

# Optimization
for t in range(400):

    # Updating Wv
    for v in range(V):
        Wn = 2 * (X[v]        @ H[v].T) + X[v]      @ Hs.T
        Wd = W[v] @ H[v] @ H[v].T       + W[v] @ Hs @ Hs.T + XXT[v] @ W[v] 
        W[v] = W[v] * (Wn / torch.maximum(Wd, eps))
        
    # Updating Hv
    for v in range(V):

        Hsum = torch.sum(torch.stack(H), dim=0)
        Hn = 2 * (W[v].T @ X[v])                           + lam2 * (Hsum @ C)
        Hd = W[v].T @ W[v] @ H[v] + H[v] + lam1/(2*V) * Hs + lam2 * (Hsum * D) + lam3 * (Hsum @ nC)
        H[v] = H[v] * (Hn / torch.maximum(Hd, eps))

    # Updating H*
    Hn = torch.zeros(r, n).type(dtype)
    Hd = torch.zeros(r, n).type(dtype)
    for v in range(V):
        Hn += 2 * (W[v].T @ X[v])
        Hd += W[v].T @ W[v] @ Hs + Hs + (lam1/2) * H[v]/V
    Hs = Hs * (Hn / torch.maximum(Hd, eps))

Hsum = torch.sum(torch.stack(H), dim=0)

# Final representation by Hybrid fusion
Hfinal = torch.cat((alpha * Hs, (1 - alpha) * (Hsum/V)), 0)

print("Done!")