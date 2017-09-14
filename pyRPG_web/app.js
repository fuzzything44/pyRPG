// Helper values and functions! Yay!
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
function set_chr_from_elem(elem, set_to, fgcolor, bgcolor) {
    if (set_to == ' ') {
        set_to = "&nbsp;";
    } // Fix spaces to not break everything
    elem.innerHTML = set_to;
    elem.className = make_color_pair(fgcolor, bgcolor);
}
function set_chr(x, y, set_to, fgcolor, bgcolor) {
    var elem = document.getElementById(x.toString() + "," + y.toString());
    if (elem != null) {
        set_chr_from_elem(elem, set_to, fgcolor, bgcolor);
    }
    else {
        // Maybe throw error here?
    }
}
// Prints given text at given x,y location with given foreground and background colors.
// Returns number of lines printed.
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
    return curr_y - y + 1;
}
function clear_screen() {
    for (var x = 0; x < SCREEN_X; x++) {
        for (var y = 0; y < SCREEN_Y; y++) {
            set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
        }
    }
}
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
        var key_pressed = event.key;
        if (key_pressed.length == 1) {
            if (current_x < max_x) {
                printc(key_pressed, current_x, current_y);
                current_x += 1;
                to_echo += key_pressed;
            }
        }
        else if (key_pressed == 'Backspace' && current_x > start_x) {
            current_x -= 1;
            printc(' ', current_x, current_y);
            to_echo = to_echo.slice(0, -1);
        }
        else if (key_pressed == "Enter") {
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
function update_hp(curr_hp, max_hp) {
    var hp_str = curr_hp.toString() + "/" + max_hp.toString(); // Get hp values in a string
    printc(hp_str + Array(18 - hp_str.length).join(' '), 8, 0); // Print hp with trailing whitespace.
}
function update_mp(curr_mp, max_mp) {
    var mp_str = curr_mp.toString() + "/" + max_mp.toString();
    printc(mp_str + Array(18 - mp_str.length).join(' '), 8, 1); // Print mp with trailing whitespace
}
function update_gold(gold) {
    printc(gold.toString() + Array(16 - gold.toString().length).join(' '), 10, 2); // Print gold
}
function update_level(level) {
    printc(level.toString() + Array(15 - level.toString().length).join(' '), 11, 3); // Print level
}
function update_exp(exp) {
    var next_level = exp.toString() + " to level";
    printc(next_level + Array(21 - next_level.length).join(' '), 5, 4);
}
function update_spell(spell) {
    printc(spell, 26, 1);
}
function update_item(item) {
    printc(item, 33, 1);
}
var old_equips = { "weapon": "", "hat": "", "shirt": "", "pants": "", "ring": "" };
function update_equip(equip_name, equip_type) {
    // If name changed...
    if (old_equips[equip_type] != equip_name) {
        // Print name with whitespace at end to fully overwrite previous
        printc(equip_name + Array(Math.max(0, equip_name.length - old_equips[equip_type].length)).join(' '), 40 + equip_type.length, ["weapon", "hat", "shirt", "pants", "ring"].indexOf(equip_type));
    }
}
var old_sidebar = "";
var lines_to_clear = 0;
function update_sidebar(sidebar) {
    if (old_sidebar != sidebar) {
        // Clear old sidebar
        for (var x = 50; x < SCREEN_X; x++) {
            for (var y = 5; y < 5 + lines_to_clear; y++) {
                set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
            }
        }
        // Draw new one.
        lines_to_clear = printc(sidebar, 50, 5);
        old_sidebar = sidebar;
    }
}
var background_tile = (function () {
    function background_tile(fgcolor, bgcolor, char, x, y) {
        this.fgc = fgcolor;
        this.bgc = bgcolor;
        this.char = char;
        this.loc_x = x;
        this.loc_y = y;
        this.html_elem = document.getElementById(x.toString() + "," + (y + 5).toString());
    }
    background_tile.prototype.print_self = function () {
        set_chr_from_elem(this.html_elem, this.char, this.fgc, colors.BLACK);
    };
    background_tile.prototype.print_as_background = function (fgtile, fgcolor) {
        set_chr_from_elem(this.html_elem, fgtile, fgcolor, this.bgc);
    };
    return background_tile;
}());
var tile = (function () {
    function tile(color, char, x, y) {
        this.color = color;
        this.char = char;
        this.loc_x = x;
        this.loc_y = y;
    }
    tile.prototype.print_self = function () {
        background[this.loc_x][this.loc_y].print_as_background(this.char, this.color);
    };
    tile.prototype.clear_self = function () {
        background[this.loc_x][this.loc_y].print_self();
    };
    return tile;
}());
var background = [[]];
function print_background() {
    for (var x = 0; x < background.length; x++) {
        for (var y = 0; y < background[x].length; y++) {
            background[x][y].print_self();
        }
    }
}
function draw_item_page(type, start) {
    // Display one item per 2 lines, max of 8 on a page
    for (var i = 0; i < 10; i++) {
        if (start + i < inv_data[type].length) {
            var item = inv_data[type][start + i];
            printc(item.name, 1, 2 * i + 8);
            printc(item.value.toString(), 50, 2 * i + 8);
            printc(item.amount.toString(), 65, 2 * i + 8);
            printc(item.desc, 2, 2 * i + 9);
        }
    }
}
function print_inventory(type) {
    clear_screen();
    print_topbar();
    // Draw borders and column info stuff. Probably a better way to do this but whatever. Doesn't get called much.
    if (type == "weapon") {
        printc("Inventory: \\fyWeapons(1)\\fw Hats(2) Shirts(3) Pants(4) Rings(5) Consumables(6)", 0, 5);
    }
    else if (type == 'hat') {
        printc("Inventory: Weapons(1) \\fyHats(2)\\fw Shirts(3) Pants(4) Rings(5) Consumables(6)", 0, 5);
    }
    else if (type == 'shirt') {
        printc("Inventory: Weapons(1) Hats(2) \\fyShirts(3)\\fw Pants(4) Rings(5) Consumables(6)", 0, 5);
    }
    else if (type == 'pants') {
        printc("Inventory: Weapons(1) Hats(2) Shirts(3) \\fyPants(4)\\fw Rings(5) Consumables(6)", 0, 5);
    }
    else if (type == 'ring') {
        printc("Inventory: Weapons(1) Hats(2) Shirts(3) Pants(4) \\fyRings(5)\\fw Consumables(6)", 0, 5);
    }
    else if (type == 'consumable') {
        printc("Inventory: Weapons(1) Hats(2) Shirts(3) Pants(4) Rings(5) \\fyConsumables(6)\\fw", 0, 5);
    }
    printc("Name/Description                                  Value          Amount", 0, 6);
    printc("--------------------------------------------------------------------------------", 0, 7); // I could make this string easier, but it's nice to just see length of it
    if (inv_data[type].length == 0) {
        printc("There's nothing here...", 0, 8);
    }
    else {
        draw_item_page(type, 0);
        printc(">", 0, 8); // Print cursor
    }
    inv_index = 0;
    inv_type = type;
}
function inv_key_manager(event) {
    var num_items = 8;
    function clear_item_page() {
        for (var x = 0; x < SCREEN_X; x++) {
            for (var y = 8; y < SCREEN_Y; y++) {
                set_chr(x, y, ' ', colors.WHITE, colors.BLACK);
            }
        }
    }
    if (event.keyCode == key_codes.ESCAPE) {
        window.removeEventListener('keydown', inv_key_manager);
        print_background();
        old_sidebar = ""; // Forces refresh of sidebar
        lines_to_clear = 25; // Full refresh
        in_inv = false;
        sock.send(JSON.stringify({ type: "inv", data: "exit" }));
    }
    else if (event.keyCode >= '1'.charCodeAt(0) && event.keyCode <= '6'.charCodeAt(0)) {
        print_inventory(["weapon", "hat", "shirt", "pants", "ring", "consumable"][event.keyCode - '1'.charCodeAt(0)]);
    }
    else if (event.keyCode == 'W'.charCodeAt(0) || event.keyCode == key_codes.UP_ARROW) {
        printc(' ', 0, (inv_index % num_items) * 2 + 8); // Remove previous cursor
        // Check if at top of screen
        if (inv_index % num_items) {
            printc('>', 0, (--inv_index % num_items) * 2 + 8);
        }
        else {
            if (inv_index--) {
                draw_item_page(inv_type, inv_index);
                printc('>', 0, (inv_index % num_items) * 2 + 8);
            }
            else {
                clear_item_page();
                if (inv_data[inv_type].length % num_items) {
                    // Draw last page of menu. However many items are there.
                    draw_item_page(inv_type, inv_data[inv_type].length - (inv_data[inv_type].length % num_items));
                    printc('>', 0, (inv_data[inv_type].length % num_items) * 2 + 6);
                }
                else {
                    // Number of total items is a multiple of how many fit
                    // So we need to draw the page before that because blank pages are bad.
                    draw_item_page(inv_type, inv_data[inv_type].length - num_items);
                    printc('>', 0, num_items * 2 + 6); // Draw cursor at end.
                }
                inv_index = inv_data[inv_type].length - 1; // Set index to be the last.
            }
        }
    }
    else if (event.keyCode == "S".charCodeAt(0) || event.keyCode == key_codes.DOWN_ARROW) {
        printc(' ', 0, (inv_index++ % num_items) * 2 + 8);
        if (inv_index != inv_data[inv_type].length) {
            if (inv_index % num_items) {
                printc('>', 0, (inv_index % num_items) * 2 + 8);
            }
            else {
                draw_item_page(inv_type, inv_index);
                printc('>', 0, (inv_index % num_items) * 2 + 8);
            }
        }
        else {
            // Wrap around to start of menu.
            clear_item_page();
            draw_item_page(inv_type, 0);
            printc('>', 0, 8);
            inv_index = 0;
        }
    }
    else if (event.keyCode == key_codes.ENTER && inv_data[inv_type].length) {
        window.removeEventListener('keydown', inv_key_manager);
        sock.send(JSON.stringify({ type: "inv", data: inv_data[inv_type][inv_index].index }));
    }
}
// End helper functions...
var username;
function ask_password(user) {
    username = user;
    printc("Enter your password:", 32, 10);
    echo_text(32, 11, 32, server_connect);
}
var sock;
var ping_int;
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
        }
        catch (e) {
            clear_screen();
            window.removeEventListener('keydown', send_keys);
            window.removeEventListener('keyup', send_keys);
            window.clearInterval(ping_int);
            printc("Error: " + e.message, 0, 10);
        }
    }, 1000); // Message every second so server knows we're still connected
}
var to_clear = [];
var inv_data = {};
var inv_index = 0;
var inv_type = "weapon";
var in_inv = false;
function get_data(event) {
    var data = JSON.parse(event.data);
    // A leading 0 means a regular update
    if (data.type == "update" && !in_inv) {
        // Clear old tiles
        for (var i = 0; i < to_clear.length; i++) {
            to_clear[i].clear_self();
        }
        to_clear = [];
        // And print new ones.
        for (var i = 0; i < data.tiles.length; i++) {
            var print_tile = new tile(data.tiles[i].color, data.tiles[i].chr, data.tiles[i].x, data.tiles[i].y);
            to_clear.push(print_tile);
            print_tile.print_self();
        }
    }
    else if (data.type == "update_extra") {
        update_hp(data.HP, data.maxHP);
        update_mp(data.MP, data.maxMP);
        update_gold(data.gold);
        update_level(data.level);
        update_exp(data.exp);
        update_spell(data.spell);
        update_item(data.item);
        update_sidebar(data.sidebar);
        update_equip(data.weapon, "weapon");
        update_equip(data.hat, "hat");
        update_equip(data.shirt, "shirt");
        update_equip(data.pants, "pants");
        update_equip(data.ring, "ring");
    }
    else if (data.type == "map") {
        for (var x = 0; x < 50; x++) {
            for (var y = 0; y < SCREEN_Y - 5; y++) {
                var bgtile = new background_tile(data.data[y * 50 + x].fgc, data.data[y * 50 + x].bgc, data.data[y * 50 + x].chr, x, y);
                background[x][y] = bgtile;
            }
        }
        if (!in_inv) {
            print_background();
        }
    }
    else if (data.type == "inv") {
        inv_data = data; // Save data for later
        in_inv = true;
        print_inventory(inv_type);
        window.addEventListener("keydown", inv_key_manager);
    }
}
function send_keys(event) {
    // When updating we want to send what key is now down
    // We just send keydown and the value corresponding to the key
    var KEY_MOV_UP = 0;
    var KEY_MOV_LEFT = 1;
    var KEY_MOV_DOWN = 2;
    var KEY_MOV_RIGHT = 3;
    var KEY_ATK_UP = 4;
    var KEY_ATK_LEFT = 5;
    var KEY_ATK_DOWN = 6;
    var KEY_ATK_RIGHT = 7;
    var KEY_ITEM = 8;
    var KEY_SPELL = 9;
    var KEY_ENTER = 10;
    var KEY_UP = 11;
    var KEY_DOWN = 12;
    var KEY_INTERACT = 13;
    var KEY_LASTSPELL = 14;
    var KEY_NEXTSPELL = 15;
    var KEY_INVENTORY = 16;
    var KEY_ESC = 17;
    var keycode_to_send_val = function (keycode) {
        var keycodes_arr = [];
        keycodes_arr['W'.charCodeAt(0)] = KEY_MOV_UP;
        keycodes_arr['A'.charCodeAt(0)] = KEY_MOV_LEFT;
        keycodes_arr['S'.charCodeAt(0)] = KEY_MOV_DOWN;
        keycodes_arr['D'.charCodeAt(0)] = KEY_MOV_RIGHT;
        keycodes_arr['I'.charCodeAt(0)] = KEY_ATK_UP;
        keycodes_arr['J'.charCodeAt(0)] = KEY_ATK_LEFT;
        keycodes_arr['K'.charCodeAt(0)] = KEY_ATK_DOWN;
        keycodes_arr['L'.charCodeAt(0)] = KEY_ATK_RIGHT;
        keycodes_arr[key_codes.SHIFT] = KEY_ITEM;
        keycodes_arr[key_codes.SPACE] = KEY_SPELL;
        keycodes_arr[key_codes.ENTER] = KEY_ENTER;
        keycodes_arr[key_codes.UP_ARROW] = KEY_UP;
        keycodes_arr[key_codes.DOWN_ARROW] = KEY_DOWN;
        keycodes_arr['Q'.charCodeAt(0)] = KEY_UP;
        keycodes_arr['E'.charCodeAt(0)] = KEY_DOWN;
        keycodes_arr['R'.charCodeAt(0)] = KEY_INTERACT;
        keycodes_arr['U'.charCodeAt(0)] = KEY_LASTSPELL;
        keycodes_arr['O'.charCodeAt(0)] = KEY_NEXTSPELL;
        keycodes_arr['V'.charCodeAt(0)] = KEY_INVENTORY;
        keycodes_arr[key_codes.ESCAPE] = KEY_ESC;
        if (keycodes_arr[keycode] == null) {
            throw new RangeError("Unknown key. This error is expected behavior so feel free to ignore it."); // Some random keycode. Throw an error so no packet is send.
        }
        return keycodes_arr[keycode];
    };
    try {
        if (!event.repeat) {
            if (event.type == "keydown") {
                sock.send(JSON.stringify({ type: "keydown", d: keycode_to_send_val(event.keyCode) }));
            }
            else if (event.type == "keyup") {
                sock.send(JSON.stringify({ type: "keyup", d: keycode_to_send_val(event.keyCode) }));
            }
        }
    }
    catch (e) {
        // Let the error go. We don't care as if connection is lost it'll be caught by our ping
    }
}
window.onload = function () {
    // Add listeners for keyboard events to stop random annoying scrolling
    window.addEventListener("keydown", function (event) {
        // Suppress behavior of tab, space, and arrow keys to stop them from moving around the keyboard.
        //  Also backspace so we don't go to previous pages on not Chrome.
        if ([key_codes.TAB, key_codes.SPACE, key_codes.DOWN_ARROW, key_codes.LEFT_ARROW, key_codes.RIGHT_ARROW, key_codes.UP_ARROW, key_codes.BACKSPACE].indexOf(event.keyCode) > -1) {
            event.preventDefault();
        }
    }, false);
    // Init background.
    background = [];
    for (var x = 0; x < 50; x++) {
        background.push([]);
        for (var y = 0; y < SCREEN_Y - 5; y++) {
            background[x].push(new background_tile(colors.WHITE, colors.BLACK, ' ', x, y));
        }
    }
    printc("Welcome to py   !", 33, 7);
    var r_color = Math.round(Math.random());
    var p_color = Math.round(Math.random());
    var g_color = Math.round(Math.random());
    printc("R", 33 + "Welcome to py".length, 7, [colors.RED, colors.YELLOW][r_color]);
    printc("P", 33 + "Welcome to pyR".length, 7, [colors.GREEN, colors.CYAN][p_color]);
    printc("G", 33 + "Welcome to pyRP".length, 7, [colors.BLUE, colors.MAGENTA][g_color]);
    printc("Enter your username", 32, 8);
    echo_text(32, 9, 24, ask_password);
};
//# sourceMappingURL=app.js.map