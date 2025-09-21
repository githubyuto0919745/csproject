const display = document.getElementById("display");

function appendDisplay(input){
    display.value += input;
}

function clearDisplay(){
    display.value = "";
}
function calculate(){
    display.value = eval(display.value);
}
function removeDisplay(){
    display.textContent = display.textContent.slice(0,-1);
    if(display.textContent === ""){
        display.textContent = "0";
    }
}

document.addEventListener("keydown", function(event){
    const key = event.key;

    if(!isNaN(key)){
        appendDisplay(key);
    }
    else if (key ==="+" || key ==="-" || key ==="*" || key ==="/" || key =="."){
        appendDisplay(key);
    }
    else if (key === "Enter"){
        calculate();
    }
    else if (key === "Backspace"){
        removeDisplay();
    }
    else if (key === "Delete"){
        clearDisplay();
    }

    
});