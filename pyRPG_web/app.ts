enum colors {
    WHITE   = 0,
    BLACK   = 1,
    RED     = 2,
    BLUE    = 3,
    CYAN    = 4,
    GREEN   = 5,
    MAGENTA = 6,
    YELLOW  = 7
}

let SCREEN_X: number = 80;
let SCREEN_Y: number = 25;


function chr_to_color(ch: string): number {
    return "wxrbcgmy".indexOf(ch);
}

function color_to_chr(col: colors): string {
    return "wxrbcgmy"[col];
}

function make_color_pair(fgcolor: colors, bgcolor: colors): string {
    return "f" + color_to_chr(fgcolor) + " b" + color_to_chr(bgcolor);
}

function set_chr(x: number, y: number, set_to: string, fgcolor: colors = colors.WHITE, bgcolor: colors = colors.BLACK) {
    let elem: HTMLElement = document.getElementById(x.toString() + "," + y.toString())
    if (elem != null) { // Make sure we got an actual element
        if (set_to == " ") {
            set_to = "&nbsp;";
        }
        // So set chr
        elem.innerHTML = set_to; // make sure set_to is only 1 character
        // And bgcolor
        elem.className = make_color_pair(fgcolor, bgcolor);
    } else {
        // Maybe throw error here?
    }
}

function printc(text: String, x: number, y: number, start_color: colors = colors.WHITE, start_bgcolor: colors = colors.BLACK) {
    let color: colors = start_color;
    let bgcolor: colors = start_bgcolor;

    let curr_x: number = x; // Where we're actually printing
    let curr_y: number = y;

    let escaped: boolean = false;
    let setting_color: boolean = false;
    let setting_bg: boolean = false;

    for (let chr_index in text) {
        let chr: string = text[chr_index];

        if (escaped) {
            if (chr == "\\") {
                set_chr(curr_x, curr_y, "\\", color, bgcolor);
                curr_x += 1;
            } else if (chr == "b") {
                setting_bg = true;
            } else if (chr == "f") {
                setting_color = true;
            } else {
                // Raise exception
            }
            escaped = false;
        } else if (setting_color) {
            color = chr_to_color(chr);
            setting_color = false;
        } else if (setting_bg) {
            bgcolor = chr_to_color(chr);
            setting_bg = false;
        } else { // No special modes on.
            if (chr == "\n") {
                curr_y += 1
                curr_x = x;
            } else if (chr == "\\") {
                escaped = true;
            } else {
                set_chr(curr_x, curr_y, chr, color, bgcolor);
                curr_x += 1;
            }
        }
    }
}

function clear_screen() {
    for (let x: number = 0; x < SCREEN_X; x++) {
        for (let y: number = 0; y < SCREEN_Y; y++) {
            set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
        }
    }
}

// Holds what key states are.
let keys = [];

class Greeter {
    timerToken: number;
    color_add: number;

    constructor(element: HTMLElement) {
        document.getElementById("7,9").className = make_color_pair(colors.GREEN + this.color_add, colors.RED + this.color_add);
        printc("abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-=_+[]{}<>", 0, 9);
    }

    start() {
        this.timerToken = setInterval(function() { document.getElementById(Math.floor(Math.random() * 80).toString() + "," + Math.floor(Math.random() * 25).toString()).className = make_color_pair(Math.floor(Math.random() * 8), Math.floor(Math.random() * 8));}, 0);
    }

    stop() {
        clearTimeout(this.timerToken);
    }

}

window.onload = () => {
    // Add listeners for keyboard events so we know when keys are pressed.
    window.addEventListener("keydown", function(event) {
        // Suppress behavior of tab, space, and arrow keys to stop them from moving around the keyboard.
        if([9, 32, 37, 38, 39, 40].indexOf(event.keyCode) > -1) {
            event.preventDefault();
        }
        keys[event.keyCode] = true;
    }, false);

    window.addEventListener("keyup", function(event) {
        keys[event.keyCode] = false;
    }, false);


    var el = document.getElementById('5,7');
    var greeter = new Greeter(el);
    greeter.start();
    //set_chr(0, 0, "a", colors.RED, colors.GREEN);
    printc("abc\\\\\\fg\\bydef\nhey", 6, 0)
};
