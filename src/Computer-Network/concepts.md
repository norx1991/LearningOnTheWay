**Short polling** is an AJAX-based timer that calls at fixed delays

**Long polling** is a technique where the server elects to hold a client’s connection open for as long as possible, delivering a response only after data becomes available or a timeout threshold has been reached. It is based on Comet.

[**WebSocket**](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) is a persistent connection between the client and the server. This is a communications protocol providing full-duplex communication channels over a single TCP connection.

[**Server Sent Event**](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events) is a mechanism that allows the server to asynchronously push the data to the client once the client-server connection is established. The server can then decide to send data whenever a new “chunk” of data is available. It can be considered as a one-way publish-subscribe model.