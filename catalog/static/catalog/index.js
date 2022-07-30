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
    fetch('api/bookmark/1')
        .then(response => response.json())
        .then(data => {
            document.querySelectorAll('.bookmark-btn')
                .forEach(button => {
                    const itemID = button.dataset.itemId 
                    if (data.length == 0){
                        button.innerHTML = '<i class="bi bi-bookmark"></i>'
                    }
                    else { 
                        // NEED TO BE CONVERTED TO STRING FOR ARRAY OF ID! CAUTION SINCE DATA IS RECEIVED IN STRING DATATYPE
                        const arrayOfID = data.map(element => JSON.stringify(element.item_id))
                        if (arrayOfID.includes(itemID)) {
                            button.innerHTML = '<i class="bi bi-bookmark-fill"></i>'
                        }
                        else { 
                            button.innerHTML = '<i class="bi bi-bookmark"></i>'
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
                    fetch(`api/bookmark/${itemID}`, {method: 'DELETE'})
                        .then(response => response.json())
                        .then(data => {return})
                }
                else { 
                    button.innerHTML = '<i class="bi bi-bookmark-fill"></i>'
                    fetch(`api/bookmark/${itemID}`, {method: 'PUT'})
                        .then(response => response.json())
                        .then(data => {return})
                }
            } 
            )

        })


    
    




})