# What happens when you type Google.com in your browser and press enter?

**Esteban Delahoz**

Every day in our lives we do searches and requests from the Chrome browser, but we never see what happens internally with everything, in addition to the fact that completely hidden tasks are happening in the background for the client, but in this article I will explain what are the things that are happening and I will introduce some concepts about DNS, TCP / IP, Firewall, HTTPS / SSL, load balancing, web servers, application server and databases, I hope and you like it, and let’s get started!.

## The OSI model.

The transformation of the information from client to server you wonder now what is the model or if right? well, it is simply the process of how data travels on the network between computers and entering a little more about the model or if it is basically a standard of connection between computers. This model is based on seven layers, where you can see the transformation of data to bits in cyberspace.

This model shows seven layers, but the main implementation of this model is called TCP / IP and is based on only 4 layers: Application, Transport, Network and Network Interface Layer, the initial three layers of this realization model are compacted in the application layer. in the upper image some protocols and the corresponding layer can be shown.

Ok, this previous introduction to be able to understand the following things, first of all analyze the structure of a URL (Uniform Location of Resources, which in summary is the one that allows access to a location to obtain a request through that location.

Ok let’s start to see what they are these 4 layers..

### TCP/IP

Ok An analogy for over tcp / ip would be this. Imagine you go to your friends house, your friend invites you to come and gives you the address of his house and now that you know that address, now you need to find a way to get there, if you are going to drive, you take the faster route and efficient while following all traffic laws to get there safely. Just as you need to know the way you are going to get to your friends’ house and follow the protocols for going and coming back, the Internet needs a system to get a page from a server and this system is known as TCP (Internet Control Protocol). transmission) / IP (Internet Protocol). This TCP / IP system using the Internet works in layers, the first layer is the application layer and the application layer contains protocols such as FTP if you are transferring files to a server or HTTP (Hypertext Transfer Protocol) if you are visiting websites . Since www.google.com is a website, our application layer uses HTTP, each different protocol connects to our next layer using one port, and since we are using HTTP, the port that is used to connect to that next layer it is port 80. Then the data is sent through port 80 to the next layer, which is TCP or Transport Layer. The TCP layer cuts all of our data into packets and these packets will individually take the fastest routes to the next layer. With each of these packets, a header is included, and this header will contain instructions on how to reassemble these packets at their next layer. The next layer is the Internet layer, this layer takes the assembled packet and attaches both where the packet came from and where it is going to arrive. This packet is then sent to the final layer in the TCP / IP system which is the network layer, the network layer will just take the packet and make sure it goes to the right machine.

### DNS request

Well When you type google.com plus ‘enter’ in your preferred browser, the following happens: the browser sends a DNS request to google.com the DNS is the initials of Domain Name System that basically allows you to resolve a name or word in the networks, that is, it allows knowing the IP address of the machine where the domain we want to access is hosted. Since the domain name points to your IP address, the Firewall (it can be a physical computer, for example, your router or it can be software installed on your PC) it checks if your browser has authorization to send / receive data from / to port 443 or any other where you allow it when configuring the firewall. Following this, the data with the https protocol, which is the one that maintains the secure connection since it maintains an ssl certificate on the server where the page is hosted, this contains keys where the https connection process is certified, following some configurations for the port 443 and if it is ok, the DNS request is sent to a DNS server in this case to the www DNS server that is named as a subdomain, this registers its A records where google.com is and translates it into an IP address as aaa.bbb.ccc.ddd where a, b, c are numbers between 0 and 255. The WWW DNS server sent the router the IP address where the google.com data can be found, now the router sends the DNS request for the IP address. The load balancer (a physical machine in the google.com infrastructure) and the browser (on your pc) initiate a communication to verify the SSL certificate (this is for a secure / encrypted communication, this communication is over TCP / IP in transport layer and https in the application layer) if the SSL negotiation ends with the agreement, the server (a physical machine when google.com is stored) uses the application server and the database to respond to the DNS request through encrypted communication.

Now that we know what happens when you type, let’s go deeper into some concepts…

### Firewall
A firewall is an added layer of security to an application. You can think of a firewall as a big gate around your house with multiple doors that can identify who is trying to come in and permit or deny them entry. These doors are referred to as ports and these ports have rules and numbers assigned to them specifying who is allowed into your application. This prevents any person with malicious intent from entering an application.

Source: [ResearchGate](https://www.researchgate.net/figure/Simplified-diagram-of-a-traditional-network-data-ingress-egress-is-restricted-and_fig3_306070104)

### HTTPS/SSL
If you look at the URL https://www.google.com you can see that before the domain name there is a protocol to connect to it that is the https:// part. When you search for a website you probably noticed that either http:// or https:// is attached to the beginning of what you’re trying to search. Although these look similar, they both define two different methods of sending and retrieving data from a server. HTTP sends and receives data in plain text, which is not secure because if a hacker gets into a network, they can now see any vital information such as credit card information exactly how it appears on your credit card. HTTPS (HyperText Transfer Protocol Secured) is HTTP with security, it makes sure that any sensitive data being sent is encrypted on it’s way there by using algorithms to encrypt it, that way if a hacker is watching, they have no way of seeing your personal information in a readable format. HTTPS will now protect data by using the SSL (Secure Sockets Layer) protocol. With the SSL protocol, the computers web browser will ask the web site to identify itself, to authenticate, the web site will then send back a copy of its SSL Certificate which is a digital certificate that verifies the identity a website. Once the web browser verifies the SSL Certificate, it will let the server know that everything looks good, and the