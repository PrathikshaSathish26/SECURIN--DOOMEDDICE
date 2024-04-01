let images = [
    "dice-01.png",
    "dice-02.png",
    "dice-03.png",
    "dice-04.png",
    "dice-05.png",
    "dice-06.png"
];
let dice = document.querySelectorAll("img");

function roll() {
    dice.forEach(function (die) {
        die.classList.add("shake");
    });
    setTimeout(function () {
        dice.forEach(function (die) {
            die.classList.remove("shake");
        });
        let dieOneValue = Math.floor(Math.random() * 6);
        let dieTwoValue = Math.floor(Math.random() * 6);
        console.log(dieOneValue, dieTwoValue);
        document.querySelector("#die-1").setAttribute("src", "assets/" + images[dieOneValue]);
        document.querySelector("#die-2").setAttribute("src", "assets/" + images[dieTwoValue]);
    }, 500); // Reduced the delay to make it smoother
}

  


