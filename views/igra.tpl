% import model 

<!DOCTYPE html>
<html>
    <style>
        table, th, td {
            border: 1px solid black;
         }        
    </style>


<body>

    <h1>The ultimate game</h1>
    

    <!-- <table style="width:100%">
        <tr>
          <td><p>{{igra.mala_mreza_0[0]}}</p>
            <p>{{igra.mala_mreza_0[1]}}</p>
            <p>{{igra.mala_mreza_0[2]}}</p>
          </td>
          <td><p>{{igra.mala_mreza_1[0]}}</p>
            <p>{{igra.mala_mreza_1[1]}}</p>
                <p>{{igra.mala_mreza_1[2]}}</p>
          </td> 
          <td><p>{{igra.mala_mreza_2[0]}}</p>
            <p>{{igra.mala_mreza_2[1]}}</p>
                <p>{{igra.mala_mreza_2[2]}}</p>
          </td>
        </tr>
        <tr>
          <td>{{igra.mala_mreza_3[0]}}
              {{igra.mala_mreza_3[1]}}
              {{igra.mala_mreza_3[2]}}

          </td>
          <td>Smith</td> 
          <td>50</td>
        </tr>
        <tr>
          <td>Eve</td>
          <td>Jackson</td> 
          <td>94</td>
        </tr>
    </table> -->




        <p> {{igra.mala_mreza_0[0]}} | {{igra.mala_mreza_1[0]}} | {{igra.mala_mreza_2[0]}} </p>
        <p> {{igra.mala_mreza_0[1]}} | {{igra.mala_mreza_1[1]}} | {{igra.mala_mreza_2[1]}} </p>
        <p> {{igra.mala_mreza_0[2]}} | {{igra.mala_mreza_1[2]}} | {{igra.mala_mreza_2[2]}} </p>
        <hr>
        <p> {{igra.mala_mreza_3[0]}} | {{igra.mala_mreza_4[0]}} | {{igra.mala_mreza_5[0]}} </p>
        <p> {{igra.mala_mreza_3[1]}} | {{igra.mala_mreza_4[1]}} | {{igra.mala_mreza_5[1]}} </p>
        <p> {{igra.mala_mreza_3[2]}} | {{igra.mala_mreza_4[2]}} | {{igra.mala_mreza_5[2]}} </p>
        <hr>
        <p> {{igra.mala_mreza_6[0]}} | {{igra.mala_mreza_7[0]}} | {{igra.mala_mreza_8[0]}} </p>
        <p> {{igra.mala_mreza_6[1]}} | {{igra.mala_mreza_7[1]}} | {{igra.mala_mreza_8[1]}} </p>
        <p> {{igra.mala_mreza_6[2]}} | {{igra.mala_mreza_7[2]}} | {{igra.mala_mreza_8[2]}} </p>



    <hr>

% if not slaba: 

    <p>Neveljavna poteza!</p>
    <p>Poskusite ponovno.</p>    

% end 
    
   

% if zmaga:

    % igra.naslednji()
    
    <h1> Zmagal je igralec {{igra.navrsti}} </h1>




% elif naslednja == 10:
    <p> Na potezi je {{igra.navrsti}} </p>

    <form action="/igra/{{id_igre}}/" method="post">
        Mreža: <input type="text" name = "mreza">
        Vrsta: <input type="text" name = "vrsta">
        Stolpec: <input type="text" name = "stolpec">
        <button type="submit">Pošlji ugib!</button>
    </form>

% else:
    <p> Na potezi je {{igra.navrsti}} </p>

    <p>Igrate v mrežo {{naslednja}}</p>
    <form action="/igra/{{id_igre}}/" method="post">
        Vrsta: <input type="text" name = "vrsta">
        Stolpec: <input type="text" name = "stolpec">
        <button type="submit">Pošlji ugib!</button>
    </form>

% end
    


  
</body>

</html>