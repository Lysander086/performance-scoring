const fs = require("fs");
let fileName = "report.csv";

fs.rmSync(fileName, {
    force: true,
});


let focusHours = 24,
    hardWantedHours = 3,
    noMas = 5,
    exercise = 4,
    days = 7,
    lWeight = 0.8,
    nWeight = 0.04,
    eWeight = 0.16;

let ultimateScore = (focusHours / hardWantedHours) * lWeight +
    (noMas / days) * nWeight +
    (exercise / days) * eWeight;

ultimateScore = parseFloat(ultimateScore).toFixed(2);

let learningScore = parseFloat(`${focusHours / hardWantedHours}`).toFixed(2);
let noMasCore = parseFloat(`${noMas / days}`).toFixed(2);
let exerciseScore = parseFloat(`${exercise / days}`).toFixed(2);


let doc =
    `,percent ,score ,weight
learning hour: ,${focusHours + " | " + hardWantedHours}, ${learningScore}, ${lWeight}
noMas: ,${noMas + " | " + days},${noMasCore}, ${nWeight}
exercise: ,${exercise + " | " + days},${exerciseScore}, ${eWeight}
final: , , , ${ultimateScore} (h)`;

fs.writeFile(fileName, doc, () => {
    console.log("Report generated.");
});

