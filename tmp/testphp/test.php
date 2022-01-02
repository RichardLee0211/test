<?php

/* from: https://www.tutorialspoint.com/php/php_operator_types.htm
 */

// echo "Hello PHP!!!!!";

/*
	$d = date("D");

	switch ($d){
	case "Mon":
	   echo "Today is Monday";
	   break;

	case "Tue":
	   echo "Today is Tuesday";
	   break;

	case "Wed":
	   echo "Today is Wednesday";
	   break;

	case "Thu":
	   echo "Today is Thursday";
	   break;

	case "Fri":
	   echo "Today is Friday";
	   break;

	case "Sat":
	   echo "Today is Saturday";
	   break;

	case "Sun":
	   echo "Today is Sunday";
	   break;

	default:
	   echo "Wonder which day is this ?";
	}

   $channel =<<<_XML_

   <channel>
      <title>What's For Dinner</title>
      <link>http://menu.example.com/ </link>
      <description>Choose what to eat tonight.</description>
   </channel>
   _XML_;

   echo <<<END
   This uses the "here document" syntax to output multiple lines with variable
   interpolation. Note that the here document terminator must appear on a line with
   just a semicolon. no extra whitespace!


   END;

   print $channel;
*/



print(__LINE__); print("\n");
print(__FILE__); print("\n");

// if(TRUE){
if(FALSE){
	print("something");
}
elseif(TRUE){
	print("something03");
}
else{
	print("something02");
}

?>
<html>

<?php

/*
$array = array( 1, 2, 3, 4, 5);

foreach( $array as $value ) {
	echo "Value is $value <br />";
}
*/


         /* First method to associate create array. */
         $salaries = array("mohammad" => 2000, "qadir" => 1000, "zara" => 500);

         // echo "Salary of mohammad is ". $salaries['mohammad'] . "<br />";
         // echo "Salary of qadir is ".  $salaries['qadir']. "<br />";
         // echo "Salary of zara is ".  $salaries['zara']. "<br />";

         // print("Salary of mohammad is ". $salaries['mohammad'] . "<br />");

         /* Second method to create array. */
         $salaries['mohammad'] = "high";
         $salaries['qadir'] = "medium";
         $salaries['zara'] = "low";

         // echo "Salary of mohammad is ". $salaries['mohammad'] . "<br />";
         // echo "Salary of qadir is ".  $salaries['qadir']. "<br />";
         // echo "Salary of zara is ".  $salaries['zara']. "<br />";


         $marks = array(
            "mohammad" => array (
               "physics" => 35,
               "maths" => 30,
               "chemistry" => 39
            ),

            "qadir" => array (
               "physics" => 30,
               "maths" => 32,
               "chemistry" => 29
            ),

            "zara" => array (
               "physics" => 31,
               "maths" => 22,
               "chemistry" => 39
            )
         );

         /* Accessing multi-dimensional array values */
/*
         echo "Marks for mohammad in physics : " ;
         echo $marks['mohammad']['physics'] . "<br />";

         echo "Marks for qadir in maths : ";
         echo $marks['qadir']['maths'] . "<br />";

         echo "Marks for zara in chemistry : " ;
         echo $marks['zara']['chemistry'] . "<br />";
*/

   $variable = "name";
   $literally = 'My $variable will not print!\\n';

   print($literally);
   print "<br />";

   $literally = "My $variable will print!\\n";

   print($literally);

   echo strlen("Hello world!");
   echo strpos("Hello world!","world");
?>



</html>
