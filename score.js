// This code is creating a report in a CSV file. It is calculating a score based on the number of hours spent focusing, the number of days of noMas, and the number of days of exercise. The score is calculated by taking the ratio of focus hours to hard wanted hours, multiplied by a weight, and adding the ratio of noMas days to total days, multiplied by a weight, and adding the ratio of exercise days to total days, multiplied by a weight. The final score is then written to the CSV file.
const fs = require("fs");
let fileName = "report.csv";

fs.rmSync(fileName, {
    force: true,
});

// try to interpret the below code
let focusHours = 13.75,
    hardWantedHours =  30,
    noMas = 4,
    exercise = 9,
    lWeight = 0.8,
    nWeight = 0.04,
    eWeight = 0.16;

let days = 7;

const exerciseTimes = 4 + 10;

let ultimateScore = (focusHours / hardWantedHours) * lWeight +
    (noMas / days) * nWeight +
    (exercise / exerciseTimes) * eWeight;

ultimateScore = parseFloat(ultimateScore).toFixed(2);

let learningScore = parseFloat(`${focusHours / hardWantedHours}`).toFixed(2);
let noMasCore = parseFloat(`${noMas / days}`).toFixed(2);
let exerciseScore = parseFloat(`${exercise / exerciseTimes}`).toFixed(2);


let doc =
    `,percent ,score ,weight
learning hour: ,${focusHours + " | " + hardWantedHours}, ${learningScore}, ${lWeight}
noMas: ,${noMas + " | " + days},${noMasCore}, ${nWeight}
exercise: ,${exercise + " | " + exerciseTimes},${exerciseScore}, ${eWeight}
final: , , , ${ultimateScore} (h)`;

fs.writeFile(fileName, doc, () => {
    console.log("Report generated.");
});

