# No Waste

### Create dev cluster
```
k3d cluster create dev --api-port 6550 -p "8081:80@loadbalancer"
```

### Deploy/run dev cluster
```
skaffold dev
```
App will be available at `http://localhost:8081/`

### Destroy dev cluster
```
k3d cluster delete dev
```