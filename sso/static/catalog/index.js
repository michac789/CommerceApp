let cards = document.querySelectorAll(".card");

cards.forEach(card =>  
    card.addEventListener("mouseover", () => 
        card.style.border = null
    )

)


cards.forEach(card =>  
    card.addEventListener("mouseout", () => 
        card.style.border = "hidden"
    )

)



