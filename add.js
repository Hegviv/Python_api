function sendPost(){
    const data = JSON.stringify({
        nev: document.getElementById("nev").value,
        suly: document.getElementById("suly").value,
        nem: document.getElementById("nem").value,
        magassag: document.getElementById("magassag").value
      });
      
      navigator.sendBeacon('http://127.0.0.1:5000/savedetails/', data);
      console.log(data);
    }