function connect() {
    let chatSocket = new WebSocket("ws://" + window.location.host + "/ws/");

    chatSocket.onopen = function (e) {
    };

    chatSocket.onclose = function (e) {
        setTimeout(function () {
            connect();
        }, 2000);
    };

    chatSocket.onerror = function (err) {
        chatSocket.close();
    };

 
}

connect();

