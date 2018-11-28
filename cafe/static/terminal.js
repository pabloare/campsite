let cafeID;
let terminalName;
$(document).ready(function () {
    'use strict';
    console.log("jquery working");
    cafeID = $("#cafe_id").text();
    terminalName = $("#terminal_name").text();
    updateContent(cafeID, terminalName);
    setInterval(function() { updateContent(cafeID, terminalName); }, 3000 );
});

let csrftoken = Cookies.get('csrftoken');
$.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

function updateContent(cafeID, terminalName) {
    let csrftoken = Cookies.get('csrftoken');
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });
    $.ajax({
        type: 'post',
        url: "/cafe/terminal/update",
        data: {
            cafe_id : cafeID,
            terminal_name: terminalName,
        },
        success: function(result) {
            $(result).prependTo("#orders");
            }
    });
}
