
$(document).ready(() => {
    loadMessage(false)
    $("#sendmessage").click(sendMessage)
})

const loadMessage = (animate_last=true) => {
    fetch(`/profile/chats/api/${$("#root")[0].dataset.receiver}`)
    .then(response => response.json())
    .then(result => {
        $("#root")[0].innerHTML = ""  
        const receiver = $("#root")[0].dataset.receiver
        let last_id = 0
        result["chat"].forEach(chat => { 
            if ( receiver == chat.sender ) { 
                $("#root")[0].innerHTML += 
                `<div id=${chat.id} class="mb-3">
                    <div class="d-inline-block border rounded-pill px-2 bg-secondary text-white">
                        ${chat.sender}: ${chat.content} (${chat.time}) <br>
                    </div>
                </div>`
                last_id = chat.id
            } 
            else { 
                $("#root")[0].innerHTML += 
                `
                    <div id=${chat.id} class="text-end mb-3" >
                        <div class="d-inline-block border rounded-pill px-2">
                            ${chat.sender}: ${chat.content} (${chat.time}) <br>
                        </div>
                    </div>`
                last_id = chat.id
            }
          
        })
        if (animate_last) {
            $(`#${last_id}`).hide(0).show(500)
        }
        checkUpdate()
    })
    .catch(error => { $("#root")[0].innerHTML += `Error: ${error}` })
}

const checkUpdate = () => {
    fetch(`/profile/chats/api/${$("#root")[0].dataset.receiver}`, {
        method: "PATCH"
    })
    .then(response => response.json())
    .then(result => {
        if (result["up_to_date"] === false) {
            loadMessage()
        } else {
            checkUpdate()
        }
    })
    .catch(error => { $("#root")[0].innerHTML += `Error: ${error}` })
}

const sendMessage = () => {
    fetch(`/profile/chats/api/${$("#root")[0].dataset.receiver}`, {
        method: "POST",
        body: JSON.stringify({
            content: $("#message")[0].value
        })
    })
    .then(response => response.json())
    .then(result => { 
        // reset the form value
        $("#message")[0].value = ""
        const receiver = $("#root")[0].dataset.receiver

        if ( receiver == result.new.sender ) { 
            $("#root")[0].innerHTML += 
            `<div id=${result.new.id} class="mb-3">
                <div class="d-inline-block border rounded-pill px-2 bg-secondary text-white">
                    ${result.new.sender}: ${result.new.content} (${result.new.time}) <br>
                </div>
            </div>`
        } 
        else { 
            $("#root")[0].innerHTML += 
            `
                <div id=${result.new.id} class="text-end mb-3" >
                    <div class="d-inline-block border rounded-pill px-2">
                        ${result.new.sender}: ${result.new.content} (${result.new.time}) <br>
                    </div>
                </div>`
        } 
        $(`#${result.new.id}`).hide(0).show(500)
    })
    .catch(error => { $("#root")[0].innerHTML += `Error: ${error}` })
}