# CPS-Architecture
###### About
This code contains a simple Client-Proxy Server-Server architecture. The file `abc.txt` is always stored in the server's directory. The client always makes a request for the file from the proxy (the required file `abc.txt` may or may not be cached with the proxy). In case the file is present in the proxy's directory, it is immediately transmitted to the client, but if it is not present, it makes a secondary connection to the server and downloads the file from there and then transmits it to the client while caching it for future requests.

###### How to run
Run the `client.py`, `proxy_server.py` and `server.py` in three separate terminals.

**Note:** This architecture can handle files of size atmost 10KB with filename being under 10B. Further, the proxy and server are available at fixed ports 44671 and 44672 respectively. This values are hardcoded, but can be changed upon the interest of the user.
