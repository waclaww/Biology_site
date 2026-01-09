document.addEventListener('click',(e) =>
    {
        let elementID = e.target.id;
        if(elementID == "alertCloseButton"){
            document.getElementById("alertMain").style.display = "none";
        }
        if(elementID == "alertMain"){
            document.getElementById("alertMain").style.display = "none";
        }
        if(elementID == "alertBody"){
            document.getElementById("alertMain").style.display = "none";
        }
    }
);