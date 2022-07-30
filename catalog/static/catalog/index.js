document.addEventListener('DOMContentLoaded', () => {
    // Hover for the frame
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

    // To fetch the initial state of bookmarking 
    
    document.querySelectorAll('.bookmark-btn')
        .forEach(button => {
            const itemID = button.dataset.itemId 
            fetch('api/bookmark/1')
                .then(response => response.json())
                .then(data => {
                    if (data.length == 0){
                        button.innerHTML = '<i class="bi bi-bookmark"></i>'
                    }
                    else { 
                        const arrayOfID = data.map(element => element.id)
                        if (arrayOfID.includes(itemID)) {
                            button.innerHTML = '<i class="bi bi-bookmark-fill"></i>'
                        }
                        else { 
                            button.innertHTML = '<i class="bi bi-bookmark"></i>'
                        }
                    }
                    }
                )
            })
        


    // For toggling function in bookmark-btn 
    document.querySelectorAll('.bookmark-btn')
        .forEach(button => {
            button.addEventListener('click', (event) => { 
                event.preventDefault()
                const itemID = button.dataset.itemId
                const bookmarkReference = document.querySelector(`.bookmark-${itemID} i`)
                if ( bookmarkReference.classList.contains('bi-bookmark-fill') ){ 
                    button.innerHTML = '<i class="bi bi-bookmark"></i>'
                    fetch(`api/bookmark/${itemID}`, {METHOD: 'DELETE'})
                        .then(response => response.json())
                        .then(data => console.log(data))
                }
                else { 
                    button.innerHTML = '<i class="bi bi-bookmark-fill"></i>'
                    fetch(`api/bookmark/${itemID}`, {METHOD: 'PUT'})
                        .then(response => response.json())
                        .then(data => console.log(data))
                }
            } 
            )

        })


    
    




})