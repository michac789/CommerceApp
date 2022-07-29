document.addEventListener('DOMContentLoaded', () => { 
    const cartReference = document.querySelector('.cart')  
    const itemCounterReference = document.querySelector('span.item-counter') 
    const itemCounterWrapperReference = document.querySelector('h4.item-counter-wrapper') 
    fetch('/api/cart/1')
        .then(response => response.json())
        .then(data => {
            if(data.length == 0) { 
                itemCounterWrapperReference.innerHTML += 
                    '<p class="lead fw-300 pt-5">Your cart is empty...</p>'  
            } 
            else { 
                itemCounterWrapperReference.innerHTML = `
                    <span class="text-primary">Your cart</span>
                    <span class="badge bg-primary rounded-pill item-counter ms-3">${data.length}</span>
                ` 
                data.forEach(item => 
                cartReference.innerHTML +=
                    `<li class="list-group-item d-flex justify-content-between lh-sm cart-item-${item.item_id}">
                    <div>
                        <h6 class="my-0">
                            <a class="text-secondary" href="../catalog/${item.item_id}">
                                ${item.item_title}
                            </a>

                            <button  data-item-id="${item.item_id}" class="remove-cart-${item.item_id}-btn btn remove-btn"><i class="bi bi-trash"></i></button>
                            </h6> 
                            <small class="text-muted"></small> 
                    </div>
                    <span class="text-muted">$13</span>
                    </li>` 
                )
                const itemID = document.querySelectorAll('button.remove-btn').forEach((button) => {
                    button.addEventListener('click', () => {
                        fetch (`/api/cart/${button.dataset.itemId}`, {method : 'DELETE'})
                            .then(response => response.json())
                            .then(data => 
                                $(`<div class="alert alert-warning container my-3">Item removed from cart...</div>`).insertAfter(".cart-container-wrapper")
                                )
                            .then(() => {
                                const deletedItem = document.querySelector(`.cart-item-${button.dataset.itemId}`) 
                                deletedItem.remove()
                            })
                    })
                })



            }
        }
        )
      


        
})

// 
//                 