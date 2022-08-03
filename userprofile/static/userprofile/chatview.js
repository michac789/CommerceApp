$(document).ready(() => {
    loadMessage(false)
    $("#sendmessage").click(sendMessage)
})

const loadMessage = (animate_last=true) => {
    fetch(`/profile/chats/api/${$("#username")[0].innerHTML}`)
    .then(response => response.json())
    .then(result => {
        $("#root")[0].innerHTML = ""
        let last_id = 0
        result["chat"].forEach(chat => {
            $("#root")[0].innerHTML += `<span id=${chat.id}>
                ${chat.sender}: ${chat.content} (${chat.time}) <br>
            </span>`
            last_id = chat.id
        })
        if (animate_last) {
            $(`#${last_id}`).hide(0).show(500)
        }
        checkUpdate()
    })
    .catch(error => { $("#root")[0].innerHTML += `Error: ${error}` })
}

const checkUpdate = () => {
    fetch(`/profile/chats/api/${$("#username")[0].innerHTML}`, {
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
    fetch(`/profile/chats/api/${$("#username")[0].innerHTML}`, {
        method: "POST",
        body: JSON.stringify({
            content: $("#message")[0].value
        })
    })
    .then(response => response.json())
    .then(result => {
        $("#message")[0].value = ""
        $("#root")[0].innerHTML += `<span id=${result.new.id}>
            ${result.new.sender}: ${result.new.content} (${result.new.time}) <br>
        </span>`
        $(`#${result.new.id}`).hide(0).show(500)
    })
    .catch(error => { $("#root")[0].innerHTML += `Error: ${error}` })
}