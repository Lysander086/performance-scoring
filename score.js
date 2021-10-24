const fs = require("fs");

let learningHours = 12,
    wantedHour = 28,
    noMas = 6,
    exercise = 7,
    days = 7,
    lWeight = 0.8,
    nWeight = 0.05,
    eWeight = 0.15;

let res =
    (learningHours / wantedHour) * lWeight +
    (noMas / days) * nWeight +
    (exercise / days) * eWeight;

res = parseFloat(res).toFixed(2);


let document = "learning: ," + learningHours + " / " + wantedHour + " , " + parseFloat(learningHours / wantedHour).toFixed(2) + "\nno mas: ," + noMas + " / " + days + "," + parseFloat(noMas / days).toFixed(2) + "\nexercise: ," + exercise + " / " + days + "," + parseFloat(exercise / days).toFixed(2) + "\nfinal: ," + res;

fs.writeFile("test node write.csv", document, () => {
});
