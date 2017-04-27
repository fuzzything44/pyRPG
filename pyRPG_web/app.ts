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
        // So set chr
        elem.innerHTML = set_to[0]; // make sure set_to is only 1 character
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
        if (curr_x >= SCREEN_X) { // Wrapped to a new line...
            curr_x = SCREEN_X - 1;
        }
        if (curr_y >= SCREEN_Y) { // Somehow printing too far down.
            curr_y = SCREEN_Y - 1;
        }

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

class Greeter {
    element: HTMLElement;
    span: HTMLElement;
    timerToken: number;

    constructor(element: HTMLElement) {
        this.element = element;
        this.element.innerHTML += "The time is: ";
        this.span = document.createElement('span');
        this.element.appendChild(this.span);
        this.span.innerText = new Date().toUTCString();
    }

    start() {
        this.timerToken = setInterval(() => this.span.innerHTML = new Date().toUTCString() + chr_to_color("g").toString(), 500);
    }

    stop() {
        clearTimeout(this.timerToken);
    }

}

window.onload = () => {
    var el = document.getElementById('test');
    var greeter = new Greeter(el);
    greeter.start();
    //set_chr(0, 0, "a", colors.RED, colors.GREEN);
    printc("abc\\\\\\fg\\bydef\nhey", 5, 0)
};