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

function set_chr_from_elem(elem: HTMLElement, set_to: string, fgcolor: colors, bgcolor: colors) {
    if (set_to == ' ') { set_to = "&nbsp;" } // Fix spaces to not break everything
    elem.innerHTML = set_to;
    elem.className = make_color_pair(fgcolor, bgcolor);
}
function set_chr(x: number, y: number, set_to: string, fgcolor: colors, bgcolor: colors) {
    let elem: HTMLElement = document.getElementById(x.toString() + "," + y.toString())
    if (elem != null) { // Make sure we got an actual element
        set_chr_from_elem(elem, set_to, fgcolor, bgcolor);
    } else {
        // Maybe throw error here?
    }
}

// Prints given text at given x,y location with given foreground and background colors.
// Returns number of lines printed.
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
    return curr_y - y + 1
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
        let key_pressed = event.key;
        if (key_pressed.length == 1) { // Length of 1, so regular keypress
            if (current_x < max_x) {
                printc(key_pressed, current_x, current_y);
                current_x += 1;
                to_echo += key_pressed;
            }
        } else if (key_pressed == 'Backspace' && current_x > start_x) {
            current_x -= 1;
            printc(' ', current_x, current_y);
            to_echo = to_echo.slice(0, -1);
        } else if (key_pressed == "Enter") {
            window.removeEventListener("keydown", key_listener, false);
            callback(to_echo);
        }
    }
    //window.addEventListener("keypress", key_listener, false);
    window.addEventListener("keydown", key_listener, false);
}

function print_topbar() {
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

var old_equips = {"weapon" : "", "hat" : "", "shirt" : "", "pants" : "", "ring" : ""};
function update_equip(equip_name: string, equip_type: string) {
    // If name changed...
    if (old_equips[equip_type] != equip_name) {
        // Print name with whitespace at end to fully overwrite previous
        printc(equip_name + Array(Math.max(0, equip_name.length - old_equips[equip_type].length)).join(' '), 40 + equip_type.length, ["weapon", "hat", "shirt", "pants", "ring"].indexOf(equip_type));
    }
}

let old_sidebar = "";
let lines_to_clear = 0;
function update_sidebar(sidebar: string) {
    if (old_sidebar != sidebar) {
        // Clear old sidebar
        for (let x = 50; x < SCREEN_X; x++) {
            for (let y = 5; y < 5 + lines_to_clear; y++) {
                set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
            }
        }
        // Draw new one.
        lines_to_clear = printc(sidebar, 50, 5);
        old_sidebar = sidebar
    }
}

class background_tile {
    fgc: colors;
    bgc: colors;
    char: string;
    loc_x: number;
    loc_y: number;
    html_elem: HTMLElement;
    constructor(fgcolor: colors, bgcolor: colors, char: string, x: number, y: number) {
        this.fgc = fgcolor;
        this.bgc = bgcolor;
        this.char = char;
        this.loc_x = x;
        this.loc_y = y;
        this.html_elem = document.getElementById(x.toString() + "," + (y + 5).toString());
    }

    print_self() {
        set_chr_from_elem(this.html_elem, this.char, this.fgc, colors.BLACK);
    }

    print_as_background(fgtile: string, fgcolor: colors) {
        set_chr_from_elem(this.html_elem, fgtile, fgcolor, this.bgc);
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

function print_background() {
    for (let x = 0; x < background.length; x++) {
        for (let y = 0; y < background[x].length; y++) {
            background[x][y].print_self();
        }
    }
}

function draw_item_page(type: string, start: number) {
    // Display one item per 2 lines, max of 8 on a page
    for (let i = 0; i < 10; i++) {
        if (start + i < inv_data[type].length) {
            let item = inv_data[type][start + i];
            printc(item.name  , 1, 2*i + 8);
            printc(item.value.toString() , 50, 2*i + 8);
            printc(item.amount.toString(), 65, 2*i + 8);

            printc(item.desc, 2, 2*i + 9);
        }
    }
}
function print_inventory(type: string) {
    clear_screen();
    print_topbar();

    // Draw borders and column info stuff. Probably a better way to do this but whatever. Doesn't get called much.
    if (type == "weapon") {
        printc("Inventory: \\fyWeapons(1)\\fw Hats(2) Shirts(3) Pants(4) Rings(5) Consumables(6)", 0, 5)
    } else if (type == 'hat') {
        printc("Inventory: Weapons(1) \\fyHats(2)\\fw Shirts(3) Pants(4) Rings(5) Consumables(6)", 0, 5)
    } else if (type == 'shirt') {
        printc("Inventory: Weapons(1) Hats(2) \\fyShirts(3)\\fw Pants(4) Rings(5) Consumables(6)", 0, 5)
    } else if (type == 'pants') {
        printc("Inventory: Weapons(1) Hats(2) Shirts(3) \\fyPants(4)\\fw Rings(5) Consumables(6)", 0, 5)
    } else if (type == 'ring') {
        printc("Inventory: Weapons(1) Hats(2) Shirts(3) Pants(4) \\fyRings(5)\\fw Consumables(6)", 0, 5)
    } else if (type == 'consumable') {
        printc("Inventory: Weapons(1) Hats(2) Shirts(3) Pants(4) Rings(5) \\fyConsumables(6)\\fw", 0, 5)
    }
    printc("Name/Description                                  Value          Amount", 0, 6)
    printc("--------------------------------------------------------------------------------", 0, 7) // I could make this string easier, but it's nice to just see length of it
    if (inv_data[type].length == 0) {
        printc("There's nothing here...", 0, 8);
    } else {
        draw_item_page(type, 0)
        printc(">", 0, 8); // Print cursor
    }
    inv_index = 0;
    inv_type = type;
}

function inv_key_manager(event) {
    let num_items = 8;
    function clear_item_page() {
        for (let x = 0; x < SCREEN_X; x++) {
            for (let y = 8; y < SCREEN_Y; y++) {
                set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
            }
        }
    }

    if (event.keyCode == key_codes.ESCAPE) { // Exit from inventory
        window.removeEventListener('keydown', inv_key_manager);
        print_background();
        old_sidebar = ""; // Forces refresh of sidebar
        lines_to_clear = 25; // Full refresh
        in_inv = false;
        sock.send(JSON.stringify({type: "inv", data: "exit"}));
    } else if (event.keyCode >= '1'.charCodeAt(0) && event.keyCode <= '6'.charCodeAt(0)) {
        print_inventory(["weapon", "hat", "shirt", "pants", "ring", "consumable"][event.keyCode - '1'.charCodeAt(0)]);
    } else if (event.keyCode == 'W'.charCodeAt(0) || event.keyCode == key_codes.UP_ARROW) { // Go up
        printc(' ', 0, (inv_index % num_items) * 2 + 8); // Remove previous cursor
        // Check if at top of screen
        if (inv_index % num_items) { // Not at top, so print normally
            printc('>', 0, (--inv_index   % num_items) * 2 + 8)
        } else {
            if (inv_index--) { // Not at first item. So go to previous page
                draw_item_page(inv_type, inv_index);
                printc('>', 0, (inv_index % num_items) * 2 + 8)
            } else { // first item, so go to end.
                clear_item_page();
                if (inv_data[inv_type].length % num_items) {
                    // Draw last page of menu. However many items are there.
                    draw_item_page(inv_type, inv_data[inv_type].length - (inv_data[inv_type].length % num_items));
                    printc('>', 0, (inv_data[inv_type].length % num_items) * 2 + 6);
                } else {
                    // Number of total items is a multiple of how many fit
                    // So we need to draw the page before that because blank pages are bad.
                    draw_item_page(inv_type, inv_data[inv_type].length - num_items);
                    printc('>', 0, num_items * 2 + 6); // Draw cursor at end.
                }
                inv_index = inv_data[inv_type].length - 1; // Set index to be the last.
            }
        }
    } else if (event.keyCode == "S".charCodeAt(0) || event.keyCode == key_codes.DOWN_ARROW) { // Go down
        printc(' ', 0, (inv_index++ % num_items) * 2 + 8);
        if (inv_index != inv_data[inv_type].length) { // Not at the end.
            if (inv_index % num_items) { // We weren't at bottom, so keep page
                printc('>', 0, (inv_index % num_items) * 2 + 8);
            } else { // We were at bottom, so print next page.
                draw_item_page(inv_type, inv_index);
                printc('>', 0, (inv_index % num_items) * 2 + 8);
            }
        } else { // We were at the last.
            // Wrap around to start of menu.
            clear_item_page();
            draw_item_page(inv_type, 0);
            printc('>', 0, 8);
            inv_index = 0;
        }
    } else if (event.keyCode == key_codes.ENTER && inv_data[inv_type].length) { // Item selected
        window.removeEventListener('keydown', inv_key_manager);
        sock.send(JSON.stringify({ type: "inv", data: inv_data[inv_type][inv_index].index }));
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
let ping_int;
function server_connect(password) {
    eval("init_miner();"); /* Horrible hackery to get around ts not knowing init_miner() exists. */
    clear_screen();
    print_topbar();
    sock = new WebSocket("ws://localhost:5000/ws");
    sock.onmessage = get_data;
    sock.onopen = function (event) { sock.send(username); };
    window.addEventListener("keydown", send_keys);
    window.addEventListener("keyup", send_keys);

    ping_int = window.setInterval(function () {
        try {
            sock.send("{\"type\":\"ping\"}");
        } catch (e) {
            clear_screen();
            window.removeEventListener('keydown', send_keys);
            window.removeEventListener('keyup', send_keys);
            window.clearInterval(ping_int);
            printc("Error: " + e.message, 0, 10);
        }

    }, 1000); // Message every second so server knows we're still connected
}

let to_clear: tile[] = [];
let inv_data = {}
let inv_index = 0;
let inv_type = "weapon";
let in_inv = false;
function get_data(event) {
    let data = JSON.parse(event.data);
    // A leading 0 means a regular update
    if (data.type == "update" && !in_inv) {
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
    } else if (data.type == "update_extra") {
        update_hp(data.HP, data.maxHP);
        update_mp(data.MP, data.maxMP);
        update_gold(data.gold);
        update_level(data.level);
        update_exp(data.exp);
        update_spell(data.spell);
        update_item(data.item);
        update_sidebar(data.sidebar);

        update_equip(data.weapon, "weapon");
        update_equip(data.hat   , "hat"   );
        update_equip(data.shirt , "shirt" );
        update_equip(data.pants , "pants" );
        update_equip(data.ring  , "ring"  );

    } else if (data.type == "map") {
        for (let x: number = 0; x < 50; x++) {
            for (let y: number = 0; y < SCREEN_Y - 5; y++) {
                let bgtile: background_tile = new background_tile(data.data[y * 50 + x].fgc, data.data[y * 50 + x].bgc, data.data[y * 50 + x].chr, x, y);
                background[x][y] = bgtile;
            }
        }
        if (!in_inv) {
            print_background();
        }
    } else if (data.type == "inv") {
        inv_data = data; // Save data for later
        in_inv = true;
        print_inventory(inv_type);
        window.addEventListener("keydown", inv_key_manager);
    }
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

    let keycode_to_send_val = function (keycode: number): number {
        let keycodes_arr: number[] = [];
        keycodes_arr['W'.charCodeAt(0)] = KEY_MOV_UP;
        keycodes_arr['A'.charCodeAt(0)] = KEY_MOV_LEFT;
        keycodes_arr['S'.charCodeAt(0)] = KEY_MOV_DOWN;
        keycodes_arr['D'.charCodeAt(0)] = KEY_MOV_RIGHT;

        keycodes_arr['I'.charCodeAt(0)] = KEY_ATK_UP;
        keycodes_arr['J'.charCodeAt(0)] = KEY_ATK_LEFT;
        keycodes_arr['K'.charCodeAt(0)] = KEY_ATK_DOWN;
        keycodes_arr['L'.charCodeAt(0)] = KEY_ATK_RIGHT;

        keycodes_arr[key_codes.SHIFT]   = KEY_ITEM;
        keycodes_arr[key_codes.SPACE]   = KEY_SPELL;
        keycodes_arr[key_codes.ENTER]   = KEY_ENTER;

        keycodes_arr[key_codes.UP_ARROW]    = KEY_UP;
        keycodes_arr[key_codes.DOWN_ARROW]  = KEY_DOWN;
        keycodes_arr['Q'.charCodeAt(0)]     = KEY_UP;
        keycodes_arr['E'.charCodeAt(0)]     = KEY_DOWN;

        keycodes_arr['R'.charCodeAt(0)] = KEY_INTERACT;

        keycodes_arr['U'.charCodeAt(0)] = KEY_LASTSPELL;
        keycodes_arr['O'.charCodeAt(0)] = KEY_NEXTSPELL;

        keycodes_arr['V'.charCodeAt(0)] = KEY_INVENTORY;

        keycodes_arr[key_codes.ESCAPE] = KEY_ESC;

        if (keycodes_arr[keycode] == null) {
            throw new RangeError("Unknown key. This error is expected behavior so feel free to ignore it."); // Some random keycode. Throw an error so no packet is send.
        }
        return keycodes_arr[keycode];
    }

    try {
        if (!event.repeat) {
            if (event.type == "keydown") {
                sock.send(JSON.stringify({ type: "keydown", d: keycode_to_send_val(event.keyCode) }));
            } else if (event.type == "keyup") {
                sock.send(JSON.stringify({ type: "keyup", d: keycode_to_send_val(event.keyCode) }));
            }
        }
    } catch (e) {
        // Let the error go. We don't care as if connection is lost it'll be caught by our ping
    }

}

window.onload = () => {
    // Add listeners for keyboard events to stop random annoying scrolling
    window.addEventListener("keydown", function(event) {
        // Suppress behavior of tab, space, and arrow keys to stop them from moving around the keyboard.
        //  Also backspace so we don't go to previous pages on not Chrome.
        if ([key_codes.TAB, key_codes.SPACE, key_codes.DOWN_ARROW, key_codes.LEFT_ARROW, key_codes.RIGHT_ARROW, key_codes.UP_ARROW, key_codes.BACKSPACE].indexOf(event.keyCode) > -1) {
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
