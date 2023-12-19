document.getElementById('edit-task-fields-btn').addEventListener('click', () => {
    for (let field of document.getElementsByClassName('form-control')) {
        field.removeAttribute('readonly')
    }

    for (let field of document.getElementsByClassName('form-check-input')) {
        field.removeAttribute('disabled')
    }

    document.getElementsByClassName('form-control')[0].focus()
    document.getElementById('edit-task-fields-btn').innerHTML = '<i class="bi bi-floppy-fill"></i>Salvar alterações'
    document.getElementById('edit-task-fields-btn').setAttribute('id', 'save-task-fields-btn')
    document.getElementById('save-task-fields-btn').addEventListener('click', () => {
        document.getElementById('submit-task-form').click()
    })    
})

const delete_task_btn = document.getElementById('delete-task-btn')
delete_task_btn.addEventListener('click', () => {
    location.href = `/task/delete/${delete_task_btn.getAttribute('data-bs-target')}/`
})

document.getElementById('status-radio').addEventListener('change', () => {
    if (document.getElementById('status-radio').checked) {
        document.getElementById('status-radio').value = 'TRUE'
    } else {
        document.getElementById('status-radio').value = 'FALSE'
    }
})
