### Como ajusto o voulme via terminal?
### *usando o pipewire, é claro.*
> # wpctl é obrigatório... POR QUE SIM, OKAY?
<img src="../assets/feraljak.png" width=128></img>
---

### Aumentar o volume em 5%
```sh 
wpctl set-volume @DEFAULT_SINK@ 5%+
```
---
### Diminuir o volume em 5%
```sh 
wpctl set-volume @DEFAULT_SINK@ 5%-
```
---