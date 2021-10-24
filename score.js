const fs = require('fs')

let learningHours = 12;
let wantedHour = 28;
let noMas = 6;
let exercise = 7;
let days = 7;


let lWeight = 0.8;
let nWeight = 0.05;
let eWeight = 0.15;

console.log("learning: " + learningHours + " / " + wantedHour + " = " + parseFloat(learningHours / wantedHour).toFixed(2));
console.log("no mas: " + noMas + " / " + days + " = " + parseFloat(noMas / days).toFixed(2));
console.log("exercise: " + exercise + " / " + days + " = " + parseFloat(exercise / days).toFixed(2));

let res = (learningHours / wantedHour) * lWeight + (noMas / days) * nWeight + (exercise / days) * eWeight
res = parseFloat(res).toFixed(2)


console.log("final: " + parseFloat(res).toFixed(2))


fs.writeFile('test node write.csv',
    "learning: ," + learningHours + " / " + wantedHour + " = " + parseFloat(learningHours / wantedHour).toFixed(2) + "\n" +
    "no mas: ," + noMas + " / " + days + " = " + parseFloat(noMas / days).toFixed(2) + "\n" +
    "exercise: ," + exercise + " / " + days + " = " + parseFloat(exercise / days).toFixed(2) +"\n"+
    "final: ," + res
    , 
    
    () => {
        // console.log("save success");
    }
)