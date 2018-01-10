var keys = {"37": "left",
            "38": "forward",
            "39": "right",
            "40": "backward",
            "0": "stop"}

var last = null;
var current_command = 0;

document.addEventListener('keydown', function(event) {
    var key = event.keyCode ? event.keyCode : event.which;
    downKey(key);
});

document.addEventListener('keyup', function(event) {
    var key = (event.keyCode ? event.keyCode : event.which) + "";
    upKey(key);
});

document.addEventListener('mousedown', function(event) {
    var btn = (event.target.nodeName != "I" ? event.target : $(event.target).parent());
    var key = $(btn).data("arrow");
    downKey(key);
});

document.addEventListener('mouseup', function(event) {
    var btn = (event.target.nodeName != "I" ? event.target : $(event.target).parent());
    var key = $(btn).data("arrow");
    upKey(key);
});

function downKey(key) {
    if (key in keys && key != last && key != current_command) {
        last = key;
        current_command = key;
        for (other_key in keys) {
            if (keys.hasOwnProperty(other_key) && other_key != key) {
                var element = jQuery('.arrow[data-arrow=' + other_key + ']');
                element.removeClass('btn-primary');
            }
        }
        var element = jQuery('.arrow[data-arrow=' + key + ']');
        element.addClass('btn-primary');
        console.log("GO " + keys[key]);
        jQuery.get('/action/' + keys[key]);
    }
}

function upKey(key) {
    if (key in keys) {
        var element = jQuery('.arrow[data-arrow=' + key + ']');
        element.removeClass('btn-primary');
    }
    last = null;
    setTimeout(function () {
        if (last == null && current_command != 0) {
            console.log("STOP");
            jQuery.get('/action/stop');
            current_command = 0;
        }
    }, 250);
}