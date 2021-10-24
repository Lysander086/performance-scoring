const fs = require("fs");
let fileName = "test node write.csv";

fs.rmSync(fileName, {
    force: true,
});


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


let doc =
    `,percent,score
learning hour: ,${learningHours + " | " + wantedHour},${learningHourScore}
noMas: ,${noMas + " | " + days},${noMasCore}
exercise: ,${exercise + " | " + days},${exerciseScore}
final: , ,${finalScore}`;

fs.writeFile(fileName, doc, () => {
});
