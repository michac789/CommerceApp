document.addEventListener('DOMContentLoaded', () => {
    const itemID = window.location.pathname.split('/')[2]
    const addCartButtonReference = document.querySelector('.add-cart-btn') 
    const addedMessageReference = document.querySelector('.added-message') 
    // Why error? while there's error checking there in DOMContentLoaded :(
    if ( !addCartButtonReference ) { 
        addCartButtonReference.addEventListener('click', () => {
            fetch (`/api/cart/${itemID}`, {method: 'PUT'})
                .then(response => response.json())
                .then(data => 
                    $(`<div class="alert alert-warning container my-3">Added to cart...</div>`).insertAfter(".item-container")
                    )
        })
    }

})