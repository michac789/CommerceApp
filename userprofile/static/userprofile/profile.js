document.addEventListener('DOMContentLoaded', () => {
    const avatarTextReference = document.querySelector('.avatar-text') 
    avatarTextReference.innerText = avatarTextReference.dataset.name[0].toUpperCase()
})