WITH REDIS

```
(.venv) gogacpp@PRINJ-lab5$ wrk -t 1 'http://localhost:8001/user/4f175a78-2879-4a11-8603-9f64071356f7' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ZjE3NWE3OC0yODc5LTRhMTEtODYwMy05ZjY0MDcxMzU2ZjciLCJleHAiOjE3NDY1OTE5OTB9.zgV2i1TCmaR7NHMHzRPew09lIDGZj6gXj9J2EfsAKZI'
Running 10s test @ http://localhost:8001/user/4f175a78-2879-4a11-8603-9f64071356f7
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    36.81ms   10.01ms 128.39ms   92.29%
    Req/Sec   274.43     53.46   363.00     80.00%
  2740 requests in 10.03s, 866.95KB read
Requests/sec:    273.18
Transfer/sec:     86.44KB
(.venv) gogacpp@PRINJ-lab5$ wrk -t 5 'http://localhost:8001/user/4f175a78-2879-4a11-8603-9f64071356f7' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ZjE3NWE3OC0yODc5LTRhMTEtODYwMy05ZjY0MDcxMzU2ZjciLCJleHAiOjE3NDY1OTE5OTB9.zgV2i1TCmaR7NHMHzRPew09lIDGZj6gXj9J2EfsAKZI'
Running 10s test @ http://localhost:8001/user/4f175a78-2879-4a11-8603-9f64071356f7
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    35.27ms    7.08ms  96.74ms   88.89%
    Req/Sec    56.85     10.13    80.00     77.40%
  2844 requests in 10.03s, 0.88MB read
Requests/sec:    283.54
Transfer/sec:     89.71KB
(.venv) gogacpp@PRINJ-lab5$ wrk -t 10 'http://localhost:8001/user/4f175a78-2879-4a11-8603-9f64071356f7' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ZjE3NWE3OC0yODc5LTRhMTEtODYwMy05ZjY0MDcxMzU2ZjciLCJleHAiOjE3NDY1OTE5OTB9.zgV2i1TCmaR7NHMHzRPew09lIDGZj6gXj9J2EfsAKZI'
Running 10s test @ http://localhost:8001/user/4f175a78-2879-4a11-8603-9f64071356f7
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    38.76ms   11.59ms 122.35ms   89.58%
    Req/Sec    27.51     15.37   200.00     93.95%
  2638 requests in 8.55s, 834.80KB read
  Socket errors: connect 0, read 0, write 0, timeout 20
Requests/sec:    308.63
Transfer/sec:     97.67KB

```

WITHOUT REDIS

```
(.venv) gogacpp@PRINJ-lab5$ wrk -t 1 'http://localhost:8001/user/e5665f03-b82f-4986-8e10-db4386266791' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ZjE3NWE3OC0yODc5LTRhMTEtODYwMy05ZjY0MDcxMzU2ZjciLCJleHAiOjE3NDY1OTE5OTB9.zgV2i1TCmaR7NHMHzRPew09lIDGZj6gXj9J2EfsAKZI'
Running 10s test @ http://localhost:8001/user/e5665f03-b82f-4986-8e10-db4386266791
  1 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    96.30ms   90.82ms 593.80ms   88.28%
    Req/Sec   145.65     62.95   250.00     76.74%
  1286 requests in 10.05s, 467.18KB read
Requests/sec:    127.95
Transfer/sec:     46.48KB
(.venv) gogacpp@PRINJ-lab5$ wrk -t 5 'http://localhost:8001/user/e5665f03-b82f-4986-8e10-db4386266791' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ZjE3NWE3OC0yODc5LTRhMTEtODYwMy05ZjY0MDcxMzU2ZjciLCJleHAiOjE3NDY1OTE5OTB9.zgV2i1TCmaR7NHMHzRPew09lIDGZj6gXj9J2EfsAKZI'
Running 10s test @ http://localhost:8001/user/e5665f03-b82f-4986-8e10-db4386266791
  5 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    87.08ms   64.41ms 415.61ms   88.80%
    Req/Sec    28.15     10.67    40.00     55.78%
  1305 requests in 10.05s, 474.08KB read
Requests/sec:    129.84
Transfer/sec:     47.17KB
(.venv) gogacpp@PRINJ-lab5$ wrk -t 10 'http://localhost:8001/user/e5665f03-b82f-4986-8e10-db4386266791' \
  -H 'accept: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI0ZjE3NWE3OC0yODc5LTRhMTEtODYwMy05ZjY0MDcxMzU2ZjciLCJleHAiOjE3NDY1OTE5OTB9.zgV2i1TCmaR7NHMHzRPew09lIDGZj6gXj9J2EfsAKZI'
Running 10s test @ http://localhost:8001/user/e5665f03-b82f-4986-8e10-db4386266791
  10 threads and 10 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    72.45ms   49.49ms 367.40ms   90.46%
    Req/Sec    16.29      5.78    30.00     66.78%
  1519 requests in 8.52s, 551.82KB read
  Socket errors: connect 0, read 0, write 0, timeout 15
Requests/sec:    178.21
Transfer/sec:     64.74KB

```