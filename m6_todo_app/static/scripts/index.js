document.getElementById('add-new-task-btn').removeAttribute('disabled')

document.getElementById('save-task-btn').addEventListener('click', () => {
    document.getElementById('submit-new-task').click()
})

const nav_links = document.getElementsByClassName('nav-link')
nav_links[0].addEventListener('click', () => {
    if (nav_links[0].classList.contains('active') == false) {
        nav_links[0].classList.add('active')
        nav_links[1].classList.remove('active')
        nav_links[2].classList.remove('active')
        document.getElementsByClassName('tasks-display')[0].style.display = 'block'
        document.getElementsByClassName('tasks-display')[1].style.display = 'none'
        document.getElementsByClassName('tasks-display')[2].style.display = 'none'
    }
})

nav_links[1].addEventListener('click', () => {
    if (nav_links[1].classList.contains('active') == false) {
        nav_links[1].classList.add('active')
        nav_links[0].classList.remove('active')
        nav_links[2].classList.remove('active')
        document.getElementsByClassName('tasks-display')[1].style.display = 'block'
        document.getElementsByClassName('tasks-display')[0].style.display = 'none'
        document.getElementsByClassName('tasks-display')[2].style.display = 'none'
    }
})

nav_links[2].addEventListener('click', () => {
    if (nav_links[2].classList.contains('active') == false) {
        nav_links[2].classList.add('active')
        nav_links[0].classList.remove('active')
        nav_links[1].classList.remove('active')
        document.getElementsByClassName('tasks-display')[2].style.display = 'block'
        document.getElementsByClassName('tasks-display')[0].style.display = 'none'
        document.getElementsByClassName('tasks-display')[1].style.display = 'none'
    }
})

let general_task = document.getElementsByClassName('general-task')
for (let task of general_task) {
    task.addEventListener('click', () => {
        location.href = `/task/datas/${task.getAttribute('data-bs-target')}/`
    })
}
