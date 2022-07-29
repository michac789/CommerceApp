document.addEventListener('DOMContentLoaded', () => {
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
    

    document.querySelectorAll('.bookmark-btn')
        .forEach(button => {
            button.addEventListener('click', () => {
                const itemID = button.dataset.itemId
                const bookmarkReference = document.querySelector('bookmark-${itemID} i')
                console.log(bookmarkReference)
            } 
            )
            console.log(button)

        })
})