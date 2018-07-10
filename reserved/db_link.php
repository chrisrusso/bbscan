<?php 
	
	//conexion a la base
	//$db = new mysqli( '70.32.96.145', 'chris', 'zbxzbxzbx??zbxcnb?77', 'luckmap' );
    $db = new mysqli( '127.0.0.1', 'usr', 'psw', 'bb_ocr');

	//definimos codificación
	mysqli_set_charset($db, "utf8");

	//definimos zona horaria
	date_default_timezone_set('America/Argentina/Buenos_Aires');
	
?>
