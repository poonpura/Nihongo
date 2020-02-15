/**
* Module that utilizes the imported verb deconjugator module in JavaScript to
* deconjugate verbs as desired by the frequency dictionary module.
*
* The JavaScript code in this module is run in the shell through the Python
* Naked module.
*
* Author: Pura Peetathawatchai
*/
const Conjugator = require('jp-verbs');

let verb = process.argv[2];
let result = Conjugator.unconjugate(String(verb));
console.log(JSON.stringify(result, null, 2));
