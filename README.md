# Sample envoy configs

Sample configs for [Envoy Fundamentals course](https://academy.tetrate.io/courses/envoy-fundamentals)

- Get [func-e](https://func-e.io/)
- Try running a sample config
```bash
func-e run -c static_resource.yaml --log-level info
```
- Hit it!
```bash
curl localhost:10000 -vvv
```
should response
```
*   Trying 127.0.0.1:10000...
* Connected to localhost (127.0.0.1) port 10000 (#0)
> GET / HTTP/1.1
> Host: localhost:10000
> User-Agent: curl/7.74.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
< HTTP/1.1 200 OK
< content-length: 3
< content-type: text/plain
< date: Sun, 27 Mar 2022 08:40:45 GMT
< server: envoy
< 
* Connection #0 to host localhost left intact
yay%
```
