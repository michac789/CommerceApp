document.addEventListener('DOMContentLoaded', () => { 
    const cartReference = document.querySelector('.cart')  
    const itemCounterReference = document.querySelector('span.item-counter') 
    const itemCounterWrapperReference = document.querySelector('h4.item-counter-wrapper') 
    fetch('/api/cart/1')
        .then(response => response.json())
        .then(data => {
            console.log(data)
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
                    `<li class="list-group-item d-flex justify-content-between lh-sm">
                    <div>
                        <h6 class="my-0">${item.item_title}</h6>
                        <small class="text-muted"></small>
                    </div>
                    <span class="text-muted">$13</span>
                    </li>` 
                
                )
            }
        }
        )
})

// 
//                 