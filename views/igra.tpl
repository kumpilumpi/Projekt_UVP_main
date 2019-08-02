% import model 

<!DOCTYPE html>
<html>
    <style>
        .center {text-align: center;}
        /* th, td {padding: 5px;} */
        table, th, td {border: 1px solid black; table-layout:fixed;}
        #velika {height: 315px; width: 315px; text-align: center; margin: auto; position: relative;}
        .mala {border-collapse: collapse; height: 100px; width: 100px;}        
    </style>


<body>

    <h1 class='center' >The ultimate game</h1>
    
<!------------ Zacetek tabele ------------>
    <p>
    <table id='velika'>

    <!-- Prva vrstica -->
        <tr>
% for mreza in range(3):
            <td>

                <table class='mala'>
    % for row in igra.velika_mreza[mreza]:
                    <tr>
        % for i in row:
                        <td> {{i}} </td>
        % end
                    </tr>
    % end
                </table>
            </td>
%end
        </tr>
    <!-- Konec prva vrstica -->
    
    <!-- Druga vrstica -->    
        <tr>
% for mreza in range(3, 6):
            <td>
    
                <table class='mala'>
    % for row in igra.velika_mreza[mreza]:
                    <tr>
        % for i in row:
                        <td> {{i}} </td>
        % end
                    </tr>
    % end
                </table>
            </td>
%end
        </tr>
        <!-- Konec druga vrstica -->

        <!-- Tretja vrstica -->
        <tr>
% for mreza in range(6, 9):
            <td>
    
                <table class='mala'>
    % for row in igra.velika_mreza[mreza]:
                    <tr>
        % for i in row:
                        <td> {{i}} </td>
        % end
                    </tr>
    % end
                </table>
            </td>
%end
        </tr>
    </p>
<!------------ Konec tabele ------------>


<!------------ Star način tiskanja mreže ------------>
        <!-- <p> {{igra.mala_mreza_0[0]}} | {{igra.mala_mreza_1[0]}} | {{igra.mala_mreza_2[0]}} </p>
        <p> {{igra.mala_mreza_0[1]}} | {{igra.mala_mreza_1[1]}} | {{igra.mala_mreza_2[1]}} </p>
        <p> {{igra.mala_mreza_0[2]}} | {{igra.mala_mreza_1[2]}} | {{igra.mala_mreza_2[2]}} </p>
        <hr>
        <p> {{igra.mala_mreza_3[0]}} | {{igra.mala_mreza_4[0]}} | {{igra.mala_mreza_5[0]}} </p>
        <p> {{igra.mala_mreza_3[1]}} | {{igra.mala_mreza_4[1]}} | {{igra.mala_mreza_5[1]}} </p>
        <p> {{igra.mala_mreza_3[2]}} | {{igra.mala_mreza_4[2]}} | {{igra.mala_mreza_5[2]}} </p>
        <hr>
        <p> {{igra.mala_mreza_6[0]}} | {{igra.mala_mreza_7[0]}} | {{igra.mala_mreza_8[0]}} </p>
        <p> {{igra.mala_mreza_6[1]}} | {{igra.mala_mreza_7[1]}} | {{igra.mala_mreza_8[1]}} </p>
        <p> {{igra.mala_mreza_6[2]}} | {{igra.mala_mreza_7[2]}} | {{igra.mala_mreza_8[2]}} </p> -->
<!------------ Star način tiskanja mreže ------------>

<br>

    <hr>

<!-- Ne izpisuje vsakič napake -->

% if slaba: 

    <p class='center'>Neveljavna poteza!</p>
    <p class='center'>Poskusite ponovno.</p>    

% end 
    
   

% if zmaga:

    % igra.naslednji()
    <h1 class='center'> Zmagal je igralec {{igra.navrsti}} </h1>
    <p>Čestitamo za zmago !!!!!</p>


% elif naslednja == 10:

    <p class='center'> Na potezi je {{igra.navrsti}} </p>
    
    <p class='center'>
    <form action="/igra/{{id_igre}}/" method="post">
        Mreža: <input type="text" name = "mreza">
        Vrsta: <input type="text" name = "vrsta">
        Stolpec: <input type="text" name = "stolpec">
        <button type="submit">Pošlji ugib!</button>
    </form>
    </p>

% else:

    <p class='center'> Na potezi je {{igra.navrsti}} </p>

    <p class='center'>Igrate v mrežo <b>{{naslednja}}</b></p>
    <p class='center'>
    <form action="/igra/{{id_igre}}/" method="post">
        Vrsta: <input type="text" name = "vrsta">
        Stolpec: <input type="text" name = "stolpec">
        <button type="submit">Pošlji ugib!</button>
    </form>
    </p>

% end
    


  
</body>

</html>