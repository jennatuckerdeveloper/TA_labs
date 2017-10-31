var score = 0;
var level = 1;
var lives = 5;
var playing = false;

var start = document.getElementById("start");
var scoreDisplay = document.getElementById("score-display");
var cells = document.querySelectorAll(".cell");
var getCells = null;

var intervalTiming = 5000;

function displayScore() {
    levelUp();
    scoreDisplay.innerHTML = "Score: " + score + "<span id='level-display'> Level: " + level + "</span><span id='lifes-display'> Lives: " + lives + "</span>";

}

function levelUp() {
    level = Math.max(Math.floor(score / 10), 1);

}

function randomCell() {
    return Math.floor(Math.random() * 16);

}

function gameOver() {
    if (lives === 0) {
        clearInterval(getCells);
        score = 0;
        level = 1;
        lives = 5;
        playing = false;
    }
}

function increaseSpeed() {
    if (getCells === null) {
        console.log("START  Every 5 seconds.");
        highlightCell();
        getCells = setInterval(highlightCell, intervalTiming);
    }
    setInterval(function () {
        clearInterval(getCells);
        intervalTiming -= 1000;
        console.log("Now every " + intervalTiming / 1000 + "seconds");
        getCells = setInterval(highlightCell, intervalTiming);

    }, 10000)
}

function highlightCell() {
    var target = randomCell();
    var prevScore = score;
    console.log("running", target);
    cells[target].style.backgroundImage = "url(https://files.slack.com/files-tmb/T0PQYS509-F7D0HMWLU-153117d43e/mole_360.jpg)";
    setTimeout(function () {
        cells[target].style.backgroundImage = "url(https://files.slack.com/files-tmb/T0PQYS509-F7E1GDMPH-646bd12a08/hole_360.jpg)";
        if (score === prevScore) {
            lives--;
            displayScore();
            gameOver();
        }
    }, 2000)
}

start.addEventListener("click", function () {
    if (!playing) {
        playing = true;
        displayScore();
        increaseSpeed();
    }
});

for (var i = 0; i < cells.length; i++) {
    cells[i].addEventListener("click", function () {
        if (playing) {
            if (this.style.backgroundImage === "url(\"https://files.slack.com/files-tmb/T0PQYS509-F7D0HMWLU-153117d43e/mole_360.jpg\")") {
                score++;
                this.style.backgroundImage = "url(https://files.slack.com/files-tmb/T0PQYS509-F7E1GDMPH-646bd12a08/hole_360.jpg)";
            }
            displayScore();
        }
    })
}