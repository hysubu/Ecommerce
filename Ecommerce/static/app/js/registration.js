
// Custom regestration alidation ......... 

function valid_password(){
    var pssword = document.getElementById('pass').value
    if(pssword.length != 8 ){
        document.getElementById("sub").innerHTML = pssword
        alert("docummm")
    }
    else{
        var msg = "Bhal Bsdk "
        document.getElementById("sub").innerHTML = msg
        alert("docc")
    }
  
  } 

  