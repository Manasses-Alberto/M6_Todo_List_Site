document.getElementById('edit-task-fields-btn').addEventListener('click', () => {
    for (let field of document.getElementsByClassName('form-control')) {
        field.removeAttribute('readonly')
    }

    for (let field of document.getElementsByClassName('form-check-input')) {
        field.removeAttribute('disabled')
    }

    document.getElementsByClassName('form-control')[0].focus()
    document.getElementById('edit-task-fields').innerHTML = '<i class="bi bi-floppy-fill"></i>Salvar alterações'
})
