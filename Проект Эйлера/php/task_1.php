<?php
$x = 1000;
$i = 0;
$y = 0;
$z = [];
while($i <= $x){
	$i+=3;
	array_push($z,$i);
	if($i == 999){
		break;
	}
}
while($y <= $x){
	$y+=5;
	array_push($z,$y);
	if( $y == 995){
		break;
	}
}
$result = array_unique($z);
$result = array_sum($result);
print_r($result);