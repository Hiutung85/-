import nest
import numpy as np
import matplotlib.pyplot as plt

nest.ResetKernel()

# Set simulation kernel
nest.SetKernelStatus({
  "local_num_threads": 1,
  "resolution": 0.1,
  "rng_seed": 1
})

# Create nodes
n1 = nest.Create("iaf_psc_alpha", 100)
n2 = nest.Create("iaf_psc_alpha", 100)
pg1 = nest.Create("poisson_generator", 1, params={
  "rate": 75000,
})
pg2 = nest.Create("poisson_generator", 1, params={
  "rate": 70000,
  "start": 0,
})
sr1 = nest.Create("spike_recorder", 1)
sr2 = nest.Create("spike_recorder", 1)

# Connect nodes
nest.Connect(n1, n2, conn_spec={
  "rule": "pairwise_bernoulli",
  "p": 0.1,
}, syn_spec={ 
  "weight": -1,
})
nest.Connect(pg1, n1)
nest.Connect(pg2, n2)
nest.Connect(n2, sr1)
nest.Connect(n1, sr2)

# Run simulation
nest.Simulate(1000)

response = {
  "events": [sr1.events, sr2.events, ]
}

