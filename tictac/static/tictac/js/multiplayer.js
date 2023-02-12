
let socket_activated = null;
let joined_lobby = false;
let automatch_began = false;
let move = 0;
let player_id = null;
let game_started = false;
let turn = 'Your turn';
let unit = null;




function join_lobby_clicked() {
    const player_name = document.querySelector('#player_name').value;
    player_id = (Math.random() + 1).toString(36).substring(2);
    if (joined_lobby == false) {
        joined_lobby = true;
        console.log(player_name + ' joining lobby');
        chatSocket = new WebSocket(
            'ws://'
            + window.location.host
            + '/ws/'
            + 'multi'
            + '/'
        );
        //socket_activated = 1;

        chatSocket.onopen = function(event) {
            //console.log('lobby_socket onopen func called');
            var message = {
                type: "data",
                'player_name': player_name,
                'id': player_id,
                'session_key': session_key,
            };
//            var message = {
//                type: "message",
//                text: "Hello, server123!",
//                text1: "Hello111, server123!"
//            };
            chatSocket.send(JSON.stringify(message));
        };


        chatSocket.onclose = function(e) {
            console.error('lobby_Chat socket closed unexpectedly');
        };


        chatSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            //console.log(typeof data);
            //console.log(data);
            document.getElementById('info_li_11').innerHTML = "In lobby ("+String(data['players'].length)+"):";
            for (i in data['players']) {
                //console.log(data['players'][i]['name']);
                //console.log(i);
                document.getElementById('info_li_'+(Number(i)+12).toString()).innerHTML = data['players'][i]['name'];

            };
            for (let i = data['players'].length; i <= 6; i = i + 1) {
                //console.log("i = " + i);
                document.getElementById('info_li_'+(i+12).toString()).innerHTML = '..';
            };


            const block = document.getElementById("info_li_3");
            if (block.contains(document.getElementById("button_automatch")) == false) {
                //console.log("The target element is inside the block.");

                const button = document.createElement("button");
                button.innerHTML = "Click me";
                button.innerHTML = "Automatch";
                button.id = "button_automatch";
//                 Add an event listener to the button
                //button.addEventListener("click", automatch_clicked());
                button.onclick = automatch_clicked;
                // Append the button to the block
                block.appendChild(button);

            };

//            document.getElementById('info_li_3').innerHTML =
//            "
//                <button id='button_automatch' onclick='button_automatch_clicked()'>
//                    Automatch
//                </button>
//            "

//            if ('status' in data) {

//                console.log(data.status);
//                document.getElementById("game_status_text").innerHTML =
//                "Game status: game started.  "+ data.players_names[0] + ' vs '+ data.players_names[1];
//                if (data.players_names[0] == player_name) {
//                    unit = 'x';
//                    move = 0;
//                };
//            };
//
//            if ('list_fields' in data) {
//                list_fields = data.list_fields
//                //console.log(list_fields);
//                console.log('clicked field...');
//
//
//                move = data.move
//                for (i in list_fields) {
//                    document.getElementById(i).innerHTML = list_fields[i]['value'];
//                    if (list_fields[i]['value'] != " ") {
//                        document.getElementById(i).classList.add('button_field_not_allowed');
//                    };
//                };
//            };
//
        };








    };
};

function automatch_clicked() {

    if (automatch_began == false) {
        automatch_began = true;
        const player_name = document.querySelector('#player_name').value;
        console.log('game_' + player_name + ' Gamesocket created');
            gameSocket = new WebSocket(
                'ws://'
                + window.location.host
                + '/ws/'
                + 'multi/'
                + player_id
                + '/'
            );

        gameSocket.onopen = function(event) {
            console.log('game_Gamesocket onopen func called');
            var message = {
                type: "data",
                'game': {
                    'status': 'joining new game',
                    'id': player_id,
                    'player_name': player_name,
                },
//            var message = {
//                type: "data",
//                'game': {
//                    'status': 'Searching for opponent',
//                    'list_fields': null,
//                    'move': null,
//                    'id': player_id,
//                    'victory_status': null,
//                    'winner': null,
//                },
//                'players': {
//                    'id': null,
//                    'name': null,
//                    'unit': null,
//                    'wins': null,
//                    'losses': null,
//                    'draws': null,
//                },
////                'id': player_id,
////                'session_key': session_key,
            };

            gameSocket.send(JSON.stringify(message));
        };


        gameSocket.onclose = function(e) {
            console.error('game_Game socket closed unexpectedly');
        };


        gameSocket.onmessage = function(e) {
            const data = JSON.parse(e.data);
            //console.log(typeof data);
            console.log(data);
            //console.log(data.players[0].name);
            if (data.game.status == 'Game started') {
                game_started = true;
                document.getElementById("info_li_4").innerHTML = data.players[0].name + ' (' + data.players[0].unit + ')'
                document.getElementById("info_li_5").innerHTML = 'vs'
                document.getElementById("info_li_6").innerHTML = data.players[1].name + ' (' + data.players[1].unit + ')'
            };



            if (data.players[0].id == player_id) {
                unit = data.players[0].unit;
            };



            if (data.players[1].id == player_id) {
                unit = data.players[1].unit;
            };



            if (data.game.move == player_id) {
            document.getElementById("info_li_7").innerHTML = 'Your turn'
            turn = 'Your turn';
            }
            else {
            document.getElementById("info_li_7").innerHTML = "Opponent's turn"
            turn = "Opponent's turn";
            };

            for (i in data.game.list_fields) {
                //console.log(typeof i);
                //console.log(i);
                //document.getElementById("field_"+i).innerHTML = '8888';
                if (data.game.list_fields[Number(i)]['value'] == " " && data.game.move == player_id) {

                    document.getElementById("field_"+i).className ='button_field_allowed';
                }
                else {
                    document.getElementById("field_"+i).className ='button_field_not_allowed';
                };
            };

        };





    };
};

function Ffunc(x) {
    if (game_started == true) {
        if (list_fields[x]['value'] == " " && turn == 'Your turn') {
            document.getElementById("field_"+x).innerHTML = unit;
            document.getElementById("field_"+x).className ='button_field_not_allowed';
            list_fields[x]['value'] = 'unit';
//            var message = {
//                type: "data",
//                'game': {
//                    'status': 'joining new game',
//                    'id': player_id,
//                    'player_name': player_name,
//                },
//
//
//            gameSocket.send(JSON.stringify(message));
        };

    };
////    console.log('list_fields: '+list_fields);
////    console.log(list_fields[x]);
////    console.log('unit: '+unit);
////    console.log('move: '+move);
//    if (list_fields[x]['value'] == " " && unit == 'x' && move == 0) {
//        document.getElementById(x).innerHTML = unit;
//        list_fields[x]['value'] = unit
//
//        move = 1
//        chatSocket.send(JSON.stringify({'message':'1', 'list_fields': list_fields, 'move': move}));
//
//    };
//
//    if (list_fields[x]['value'] == " " && unit == 'o' && move == 1) {
//        document.getElementById(x).innerHTML = unit;
//        list_fields[x]['value'] = unit
//
//        move = 0
//        chatSocket.send(JSON.stringify({'message':'1', 'list_fields': list_fields, 'move': move}));
//    };
};

