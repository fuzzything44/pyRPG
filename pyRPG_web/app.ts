// Helper values and functions! Yay!
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

function set_chr(x: number, y: number, set_to: string, fgcolor: colors, bgcolor: colors) {
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


enum key_codes {
    BACKSPACE = 8,
    TAB = 9,
    ENTER = 13,
    SHIFT = 16,
    ESCAPE = 27,
    SPACE = 32,
    LEFT_ARROW = 37,
    UP_ARROW = 38,
    RIGHT_ARROW = 39,
    DOWN_ARROW = 40
}

function echo_text(start_x: number, start_y: number, x_len: number, callback) {
    var to_echo = "";
    var current_x: number = start_x;
    var current_y: number = start_y;
    var max_x: number = start_x + x_len;

    // Get keypresses and add them to the string.
    function key_listener(event) {
        if (event.type == "keypress") {
            if (event.keyCode == key_codes.ENTER) {
                window.removeEventListener("keypress", key_listener, false);
                window.removeEventListener("keydown", key_listener, false);
                callback(to_echo);
            }
            if (current_x < max_x) {
                let char: string = String.fromCharCode(event.keyCode);
                printc(char, current_x, current_y);
                current_x += 1;
                to_echo += char;
            }
        } else if (event.keyCode == key_codes.BACKSPACE && to_echo.length > 0) {
            current_x -= 1;
            printc(' ', current_x, current_y);
            to_echo = to_echo.slice(0, -1);
        } else if (event.keyCode == key_codes.SPACE && current_x < max_x) { // Handle space separately because it's not a keypress for some reason.
            printc(' ', current_x, current_y);
            current_x += 1;
            to_echo += ' ';
        }
    }
    window.addEventListener("keypress", key_listener, false);
    window.addEventListener("keydown", key_listener, false);
}

function draw_topbar() {
    // Draw HP/MP/Gold/Level/EXP
    printc("HP:\nMP:\nGold:\nLevel\n? to level", 5, 0);
    // Draw spellbox, itembox
    printc("#####  #####", 25, 0);
    printc("#   #  #   #", 25, 1);
    printc("#   #  #   #", 25, 2);
    printc("#   #  #   #", 25, 3);
    printc("#####  #####", 25, 4);

    // Draw equipment
    printc("Weapon:", 39, 0);
    printc("Hat:", 39, 1);
    printc("Shirt:", 39, 2);
    printc("Pants:", 39, 3);
    printc("Ring:", 39, 4);

}

function update_hp(curr_hp: number, max_hp: number) {
    let hp_str = curr_hp.toString() + "/" + max_hp.toString(); // Get hp values in a string
    printc(hp_str + Array(18 - hp_str.length).join(' '), 8, 0); // Print hp with trailing whitespace.

}

function update_mp(curr_mp: number, max_mp: number) {
    let mp_str = curr_mp.toString() + "/" + max_mp.toString()
    printc(mp_str + Array(18 - mp_str.length).join(' '), 8, 1); // Print mp with trailing whitespace

}

function update_gold(gold: number) {
    printc(gold.toString() + Array(16 - gold.toString().length).join(' '), 10, 2); // Print gold

}

function update_level(level: number) {
    printc(level.toString() + Array(15 - level.toString().length).join(' '), 11, 3); // Print level

}

function update_exp(exp: number) {
    let next_level = exp.toString() + " to level";
    printc(next_level + Array(21 - next_level.length).join(' '), 5, 4);

}

function update_spell(spell: string) {
    printc(spell, 26, 1);

}

function update_item(item: string) {
    printc(item, 33, 1);

}

function update_equip(equip_name: string, equip_type: string) {
    // Create an array with all functions to call. Then index off that and call it
    [(name) => printc(name + Array(39 - "Weapon:".length - name.length).join(' '), 39 + "Weapon:".length, 0),
     (name) => printc(name + Array(39 - "hat:".length -    name.length).join(' '), 39 + "hat:".length, 1),
     (name) => printc(name + Array(39 - "shirt:".length -  name.length).join(' '), 39 + "shirt:".length, 2),
     (name) => printc(name + Array(39 - "pants:".length -  name.length).join(' '), 39 + "pants:".length, 3),
     (name) => printc(name + Array(39 - "ring:".length -   name.length).join(' '), 39 + "ring:".length, 4)
    ][["weapon", "hat", "shirt", "pants", "ring"].indexOf(equip_type)](equip_name);
}


class background_tile {
    fgc: colors;
    bgc: colors;
    char: string;
    loc_x: number;
    loc_y: number;
    constructor(fgcolor: colors, bgcolor: colors, char: string, x: number, y: number) {
        this.fgc = fgcolor;
        this.bgc = bgcolor;
        this.char = char;
        this.loc_x = x;
        this.loc_y = y;
    }

    print_self() {
        set_chr(this.loc_x, this.loc_y + 5, this.char, this.fgc, colors.BLACK);
    }

    print_as_background(fgtile: string, fgcolor: colors) {
        set_chr(this.loc_x, this.loc_y + 5, fgtile, fgcolor, this.bgc);
    }
}

class tile {
    color: colors;
    char: string;
    loc_x: number;
    loc_y: number;

    constructor(color: colors, char: string, x: number, y: number) {
        this.color = color;
        this.char = char;
        this.loc_x = x;
        this.loc_y = y;
    }

    print_self() {
        background[this.loc_x][this.loc_y].print_as_background(this.char, this.color);
    }

    clear_self() {
        background[this.loc_x][this.loc_y].print_self();
    }

}
let background: background_tile[][] = [[]];

function draw_background() {
    for (let x = 0; x < background.length; x++) {
        for (let y = 0; y < background[x].length; y++) {
            background[x][y].print_self();
        }
    }
}
// End helper functions...

let username: string;
function ask_password(user) {
    username = user;
    printc("Enter your password:", 32, 10);
    echo_text(32, 11, 32, server_connect);
}

let sock: WebSocket;
function server_connect(password) {
    clear_screen();
    draw_topbar();
    sock = new WebSocket("ws://localhost:5000/ws");
    sock.onmessage = get_data;
    sock.onopen = function(event) { sock.send(username); };
    window.addEventListener("keydown", send_keys);
}

let to_clear: tile[] = [];
function get_data(event) {
    let data = JSON.parse(event.data);
    // A leading 0 means a regular update
    if (data.type == "update") {
        // Clear old tiles
        for (let i: number = 0; i < to_clear.length; i++) {
            to_clear[i].clear_self();
        }
        to_clear = [];

        // And print new ones.
        for (let i: number = 0; i < data.tiles.length; i++) {
            let print_tile: tile = new tile(data.tiles[i].color, data.tiles[i].chr, data.tiles[i].x, data.tiles[i].y);
            to_clear.push(print_tile);
            print_tile.print_self();
        }
    } else if (data.type == "map") {
        for (let x: number = 0; x < 50; x++) {
            for (let y: number = 0; y < SCREEN_Y - 5; y++) {
                let bgtile: background_tile = new background_tile(data.data[y * 50 + x].fgc, data.data[y * 50 + x].bgc, data.data[y * 50 + x].chr, x, y);
                bgtile.print_self();
                background[x][y] = bgtile;
            }
        }
        draw_background();
    }
    set_chr(0, 0, 'a', colors.RED, colors.GREEN);
}

function send_keys(event) {
    // When updating we want to send what key is now down
    // We just send keydown and the value corresponding to the key
    let KEY_MOV_UP      = 0
    let KEY_MOV_LEFT    = 1
    let KEY_MOV_DOWN    = 2
    let KEY_MOV_RIGHT   = 3

    let KEY_ATK_UP      = 4
    let KEY_ATK_LEFT    = 5
    let KEY_ATK_DOWN    = 6
    let KEY_ATK_RIGHT   = 7

    let KEY_ITEM        = 8
    let KEY_SPELL       = 9
    let KEY_ENTER       = 10

    let KEY_UP          = 11
    let KEY_DOWN        = 12

    let KEY_INTERACT    = 13

    let KEY_LASTSPELL   = 14
    let KEY_NEXTSPELL   = 15

    let KEY_INVENTORY   = 16
    let KEY_ESC         = 17

    let keycode_to_send_val = function(keycode: number): number {
        return 0; // TODO: Actually write this function. Not really sure how without a bunch of annoying ifs though
    }

    if (!event.repeat) {
        if (event.type == "keydown") {
            sock.send(JSON.stringify({ type : "keydown", d : keycode_to_send_val(event.keyCode) }));
        } else if (event.type == "keyup") {
            sock.send(JSON.stringify({ type : "keyup", d : keycode_to_send_val(event.keyCode) }));
        }
    }

}

window.onload = () => {
    // Add listeners for keyboard events to stop random annoying scrolling
    window.addEventListener("keydown", function(event) {
        // Suppress behavior of tab, space, and arrow keys to stop them from moving around the keyboard.
        if ([key_codes.TAB, key_codes.SPACE, key_codes.DOWN_ARROW, key_codes.LEFT_ARROW, key_codes.RIGHT_ARROW, key_codes.UP_ARROW].indexOf(event.keyCode) > -1) {
            event.preventDefault();
        }
    }, false);

    // Init background.
    background = [];
    for (let x = 0; x < 50; x++) {
        background.push([]);
        for (let y = 0; y < SCREEN_Y - 5; y++) {
            background[x].push(new background_tile(colors.WHITE, colors.BLACK, ' ', x, y));
        }
    }

    printc("Welcome to py   !", 33, 7);
    let r_color = Math.round(Math.random());
    let p_color = Math.round(Math.random());
    let g_color = Math.round(Math.random());
    printc("R", 33 + "Welcome to py".length, 7, [colors.RED, colors.YELLOW][r_color]);
    printc("P", 33 + "Welcome to pyR".length, 7, [colors.GREEN, colors.CYAN][p_color]);
    printc("G", 33 + "Welcome to pyRP".length, 7, [colors.BLUE, colors.MAGENTA][g_color]);

    printc("Enter your username", 32, 8);
    echo_text(32, 9, 24, ask_password);
};
