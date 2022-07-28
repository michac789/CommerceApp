document.addEventListener('DOMContentLoaded', () => {
    const cartReference = document.querySelector('.cart')  

    fetch('/api/cart/1')
        .then(response => response.json())
        .then(data => data.forEach(item => 
            cartReference.innerHTML +=
                `<li class="list-group-item d-flex justify-content-between lh-sm">
                <div>
                    <h6 class="my-0">${item.item_title}</h6>
                    <small class="text-muted"></small>
                </div>
                <span class="text-muted">$13</span>
                </li>`
            )
        )
})