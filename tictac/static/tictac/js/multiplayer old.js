
let socket_activated = null;
let player = null;
let move = 0;



function Ffunc(x) {
    console.log('list_fields: '+list_fields);
    console.log(list_fields[x]);
    console.log('unit: '+unit);
    console.log('move: '+move);
    if (list_fields[x]['value'] == " " && unit == 'x' && move == 0) {
        document.getElementById(x).innerHTML = unit;
        list_fields[x]['value'] = unit

        move = 1
        chatSocket.send(JSON.stringify({'message':'1', 'list_fields': list_fields, 'move': move}));

    };

    if (list_fields[x]['value'] == " " && unit == 'o' && move == 1) {
        document.getElementById(x).innerHTML = unit;
        list_fields[x]['value'] = unit

        move = 0
        chatSocket.send(JSON.stringify({'message':'1', 'list_fields': list_fields, 'move': move}));
    };
};

function automatch_clicked() {
    const player_name = document.querySelector('#player_name').value;
    if (player == null) {
        console.log(list_fields);

        console.log('button automatch clicked by '+player_name);
        chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/'
            + 'multi/'
            + player_name
            + '/'
        );
        socket_activated = 1;
        player = player_name;

        chatSocket.onopen = function(event) {
            console.log('socket onopen func called');
            var message = {
                type: "message",
                text: "Hello, server123!"
            };
            chatSocket.send(JSON.stringify(message));
        };


        chatSocket.onclose = function(e) {
            console.error('Chat socket closed unexpectedly');
        };


        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            console.log(typeof data);
            console.log(data);
            if ('status' in data) {
                console.log(data.status);
                document.getElementById("game_status_text").innerHTML =
                "Game status: game started.  "+ data.players_names[0] + ' vs '+ data.players_names[1];
                if (data.players_names[0] == player_name) {
                    unit = 'x';
                    move = 0;
                };
            };

            if ('list_fields' in data) {
                list_fields = data.list_fields
                //console.log(list_fields);
                console.log('clicked field...');


                move = data.move
                for (i in list_fields) {
                    document.getElementById(i).innerHTML = list_fields[i]['value'];
                    if (list_fields[i]['value'] != " ") {
                        document.getElementById(i).classList.add('button_field_not_allowed');
                    };
                };
            };

        };








    };
};