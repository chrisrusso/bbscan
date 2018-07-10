<?php

	/*
	(1) Hyderabad 2012, Buenos Aires, 2013, Bahrain 2013, Hyderabad 2014
	(2) Resonance fue diseñada para realizar mapas de aplicaciones web
	(3) Localizando e informando fallas en las mismas
	(4) Las cuales podrían exponer información de los usuarios y las empresas responsables
	(5) Revisión Febrero 2014
	(5) Revisión Febrero 2016
	*/
	
	//modafinil: Flushes ob buffers
	include_once("db_link.php");
	
	/********************************************************************************/
	/********** Redefiniciones ******************************************************/
	
	Function adios()						{ die; }
	Function clonazepam()					{ set_time_limit(0); }
	Function diazepam()						{ ignore_user_abort(True); }
	function modafinil() 					{ flush(); ob_flush(); }
	Function walk($where)					{ header("Location: $where"); }
	Function session_rock()					{ session_start(); }
	Function session_clear()				{ session_destroy(); }
	Function session_close()				{ session_write_close(); }
	Function session_user_check($where)		{ if (!$_SESSION['user']) { walk($where); } }
	
	/********************************************************************************/
	/********** Funciones de verdad *************************************************/
	
    Function heroin() {
		
		//leemos el error final
		$error_final = error_get_last();
		
		//si el error final fue e_error
		if (!is_null($error_final) && $error_final['type'] === E_ERROR) {
		
			error_log( "Terminal error! Inicio de cocaine() handler..." );
			
			//definimos el operador php
			$operador_php	= "C:\Users\chris_000\Desktop\curl\alpha.php";
			
			error_log( "Definiendo operador double_phase.php" );
			
			//informamos
			error_log( "Lanzando nuevo operador double_phase, cierre de cocaine()..." );
			
			//armamos una cadena de descripción
			$descripcion = array(
			0 => array("pipe", "r"),
			1 => array("pipe", "w"),
			2 => array("file", "proc_open_errors", "a+")
			);
			
			//lanazamos de nuevo el mismo operador
			$command = "start /min php $operador_php";
			$process = proc_open($command, $descripcion, $pipe);
			
			//esperamos a la creación del recurso
			if (is_resource($process)) {
				print_r($process);
				sleep(5);
				fclose($pipe[0]);
				fclose($pipe[1]);
				$process_response = proc_close($process);
				echo $process_response;
			}
			
			//cerramos
			die;
		
		}
	}
    
	Function cocaine() {
		
		//leemos el error final
		$error_final = error_get_last();
		
		//si el error final fue e_error
		if (!is_null($error_final) && $error_final['type'] === E_ERROR) {
		
			error_log( "Terminal error! Inicio de cocaine() handler..." );
			
			//definimos el operador php
			$operador_php	= "C:\Users\chris_000\Desktop\curl\curl.php";
			
			error_log( "Definiendo operador double_phase.php" );
			
			//informamos
			error_log( "Lanzando nuevo operador double_phase, cierre de cocaine()..." );
			
			//armamos una cadena de descripción
			$descripcion = array(
			0 => array("pipe", "r"),
			1 => array("pipe", "w"),
			2 => array("file", "proc_open_errors", "a+")
			);
			
			//lanazamos de nuevo el mismo operador
			$command = "start /min php $operador_php";
			$process = proc_open($command, $descripcion, $pipe);
			
			//esperamos a la creación del recurso
			if (is_resource($process)) {
				print_r($process);
				sleep(5);
				fclose($pipe[0]);
				fclose($pipe[1]);
				$process_response = proc_close($process);
				echo $process_response;
			}
			
			//cerramos
			die;
		
		}
	}
	
	Function posicion($fichero) {
	$posicion = realpath($fichero);
	return $posicion;
	}

	Function deliver($cadena) {
	$cadena = Json_encode($cadena, True);
	echo $cadena;
	}

	Function mamarachear($fichero, $mamarracho) {
	$procesador = fopen($fichero,"a");
	fwrite($procesador, $mamarracho);
	fclose($procesador);
	}

	Function db_ask($db_link, $ask) {
	$feedback = mysqli_query($db_link, $ask)or die(mysqli_error($db_link));
	return $feedback;
	}

	Function db_ob($db_link, $ask) {
	$feedback = mysqli_fetch_object(mysqli_query($db_link, $ask));
	return $feedback;
	}

	Function db_ob_all($db_link, $ask) {
	$feedback = mysqli_query($db_link, $ask);
	while ($row = mysqli_fetch_object($feedback)) { $value[] = $row; }
	return $value;
	}

	Function db_assoc($db_link, $ask) {
	$feedback = mysqli_query($db_link, $ask);
	while ($row = mysqli_fetch_assoc($feedback)) { $value[] = $row; }
	return $value;
	}

	Function db_fill_row($db_link, $ask, $row_name) {
	$run = mysqli_query($db_link, $ask);
	while ($row = mysqli_fetch_assoc($run)) { $feedback[] = $row[$row_name]; }
	return $feedback;
	}

	Function db_assoc_one($db_link, $ask) {
	$feedback = mysqli_fetch_assoc(mysqli_query($db_link, $ask));
	return $feedback;
	}

	Function db_num($db_link, $ask) {
	$feedback = mysqli_num_rows($db_link, $ask);
	return $feedback;
	}

	Function db_one($db_link, $ask) {
	$feedback = mysqli_result(mysqli_query($db_link, $ask),0);
	return $feedback;
	}

	Function deliver_mail($desde, $hacia, $email_header, $email_body) {

	$headers[] = "MIME-Version: 1.0";
	$headers[] = "Content-type: text/html; charset=\"UTF-8\"";
	$headers[] = "From: $desde";
	$headers[] = "Reply-To: $desde";

	mail($hacia, $email_header, $email_body, implode("\n", $headers));
	}
	
	function array_orderby() {
		
	$args = func_get_args();
	$data = array_shift($args);
	foreach ($args as $n => $field) {
		if (is_string($field)) {
		$tmp = array();
		foreach ($data as $key => $row)
		$tmp[$key] = $row[$field];
		$args[$n] = $tmp;
		}
	}
	$args[] = &$data;
	call_user_func_array('array_multisort', $args);
	return array_pop($args);
	}

	
?>