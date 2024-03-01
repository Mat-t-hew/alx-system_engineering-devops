0x10. HTTPS SSL Summary:
What is HTTPS?

HTTPS is an extension of HTTP, the protocol used for transmitting data over the internet. It adds a layer of encryption using SSL/TLS protocols to ensure secure communication between a client (such as a web browser) and a server.
What are the 2 main elements that SSL is providing?

SSL provides two main elements:
Encryption: SSL encrypts data transmitted between the client and the server, making it unreadable to anyone intercepting the communication.
Authentication: SSL certificates validate the identity of the server, ensuring that the client is connecting to the intended server and not a malicious entity.
HAProxy SSL termination on Ubuntu 16.04

HAProxy is a popular open-source load balancer and proxy server. SSL termination refers to the process of decrypting SSL-encrypted traffic at the load balancer and forwarding it as plain HTTP to the backend servers.
HAProxy can be configured for SSL termination on Ubuntu 16.04, allowing it to handle SSL encryption and decryption efficiently, offloading this task from backend servers.
Bash function

In Bash scripting, functions provide a way to organize and reuse code blocks. They encapsulate a set of commands, making the script more modular and easier to maintain.
The use of a Bash function in the provided context likely refers to encapsulating the logic for querying DNS information into a reusable function for better code organization.
Purpose of encrypting traffic

The primary purpose of encrypting traffic, achieved through SSL/TLS encryption, is to ensure data confidentiality and integrity. Encryption prevents unauthorized parties from intercepting and reading sensitive information transmitted over the network.
SSL termination

SSL termination is the process of decrypting SSL-encrypted traffic at a network endpoint, such as a load balancer or proxy server, before forwarding it to the intended destination.
SSL termination allows the intermediary server to inspect, manipulate, or route the decrypted traffic based on application layer information, such as HTTP headers, while offloading the decryption overhead from backend servers.
Understanding HTTPS, SSL, and SSL termination is essential for securing web communications, ensuring data privacy, and optimizing network performance in modern web infrastructure setups.
