var colors;
(function (colors) {
    colors[colors["WHITE"] = 0] = "WHITE";
    colors[colors["BLACK"] = 1] = "BLACK";
    colors[colors["RED"] = 2] = "RED";
    colors[colors["BLUE"] = 3] = "BLUE";
    colors[colors["CYAN"] = 4] = "CYAN";
    colors[colors["GREEN"] = 5] = "GREEN";
    colors[colors["MAGENTA"] = 6] = "MAGENTA";
    colors[colors["YELLOW"] = 7] = "YELLOW";
})(colors || (colors = {}));
var SCREEN_X = 80;
var SCREEN_Y = 25;
function chr_to_color(ch) {
    return "wxrbcgmy".indexOf(ch);
}
function color_to_chr(col) {
    return "wxrbcgmy"[col];
}
function make_color_pair(fgcolor, bgcolor) {
    return "f" + color_to_chr(fgcolor) + " b" + color_to_chr(bgcolor);
}
function set_chr(x, y, set_to, fgcolor, bgcolor) {
    if (fgcolor === void 0) { fgcolor = colors.WHITE; }
    if (bgcolor === void 0) { bgcolor = colors.BLACK; }
    var elem = document.getElementById(x.toString() + "," + y.toString());
    if (elem != null) {
        if (set_to == " ") {
            set_to = "&nbsp;";
        }
        // So set chr
        elem.innerHTML = set_to; // make sure set_to is only 1 character
        // And bgcolor
        elem.className = make_color_pair(fgcolor, bgcolor);
    }
    else {
        // Maybe throw error here?
    }
}
function printc(text, x, y, start_color, start_bgcolor) {
    if (start_color === void 0) { start_color = colors.WHITE; }
    if (start_bgcolor === void 0) { start_bgcolor = colors.BLACK; }
    var color = start_color;
    var bgcolor = start_bgcolor;
    var curr_x = x; // Where we're actually printing
    var curr_y = y;
    var escaped = false;
    var setting_color = false;
    var setting_bg = false;
    for (var chr_index in text) {
        var chr = text[chr_index];
        if (escaped) {
            if (chr == "\\") {
                set_chr(curr_x, curr_y, "\\", color, bgcolor);
                curr_x += 1;
            }
            else if (chr == "b") {
                setting_bg = true;
            }
            else if (chr == "f") {
                setting_color = true;
            }
            else {
                // Raise exception
            }
            escaped = false;
        }
        else if (setting_color) {
            color = chr_to_color(chr);
            setting_color = false;
        }
        else if (setting_bg) {
            bgcolor = chr_to_color(chr);
            setting_bg = false;
        }
        else {
            if (chr == "\n") {
                curr_y += 1;
                curr_x = x;
            }
            else if (chr == "\\") {
                escaped = true;
            }
            else {
                set_chr(curr_x, curr_y, chr, color, bgcolor);
                curr_x += 1;
            }
        }
    }
}
function clear_screen() {
    for (var x = 0; x < SCREEN_X; x++) {
        for (var y = 0; y < SCREEN_Y; y++) {
            set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
        }
    }
}
// Holds what key states are.
var keys = [];
var key_codes;
(function (key_codes) {
    key_codes[key_codes["BACKSPACE"] = 8] = "BACKSPACE";
    key_codes[key_codes["TAB"] = 9] = "TAB";
    key_codes[key_codes["ENTER"] = 13] = "ENTER";
    key_codes[key_codes["SHIFT"] = 16] = "SHIFT";
    key_codes[key_codes["ESCAPE"] = 27] = "ESCAPE";
    key_codes[key_codes["SPACE"] = 32] = "SPACE";
    key_codes[key_codes["LEFT_ARROW"] = 37] = "LEFT_ARROW";
    key_codes[key_codes["UP_ARROW"] = 38] = "UP_ARROW";
    key_codes[key_codes["RIGHT_ARROW"] = 39] = "RIGHT_ARROW";
    key_codes[key_codes["DOWN_ARROW"] = 40] = "DOWN_ARROW";
})(key_codes || (key_codes = {}));
function echo_text(start_x, start_y, x_len, callback) {
    var to_echo = "";
    var current_x = start_x;
    var current_y = start_y;
    var max_x = start_x + x_len;
    // Get keypresses and add them to the string.
    function key_listener(event) {
        if (event.type == "keypress") {
            if (event.keyCode == key_codes.ENTER) {
                window.removeEventListener("keypress", key_listener, false);
                window.removeEventListener("keydown", key_listener, false);
                callback(to_echo);
            }
            if (current_x < max_x) {
                var char = String.fromCharCode(event.keyCode);
                printc(char, current_x, current_y);
                current_x += 1;
                to_echo += char;
            }
        }
        else if (event.keyCode == key_codes.BACKSPACE && to_echo.length > 0) {
            current_x -= 1;
            printc(' ', current_x, current_y);
            to_echo = to_echo.slice(0, -1);
        }
        else if (event.keyCode == key_codes.SPACE && current_x < max_x) {
            printc(' ', current_x, current_y);
            current_x += 1;
            to_echo += ' ';
        }
    }
    window.addEventListener("keypress", key_listener, false);
    window.addEventListener("keydown", key_listener, false);
}
window.onload = function () {
    // Add listeners for keyboard events so we know when keys are pressed.
    window.addEventListener("keydown", function (event) {
        // Suppress behavior of tab, space, and arrow keys to stop them from moving around the keyboard.
        if ([key_codes.TAB, key_codes.SPACE, key_codes.DOWN_ARROW, key_codes.LEFT_ARROW, key_codes.RIGHT_ARROW, key_codes.UP_ARROW].indexOf(event.keyCode) > -1) {
            event.preventDefault();
        }
        keys[event.keyCode] = true;
    }, false);
    window.addEventListener("keyup", function (event) {
        keys[event.keyCode] = false;
    }, false);
    printc("Welcome to py   !", 33, 7);
    var r_color = Math.round(Math.random());
    var p_color = Math.round(Math.random());
    var g_color = Math.round(Math.random());
    printc("R", 33 + "Welcome to py".length, 7, [colors.RED, colors.YELLOW][r_color]);
    printc("P", 33 + "Welcome to pyR".length, 7, [colors.BLUE, colors.CYAN][p_color]);
    printc("G", 33 + "Welcome to pyRP".length, 7, [colors.GREEN, colors.MAGENTA][g_color]);
    printc("Enter your username", 32, 8);
    echo_text(5, 5, 10, function (text) { return echo_text(0, 10, 15, [r_color, p_color, g_color]); });
};
//# sourceMappingURL=app.js.map