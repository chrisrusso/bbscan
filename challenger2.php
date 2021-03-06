<?php

	/* 1. Preparamos la información para Selenium *********************************************/
	/******************************************************************************************/
	
	//definimos namespace
	namespace Facebook\WebDriver;
	
	//clases de webdriver
	use Exception;
	use Facebook\WebDriver\Remote\RemoteWebDriver;
	use Facebook\WebDriver\Remote\DesiredCapabilities;
	
	//incluimos el loader
	require_once('vendor/autoload.php');
	
	/* 2. Preparamos la mesa para la cena *****************************************************/
	/******************************************************************************************/
	
	//inclusiones
	include_once("reserved/db_link.php");
	include_once("reserved/funciones.php");
	
	//no rush
	clonazepam();
	
	//enviamos los errores a php_errors
	ini_set("log_errors", E_ALL);
	ini_set("error_log", "php_errors");
	//register_shutdown_function('cocaine');
	
	/* Arrancamos el chrome *******************************************************************/
	/******************************************************************************************/
	
	//arrancamos el chrome
	$servidor		= 'http://localhost:4444/wd/hub';
	$condiciones	= DesiredCapabilities::chrome();
	$browser		= RemoteWebDriver::create($servidor, $condiciones, 60000);
	
	/* Definimos variables ********************************************************************/
	/******************************************************************************************/
	
	//definimos la posición inicial fuera del bucle.
	$player->ganancias = 0;
	$player->perdidas = 0;
	$player->posicion_inicial = 1;
	$player->posicion = $player->posicion_inicial;
	$player->ronda = 1;
	$player->username = 'chrusso';
	$player->password = 'KCCqHhdfuf';
    $player->xvalue_inicial = 2;
    $player->xvalue = $player->xvalue_inicial;
	
	//bancamos que arranque chrome
	$sleep = rand(3000000, 3200000);
	usleep($sleep);
	echo "\r\n esperando... \r\n ";
	
	//acomodamos dimensiones
	$browser->manage()->window()->maximize();

	/* Primera fase de Selenium ***************************************************************/
	/******************************************************************************************/
	
	//pedimos la url
	$browser->get("https://www.bustabit.com/login/");
	
	//esperamos el form
	$elem = $browser->wait()->until(WebDriverExpectedCondition::presenceOfElementLocated(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/span/input')));
	
	//llenamos el username
	$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[1]/div/span/input'))->sendKeys($player->username);
	
	//llenamos el password
	$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[1]/div[2]/div/span/input'))->sendKeys($player->password);
	
	//click para enviar
	$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/form/div[2]/button'))->click();
	
	sleep(3);
	
	//esperamos la presencia de los records
	$elem = $browser->wait()->until(WebDriverExpectedCondition::presenceOfElementLocated(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[1]/div/ul/li[2]/a')));
	
	//click en los records
	$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[1]/div/ul/li[2]/a'))->click();
	
	//solo para refinar
	//sleep(10); die;
	
	//keyword on
	//$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[4]/div/div/button/span[2]'))->click();
	
	/* Avisamos el comienzo *******************************************************************/
	/******************************************************************************************/
	
	echo "\r\n  Inicializando... \r\n";
	
	while (1 == 1) {
		
		/* Supervisión ****************************************************************************/
		/******************************************************************************************/
		
		//slower
		$sleep = rand(2000000, 2200000);
		usleep($sleep);
		
		//buscamos el valor del lround
		$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a'));
		$info->lround_value	= $elem->getText();
		$info->lround_value = substr($info->lround_value, 0, -2);
		
		//buscamos el id del lround
		$info->lround_id	= $elem->getAttribute('href');
		$info->lround_id	= str_replace("https://www.bustabit.com/game/","", $info->lround_id);
		
		//buscamos el hash de lround
		$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/input'));
		$info->lround_hash	= $elem->getAttribute('value');
		
		//calculamos el número final
		$info->lround_lnumber = substr($info->lround_id, -1);
		
		//calculamos el número final del próximo round
		$info->nxround_id = $info->lround_id + 1;
		$info->nxround_lnumber = $info->lround_lnumber + 1;
		
		//si es la primera vez
		if ($player->ronda == 1 || $player->espera == 'off' ) {
			
			//buscamos las condiciones para comenzar
			//if ( $info->nxround_lnumber == '1' || $info->nxround_lnumber == '3' || $info->nxround_lnumber == '7' || $info->nxround_lnumber == '9' ) {
				
				$player->lhash = $info->lround_hash;
				$player->espera = 'on';
				$player->accion = 'on';
				$player->ronda++;
				
				//informamos
                echo "\r\n  Mandamos $player->posicion! al round #$info->nxround_id \r\n";
                
                $elem = $browser->wait(120, 2000)->until(WebDriverExpectedCondition::elementToBeClickable(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/div[1]/span/input')));
                
                //seleccionamos
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/div[1]/span/input'));
                
                //es necesario eliminar así la información para evadir errores serios
                $elem->sendKeys(array(WebDriverKeys::CONTROL, 'a'));
                $elem->sendKeys("$player->posicion");
                usleep(100000);
                
                $elem = $browser->wait(120, 2000)->until(WebDriverExpectedCondition::elementToBeClickable(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/div[2]/span/input')));
                
                echo "\r\n  Xvalue disponible, llenando informacion."; 
                
                //es necesario eliminar así la información para evadir errores serios
                $elem->sendKeys(array(WebDriverKeys::CONTROL, 'a'));
                $elem->sendKeys("$player->xvalue");
                usleep(100000);
                
                echo "\r\n  Enviando."; 
                
                //enviamos
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[3]'))->click();
				
			//}
			
		}
		
		//revisamos si ya apareció el resultado 
		if ($player->lhash != $info->lround_hash && $player->accion == 'on') {
			
			//buscamos el hash de la posicion
			$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/input'));
			$player->posicion_hash	= $elem->getAttribute('value');
			
			//buscamos el valor del lround
			$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a'));
			$player->posicion_value	= $elem->getText();
			$player->posicion_value = substr($info->lround_value, 0, -2);
			
			//sacamos la espera
			$player->espera = 'off';
			
			//revisamos si perdimos
			if ($player->posicion_value < $player->xvalue) {
				
				/* Revisamos dinero ***********************************************************************/
				/******************************************************************************************/
				
				//buscamos el dinero
				$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[2]/nav/div/div[2]/ul[2]/li[2]/a/span'));
				$player->dinero	= $elem->getText();
				$player->dinero = substr($player->dinero, 6);
				$player->dinero = str_replace(",","", $player->dinero);
				
				/* Recalculamos ***************************************************************************/
				/******************************************************************************************/
				
				//calculamos ganancias
				$player->perdidas++;
				$player->ganancias = $player->ganancias - $player->posicion;
				
				/* Informamos *****************************************************************************/
				/******************************************************************************************/
				
				$player->referencia = "Perdimos round #$info->lround_id. Ganancias: $player->ganancias. Posicion: $player->posicion. Perdidas: $player->perdidas. Dinero: $player->dinero";
				
				$db_feedback = db_ask($db, "
				INSERT INTO performance SET
				round				= '$info->lround_id.',
				dinero				= '$player->dinero',
				ganancias			= '$player->ganancias',
				posicion			= '$player->posicion',
				perdidas			= '$player->perdidas',
				referencia			= '$player->referencia'
				");
				
				echo "\r\n $player->referencia \r\n";
				
				/* Acomodamos posición ********************************************************************/
				/******************************************************************************************/
				
				$player->posicion = $player->posicion;
                $player->xvalue++;
				
				/* Reiniciamos (if needed) ****************************************************************/
				/******************************************************************************************/
				
				//si perdemos 7
				//if ($player->perdidas == 7) {
					
					//$player->posicion = $player->posicion_inicial * 10;
					//$player->perdidas = 0;
					
					//echo "\r\n  Se ha alcanzado un máximo. Comenzamos de nuevo... \r\n";
					
				//}
				
			}
			
			//revisamos si perdimos
			if ($player->posicion_value >= $player->xvalue) {
				
				/* Revisamos dinero ***********************************************************************/
				/******************************************************************************************/
				
				//buscamos el dinero
				$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[2]/nav/div/div[2]/ul[2]/li[2]/a/span'));
				$player->dinero	= $elem->getText();
				$player->dinero = substr($player->dinero, 6);
				$player->dinero = str_replace(",","", $player->dinero);
				
				/* Recalculamos ***************************************************************************/
				/******************************************************************************************/
				
				//calculamos ganancias
				$player->perdidas = 0;
				$player->ganancias = $player->ganancias + $player->posicion;
				
				/* Informamos *****************************************************************************/
				/******************************************************************************************/
				
				$player->referencia = "Ganamos round #$info->lround_id. Ganancias: $player->ganancias. Posicion: $player->posicion_inicial. Perdidas: $player->perdidas. Dinero: $player->dinero";
				
				$db_feedback = db_ask($db, "
				INSERT INTO performance SET
				round				= '$info->lround_id.',
				dinero				= '$player->dinero',
				ganancias			= '$player->ganancias',
				posicion			= '$player->posicion',
				perdidas			= '$player->perdidas',
				referencia			= '$player->referencia'
				");
				
				echo "\r\n $player->referencia \r\n";
				
				/* Acomodamos posición ********************************************************************/
				/******************************************************************************************/
				
				$player->posicion   = $player->posicion_inicial;
                $player->xvalue     = $player->xvalue_inicial;
				
			}
			
			$player->accion = 'off';
			$player->lhash = $info->lround_hash;
			
		}
	
	}
	
	/* Cerramos el browser ********************************************************************/
	/******************************************************************************************/

	//cerramos firefox, esperamos
	$browser->quit();
		
?>