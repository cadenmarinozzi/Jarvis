let started = false;
let audio = new Audio();
audio.src = "data:audio/mpeg;base64,SUQzBAAAAAABEVRYWFgAAAAtAAADY29tbWVudABCaWdTb3VuZEJhbmsuY29tIC8gTGFTb25vdGhlcXVlLm9yZwBURU5DAAAAHQAAA1N3aXRjaCBQbHVzIMKpIE5DSCBTb2Z0d2FyZQBUSVQyAAAABgAAAzIyMzUAVFNTRQAAAA8AAANMYXZmNTcuODMuMTAwAAAAAAAAAAAAAAD/80DEAAAAA0gAAAAATEFNRTMuMTAwVVVVVVVVVVVVVUxBTUUzLjEwMFVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/zQsRbAAADSAAAAABVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVf/zQMSkAAADSAAAAABVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV";
let canvas = document.getElementsByTagName("canvas")[0];
let playLocal = document.getElementById("play_locally");
let sendToWebsocket = document.getElementById("send_to_websocket");
let useMicrophone = document.getElementById("use_microphone");
let wakeupTime = document.getElementById("wakeup_time");
let inputBox = document.getElementsByClassName("input-box")[0];
let context = canvas.getContext("2d");
let radius = 150;
let lines = 150;
let width = canvas.parentElement.clientWidth;
let height = canvas.parentElement.clientHeight;
let centerX = width / 2;
let centerY = height / 2;
canvas.width = width;
canvas.height = height;

function line(x, y, endX, endY) {
    context.beginPath();
    context.moveTo(x, y);
    context.lineTo(endX, endY);
    context.stroke();
}

class FrequencyData {
    constructor() {
        this.audioContext = null;
        this.source = null;
        this.analyser = null;
    }

    getFrequencies() {
        if (!this.audioContext) {
            this.audioContext = new window.AudioContext();
            this.source = this.audioContext.createMediaElementSource(audio);
            this.analyser = this.audioContext.createAnalyser();
        }

        this.source.connect(this.analyser);
        this.analyser.connect(this.audioContext.destination);

        return [new Uint8Array(this.analyser.frequencyBinCount), this.analyser];
    }
}

let frequencyData = new FrequencyData();

window.addEventListener("touchstart", function() {
    if (!started) {
        audio.play();
        started = true;
    }
});

function fade() {
    let volumeStep = audio.volume / 5000;

    function ramp() {
        audio.volume = Math.max(0, audio.volume - volumeStep);

        if (audio.volume > 0) {
            setTimeout(ramp, 0.005);
        }
    }

    ramp();
}

let host = "98.210.224.5";
let port = "8080";
let connected = false;
let renderIndex;

function render(static) {
    width = window.innerWidth;
    height = window.innerHeight - 77;
    centerX = width / 2;
    centerY = height / 2;
    canvas.width = width;
    canvas.height = height;
    renderIndex = 0;

    if (!static) {
        renderIndex = 1;
        var [frequencies, analyser] = frequencyData.getFrequencies();
        analyser.getByteFrequencyData(frequencies);
    }

    context.clearRect(0, 0, width, height);

    for (let index = 0; index < lines; index++) {
        let frequency = static ? 1 : (frequencies[index] || 1);
        let circumference = Math.PI * 2 / radius;
        let x = Math.cos(circumference * index);
        let y = Math.sin(circumference * index);
        context.strokeStyle = connected ? "rgb(254," + frequency / 2 + ",255)" : "rgb(90, 90, 90)";
        line(centerX + radius * x, centerY + radius * y, centerX + (radius + frequency) * x, centerY + (radius + frequency) * y); // polar to cartesian coordinates
    }

    setTimeout(function() {
        if (renderIndex == 1) {
            render();

            return;
        }

        render(true);
    }, 0);
}

render(true);

wakeupTime.onkeydown = function(event) {
    return false;
}

inputBox.addEventListener("keydown", function(event) {
    if (useMicrophone.textContent == "\u2713" || !connected) {
        event.preventDefault();
    }
});

function connect() {
    let webSocket = new WebSocket("ws://" + host + ":" + port);

    webSocket.onopen = function(event) {
        connected = true;

        inputBox.onkeydown = function(event) { // Overwrites
            if (event.key == "Enter") {
                webSocket.send("exec___" + inputBox.value);
                inputBox.value = "";
            }
        }

        playLocal.onclick = function(event) {
            if (connected) {
                if (playLocal.textContent == "x") {
                    playLocal.textContent = "\u2713";
                    playLocal.style.background = "rgb(255, 201, 255)";
                    playLocal.style.color = "rgb(22, 22, 22)";
                    webSocket.send("playLocal__true");
            
                    return;
                }
            
                playLocal.textContent = "x";
                playLocal.style.background = "rgb(22, 22, 22)";
                playLocal.style.color = "rgb(255, 255, 255)";
                webSocket.send("playLocal__false");

                return;
            }

            return false;
        }
        
        sendToWebsocket.onclick = function(event) {
            if (connected) {
                if (sendToWebsocket.textContent == "x") {
                    sendToWebsocket.textContent = "\u2713";
                    sendToWebsocket.style.background = "rgb(255, 201, 255)";
                    sendToWebsocket.style.color = "rgb(22, 22, 22)";
                    webSocket.send("sendToWebsocket__true");
            
                    return;
                }
            
                sendToWebsocket.textContent = "x";
                sendToWebsocket.style.background = "rgb(22, 22, 22)";
                sendToWebsocket.style.color = "rgb(255, 255, 255)";
                webSocket.send("sendToWebsocket__false");

                return;
            }

            return false;
        }
        
        useMicrophone.onclick = function(event) {
            if (connected) {
                if (useMicrophone.textContent == "x") {
                    useMicrophone.textContent = "\u2713";
                    useMicrophone.style.background = "rgb(255, 201, 255)";
                    useMicrophone.style.color = "rgb(22, 22, 22)";
                    webSocket.send("useMicrophone__true");
            
                    return;
                }
            
                useMicrophone.textContent = "x";
                useMicrophone.style.background = "rgb(22, 22, 22)";
                useMicrophone.style.color = "rgb(255, 255, 255)";
                webSocket.send("useMicrophone__false");

                return;
            }

            return false;
        }

        wakeupTime.onkeydown = function(event) {
            if (connected) {
                if (wakeupTime.value.match(/(0[1-9]|1[0-2]):(0[1-9]|1[0-2]):(0[1-9]|1[0-2])\s+(\bAM\b|\bPM\b)/g)) {
                    webSocket.send("wakeupTime__" + wakeupTime.value);
                    wakeupTime.style.color = "rgb(255, 255, 255)";

                    return;
                }

                wakeupTime.style.color = "rgb(65, 65, 65)";

                return;
            }

            return false;
        }
    }

    webSocket.onmessage = function(event) {
        let message = event.data;
        audio.src = "";

        if (message.includes("RkFERUZPUkFVRElP")) {
            audio.src = "data:audio/mp3;base64," + message.replace("RkFERUZPUkFVRElP", "");
            audio.play();

            setTimeout(function() {
                fade();
            }, 25000);

            render();
        } else if (message.includes("ibmWatson")) {
            let configuration = JSON.parse(message);
            
            if (configuration.useMicrophone) {
                useMicrophone.textContent = "\u2713";
                useMicrophone.style.background = "rgb(255, 201, 255)";
                useMicrophone.style.color = "rgb(22, 22, 22)";
            } else {
                useMicrophone.textContent = "x";
                useMicrophone.style.background = "rgb(22, 22, 22)";
                useMicrophone.style.color = "rgb(255, 255, 255)";
            }

            if (configuration.playLocal) {
                playLocal.textContent = "\u2713";
                playLocal.style.background = "rgb(255, 201, 255)";
                playLocal.style.color = "rgb(22, 22, 22)";
            } else {
                playLocal.textContent = "x";
                playLocal.style.background = "rgb(22, 22, 22)";
                playLocal.style.color = "rgb(255, 255, 255)";
            }

            if (configuration.sendToWebsocket) {
                sendToWebsocket.textContent = "\u2713";
                sendToWebsocket.style.background = "rgb(255, 201, 255)";
                sendToWebsocket.style.color = "rgb(22, 22, 22)";
            } else {
                sendToWebsocket.textContent = "x";
                sendToWebsocket.style.background = "rgb(22, 22, 22)";
                sendToWebsocket.style.color = "rgb(255, 255, 255)";
            }

            wakeupTime.value = configuration.wakeupTime;
        } else {
            audio.src = "data:audio/mp3;base64," + message;
            audio.play();
            render();
        }
    }

    webSocket.onclose = function(event) {
        connected = false;
        setTimeout(connect, 1000);
    }

    webSocket.onerror = function(event) {
        webSocket.close();
    }
}

connect();