var last_clicked = [];
const ignore_arr = ["AC", "Ans", "Inv", "x\u00b2", "x!", "x\u02b8", "x<sup>y</sup>"];
const add_brack_arr = ["sin", "cos", "tan", "log\u2081\u2080", "ln", "\u221a"];
const btn_char_length = {
    "sin": 4,
    "cos": 4,
    "tan": 4,
    "log\u2081\u2080": 6,
    "log\u2093": 4,
    "ln": 3,
    "\u221a": 2
}

window.addEventListener('load', function () {
    const button_wrapper = document.getElementById("all_buttons");
    const input_field = document.getElementById("user_input");
    button_wrapper.addEventListener('click', (event) => {
    const is_button = event.target.nodeName === "BUTTON";
    if (!is_button) {
        return;
    }
    const clicked_btn = event.target.innerHTML;
    if (clicked_btn == "\u2b05") {
        return erase_chars (input_field);
    }
    if (clicked_btn == "AC") {
        input_field.innerHTML = "";
    }

    if (ignore_arr.includes(clicked_btn)) {
        return;
    }

    if (add_brack_arr.includes(clicked_btn)) {
        input_field.innerHTML += clicked_btn + "(";
        last_clicked.push(clicked_btn);
        return;
    }
    input_field.innerHTML += clicked_btn;

    last_clicked.push(clicked_btn);
    console.log(last_clicked);
    })
})

function erase_chars (input_field) {
    var num_chars_to_erase = 1;
    if (last_clicked[last_clicked.length - 1] in btn_char_length) {
        num_chars_to_erase = btn_char_length[last_clicked[last_clicked.length - 1]];
    }
    input_field.innerHTML = input_field.innerHTML.substring(0, input_field.innerHTML.length -  num_chars_to_erase);
    last_clicked.pop(last_clicked[-1]);
    console.log(last_clicked);
    return;
}