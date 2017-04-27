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
        elem.innerHTML = set_to[0];
        elem.className = make_color_pair(fgcolor, bgcolor);
    }
    else {
    }
}
function printc(text, x, y, start_color, start_bgcolor) {
    if (start_color === void 0) { start_color = colors.WHITE; }
    if (start_bgcolor === void 0) { start_bgcolor = colors.BLACK; }
    var color = start_color;
    var bgcolor = start_bgcolor;
    var curr_x = x;
    var curr_y = y;
    var escaped = false;
    var setting_color = false;
    var setting_bg = false;
    for (var chr_index in text) {
        if (curr_x >= SCREEN_X) {
            curr_x = SCREEN_X - 1;
        }
        if (curr_y >= SCREEN_Y) {
            curr_y = SCREEN_Y - 1;
        }
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
var Greeter = (function () {
    function Greeter(element) {
        this.element = element;
        this.element.innerHTML += "The time is: ";
        this.span = document.createElement('span');
        this.element.appendChild(this.span);
        this.span.innerText = new Date().toUTCString();
    }
    Greeter.prototype.start = function () {
        var _this = this;
        this.timerToken = setInterval(function () { return _this.span.innerHTML = new Date().toUTCString() + chr_to_color("g").toString(); }, 500);
    };
    Greeter.prototype.stop = function () {
        clearTimeout(this.timerToken);
    };
    return Greeter;
}());
window.onload = function () {
    var el = document.getElementById('test');
    var greeter = new Greeter(el);
    greeter.start();
    printc("abc\\\\\\fg\\bydef\nhey", 5, 0);
};
