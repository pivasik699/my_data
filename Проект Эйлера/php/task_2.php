<?php

	$arr = [];
	$f = [1,2];
	array_push($arr,$f[1]);
	while(true){
		$f[0] = $f[0] + $f[1];
		if($f[0] % 2 == 0){
			array_push($arr,$f[0]);
		}
		$f[1] = $f[0] + $f[1];
		if($f[1] % 2 == 0){
			array_push($arr,$f[1]);
		}
		print_r ($arr);
		if($f[0] >= 4000000){
			break;
		}
		elseif($f[1] >= 4000000){
			break;
		}
	}
	$sum = array_sum($arr);
	echo $sum;
?>