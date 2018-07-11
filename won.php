<?php

	/* Preparamos la información para Selenium ************************************************/
	/******************************************************************************************/
	
	//definimos namespace
	namespace Facebook\WebDriver;

	//clases de webdriver
	use Exception;
	use Facebook\WebDriver\Remote\RemoteWebDriver;
	use Facebook\WebDriver\Remote\DesiredCapabilities;
	
    comienzo:
    
    /* Revision horaria ***********************************************************************/
	/******************************************************************************************/
    
    //definimos la hora
    date_default_timezone_set('UTC');
    $ahora = strtotime("now");
    $ahora = strftime('%H:%M', $ahora);
    
    //predefinimos el off
    $params->sys = 'off';
    
    //buscamos las 00:00, 16:00, 13:00, 08:00
    if ($ahora >= "00:00" and $ahora < "01:02") { echo "\r\n Informacion: [00] o'clock"; $params->sys = 'on'; }
    if ($ahora >= "15:58" and $ahora < "17:02") { echo "\r\n Informacion: [16] o'clock"; $params->sys = 'on'; }
    if ($ahora >= "12:58" and $ahora < "14:02") { echo "\r\n Informacion: [13] o'clock"; $params->sys = 'on'; }
    if ($ahora >= "07:58" and $ahora < "09:02") { echo "\r\n Informacion: [08] o'clock"; $params->sys = 'on'; }
    
    echo "\r\n No ahora ($ahora)...";
    
    if ($params->sys == 'on') {
	
        /* 2. Preparamos la mesa para la cena *****************************************************/
        /******************************************************************************************/
        
        //inclusiones
        require_once('vendor/autoload.php');
        require_once("reserved/db_link.php");
        require_once("reserved/funciones.php");
        
        //no rush
        clonazepam();
        
        //enviamos los errores a php_errors
        ini_set("log_errors", E_ALL);
        ini_set("error_log", "php_errors");
        
        /* Arrancamos el chrome *******************************************************************/
        /******************************************************************************************/
        
        //arrancamos el chrome
        $servidor		= 'http://localhost:4444/wd/hub';
        $condiciones	= DesiredCapabilities::chrome();
        $browser		= RemoteWebDriver::create($servidor, $condiciones, 60000);
        
        /* Definimos variables ********************************************************************/
        /******************************************************************************************/
        
        //variables ancladas
        $player->perdida_maxima     = 8;
        $player->posicion_inicial   = 100;
        $params->salida		        = 100;
        $player->username           = 'chrusso';
        $player->password           = 'KCCqHhdfuf';
        
        //variables dinamicas
        $player->ganancias          = 0;
        $player->perdidas           = 0;
        $player->posicion           = $player->posicion_inicial;
        $player->ronda              = 1;
        $player->espera             = 'off';
        
        //bancamos que arranque chrome
        $sleep = rand(3000000, 3200000);
        usleep($sleep);
        echo "\r\n esperando...";
        
        //acomodamos dimensiones
        $browser->manage()->window()->maximize();
        
        

        /* Acceso *********************************************************************************/
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
        
        //keyword on
        $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[4]/div/div/button/span[2]'))->click();
        
        /* Avisamos el comienzo *******************************************************************/
        /******************************************************************************************/
        
        echo "\r\n  Inicializando...";
        
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
            
            //si es la primera vez o no espera feedback
            if ($player->espera == 'off' ) {
                    
                $elem = $browser->wait(600, 1000)->until(WebDriverExpectedCondition::elementToBeClickable(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/div[1]/span/input')));
                
                //seleccionamos
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/div[1]/span/input'))->click();
                
                //es necesario eliminar así la información para evadir errores serios
                $elem->sendKeys(array(WebDriverKeys::CONTROL, 'a'));
                $elem->sendKeys("$player->posicion;");
                usleep(300000);
                
                //seleccionamo
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[2]/div[2]/span/input'))->click();
                
                //es necesario eliminar así la información para evadir errores serios
                $elem->sendKeys(array(WebDriverKeys::CONTROL, 'a'));
                $elem->sendKeys("1000");
                usleep(300000);
                
                //enviamos
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[1]/div[2]/div/div/div/div/form/div[3]'))->click();
                
                //informamos
                echo "\r\n  Mandamos $player->posicion! al round #$info->nxround_id";
                
                $player->lhash = $info->lround_hash;
                $player->espera = 'on';
                $player->accion = 'on';
                $player->ronda++;
                
                //esperamos
                sleep(1);
                
            }
            
            //revisamos si ya apareció el concluyo la ronda 
            if ($player->lhash != $info->lround_hash && $player->accion == 'on') {
                
                //buscamos el hash de la posicion
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[5]/input'));
                $player->posicion_hash	= $elem->getAttribute('value');
                
                //buscamos el valor del lround
                $elem = $browser->findElement(WebDriverBy::xpath('//html/body/div[1]/div/div/div/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div/div/table/tbody/tr[1]/td[1]/a'));
                $player->posicion_value	= $elem->getText();
                $player->posicion_value = $info->lround_value;
                
                //sacamos la espera
                $player->espera = 'off';
                
                //revisamos si perdimos
                if ($player->posicion_value < 1000) {
                    
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
                    
                    $player->referencia = "Valor: $player->posicion_value. Perdimos round #$info->lround_id. Ganancias: $player->ganancias. Posicion: $player->posicion. Perdidas: $player->perdidas. Dinero: $player->dinero";
                    
                    $db_feedback = db_ask($db, "
                    INSERT IGNORE INTO performance SET
                    round				= '$info->lround_id',
                    dinero				= '$player->dinero',
                    ganancias			= '$player->ganancias',
                    posicion			= '$player->posicion',
                    perdidas			= '$player->perdidas',
                    referencia			= '$player->referencia'
                    ");
                    
                    echo "\r\n $player->referencia";
                    
                }
                
                //revisamos si perdimos
                if ($player->posicion_value >= 1000) {
                    
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
                    $player->ganancias = $player->ganancias + ($player->posicion * 1000);
                    
                    /* Informamos *****************************************************************************/
                    /******************************************************************************************/
                    
                    $player->referencia = "Valor: $player->posicion_value. Ganamos round #$info->lround_id. Ganancias: $player->ganancias. Posicion: $player->posicion_inicial. Perdidas: $player->perdidas. Dinero: $player->dinero";
                    
                    $db_feedback = db_ask($db, "
                    INSERT IGNORE INTO performance SET
                    round				= '$info->lround_id',
                    dinero				= '$player->dinero',
                    ganancias			= '$player->ganancias',
                    posicion			= '$player->posicion',
                    perdidas			= '$player->perdidas',
                    referencia			= '$player->referencia'
                    ");
                    
                    echo "\r\n $player->referencia";
                    
                    /* Acomodamos posición ********************************************************************/
                    /******************************************************************************************/
                    
                    $player->posicion = $player->posicion_inicial;
                    
                }
                
                /* Revision horaria ***********************************************************************/
                /******************************************************************************************/
                
                //definimos la hora
                date_default_timezone_set('UTC');
                $ahora = strtotime("now");
                $ahora = strftime('%H:%M', $ahora);
                
                //predefinimos el off
                $params->sys = 'off';
                
                //buscamos las 00:00, 16:00, 13:00, 08:00
                if ($ahora >= "00:00" and $ahora < "01:02") { $params->sys = 'on'; }
                if ($ahora >= "15:59" and $ahora < "17:01") { $params->sys = 'on'; }
                if ($ahora >= "12:59" and $ahora < "14:01") { $params->sys = 'on'; }
                if ($ahora >= "07:59" and $ahora < "09:01") { $params->sys = 'on'; }
                    
                //si perdemos 7
                if ($params->sys == 'off') {
                    
        
                    //calculamos espera
                    echo "\r\n  Se ha alcanzado un maximo. Esperamos...";
                    
                    //reiniciamos
                    $player->posicion = $player->posicion_inicial;
                    $player->perdidas = 0;
                    $player->ganancias = 0;
                    
                    /* Cerramos el browser ********************************************************************/
                    /******************************************************************************************/

                    //cerramos firefox, esperamos
                    $browser->quit();
                    
                    /* Volvemos a empezar *********************************************************************/
                    /******************************************************************************************/
                    Goto comienzo;
                    
                }
                
                //volvemos a poner accion en off
                $player->accion = 'off';
                $player->lhash = $info->lround_hash;
                
            }
        
        }
    
    }
    
    /* Volvemos a empezar *********************************************************************/
    /******************************************************************************************/
    
    sleep(20);
    Goto comienzo;
		
?>