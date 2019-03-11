# kubectl shortcuts

A few shortcuts for kubectl based on our environment.

To use place these in `~/bin` or add to your path.

### pod
will give a list of pods to select based on your context.

`pod` will bring up the bash for the pod that you select.

`pod logs` will bring up the logs for the pod that you select.

`pod laravel-logs` will bring up the laravel logs for the pod that you select.

`pod describe` will describe the pod that you select.

`pod k` will ask to change context before selecting pods.

### kontext
will give a list of context to select and set the context base on your choice.


### kg

`kg` shortcut for `kubectl get pods`.

`kg a` shortcut for `kubectl get pods --all-namespaces`.

`kg k` will ask to change context, then shortcut for `kubectl get pods`.
