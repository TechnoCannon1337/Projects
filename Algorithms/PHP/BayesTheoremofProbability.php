<body>
<?php
//Baye's Theorem is used to calculate probailities of events based on prior knowledge
function BayesProbability($A, $B)
{
    $FirstEvent = $A;
    $SecondEvent = $B;
    $MarginofError = (1-$SecondEvent);
    $Unaffected = (1-$FirstEvent);
    $Probability = (($FirstEvent*$SecondEvent)/(($FirstEvent*$SecondEvent)+($Unaffected*$MarginofError)));
    print round($FirstEvent*100, 0, PHP_ROUND_HALF_UP) . " percent of the population have been diagnosed for Technophobia using a test with " . round($SecondEvent*100, 0, PHP_ROUND_HALF_UP) . " percent accuracy and a " . round($MarginofError*100, 0, PHP_ROUND_HALF_UP) . " percent margin of error, which means there's a " . round($Probability*100,0, PHP_ROUND_HALF_UP) ." percent probability that you may also suffer from Tehcnophobia.<p> On a positive note, however " . round($Unaffected*100, 0, PHP_ROUND_HALF_UP) . " percent of our Cyber Citizens are most likely to be Source Code Fanatics! <p> CyberNation: Code or DIY!";
    return $Probability;
}

BayesProbability(.05, .9);
?>
</body>
