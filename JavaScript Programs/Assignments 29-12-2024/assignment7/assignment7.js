// Assingment 7

document.forms[0].addEventListener('submit', function (e){
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let age = document.getElementById("age").value;
    let error = document.getElementById("error");
    error.innerHTML=""
    
    if(!name.trim()){
        e.preventDefault();
        let li = document.createElement('li')
        li.innerHTML = "Please enter a valid name."
        
        error.appendChild(li);
    }

    if(!email.includes("@")){
        e.preventDefault()
        let li = document.createElement('li')
        li.innerHTML = "Please enter a valid email."
        error.appendChild(li);
    }

    if(age && age<18){
        e.preventDefault()
        let li = document.createElement('li')
        li.innerHTML = "Age should be greter than 18"
        error.appendChild(li);
    }
})