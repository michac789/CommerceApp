document.addEventListener('DOMContentLoaded', () => {
    const itemID = window.location.pathname.split('/')[2]
    const addCartButtonReference = document.querySelector('.add-cart-btn') 
    const addedMessageReference = document.querySelector('.added-message')
    const addToCartBtn = document.querySelector('.add-to-cart-btn')

    fetch ('/api/cart/1').then( response => response.json() ).then( data => {
        console.log(data.map(item => item.item_id ))
        if ( data.map(item => item.item_id ).includes(parseFloat(itemID)) ) {
            addToCartBtn.classList.add("disabled") 
            addToCartBtn.innerHTML = "Added to cart"
        }



    } )    
    addCartButtonReference.addEventListener('click', () => {
        fetch (`/api/cart/${itemID}`, {method: 'PUT'})
            .then(response => response.json())
            .then(data => {
                $(`<div class="alert alert-warning container my-3">Added to cart...</div>`).insertAfter(".item-container")
                addToCartBtn.classList.add("disabled") 
                addToCartBtn.innerHTML = "Added to cart"
            })
    }) 


    
    

})