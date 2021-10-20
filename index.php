<html>
 <head>
  <meta charset="UTF-8">
  <title>Brute Force</title>
 </head>
 <body>
  <form method="post">
   <table align="center">
    <tr>
     <th>
      BruteForce WebPage   
     </th>
    </tr>
    <tr>
     <td>
      User:
     </td>
     <td>
      <input type="text" name="user">
     </td>
    </tr>
    <tr>
     <td>
      Password:
     </td>
     <td>
      <input type="password" name="password">
     </td>
    </tr>
    <tr>
     <td>
      <input type="submit" value="Login" name="login">
     </td>
    </tr>
   </table>
  </form>
 </body>
</html>
<?php
    if(isset($_POST["login"]))
    {
        $realUser = "manolo";
        $realPassword = "1234";
        $user = $_POST["user"];
        $password = $_POST["password"]; 
        if($realUser == $user AND $realPassword == $password)
        {
            echo "<center>Congratulations!!! :-)</center>";
        }
    }
?>
