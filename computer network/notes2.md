WEB AND HTTP

udp - user dataterm protocol (elastic because it is adaptable and expandable)
http - hypertext transfer protocol and it is used in application layer.
hhtp is a public one

web page consists of 'objects' each of which can be stored on different web servers

it contains html files and jpeg images java applet etc

url - uniform resource locator.
web page consists of base html file which includes several referenced objects each addresable by a url.

www.someschool.edu/someDept/pic.gif

here www.someschool.edu is host name and the remaining is path name

it is client server model
client is the brower, browser will requests and recieve using http protocol and 'display' web objects
server: web server sends objects in response to requests

webpage: consists of objects, an object is a file that is addresable by a single url
structure of a web page:
a page with html text + 5 jpeg images = 6 objects
the base html file references other objects using their url.
url structure: each url has two components
 host name and path name

web brower implement the client side of the http

web server implement the server side of htttp
how http works(client server interaction)
 user requests a web page
 browser ends http request messages for the objects in the page to the server.
 since it is public it will publish tcp connection with the server (not udp)

message flow:
server recieves request messages from its socket and then sends response messages into its socket.
once a message is sent into the socket its in the hands of tcp
tcp provides reliable data transfer

http is 'stateless' protocol - it resends the object completely fresh as if for the first time (so incase crash happens or lock, no admin has to be bothered and we can get info fresh)

if client requests the same object twice within a few seconds: the server does not remember it already served that object

protocol that maintain 'state' are complex- past history must be maintained. if server client crashed their view of state must be inconsistent

2 types of htttp connection
1.non persistent http 
    suppose a webpage has1  html file and 3 image. the client may need 4 seperate tcp connection to download.
    tcp connection opened
    at most one object sent over tcp connection
    tcp connection closed
2.persistent http
    for the same webpage with 1 html and 3 image, the object can be transfered using one tcp connection.
    tcp connection opened to a server
    multiple objects can be sent over single tcp
    conenection between client and that server
    tcp connection closed

rtt (round trip delay) : time for a small packet to travel from client to server and back

http response time (per object)
one rtt to initiate tcp connection
one rtt for http request and first few bytes of htttp response to return

non persistent http response time = 2rtt + file transmission time

persistent http
non persistent http issues get covered, the issues are:
requires 2 rtt per object
os overhead for each tcp connection
browders often open multiple parallel tcp connections to fetch referenced onbjects in parallel

persistent http:
server leaves connection open after sending response
subsequent http messages between same client sent over open connection
client sends requests as soon as it ecnounters a refereneced object

http request messahe: 2 types of http messages are request and response
http request messahe: ascii(human readable format)

GET /index,html HTTP/1.1\r\n (here r is carriage return (return wil return back to the first line) character and n is line feed character)

request line - 3 fields
1.method field (GET,POST,HEAD,PUT,DELETE)
2.url field (object beign requested)
3.http version field (eg http/1.1)

first line = request line
remaining lines = header lines
followed by a blank line than an entity body (empty for GET, used for POST)

GET - most common requests an object, no entity body
    forms can also use GET.appending input data to the URL

POST - used when submitting form data; entity body contains form field values
HEAD - like GET, but server responds without the actual object used for debugging

PUT - uploads an object to a specified path o na server


