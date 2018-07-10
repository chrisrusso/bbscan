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
    ini_set('mysqli.reconnect', 'on');
	register_shutdown_function('cocaine');
	
	/* Arrancamos el chrome *******************************************************************/
	/******************************************************************************************/
	
	//arrancamos el chrome
	$servidor		= 'http://localhost:4444/wd/hub';
	$condiciones	= DesiredCapabilities::chrome();
	$browser		= RemoteWebDriver::create($servidor, $condiciones, 60000);
	
	/* Seleccionamos lround *******************************************************************/
	/******************************************************************************************/
	
	//buscamos el más nuevo
	$lround = db_ob($db, "
	SELECT		round
	FROM		crawler
	ORDER BY	round desc
	LIMIT		0,1
	");
	
	//si el final round es 0, comenzamos por 1, si el final round no es 0, comenzamos por final round más uno.
	if ($lround == '') { $round = 1; }	else { $round = $lround->round + 1 ; }
	
	//bancamos que arranque chrome
	sleep(10);
	echo "sleep $sleep";

	/* Primera fase de Selenium ***************************************************************/
	/******************************************************************************************/
	
	$primera_ronda = 4000000;
	
	while (1 == 1) {
		
		//round id
		echo "\r\n $round";
			
		// adding cookie
		//$browser->manage()->deleteAllCookies();
		
		//solo la primera vez
		if ($primera_ronda != '') {

			//pedimos la url
			$browser->get("https://www.bustabit.com/game/".$round);
			
			//esperamos que labure
			$sleep = rand(2500000, 4000000);
			$sleep = $sleep + $primera_ronda;
			usleep($sleep);
			echo "\r\n micro sleep $sleep";
			
			//marcamos primera en zero
			$primera_ronda = '';
		
		}
		
		//esperamos que labure
		$sleep = rand(150000, 180000);
		usleep($sleep);
		
		//en vez de esperar al azar, esperamos la presencia de un valor.
		$element = $browser->wait()->until(WebDriverExpectedCondition::presenceOfElementLocated(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/h4')));
		
		/* Buscamos el Game # *********************************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: busqueda de Game";
		
		$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/h4'));
		$info->round = $elem->getText();
		$info->round = str_replace("GAME #","", $info->round);
		
		/* Buscamos el value **********************************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: busqueda de Value";
		
		$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/h5[1]/span[2]'));
		$info->value = $elem->getText();
		$info->value = str_replace("x","", $info->value);
		
		/* Definimos class  ***********************************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: value low or hi";
		
		if ($info->value < 2 ) { $info->class = 'low'; }
		if ($info->value >= 2 ) { $info->class = 'hi'; }
		
		/* Buscamos la fecha de creacion  *********************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: busqueda de fecha de creación";
		
		$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/h5[2]/span[2]'));
		$info->creacion = $elem->getText();
		
		//acomodamos la fecha
		$info->creacion = substr($info->creacion, 5); 
		$info->creacion = substr($info->creacion, 0, -4); 
		$info->creacion = strtotime($info->creacion);
		$info->creacion = date("Y-m-d H:i:s", $info->creacion);
		
		goto cierre;
		
		/* Buscamos winners ***********************************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: busqueda de winners";
		
		$elements = $browser->findElements(WebDriverBy::cssSelector('a.green-color'));
		
		foreach ($elements as $element) {
			$info->players->winners [] = $element->getText();
		}
		
		
		/* Buscamos losers ************************************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: busqueda de losers";
		
		$elements = $browser->findElements(WebDriverBy::cssSelector('a.red-color'));
		
		foreach ($elements as $element) {
			$info->players->losers[] = $element->getText();
		}
		
		/* Hacemos calculos sobre ambos ***********************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: calculos de players";
		
		$info->players->winners_size = sizeof($info->players->winners);
		$info->players->losers_size = sizeof($info->players->losers);
		$info->players->size = $info->players->winners_size + $info->players->losers_size;
		
		$winners_size	= $info->players->winners_size;
		$losers_size	= $info->players->losers_size;
		$players_size	= $info->players->size;
		
		/* Buscamos el dinero de la ronda *********************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: calculos de money";
		
		$elevador = 1;
		
		while ($elevador <= $info->players->size ) {
		
			$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[2]/div/table/tbody/tr['.$elevador.']/td[2]'));
			$money = $elem->getText();
			$money = str_replace(",","", $money);
			$info->money[] = $money;
			
			$elevador++;
		
		}
		
		/* Calculamos el dinero y calculamos la media por usuario *********************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: acomodando variables de money";
		
		$info->money_sum = array_sum($info->money);
		$info->avmoney = $info->money_sum / $info->players->size;
		
		
		/* Enviamos la información a la db ********************************************************/
		/******************************************************************************************/
		
		cierre:
        
        //aca calcular las estadisticas
        //https://www.bustabit.com/statistics
        
        /* Busqueda de valores ********************************************************************/
		/******************************************************************************************/
        /*
        //pedimos la url
        $browser->get("https://www.bustabit.com/statistics");
        
        echo "\r\n Procesos: busqueda de valores";
        
        sleep(2);
        
        //bankroll
        $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div/table/tbody/tr[3]/td[3]'));
		$info->money_bankroll = $elem->getText();
        $info->money_bankroll = substr($info->money_bankroll, 5);
        $info->money_bankroll = str_replace(",","", $info->money_bankroll);
		
        //money_in
        $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div/table/tbody/tr[5]/td[3]'));
		$info->money_in = $elem->getText();
        $info->money_in = substr($info->money_in, 5);
        $info->money_in = str_replace(",","", $info->money_in);
        
        //money_ou
        $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div/table/tbody/tr[6]/td[3]'));
		$info->money_ou = $elem->getText();
        $info->money_ou = substr($info->money_ou, 5);
        $info->money_ou = str_replace(",","", $info->money_ou);
        
        $info->money_diferencia = $info->money_in - $info->money_ou;
        
        //money_inversores
        $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div/table/tbody/tr[7]/td[3]'));
		$info->money_inversores = $elem->getText();
        $info->money_inversores = substr($info->money_inversores, 5);
        $info->money_inversores = str_replace(",","", $info->money_inversores);
        
        //money_comisiones
        $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/main/div[2]/div/table/tbody/tr[8]/td[3]'));
		$info->money_comisiones = $elem->getText();
        $info->money_comisiones = substr($info->money_comisiones, 5);
        $info->money_comisiones = str_replace(",","", $info->money_comisiones);
        
        $info->money_ou_perc = ($info->money_ou * 100) / $info->money_in;
        $info->money_in_perc = 100 - $info->money_ou_perc;
        
        //pedimos la url
        $browser->get("https://www.bustabit.com/game/".$round);
        
        */
		/* Enviamos la información a la db ********************************************************/
		/******************************************************************************************/
        
		echo "\r\n Procesos: enviamos a la db";

		//enviamos la información a la base
		//$db_feedback = db_ask($db, "
		//INSERT IGNORE INTO crawler SET
		//round				= '$info->round',
		//value				= '$info->value',
		//class				= '$info->class',
		//winners			= '$winners_size',
		//losers			= '$losers_size',
		//players			= '$players_size',
		//money				= '$info->money_sum',
		//avmoney			= '$info->avmoney',
		//creacion			= '$info->creacion'
		//");
		
		//enviamos la información a la base
		$db_feedback = db_ask($db, "
		INSERT IGNORE INTO crawler SET
		round				= '$info->round',
		value				= '$info->value',
		class				= '$info->class',
		creacion			= '$info->creacion'
		");
		
		print_r($info);
		
		/* Liberamos variables  *******************************************************************/
		/******************************************************************************************/
		
		echo "\r\n Procesos: liberamos variables";
		
		unset($sleep);
		unset($info);
		unset($winners_size);
		unset($losers_size);
		unset($players_size);
		unset($elem);
		unset($elements);
		
		/* Proximo  *******************************************************************************/
		/******************************************************************************************/
        
		proximo:
		
		//hace click en proximo
		Try {
			//click en proximo
			$elem = $browser->wait(1, 50)->until(WebDriverExpectedCondition::presenceOfElementLocated(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/nav/ul/li[2]/a')));
			$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/nav/ul/li[2]/a'))->click();
		}
		
		//en caso de no haber próximo disponible
		Catch (Exception $e) {
			
			echo "\r\n Procesos: proxima ronda aun no disponible";
			
			//click en previo
			$elem = $browser->wait()->until(WebDriverExpectedCondition::presenceOfElementLocated(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/nav/ul/li[1]/a')));
			$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/nav/ul/li[1]/a'))->click();
			
			//click en proximo
			$elem = $browser->wait()->until(WebDriverExpectedCondition::presenceOfElementLocated(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/nav/ul/li[2]/a')));
			$elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[2]/div[2]/div/div/div[2]/div/div[1]/nav/ul/li[2]/a'))->click();
			
			//vuelve a próximo
			goto proximo;
			
		}
		
		
		//anunciamos
		echo "\r\n Procesos: proxima ronda";
		
		//proxima ronda
		$round++;
		
		
	
	}
	
	/* Cerramos el browser ********************************************************************/
	/******************************************************************************************/

	//cerramos firefox, esperamos
	$browser->quit();
		
?>