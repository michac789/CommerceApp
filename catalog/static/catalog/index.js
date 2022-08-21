document.addEventListener('DOMContentLoaded', () => {  

    // for time-based filtering
    $("#flexRadioWeek").change(function() {
        let tmp = window.location.href 
        let timeQueryParameter; 
        if (tmp.includes("time")){
            timeQueryParameter = tmp.match(/time=[^&]*(?=&)/)[0]  
            tmp = tmp.replace(timeQueryParameter + "&", "") 
        }
        if (this.checked) {  
            window.location.href = tmp + (tmp.includes("?") ? "" : "?") + "time=7&"
        } 



    })
    $("#flexRadioMonth").change(function() {
        let tmp = window.location.href 
        let timeQueryParameter; 
        if (tmp.includes("time")){
            timeQueryParameter = tmp.match(/time=[^&]*(?=&)/)[0]
            tmp = tmp.replace(timeQueryParameter + "&", "")
        }
        if (this.checked) { 
            window.location.href = tmp + (tmp.includes("?") ? "" : "?") + "time=30&"
        } 


    })
    $("#flexRadioYear").change(function() {
        let tmp = window.location.href 
        let timeQueryParameter; 
        if (tmp.includes("time")){
            timeQueryParameter = tmp.match(/time=[^&]*(?=&)/)[0]
            tmp = tmp.replace(timeQueryParameter + "&", "")
        }
        if (this.checked) { 
            window.location.href = tmp + (tmp.includes("?") ? "" : "?") + "time=365&"
        } 
    })


    // for price form 
    document.querySelector(".price-range-form").addEventListener("submit", function (event) { 
        event.preventDefault();
        const min = document.querySelector('#min-price').value
        const max = document.querySelector('#max-price').value
        let tmp = window.location.href  
        // if no query 
        tmp = tmp + (tmp.includes("?") ? "" : "?")
        if ( tmp.includes('price') ) { 
            const priceQueryParameter = tmp.match(/price=[^&]*(?=&)/)[0]
            tmp = tmp.replace(priceQueryParameter + "&", "") 
            tmp += `price=${min}-${max}&`  
            console.log(tmp)
            window.location.href = tmp 
        } else {
            tmp += `price=${min}-${max}&` 
            console.log(tmp)
            window.location.href = tmp 
        }

    })


    // show bookmarked item feature
    $("#bookmark").change(function() {
        const tmp = window.location.href
        if (this.checked) {
            window.location.href = tmp + (tmp.includes("?") ? "" : "?") + "bookmarked=t&"
        } else {
            const x = tmp.split('bookmarked=t&')
            window.location.href = x[0] + (x[1] ? x[1] : "")
        }
    })  


    // for category (only clothing)
    $("#flexCheckClothing").change(function() {
        const tmp = window.location.href 
        if(this.checked){ 
            let tmp = window.location.href  
            // if no query 
            tmp = tmp + (tmp.includes("?") ? "" : "?")
            
            // if there's a current category inside there case
            if ( tmp.includes('category') ){  

                const categoryQueryParameter = tmp.match(/category=[^&]*(?=&)/)[0]
                tmp = tmp.replace(categoryQueryParameter + "&", "") 
                window.location.href = tmp + categoryQueryParameter + "_CL&"   
            } else { 
                window.location.href = tmp + "category=CL&" 
            }
        } else { 
            const categoryQueryParameterValues = tmp.match(/(?=category=)[^&]*(?=&)/)  
            if ( categoryQueryParameterValues.includes('_') ) { 
                tmp = tmp.replace("_CL", "")
            } else { 
                tmp = tmp.replace("category=CL&", "")
            }
            window.location.href = tmp 
        }
    })


    // Hover for the frame
    let cards = document.querySelectorAll(".card");
    // initializing
    cards.forEach(card =>  
        card.style.border = "hidden"
    )
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


    // pagination 
    // const paginationNavReference = document.querySelector('.pagination')
    // const numberOfPages = paginationNavReference.dataset.paginationNumber 
    // console.log(paginationNavReference)

    // for( let i = 1; i <= numberOfPages; i++) {
    //     paginationNavReference.innerHTML += `
    //     <li class="page-item">
    //         <a class="page-link" href="/catalog?page=${i}" aria-label="Previous">
    //             <span aria-hidden="true">${i}</span>
    //         </a>
    //     </li> 
        
    //     `

    // }
    
    




})