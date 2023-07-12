function showPass(elementId, buttonId){
    var card = document.getElementById(elementId);
    var showCard = document.getElementById(buttonId);

    if(card.style.display === "block"){
        card.style.display = "none";
        showCard.classList.replace('bi-eye-slash-fill', 'bi-eye-fill');
    }else{
        card.style.display = "block";
        showCard.classList.replace('bi-eye-fill', 'bi-eye-slash-fill');
    }
}