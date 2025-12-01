### How do I change the volume via a terminal command?
### *using pipewire of course.*
> # wpctl is required... BECAUSE IT JUST IS, OKAY?
<img src="../assets/feraljak.png" width=128></img>
*Funny bald man with glasses*
---

### Raise the volume by five percent
```sh 
wpctl set-volume @DEFAULT_SINK@ 5%+
```
---
### Lower the volume by five percent
```sh 
wpctl set-volume @DEFAULT_SINK@ 5%-
```
---