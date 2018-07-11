<?php 
	
	//conexion a la base
	$db = new mysqli( '127.0.0.1', 'root', '', 'luckmap');

	//definimos codificación
	mysqli_set_charset($db, "utf8");

	//definimos zona horaria
	date_default_timezone_set('America/Argentina/Buenos_Aires');
	
?>
