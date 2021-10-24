const fs = require("fs");

let learningHours = 12,
    wantedHour = 28,
    noMas = 6,
    exercise = 7,
    days = 7,
    lWeight = 0.9,
    nWeight = 0.04,
    eWeight = 0.06;

let finalScore =
    (learningHours / wantedHour) * lWeight +
    (noMas / days) * nWeight +
    (exercise / days) * eWeight;

finalScore = parseFloat(finalScore).toFixed(2);


let learningHourScore = parseFloat(learningHours / wantedHour).toFixed(2);
let noMasCore = parseFloat(noMas / days).toFixed(2);
let exerciseScore = parseFloat(exercise / days).toFixed(2);


let document = "learning: ," + learningHours + " / " + wantedHour + " , " + learningHourScore + "\nno mas: ," + noMas + " / " + days + "," + noMasCore + "\nexercise: ," + exercise + " / " + days + "," + exerciseScore + "\nfinal: ," + finalScore;

let doc = `,percent,score\n
           learning hour: ,${learningHours + "/" + wantedHour}, ${learningHourScore}\n
           noMas: ,${noMas + "/" + days}, ${noMasCore}\n
           exercise: ,${exercise + "/" + days}, ${exerciseScore}\n
           final: ,, ${finalScore}\n
           `;

fs.writeFile("test node write.csv", document, () => {
});
