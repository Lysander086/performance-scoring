const fs = require("fs");
let fileName = "test node write.csv";

fs.rmSync(fileName, {
    force: true,
});


let learningHours = 14,
    wantedHour = 19,
    hardWantedHours = 28,
    noMas = 5,
    exercise = 5,
    days = 7,
    lWeight = 0.8,
    nWeight = 0.04,
    eWeight = 0.16;

let finalScore =
    (learningHours / wantedHour) * lWeight +
    (noMas / days) * nWeight +
    (exercise / days) * eWeight;

let hardFinal = (learningHours / hardWantedHours) * lWeight +
    (noMas / days) * nWeight +
    (exercise / days) * eWeight;

finalScore = parseFloat(finalScore).toFixed(2);
hardFinal = parseFloat(hardFinal).toFixed(2);


let learningHourScore = parseFloat(learningHours / wantedHour).toFixed(2);
let noMasCore = parseFloat(noMas / days).toFixed(2);
let exerciseScore = parseFloat(exercise / days).toFixed(2);


let doc =
    `,percent ,score ,weight
learning hour: ,${learningHours + " | " + wantedHour},${learningHourScore}, ${lWeight}
noMas: ,${noMas + " | " + days},${noMasCore}, ${nWeight}
exercise: ,${exercise + " | " + days},${exerciseScore}, ${eWeight}
final: , ,${hardFinal} ,${finalScore}`;

fs.writeFile(fileName, doc, () => {
});
