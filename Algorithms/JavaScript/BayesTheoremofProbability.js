//Baye's Theorem is used to calculate probailities of events based on prior knowledge
function BayesProbability($A, $B)
{
    var $FirstEvent = $A;
    var $SecondEvent = $B;
    var $MarginofError = (1-$SecondEvent);
    var $Unaffected = (1-$FirstEvent);
    var $Probability = (($FirstEvent*$SecondEvent)/(($FirstEvent*$SecondEvent)+($Unaffected*$MarginofError)));
    console.log(($FirstEvent*100).toFixed(0) + " percent of the population have been diagnosed for Technophobia using a test with " + ($SecondEvent*100).toFixed(0) + " percent accuracy and a " + ($MarginofError*100).toFixed(0) + " percent margin of error, which means there's a " + ($Probability*100).toFixed(0) + " percent probability that you may also suffer from Tehcnophobia. \n \n  On a positive note, however " + ($Unaffected*100).toFixed(0) + " percent of our Cyber Citizens are most likely to be Source Code Fanatics! \n CyberNation: Code or DIY!");
    return $Probability;
}

BayesProbability(.05, .9);
