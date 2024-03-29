let images=["dice-01.png",
"dice-02.png",
"dice-03.png",
"dice-04.png",
"dice-05.png",
"dice-06.png"];
let dice=document.querySelectorAll("img");

function roll(){
    dice.forEach(function(die){
        die.classList.add("shake");
    });
    setTimeout(function(){
        dice.forEach(function(die){
            die.classList.remove("shake");
        });
        let dieOneValue = Math.floor((Math.random()*(1,6)));
        let dieTwoValue = Math.floor((Math.random()*(1,6)));
        console.log(dieOneValue,dieTwoValue);
        document.querySelector("#die-1").setAttribute("src", images[dieOneValue]);
        document.querySelector("#die-2").setAttribute("src", images[dieTwoValue]);
    },
    1000
    );
}
function undoom() {
    var dieAInput = document.getElementById("die-a-input").value;
    var dieBInput = document.getElementById("die-b-input").value;
    
    // Convert input strings to arrays
    var dieA = dieAInput.split(",").map(Number);
    var dieB = dieBInput.split(",").map(Number);

    // Send POST request to server
    fetch('/undoom', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({dieA: dieA, dieB: dieB})
    })
    .then(response => response.json())
    .then(data => {
        // Display the result
        document.getElementById("result").innerHTML = "New Die A: " + data.newDieA.toString() + "<br>New Die B: " + data.newDieB.toString();
    })
    .catch(error => console.error('Error:', error));
}


