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
var Greeter = (function () {
    function Greeter(element) {
        document.getElementById("7,9").className = make_color_pair(colors.GREEN + this.color_add, colors.RED + this.color_add);
        printc("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]{}<>", 0, 9);
    }
    Greeter.prototype.start = function () {
        this.timerToken = setInterval(function () { document.getElementById(Math.floor(Math.random() * 80).toString() + "," + Math.floor(Math.random() * 25).toString()).className = make_color_pair(Math.floor(Math.random() * 8), Math.floor(Math.random() * 8)); }, 0);
    };
    Greeter.prototype.stop = function () {
        clearTimeout(this.timerToken);
    };
    return Greeter;
}());
window.onload = function () {
    // Add listeners for keyboard events so we know when keys are pressed.
    window.addEventListener("keydown", function (event) {
        // Suppress behavior of tab, space, and arrow keys to stop them from moving around the keyboard.
        if ([9, 32, 37, 38, 39, 40].indexOf(event.keyCode) > -1) {
            event.preventDefault();
        }
        keys[event.keyCode] = true;
    }, false);
    window.addEventListener("keyup", function (event) {
        keys[event.keyCode] = false;
    }, false);
    var el = document.getElementById('5,7');
    var greeter = new Greeter(el);
    greeter.start();
    //set_chr(0, 0, "a", colors.RED, colors.GREEN);
    printc("abc\\\\\\fg\\bydef\nhey", 6, 0);
};
